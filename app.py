#!/usr/bin/env python3
"""
JayaMotor Web App - Flask Backend
Modern web version of JayaMotor application
"""

import sys
import logging
from pathlib import Path
from datetime import datetime, date, timedelta
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from config import APP_TITLE, APP_VERSION, DEBUG
from database.connection import DatabaseManager
from database.schema import initialize_database
from business.services import TransaksiService
from business.import_service import ImportService
from business.exceptions import ValidationErrors, RecordNotFound
from werkzeug.utils import secure_filename

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

# Initialize database
import os
db_file = Path(__file__).parent / "data" / "jaya_motor.db"
if db_file.exists():
    # Database already exists, just connect
    logger.info("Database exists, connecting...")
    DatabaseManager.initialize()
    logger.info("[OK] Database connected")
else:
    # Database doesn't exist, create fresh with seed data
    logger.info("Initializing database...")
    initialize_database()
    logger.info("[OK] Database initialized")

# Initialize services
transaksi_service = TransaksiService()

# Configure upload folder for imports
UPLOAD_FOLDER = Path(__file__).parent / 'uploads'
UPLOAD_FOLDER.mkdir(exist_ok=True)
app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Configure upload folder for documents (invoices, etc)
UPLOADS_FAKTUR_FOLDER = Path(__file__).parent / 'static' / 'uploads' / 'faktur'
UPLOADS_FAKTUR_FOLDER.mkdir(parents=True, exist_ok=True)
ALLOWED_DOC_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}


# Cache control - prevent caching
@app.after_request
def set_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# =====================================================================
# ROUTES - Pages
# =====================================================================

@app.route('/')
def index():
    """Landing page"""
    return render_template('landing.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard page"""
    return render_template('dashboard.html', app_title=APP_TITLE, app_version=APP_VERSION)


@app.route('/transaksi')
def transaksi_page():
    """Transaction management page"""
    return render_template('transaksi.html', app_title=APP_TITLE)


@app.route('/transaksi-draft')
def transaksi_draft_page():
    """Transaction draft approval page"""
    return render_template('transaksi_draft.html', app_title=APP_TITLE)


@app.route('/laporan')
def laporan_page():
    """Report page"""
    return render_template('laporan.html', app_title=APP_TITLE)


@app.route('/type-motor')
def type_motor_page():
    """Type motor master data page"""
    return render_template('type_motor.html', app_title=APP_TITLE)


@app.route('/stok-motor')
def stok_motor_page():
    """Stok motor inventory page"""
    return render_template('stok_motor.html', app_title=APP_TITLE)


@app.route('/import-stok')
def import_stok_page():
    """Import stok motor from Excel"""
    return render_template('import_stok.html', app_title=APP_TITLE)


@app.route('/broker-master')
def broker_master_page():
    """Master broker/sales management page"""
    return render_template('broker_master.html', app_title=APP_TITLE)


@app.route('/master-leasing')
def master_leasing_page():
    """Master leasing company management page"""
    return render_template('master_leasing.html', app_title=APP_TITLE)


@app.route('/laporan-hutang-sales')
def laporan_hutang_sales_page():
    """Sales debt report page"""
    return render_template('laporan_hutang_sales.html', app_title=APP_TITLE)


@app.route('/jurnal-informasi')
def jurnal_informasi_page():
    """Information journal - complete motor journey"""
    return render_template('jurnal_informasi.html', app_title=APP_TITLE)


@app.route('/pindah-stok')
def pindah_stok_page():
    """Stock transfer management page"""
    return render_template('pindah_stok.html', app_title=APP_TITLE)


# =====================================================================
# API - Broker (Master Data)
# =====================================================================

@app.route('/api/broker', methods=['GET'])
def get_brokers():
    """Get all active brokers"""
    try:
        from database.models import Broker
        session = DatabaseManager.get_session()
        brokers = session.query(Broker).filter_by(status='A').order_by(Broker.nama).all()

        data = []
        for b in brokers:
            data.append({
                'id': b.id,
                'nama': b.nama,
                'tipe': b.tipe,
                'alamat': b.alamat,
                'kota': b.kota,
                'telp': b.telp,
                'kontak_person': b.kontak_person,
                'email': b.email,
                'status': b.status,
            })

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        logger.error(f"Error fetching brokers: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/broker/<int:broker_id>', methods=['GET'])
def get_broker_detail(broker_id):
    """Get broker detail"""
    try:
        from database.models import Broker
        session = DatabaseManager.get_session()
        broker = session.query(Broker).filter_by(id=broker_id).first()

        if not broker:
            return jsonify({'success': False, 'error': 'Broker tidak ditemukan'}), 404

        data = {
            'id': broker.id,
            'nama': broker.nama,
            'tipe': broker.tipe,
            'alamat': broker.alamat,
            'kota': broker.kota,
            'telp': broker.telp,
            'kontak_person': broker.kontak_person,
            'email': broker.email,
            'status': broker.status,
        }

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        logger.error(f"Error fetching broker detail: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/broker', methods=['POST'])
def create_broker():
    """Create new broker"""
    try:
        from database.models import Broker
        data = request.json

        # Validation
        if not data.get('nama'):
            return jsonify({'success': False, 'error': 'Nama broker harus diisi'}), 400

        session = DatabaseManager.get_session()

        # Check duplicate
        existing = session.query(Broker).filter_by(nama=data['nama']).first()
        if existing:
            return jsonify({'success': False, 'error': 'Nama broker sudah terdaftar'}), 400

        # Create
        broker = Broker(
            nama=data['nama'],
            tipe=data.get('tipe', 'B'),
            alamat=data.get('alamat'),
            kota=data.get('kota'),
            telp=data.get('telp'),
            kontak_person=data.get('kontak_person'),
            email=data.get('email'),
            status=data.get('status', 'A'),
        )

        session.add(broker)
        session.commit()

        return jsonify({
            'success': True,
            'message': 'Broker berhasil dibuat',
            'id': broker.id
        }), 201
    except Exception as e:
        logger.error(f"Error creating broker: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/broker/<int:broker_id>', methods=['PUT'])
def update_broker(broker_id):
    """Update broker"""
    try:
        from database.models import Broker
        data = request.json
        session = DatabaseManager.get_session()

        broker = session.query(Broker).filter_by(id=broker_id).first()
        if not broker:
            return jsonify({'success': False, 'error': 'Broker tidak ditemukan'}), 404

        # Update fields
        if 'nama' in data:
            # Check duplicate on other brokers
            existing = session.query(Broker).filter(
                Broker.nama == data['nama'],
                Broker.id != broker_id
            ).first()
            if existing:
                return jsonify({'success': False, 'error': 'Nama broker sudah terdaftar'}), 400
            broker.nama = data['nama']

        if 'tipe' in data:
            broker.tipe = data['tipe']
        if 'alamat' in data:
            broker.alamat = data['alamat']
        if 'kota' in data:
            broker.kota = data['kota']
        if 'telp' in data:
            broker.telp = data['telp']
        if 'kontak_person' in data:
            broker.kontak_person = data['kontak_person']
        if 'email' in data:
            broker.email = data['email']
        if 'status' in data:
            broker.status = data['status']

        session.commit()

        return jsonify({
            'success': True,
            'message': 'Broker berhasil diupdate',
        })
    except Exception as e:
        logger.error(f"Error updating broker: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/broker/<int:broker_id>', methods=['DELETE'])
def delete_broker(broker_id):
    """Delete broker"""
    try:
        from database.models import Broker
        session = DatabaseManager.get_session()

        broker = session.query(Broker).filter_by(id=broker_id).first()
        if not broker:
            return jsonify({'success': False, 'error': 'Broker tidak ditemukan'}), 404

        session.delete(broker)
        session.commit()

        return jsonify({'success': True, 'message': 'Broker berhasil dihapus'})
    except Exception as e:
        logger.error(f"Error deleting broker: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# API - Leasing (Master Leasing Companies)
# =====================================================================

@app.route('/api/leasing', methods=['GET'])
def get_leasing():
    """Get all leasing companies"""
    try:
        from database.models import Leasing
        session = DatabaseManager.get_session()
        leasings = session.query(Leasing).order_by(Leasing.nama).all()

        data = []
        for l in leasings:
            data.append({
                'id': l.id,
                'kode': l.kode,
                'nama': l.nama,
                'alamat': l.alamat,
                'kota': l.kota,
                'telp': l.telp,
            })

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        logger.error(f"Error fetching leasing: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/leasing/<int:leasing_id>', methods=['GET'])
def get_leasing_detail(leasing_id):
    """Get leasing company detail"""
    try:
        from database.models import Leasing
        session = DatabaseManager.get_session()
        leasing = session.query(Leasing).filter_by(id=leasing_id).first()

        if not leasing:
            return jsonify({'success': False, 'error': 'Leasing tidak ditemukan'}), 404

        data = {
            'id': leasing.id,
            'kode': leasing.kode,
            'nama': leasing.nama,
            'alamat': leasing.alamat,
            'kota': leasing.kota,
            'telp': leasing.telp,
        }

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        logger.error(f"Error fetching leasing detail: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/leasing', methods=['POST'])
def create_leasing():
    """Create new leasing company"""
    try:
        from database.models import Leasing
        data = request.json

        # Validation
        if not data.get('nama'):
            return jsonify({'success': False, 'error': 'Nama leasing harus diisi'}), 400
        if not data.get('kode'):
            return jsonify({'success': False, 'error': 'Kode leasing harus diisi'}), 400

        session = DatabaseManager.get_session()

        # Check duplicate kode
        existing = session.query(Leasing).filter_by(kode=data['kode']).first()
        if existing:
            return jsonify({'success': False, 'error': 'Kode leasing sudah terdaftar'}), 400

        # Create
        leasing = Leasing(
            kode=data['kode'],
            nama=data['nama'],
            alamat=data.get('alamat'),
            kota=data.get('kota'),
            telp=data.get('telp'),
        )

        session.add(leasing)
        session.commit()

        return jsonify({
            'success': True,
            'message': 'Leasing berhasil dibuat',
            'id': leasing.id
        }), 201
    except Exception as e:
        logger.error(f"Error creating leasing: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/leasing/<int:leasing_id>', methods=['PUT'])
def update_leasing(leasing_id):
    """Update leasing company"""
    try:
        from database.models import Leasing
        data = request.json
        session = DatabaseManager.get_session()

        leasing = session.query(Leasing).filter_by(id=leasing_id).first()
        if not leasing:
            return jsonify({'success': False, 'error': 'Leasing tidak ditemukan'}), 404

        # Update fields
        if 'kode' in data:
            # Check duplicate on other leasings
            existing = session.query(Leasing).filter(
                Leasing.kode == data['kode'],
                Leasing.id != leasing_id
            ).first()
            if existing:
                return jsonify({'success': False, 'error': 'Kode leasing sudah terdaftar'}), 400
            leasing.kode = data['kode']

        if 'nama' in data:
            leasing.nama = data['nama']
        if 'alamat' in data:
            leasing.alamat = data['alamat']
        if 'kota' in data:
            leasing.kota = data['kota']
        if 'telp' in data:
            leasing.telp = data['telp']

        session.commit()

        return jsonify({
            'success': True,
            'message': 'Leasing berhasil diupdate',
        })
    except Exception as e:
        logger.error(f"Error updating leasing: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/leasing/<int:leasing_id>', methods=['DELETE'])
def delete_leasing(leasing_id):
    """Delete leasing company"""
    try:
        from database.models import Leasing
        session = DatabaseManager.get_session()

        leasing = session.query(Leasing).filter_by(id=leasing_id).first()
        if not leasing:
            return jsonify({'success': False, 'error': 'Leasing tidak ditemukan'}), 404

        session.delete(leasing)
        session.commit()

        return jsonify({'success': True, 'message': 'Leasing berhasil dihapus'})
    except Exception as e:
        logger.error(f"Error deleting leasing: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# API - Transaksi (Transactions)
# =====================================================================

@app.route('/api/transaksi-draft/<int:transaksi_id>', methods=['GET'])
def get_transaksi_draft_detail(transaksi_id):
    """Get Draft transaksi detail for review (view-only)"""
    try:
        from database.models import Transaksi
        from sqlalchemy.orm import joinedload

        session = DatabaseManager.get_session()
        transaksi = session.query(Transaksi).options(
            joinedload(Transaksi.detail),
            joinedload(Transaksi.broker),
            joinedload(Transaksi.dealer),
            joinedload(Transaksi.motor)
        ).filter(Transaksi.id == transaksi_id).first()

        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        # Only allow viewing Draft transaksi
        if transaksi.status_transaksi != 'D':
            return jsonify({'success': False, 'error': 'Hanya transaksi Draft yang bisa di-review'}), 400

        detail = transaksi.detail
        motor = transaksi.motor
        motor_type = motor.type_motor.nama_type if motor and motor.type_motor else "N/A"

        data = {
            'id': transaksi.id,
            'nota': transaksi.nota,
            'tanggal': transaksi.tanggal.isoformat() if transaksi.tanggal else None,
            'created_at': transaksi.created_at.isoformat(),
            'nama_pembeli': transaksi.nama_pembeli,
            'alamat_pembeli': transaksi.alamat_pembeli or '-',
            'telp_pembeli': transaksi.telp_pembeli or '-',
            'dealer_nama': transaksi.dealer.nama if transaksi.dealer else '-',
            'broker_nama': transaksi.broker.nama if transaksi.broker else '-',
            'motor_type': motor_type,
            'no_mesin': motor.no_mesin if motor else '-',
            'no_rangka': motor.no_rangka if motor else '-',
            'warna': motor.warna if motor else '-',
            'dp': float(detail.dp) if detail and detail.dp else 0,
            'subsidi': float(detail.subsidi) if detail and detail.subsidi else 0,
            'status': transaksi.status_transaksi,
        }

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching draft detail: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi-draft', methods=['GET'])
def get_transaksi_draft():
    """Get all draft transactions pending approval"""
    try:
        from database.models import Transaksi
        from sqlalchemy.orm import joinedload

        # Query only draft transaksi
        session = DatabaseManager.get_session()
        query = session.query(Transaksi).options(
            joinedload(Transaksi.detail),
            joinedload(Transaksi.dealer),
            joinedload(Transaksi.motor)
        ).filter(
            Transaksi.status_transaksi == 'D'
        )

        transaksi_list = query.order_by(Transaksi.created_at.desc()).all()

        # Convert to dict
        data = []
        for t in transaksi_list:
            detail = t.detail
            motor = t.motor
            motor_type = motor.type_motor.nama_type if motor and motor.type_motor else "N/A"
            broker_name = t.broker.nama if t.broker else ''

            data.append({
                'id': t.id,
                'nota': t.nota,
                'tanggal': t.tanggal.isoformat(),
                'created_at': t.created_at.isoformat(),
                'customer_name': t.nama_pembeli,
                'customer_phone': t.telp_pembeli,
                'customer_alamat': t.alamat_pembeli or '-',
                'motor_type': motor_type,
                'no_mesin': motor.no_mesin if motor else '-',
                'dealer_name': t.dealer.nama if t.dealer else '-',
                'broker_name': broker_name,
                'dp': float(detail.dp) if detail and detail.dp else 0,
                'subsidi': float(detail.subsidi) if detail and detail.subsidi else 0,
                'status': t.status_transaksi,
            })

        return jsonify({'success': True, 'data': data, 'count': len(data)})

    except Exception as e:
        logger.error(f"Error fetching draft transaksi: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi', methods=['GET'])
def get_transaksi():
    """Get all transactions with optional filtering"""
    try:
        from database.models import Transaksi
        from sqlalchemy.orm import joinedload

        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        dealer_id = request.args.get('dealer_id')
        status = request.args.get('status')

        # Convert date strings (default to last 30 days)
        start_date = None
        end_date = None
        if start_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        else:
            start_date = date.today() - timedelta(days=30)

        if end_date_str:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        else:
            end_date = date.today()

        # Query with eager loading to avoid lazy-load errors
        session = DatabaseManager.get_session()
        query = session.query(Transaksi).options(
            joinedload(Transaksi.detail)
        ).filter(
            Transaksi.tanggal.between(start_date, end_date)
        )

        # Exclude draft transaksi unless explicitly filtered
        if not status:
            query = query.filter(Transaksi.status_transaksi != 'D')

        if dealer_id:
            query = query.filter(Transaksi.dealer_id == int(dealer_id))
        if status:
            query = query.filter(Transaksi.status_transaksi == status)

        transaksi_list = query.order_by(Transaksi.tanggal.desc()).all()

        # Convert to dict
        data = []
        for t in transaksi_list:
            detail = t.detail
            motor_type = t.motor.type_motor.nama_type if t.motor and t.motor.type_motor else "N/A"
            broker_name = t.broker.nama if t.broker else ''
            data.append({
                'id': t.id,
                'nota': t.nota,
                'tanggal_nota': t.tanggal.isoformat(),
                'customer_name': t.nama_pembeli,
                'customer_phone': t.telp_pembeli,
                'motor_type': motor_type,
                'broker_id': t.broker_id,
                'broker_name': broker_name,
                'dp': float(detail.dp) if detail and detail.dp else 0,
                'subsidi': float(detail.subsidi) if detail and detail.subsidi else 0,
                'diskon_ahm': float(detail.diskon_ahm) if detail and detail.diskon_ahm else 0,
                'diskon_dealer': float(detail.diskon_dealer) if detail and detail.diskon_dealer else 0,
                'diskon_leasing': float(detail.diskon_leasing) if detail and detail.diskon_leasing else 0,
                'hutang_sales': float(detail.hutang_sales) if detail and detail.hutang_sales else 0,
                'hutang_leasing': float(detail.hutang_leasing) if detail and detail.hutang_leasing else 0,
                'tgl_hutang_dibayar': detail.tgl_hutang_dibayar.isoformat() if detail and detail.tgl_hutang_dibayar else None,
                'status': t.status_transaksi,
            })

        return jsonify({'success': True, 'data': data, 'count': len(data)})

    except Exception as e:
        logger.error(f"Error fetching transaksi: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>', methods=['GET'])
def get_transaksi_detail(transaksi_id):
    """Get transaction detail"""
    try:
        from database.models import Transaksi
        from sqlalchemy.orm import joinedload

        session = DatabaseManager.get_session()
        # Eager load detail and leasing to avoid lazy-load errors
        transaksi = session.query(Transaksi).options(
            joinedload(Transaksi.detail),
            joinedload(Transaksi.broker),
            joinedload(Transaksi.dealer)
        ).filter(
            Transaksi.id == transaksi_id
        ).first()

        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        # Block access to Draft transaksi (must be approved first)
        if transaksi.status_transaksi == 'D':
            return jsonify({'success': False, 'error': 'Transaksi masih dalam status Draft. Harus di-approve terlebih dahulu di Transaksi Draft'}), 403

        detail = transaksi.detail
        motor_type = transaksi.motor.type_motor.nama_type if transaksi.motor and transaksi.motor.type_motor else "N/A"

        # Recalculate hutang to ensure accuracy
        sistem = detail.sistem_pembayaran if detail else 'Cash'
        otr = float(detail.otr) if detail and detail.otr else 0
        ketentuan_dp_val = float(detail.ketentuan_dp) if detail and detail.ketentuan_dp else 0
        dp = float(detail.dp) if detail and detail.dp else 0
        subsidi = float(detail.subsidi) if detail and detail.subsidi else 0
        diskon_ahm = float(detail.diskon_ahm) if detail and detail.diskon_ahm else 0
        diskon_dealer = float(detail.diskon_dealer) if detail and detail.diskon_dealer else 0
        diskon_leasing = float(detail.diskon_leasing) if detail and detail.diskon_leasing else 0

        hutang = calculate_debts(sistem, otr, ketentuan_dp_val, dp, subsidi, diskon_ahm, diskon_dealer, diskon_leasing)
        hutang_sales_calc = hutang['hutang_sales']
        hutang_leasing_calc = hutang['hutang_leasing']

        data = {
            'id': transaksi.id,
            'nota': transaksi.nota,
            'tanggal_nota': transaksi.tanggal.isoformat(),
            'customer_name': transaksi.nama_pembeli,
            'customer_phone': transaksi.telp_pembeli,
            'customer_alamat': transaksi.alamat_pembeli,
            'kelurahan_pembeli': transaksi.kelurahan_pembeli,
            'kecamatan_pembeli': transaksi.kecamatan_pembeli,
            'kabupaten_pembeli': transaksi.kabupaten_pembeli,
            'nama_surat': transaksi.nama_surat,
            'alamat_surat': transaksi.alamat_surat,
            'kelurahan_surat': transaksi.kelurahan_surat,
            'kecamatan_surat': transaksi.kecamatan_surat,
            'kabupaten_surat': transaksi.kabupaten_surat,
            'no_surat_pemberitahuan': transaksi.no_surat_pemberitahuan,
            'tgl_surat_pemberitahuan': transaksi.tgl_surat_pemberitahuan.isoformat() if transaksi.tgl_surat_pemberitahuan else None,
            'dealer_id': transaksi.dealer_id,
            'motor_type': motor_type,
            'type_motor_id': transaksi.motor.type_id if transaksi.motor and transaksi.motor.type_id else None,
            'stok_id': transaksi.motor_id if transaksi.motor_id else None,
            'broker_id': transaksi.broker_id,
            'no_chassis': transaksi.motor.no_rangka if transaksi.motor else '',
            'no_engine': transaksi.motor.no_mesin if transaksi.motor else '',
            'warna': transaksi.motor.warna if transaksi.motor else '',
            'harga_dasar': float(detail.harga_dasar) if detail and detail.harga_dasar else 0,
            'otr': float(detail.otr) if detail and detail.otr else 0,
            'sistem_pembayaran': detail.sistem_pembayaran if detail else 'Cash',
            'ketentuan_dp': float(detail.ketentuan_dp) if detail and detail.ketentuan_dp else 0,
            'dp': float(detail.dp) if detail and detail.dp else 0,
            'tgl_bayar_dp': detail.tgl_bayar_dp.isoformat() if detail and detail.tgl_bayar_dp else None,
            'ket_dp': detail.ket_dp if detail else '',
            'subsidi': float(detail.subsidi) if detail and detail.subsidi else 0,
            'diskon_ahm': float(detail.diskon_ahm) if detail and detail.diskon_ahm else 0,
            'diskon_dealer': float(detail.diskon_dealer) if detail and detail.diskon_dealer else 0,
            'diskon_leasing': float(detail.diskon_leasing) if detail and detail.diskon_leasing else 0,
            'insentif_penjual': float(detail.insentif) if detail and detail.insentif else 0,
            'hutang_sales': hutang_sales_calc,
            'hutang_leasing': hutang_leasing_calc,
            'total_terbayar': float(detail.total_terbayar) if detail and detail.total_terbayar else 0,
            'status_hutang': detail.status_hutang if detail else 'Belum',
            'tgl_hutang_dibayar': detail.tgl_hutang_dibayar.isoformat() if detail and detail.tgl_hutang_dibayar else None,
            'leasing_id': detail.leasing_id if detail else None,
            'leasing_nama': detail.leasing.nama if detail and detail.leasing else 'N/A',
            'broker_nama': transaksi.broker.nama if transaksi.broker else 'N/A',
            'dealer_nama': transaksi.dealer.nama if transaksi.dealer else 'N/A',
            'no_faktur': transaksi.no_faktur,
            'tgl_faktur': transaksi.tgl_faktur.isoformat() if transaksi.tgl_faktur else None,
            'file_faktur': transaksi.file_faktur,
            'no_polisi': transaksi.no_polisi,
            'tgl_biro': transaksi.tgl_biro.isoformat() if transaksi.tgl_biro else None,
            'no_bpkb': transaksi.no_bpkb,
            'tgl_terima_bpkb': transaksi.tgl_terima_bpkb.isoformat() if transaksi.tgl_terima_bpkb else None,
            'tgl_serah_terima': transaksi.tgl_serah_terima.isoformat() if transaksi.tgl_serah_terima else None,
            'status': transaksi.status_transaksi,
        }

        return jsonify({'success': True, 'data': data})

    except RecordNotFound:
        return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404
    except Exception as e:
        logger.error(f"Error fetching transaksi detail: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi', methods=['POST'])
def create_transaksi():
    """Create new transaction"""
    try:
        data = request.json
        logger.info(f"[POST /api/transaksi] Received data: {data}")

        # Validate required fields
        required_fields = ['nota', 'tanggal_nota', 'customer_name', 'motor_type']
        for field in required_fields:
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return jsonify({'success': False, 'error': f'Field {field} required'}), 400

        # Map field names to model fields
        stok_id = data.get('stok_id')
        if not stok_id:
            logger.error("Missing stok_id")
            return jsonify({'success': False, 'error': 'Field stok_id required'}), 400

        logger.info(f"[POST /api/transaksi] Creating with stok_id={stok_id}")

        # Map status values - Default to DRAFT (D)
        status_map = {
            'Draft': 'D',
            'Pending': 'P',
            'Approved': 'A',
            'Paid': 'L',
            'Cancelled': 'C'
        }
        status_value = data.get('status', 'D')  # Default: Draft
        status_code = status_map.get(status_value, status_value)  # Try map, fall back to original

        transaksi_data = {
            'nota': data['nota'],
            'tanggal': datetime.strptime(data['tanggal_nota'], '%Y-%m-%d').date(),
            'dealer_id': data.get('dealer_id', 1),  # Default to first dealer
            'nama_pembeli': data['customer_name'],
            'alamat_pembeli': data.get('customer_alamat'),
            'kelurahan_pembeli': data.get('kelurahan_pembeli'),
            'kecamatan_pembeli': data.get('kecamatan_pembeli'),
            'kabupaten_pembeli': data.get('kabupaten_pembeli'),
            'nama_surat': data.get('nama_surat'),
            'telp_pembeli': data.get('customer_phone'),
            'motor_id': int(stok_id),  # Use stok_id as motor_id
            'broker_id': int(data.get('broker_id')) if data.get('broker_id') else None,
            'status_transaksi': status_code,
            # Financial details (will be created separately)
            'harga_dasar': data.get('harga_dasar', 0),
            'sistem_pembayaran': data.get('sistem_pembayaran', 'Cash'),
            'ketentuan_dp': data.get('ketentuan_dp', 0),
            'dp': data.get('dp', 0),
            'tgl_bayar_dp': data.get('tgl_bayar_dp'),
            'ket_dp': data.get('ket_dp'),
            'subsidi': data.get('subsidi', 0),
            'diskon_ahm': data.get('diskon_ahm', 0),
            'diskon_dealer': data.get('diskon_dealer', 0),
            'diskon_leasing': data.get('diskon_leasing', 0),
            'insentif': data.get('insentif_penjual', 0),
            'hutang_sales': 0,  # Will be calculated after detail is created
            'tgl_hutang_dibayar': data.get('tgl_hutang_dibayar'),
            'leasing_id': int(data.get('leasing_id')) if data.get('leasing_id') else None,
        }
        logger.info(f"[POST /api/transaksi] Calling service.create_transaksi")
        transaksi = transaksi_service.create_transaksi(transaksi_data)
        logger.info(f"[POST /api/transaksi] Service call succeeded: ID={transaksi.id}")

        # Update stok status if stok_id provided (hutang will auto-calculate on first edit)
        if data.get('stok_id'):
            from database.models import StokMotor
            session = DatabaseManager.get_session()
            try:
                stok = session.query(StokMotor).filter_by(id=int(data['stok_id'])).first()
                if stok:
                    stok.status = 'S'  # Sold
                    stok.tgl_status = datetime.utcnow()
                    session.commit()
            finally:
                session.close()

        return jsonify({
            'success': True,
            'message': 'Transaksi berhasil dibuat',
            'id': transaksi.id
        }), 201

    except ValidationErrors as e:
        error_details = str(e)
        logger.error(f"Validation error: {error_details}")
        # Return detailed error info
        return jsonify({
            'success': False,
            'error': error_details,
            'errors': e.errors if hasattr(e, 'errors') else []
        }), 400
    except Exception as e:
        logger.error(f"Error creating transaksi: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


def calculate_debts(sistem_pembayaran, otr, ketentuan_dp, dp_dibayar=0, subsidi=0, diskon_ahm=0, diskon_dealer=0, diskon_leasing=0):
    """
    Calculate sales and leasing debts based on payment system

    Pokok hutang = OTR - (subsidi + diskon_ahm + diskon_dealer + diskon_leasing)

    CASH:
      ketentuan_dp = OTR (untuk cash, DP target = full OTR amount)
      hutang_sales = ketentuan_dp - dp_sudah_dibayar
      hutang_leasing = 0

    KREDIT:
      hutang_sales = ketentuan_dp - dp_sudah_dibayar
      hutang_leasing = pokok - ketentuan_dp
    """
    otr = float(otr or 0)
    ketentuan_dp = float(ketentuan_dp or 0)
    dp_dibayar = float(dp_dibayar or 0)
    subsidi = float(subsidi or 0)
    diskon_ahm = float(diskon_ahm or 0)
    diskon_dealer = float(diskon_dealer or 0)
    diskon_leasing = float(diskon_leasing or 0)

    # Pokok = harga setelah semua diskon
    total_diskon = subsidi + diskon_ahm + diskon_dealer + diskon_leasing
    pokok = max(0, otr - total_diskon)

    if sistem_pembayaran == "Cash":
        # CASH: For cash sales, ketentuan_dp (DP requirement) = full OTR
        ketentuan_dp = otr
        hutang_sales = max(0, ketentuan_dp - dp_dibayar)
        hutang_leasing = 0
    else:  # Kredit
        # KREDIT: Hutang sales = sisa DP yang harus dikumpulkan
        hutang_sales = max(0, ketentuan_dp - dp_dibayar)
        hutang_leasing = max(0, pokok - ketentuan_dp)

    return {'hutang_sales': hutang_sales, 'hutang_leasing': hutang_leasing}


@app.route('/api/transaksi/<int:transaksi_id>', methods=['PUT'])
def update_transaksi(transaksi_id):
    """Update transaction"""
    try:
        from database.models import Transaksi
        from sqlalchemy.orm import joinedload

        data = request.json

        # Get existing transaksi with eager loading
        session = DatabaseManager.get_session()
        transaksi = session.query(Transaksi).options(
            joinedload(Transaksi.detail)
        ).filter(Transaksi.id == transaksi_id).first()

        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        # Block editing Draft transaksi
        if transaksi.status_transaksi == 'D':
            return jsonify({'success': False, 'error': 'Tidak bisa mengedit transaksi Draft. Harus di-approve terlebih dahulu di Transaksi Draft.'}), 403

        # Map field names for update
        update_data = {}
        if 'tanggal_nota' in data:
            if data['tanggal_nota']:
                if isinstance(data['tanggal_nota'], str):
                    update_data['tanggal'] = datetime.strptime(data['tanggal_nota'], '%Y-%m-%d').date()
                else:
                    update_data['tanggal'] = data['tanggal_nota']
            else:
                update_data['tanggal'] = None
        if 'customer_name' in data:
            update_data['nama_pembeli'] = data['customer_name']
        if 'customer_phone' in data:
            update_data['telp_pembeli'] = data['customer_phone']
        if 'customer_alamat' in data:
            update_data['alamat_pembeli'] = data['customer_alamat']
        if 'kelurahan_pembeli' in data:
            update_data['kelurahan_pembeli'] = data['kelurahan_pembeli']
        if 'kecamatan_pembeli' in data:
            update_data['kecamatan_pembeli'] = data['kecamatan_pembeli']
        if 'kabupaten_pembeli' in data:
            update_data['kabupaten_pembeli'] = data['kabupaten_pembeli']
        if 'nama_surat' in data:
            update_data['nama_surat'] = data['nama_surat']
        if 'alamat_surat' in data:
            update_data['alamat_surat'] = data['alamat_surat']
        if 'kelurahan_surat' in data:
            update_data['kelurahan_surat'] = data['kelurahan_surat']
        if 'kecamatan_surat' in data:
            update_data['kecamatan_surat'] = data['kecamatan_surat']
        if 'kabupaten_surat' in data:
            update_data['kabupaten_surat'] = data['kabupaten_surat']
        if 'no_surat_pemberitahuan' in data:
            update_data['no_surat_pemberitahuan'] = data['no_surat_pemberitahuan']
        if 'tgl_surat_pemberitahuan' in data:
            if data['tgl_surat_pemberitahuan']:
                if isinstance(data['tgl_surat_pemberitahuan'], str):
                    update_data['tgl_surat_pemberitahuan'] = datetime.strptime(data['tgl_surat_pemberitahuan'], '%Y-%m-%d').date()
                else:
                    update_data['tgl_surat_pemberitahuan'] = data['tgl_surat_pemberitahuan']
            else:
                update_data['tgl_surat_pemberitahuan'] = None
        if 'status' in data:
            update_data['status_transaksi'] = data['status']
        if 'broker_id' in data:
            update_data['broker_id'] = int(data['broker_id']) if data['broker_id'] else None
        if 'no_faktur' in data:
            update_data['no_faktur'] = data['no_faktur']
        if 'tgl_faktur' in data:
            if data['tgl_faktur']:
                if isinstance(data['tgl_faktur'], str):
                    update_data['tgl_faktur'] = datetime.strptime(data['tgl_faktur'], '%Y-%m-%d').date()
                else:
                    update_data['tgl_faktur'] = data['tgl_faktur']
            else:
                update_data['tgl_faktur'] = None
        if 'no_polisi' in data:
            no_polisi = data['no_polisi'].strip().replace(' ', '') if data['no_polisi'] else None
            if no_polisi:
                existing = session.query(Transaksi).filter(
                    Transaksi.no_polisi == no_polisi,
                    Transaksi.id != transaksi.id
                ).first()
                if existing:
                    session.close()
                    return jsonify({'success': False, 'error': f'Nomor polisi {no_polisi} sudah ada di nota {existing.nota}'}), 400
            update_data['no_polisi'] = no_polisi
        if 'tgl_biro' in data:
            if data['tgl_biro']:
                if isinstance(data['tgl_biro'], str):
                    update_data['tgl_biro'] = datetime.strptime(data['tgl_biro'], '%Y-%m-%d').date()
                else:
                    update_data['tgl_biro'] = data['tgl_biro']
            else:
                update_data['tgl_biro'] = None
        if 'no_bpkb' in data:
            update_data['no_bpkb'] = data['no_bpkb']
        if 'tgl_terima_bpkb' in data:
            if data['tgl_terima_bpkb']:
                if isinstance(data['tgl_terima_bpkb'], str):
                    update_data['tgl_terima_bpkb'] = datetime.strptime(data['tgl_terima_bpkb'], '%Y-%m-%d').date()
                else:
                    update_data['tgl_terima_bpkb'] = data['tgl_terima_bpkb']
            else:
                update_data['tgl_terima_bpkb'] = None
        if 'tgl_serah_terima' in data:
            if data['tgl_serah_terima']:
                if isinstance(data['tgl_serah_terima'], str):
                    update_data['tgl_serah_terima'] = datetime.strptime(data['tgl_serah_terima'], '%Y-%m-%d').date()
                else:
                    update_data['tgl_serah_terima'] = data['tgl_serah_terima']
            else:
                update_data['tgl_serah_terima'] = None

        # Update transaksi
        if update_data:
            transaksi_service.update_transaksi(transaksi_id, update_data)
            # Re-fetch with eager loading
            transaksi = session.query(Transaksi).options(
                joinedload(Transaksi.detail)
            ).filter(Transaksi.id == transaksi_id).first()

        # Update stok status if stok_id provided (use same session to keep transaksi attached)
        if data.get('stok_id'):
            from database.models import StokMotor
            stok = session.query(StokMotor).filter_by(id=int(data['stok_id'])).first()
            if stok:
                stok.status = 'S'  # Sold
                stok.tgl_status = datetime.utcnow()
                session.commit()

        # Update detail only if financial fields explicitly provided
        # Skip detail update if not needed - prevents date conversion issues
        financial_fields = ['harga_dasar', 'dp', 'subsidi', 'diskon_ahm', 'diskon_dealer', 'diskon_leasing', 'insentif_penjual', 'leasing_id', 'sistem_pembayaran', 'ketentuan_dp']
        if transaksi.detail and any(f in data for f in financial_fields):
            detail_data = {}
            if 'harga_dasar' in data:
                detail_data['harga_dasar'] = data['harga_dasar']
            if 'sistem_pembayaran' in data:
                detail_data['sistem_pembayaran'] = data['sistem_pembayaran']
            if 'ketentuan_dp' in data:
                detail_data['ketentuan_dp'] = data['ketentuan_dp']
            if 'dp' in data:
                detail_data['dp'] = data['dp']
            if 'subsidi' in data:
                detail_data['subsidi'] = data['subsidi']
            if 'diskon_ahm' in data:
                detail_data['diskon_ahm'] = data['diskon_ahm']
            if 'diskon_dealer' in data:
                detail_data['diskon_dealer'] = data['diskon_dealer']
            if 'diskon_leasing' in data:
                detail_data['diskon_leasing'] = data['diskon_leasing']
            if 'insentif_penjual' in data:
                detail_data['insentif'] = data['insentif_penjual']
            if 'leasing_id' in data:
                detail_data['leasing_id'] = int(data['leasing_id']) if data['leasing_id'] else None
            if 'ket_dp' in data:
                detail_data['ket_dp'] = data['ket_dp']

            # Auto-calculate hutang_sales and hutang_leasing based on payment system
            sistem = data.get('sistem_pembayaran', transaksi.detail.sistem_pembayaran)
            otr = float(data.get('harga_dasar', transaksi.detail.otr or 0) or 0)
            ketentuan_dp = float(data.get('ketentuan_dp', transaksi.detail.ketentuan_dp or 0) or 0)
            dp_dibayar = float(data.get('dp', transaksi.detail.dp or 0) or 0)
            subsidi = float(data.get('subsidi', transaksi.detail.subsidi or 0) or 0)
            diskon_ahm = float(data.get('diskon_ahm', transaksi.detail.diskon_ahm or 0) or 0)
            diskon_dealer = float(data.get('diskon_dealer', transaksi.detail.diskon_dealer or 0) or 0)
            diskon_leasing = float(data.get('diskon_leasing', transaksi.detail.diskon_leasing or 0) or 0)

            debts = calculate_debts(sistem, otr, ketentuan_dp, dp_dibayar, subsidi, diskon_ahm, diskon_dealer, diskon_leasing)
            detail_data['hutang_sales'] = debts['hutang_sales']
            detail_data['hutang_leasing'] = debts['hutang_leasing']

            if detail_data:
                transaksi_service.detail_repo.update(transaksi.detail.id, detail_data)

        return jsonify({
            'success': True,
            'message': 'Transaksi berhasil diupdate',
            'id': transaksi.id
        })

    except ValidationErrors as e:
        logger.error(f"Validation error updating transaksi: {e.errors}")
        return jsonify({'success': False, 'error': str(e), 'details': e.errors}), 400
    except Exception as e:
        logger.error(f"Error updating transaksi: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>/bayar-hutang', methods=['POST'])
def bayar_hutang_sales(transaksi_id):
    """Record payment for sales debt (supports partial/installment payments)"""
    try:
        from database.models import Transaksi, TransaksiDetail, PembayaranHutang
        from sqlalchemy.orm import joinedload

        data = request.json
        nominal = data.get('nominal')  # Payment amount
        tgl_pembayaran = data.get('tgl_pembayaran')
        metode = data.get('metode', 'Cash')
        keterangan = data.get('keterangan')

        if not nominal or nominal <= 0:
            return jsonify({'success': False, 'error': 'Nominal pembayaran harus > 0'}), 400
        if not tgl_pembayaran:
            return jsonify({'success': False, 'error': 'Tanggal pembayaran required'}), 400

        # Convert string to date
        if isinstance(tgl_pembayaran, str):
            tgl_pembayaran = datetime.strptime(tgl_pembayaran, '%Y-%m-%d').date()

        session = DatabaseManager.get_session()
        transaksi = session.query(Transaksi).options(
            joinedload(Transaksi.detail)
        ).filter(Transaksi.id == transaksi_id).first()

        if not transaksi or not transaksi.detail:
            return jsonify({'success': False, 'error': 'Transaksi atau detail tidak ditemukan'}), 404

        # Block payment recording for Draft transaksi
        if transaksi.status_transaksi == 'D':
            return jsonify({'success': False, 'error': 'Tidak bisa mencatat pembayaran untuk transaksi Draft. Harus di-approve terlebih dahulu.'}), 403

        detail = transaksi.detail
        sisa_hutang = float(detail.hutang_sales or 0) - float(detail.total_terbayar or 0)

        if sisa_hutang <= 0:
            return jsonify({'success': False, 'error': 'Tidak ada hutang yang perlu dibayar'}), 400

        if nominal > sisa_hutang:
            return jsonify({'success': False, 'error': f'Pembayaran melebihi sisa hutang (Rp {int(sisa_hutang):,})'}), 400

        # Update detail transaksi
        detail.total_terbayar = float(detail.total_terbayar or 0) + nominal
        sisa_hutang_baru = float(detail.hutang_sales or 0) - detail.total_terbayar

        # Set status hutang
        if sisa_hutang_baru <= 0:
            detail.status_hutang = 'Lunas'
            detail.tgl_hutang_dibayar = tgl_pembayaran
        else:
            detail.status_hutang = 'Cicilan'

        # Record payment
        pembayaran = PembayaranHutang(
            transaksi_id=transaksi_id,
            nominal=nominal,
            tgl_pembayaran=tgl_pembayaran,
            metode=metode,
            keterangan=keterangan,
            sisa_hutang=max(0, sisa_hutang_baru)
        )
        session.add(pembayaran)
        session.commit()

        logger.info(f"[Bayar Hutang] Transaksi {transaksi_id}: Pembayaran Rp {int(nominal):,}, Sisa: Rp {int(max(0, sisa_hutang_baru)):,}")

        return jsonify({
            'success': True,
            'message': 'Pembayaran hutang berhasil dicatat',
            'data': {
                'transaksi_id': transaksi_id,
                'nominal': nominal,
                'total_terbayar': float(detail.total_terbayar),
                'sisa_hutang': max(0, sisa_hutang_baru),
                'status_hutang': detail.status_hutang,
                'tgl_pembayaran': tgl_pembayaran.isoformat()
            }
        })

    except Exception as e:
        logger.error(f"Error recording hutang payment: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>/pembayaran-history', methods=['GET'])
def get_pembayaran_history(transaksi_id):
    """Get payment history for a transaction"""
    try:
        from database.models import PembayaranHutang

        session = DatabaseManager.get_session()
        pembayaran_list = session.query(PembayaranHutang).filter(
            PembayaranHutang.transaksi_id == transaksi_id
        ).order_by(PembayaranHutang.tgl_pembayaran).all()

        data = [{
            'tgl_pembayaran': p.tgl_pembayaran.isoformat() if isinstance(p.tgl_pembayaran, date) else p.tgl_pembayaran,
            'nominal': float(p.nominal),
            'sisa_hutang': float(p.sisa_hutang),
            'metode': p.metode,
            'keterangan': p.keterangan
        } for p in pembayaran_list]

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching pembayaran history: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/jurnal-informasi', methods=['GET'])
def get_jurnal_informasi():
    """Get complete motor journey information"""
    try:
        from database.models import Transaksi, TransaksiDetail
        from sqlalchemy.orm import joinedload

        tgl_awal = request.args.get('tgl_awal')
        tgl_akhir = request.args.get('tgl_akhir')
        search = request.args.get('search', '').strip()

        session = DatabaseManager.get_session()
        query = session.query(Transaksi).options(
            joinedload(Transaksi.detail),
            joinedload(Transaksi.dealer),
            joinedload(Transaksi.motor),
            joinedload(Transaksi.broker)
        ).filter(
            Transaksi.status_transaksi != 'D'  # Exclude Draft - not yet approved
        )

        # Apply date filters
        if tgl_awal:
            tgl_awal_date = datetime.strptime(tgl_awal, '%Y-%m-%d').date()
            query = query.filter(Transaksi.tanggal >= tgl_awal_date)

        if tgl_akhir:
            tgl_akhir_date = datetime.strptime(tgl_akhir, '%Y-%m-%d').date()
            query = query.filter(Transaksi.tanggal <= tgl_akhir_date)

        # Apply search filter
        if search:
            query = query.filter(
                (Transaksi.nota.ilike(f"%{search}%")) |
                (Transaksi.motor.has(no_mesin=search)) if hasattr(Transaksi, 'motor') else False
            )

        transaksi_list = query.order_by(Transaksi.tanggal.desc()).all()

        data = []
        for t in transaksi_list:
            detail = t.detail
            motor = t.motor

            data.append({
                'id': t.id,
                'tanggal': t.tanggal.isoformat() if t.tanggal else None,
                'nota': t.nota,
                'dealer_nama': t.dealer.nama if t.dealer else 'N/A',
                'no_mesin': motor.no_mesin if motor else 'N/A',
                'no_rangka': motor.no_rangka if motor else 'N/A',
                'motor_type': motor.type_motor.nama_type if motor and motor.type_motor else 'N/A',
                'warna': motor.warna if motor else 'N/A',
                'customer_name': t.nama_pembeli,
                'customer_alamat': t.alamat_pembeli or 'N/A',
                'customer_phone': t.telp_pembeli or 'N/A',
                'tgl_faktur': t.tgl_faktur.isoformat() if t.tgl_faktur else None,
                'no_faktur': t.no_faktur,
                'file_faktur': t.file_faktur,
                'no_polisi': t.no_polisi,
                'no_surat_pemberitahuan': t.no_surat_pemberitahuan,
                'tgl_surat_pemberitahuan': t.tgl_surat_pemberitahuan.isoformat() if t.tgl_surat_pemberitahuan else None,
                'nama_surat': t.nama_surat,
                'no_bpkb': t.no_bpkb,
                'tgl_biro': t.tgl_biro.isoformat() if t.tgl_biro else None,
                'tgl_terima_bpkb': t.tgl_terima_bpkb.isoformat() if t.tgl_terima_bpkb else None,
                'tgl_serah_terima': t.tgl_serah_terima.isoformat() if t.tgl_serah_terima else None,
                'broker_nama': t.broker.nama if t.broker else 'N/A',
                'ket_dp': detail.ket_dp if detail else None,
                'dp': float(detail.dp) if detail and detail.dp else 0,
                'subsidi': float(detail.subsidi) if detail and detail.subsidi else 0,
                'diskon_ahm': float(detail.diskon_ahm) if detail and detail.diskon_ahm else 0,
                'diskon_dealer': float(detail.diskon_dealer) if detail and detail.diskon_dealer else 0,
                'diskon_leasing': float(detail.diskon_leasing) if detail and detail.diskon_leasing else 0,
                'insentif': float(detail.insentif) if detail and detail.insentif else 0,
                'leasing_nama': detail.leasing.nama if detail and detail.leasing else 'N/A',
                'tgl_hutang_dibayar': detail.tgl_hutang_dibayar.isoformat() if detail and detail.tgl_hutang_dibayar else None,
                'status': t.status_transaksi,
            })

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching jurnal informasi: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>', methods=['DELETE'])
def delete_transaksi(transaksi_id):
    """Delete transaction"""
    try:
        transaksi = transaksi_service.repo.get_by_id(transaksi_id)
        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        transaksi_service.repo.delete(transaksi_id)

        return jsonify({
            'success': True,
            'message': 'Transaksi berhasil dihapus'
        })

    except Exception as e:
        logger.error(f"Error deleting transaksi: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>/approve', methods=['POST'])
def approve_transaksi(transaksi_id):
    """Approve posting transaksi (Draft → Approved/Posted) and update motor status to Sold"""
    try:
        from database.models import Transaksi, StokMotor

        session = DatabaseManager.get_session()
        transaksi = session.query(Transaksi).filter_by(id=transaksi_id).first()

        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        if transaksi.status_transaksi != 'D':
            return jsonify({'success': False, 'error': 'Hanya transaksi draft yang bisa di-approve'}), 400

        # Update status ke Approved/Posted
        transaksi.status_transaksi = 'A'
        transaksi.updated_at = datetime.utcnow()
        session.commit()

        # Update motor status to 'S' (Sold) via TransaksiDetail
        if transaksi.detail:
            motor = session.query(StokMotor).filter_by(id=transaksi.detail.stok_motor_id).first()
            if motor:
                motor.status = 'S'  # Sold
                session.commit()
                logger.info(f"Motor {motor.no_mesin} status updated to Sold (transaksi {transaksi_id})")

        logger.info(f"Transaksi {transaksi_id} approved and posted by supervisor")

        return jsonify({
            'success': True,
            'message': 'Transaksi berhasil di-approve dan posting ke sistem',
            'data': {
                'id': transaksi.id,
                'status': transaksi.status_transaksi,
                'updated_at': transaksi.updated_at.isoformat()
            }
        })

    except Exception as e:
        logger.error(f"Error approving transaksi: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>/upload-faktur', methods=['POST'])
def upload_faktur(transaksi_id):
    """Upload invoice file for transaction"""
    try:
        from database.models import Transaksi

        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'File tidak ditemukan dalam request'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'File tidak dipilih'}), 400

        # Check file extension
        if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_DOC_EXTENSIONS):
            return jsonify({'success': False, 'error': 'Format file tidak didukung. Hanya PDF, PNG, JPG, JPEG'}), 400

        # Verify transaksi exists
        session = DatabaseManager.get_session()
        transaksi = session.query(Transaksi).filter_by(id=transaksi_id).first()
        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        # Save file with unique name: transaksi_id_timestamp.ext
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f'faktur_{transaksi_id}_{timestamp}.{ext}'
        filepath = UPLOADS_FAKTUR_FOLDER / filename

        file.save(str(filepath))

        # Update transaksi with file path and other data from request
        no_faktur = request.form.get('no_faktur', '').strip()
        tgl_faktur_str = request.form.get('tgl_faktur', '').strip()

        update_data = {
            'file_faktur': f'uploads/faktur/{filename}'
        }

        if no_faktur:
            update_data['no_faktur'] = no_faktur
        if tgl_faktur_str:
            try:
                update_data['tgl_faktur'] = datetime.strptime(tgl_faktur_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        transaksi_service.repo.update(transaksi_id, update_data)

        return jsonify({
            'success': True,
            'message': 'File faktur berhasil diupload',
            'filename': filename,
            'filepath': f'uploads/faktur/{filename}'
        }), 201

    except Exception as e:
        logger.error(f"Error uploading faktur: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/transaksi/<int:transaksi_id>/delete-faktur', methods=['DELETE'])
def delete_faktur(transaksi_id):
    """Delete invoice file for transaction"""
    try:
        from database.models import Transaksi
        import os

        session = DatabaseManager.get_session()
        transaksi = session.query(Transaksi).filter_by(id=transaksi_id).first()
        if not transaksi:
            return jsonify({'success': False, 'error': 'Transaksi tidak ditemukan'}), 404

        if transaksi.file_faktur:
            # Delete file from disk
            filepath = Path(__file__).parent / 'static' / transaksi.file_faktur
            if filepath.exists():
                os.remove(str(filepath))

            # Update transaksi to remove file reference
            transaksi_service.repo.update(transaksi_id, {
                'file_faktur': None,
                'no_faktur': None,
                'tgl_faktur': None
            })

            return jsonify({'success': True, 'message': 'File faktur berhasil dihapus'})
        else:
            return jsonify({'success': False, 'error': 'Tidak ada file faktur untuk dihapus'}), 404

    except Exception as e:
        logger.error(f"Error deleting faktur: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# API - Master Data
# =====================================================================

@app.route('/api/dealers', methods=['GET'])
def get_dealers():
    """Get all dealers"""
    try:
        dealers = transaksi_service.dealer_repo.get_all()
        data = [{
            'id': d.id,
            'kode_dealer': d.kode_dealer,
            'nama': d.nama,
            'kota': d.kota,
            'status': d.status,
        } for d in dealers]

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching dealers: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor', methods=['GET'])
def get_type_motor():
    """Get all type motor"""
    try:
        from database.models import TypeMotor
        session = DatabaseManager.get_session()
        types = session.query(TypeMotor).filter_by(status='A').all()

        data = [{
            'id': t.id,
            'kd_type': t.kode_type,
            'nama_type': t.nama_type,
            'ket_nomesin': t.prefix_nomesin or '',
            'ket_norangka': t.prefix_norangka or '',
            'harga_otr': float(t.otr) if t.otr else 0,
            'harga_dasar': float(t.harga_dasar) if t.harga_dasar else 0,
            'tgl_expired_harga': t.tgl_expired_harga.isoformat() if t.tgl_expired_harga else None,
        } for t in types]
        session.close()

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching type motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor/available', methods=['GET'])
def get_type_motor_with_stock():
    """Get only type motor that have available stock (status='R')"""
    try:
        from database.models import TypeMotor, StokMotor
        session = DatabaseManager.get_session()

        # Get all type motors that have stok with status='R'
        available_types = session.query(TypeMotor).join(
            StokMotor, StokMotor.type_id == TypeMotor.id
        ).filter(
            StokMotor.status == 'R'
        ).distinct().all()

        session.close()

        data = [{
            'id': t.id,
            'kd_type': t.kd_type,
            'nama_type': t.nama_type,
            'harga_otr': t.harga_otr,
            'harga_dasar': t.harga_dasar,
            'ket_nomesin': t.ket_nomesin,
            'ket_norangka': t.ket_norangka,
            'tgl_expired_harga': t.tgl_expired_harga.isoformat() if t.tgl_expired_harga else None,
        } for t in available_types]

        return jsonify({'data': data}), 200

    except Exception as e:
        logger.error(f"Error getting available type motors: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor/<int:type_id>', methods=['GET'])
def get_type_motor_detail(type_id):
    """Get type motor detail"""
    try:
        from database.models import TypeMotor
        session = DatabaseManager.get_session()
        type_motor = session.query(TypeMotor).filter_by(id=type_id).first()
        session.close()

        if not type_motor:
            return jsonify({'success': False, 'error': 'Type motor tidak ditemukan'}), 404

        data = {
            'id': type_motor.id,
            'kd_type': type_motor.kode_type,
            'nama_type': type_motor.nama_type,
            'ket_nomesin': type_motor.prefix_nomesin or '',
            'ket_norangka': type_motor.prefix_norangka or '',
            'harga_otr': float(type_motor.otr) if type_motor.otr else 0,
            'harga_dasar': float(type_motor.harga_dasar) if type_motor.harga_dasar else 0,
            'tgl_expired_harga': type_motor.tgl_expired_harga.isoformat() if type_motor.tgl_expired_harga else None,
        }

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching type motor detail: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor', methods=['POST'])
def create_type_motor():
    """Create new type motor"""
    try:
        data = request.json

        if not data.get('kd_type') or not data.get('nama_type'):
            return jsonify({'success': False, 'error': 'Kode Type dan Nama Type required'}), 400

        from database.models import TypeMotor
        session = DatabaseManager.get_session()

        # Parse tgl_expired_harga if provided
        tgl_expired = None
        if data.get('tgl_expired_harga'):
            try:
                tgl_expired = datetime.strptime(data['tgl_expired_harga'], '%Y-%m-%d').date()
            except:
                pass

        type_motor = TypeMotor(
            kode_type=data['kd_type'],
            nama_type=data['nama_type'],
            prefix_nomesin=data.get('ket_nomesin', ''),
            prefix_norangka=data.get('ket_norangka', ''),
            otr=data.get('harga_otr', 0),
            tgl_expired_harga=tgl_expired,
            status='A'
        )

        session.add(type_motor)
        session.commit()
        type_id = type_motor.id
        session.close()

        return jsonify({
            'success': True,
            'message': 'Type motor berhasil dibuat',
            'id': type_id
        }), 201

    except Exception as e:
        logger.error(f"Error creating type motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor/<int:type_id>', methods=['PUT'])
def update_type_motor(type_id):
    """Update type motor"""
    try:
        data = request.json

        from database.models import TypeMotor
        session = DatabaseManager.get_session()
        type_motor = session.query(TypeMotor).filter_by(id=type_id).first()

        if not type_motor:
            session.close()
            return jsonify({'success': False, 'error': 'Type motor tidak ditemukan'}), 404

        if 'kd_type' in data:
            type_motor.kode_type = data['kd_type']
        if 'nama_type' in data:
            type_motor.nama_type = data['nama_type']
        if 'ket_nomesin' in data:
            type_motor.prefix_nomesin = data['ket_nomesin']
        if 'ket_norangka' in data:
            type_motor.prefix_norangka = data['ket_norangka']
        if 'harga_otr' in data:
            type_motor.otr = data['harga_otr']
        if 'tgl_expired_harga' in data:
            if data['tgl_expired_harga']:
                try:
                    type_motor.tgl_expired_harga = datetime.strptime(data['tgl_expired_harga'], '%Y-%m-%d').date()
                except:
                    pass
            else:
                type_motor.tgl_expired_harga = None

        session.commit()
        session.close()

        return jsonify({
            'success': True,
            'message': 'Type motor berhasil diupdate',
            'id': type_id
        })

    except Exception as e:
        logger.error(f"Error updating type motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor/<int:type_id>', methods=['DELETE'])
def delete_type_motor(type_id):
    """Delete type motor"""
    try:
        from database.models import TypeMotor
        session = DatabaseManager.get_session()
        type_motor = session.query(TypeMotor).filter_by(id=type_id).first()

        if not type_motor:
            session.close()
            return jsonify({'success': False, 'error': 'Type motor tidak ditemukan'}), 404

        session.delete(type_motor)
        session.commit()
        session.close()

        return jsonify({
            'success': True,
            'message': 'Type motor berhasil dihapus'
        })

    except Exception as e:
        logger.error(f"Error deleting type motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor/import/excel', methods=['POST'])
def import_type_motor_excel():
    """Import type motor from Excel file (Harga OTR format)"""
    try:
        from business.type_motor_import_service import TypeMotorImportService

        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400

        # Validate file extension
        if not file.filename.lower().endswith(('xlsx', 'xls')):
            return jsonify({'success': False, 'error': 'File harus berformat Excel (.xlsx atau .xls)'}), 400

        # Save uploaded file temporarily
        filename = secure_filename(file.filename)
        temp_path = Path(app.config['UPLOAD_FOLDER']) / f"temp_{filename}"
        file.save(str(temp_path))

        # Get tgl_expired from form data if provided, otherwise default 1 month from today
        from datetime import date
        from dateutil.relativedelta import relativedelta

        tgl_expired_str = request.form.get('tgl_expired')
        tgl_expired = None
        if tgl_expired_str:
            try:
                tgl_expired = datetime.strptime(tgl_expired_str, '%Y-%m-%d').date()
            except:
                pass

        if tgl_expired is None:
            tgl_expired = date.today() + relativedelta(months=1)

        # Import using service
        import_service = TypeMotorImportService()
        result = import_service.import_from_excel(str(temp_path), tgl_expired)

        # Clean up temp file
        try:
            temp_path.unlink()
        except:
            pass

        return jsonify(result), (200 if result['success'] else 400)

    except Exception as e:
        logger.error(f"Error importing type motor: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# API - Stok Motor (Inventory)
# =====================================================================

@app.route('/api/stok-motor', methods=['GET'])
def get_stok_motor():
    """Get all stok motor with optional filters"""
    try:
        from database.models import StokMotor, TypeMotor, Dealer, StokTransfer, Broker
        from sqlalchemy import or_
        session = DatabaseManager.get_session()

        type_id = request.args.get('type_id')
        status = request.args.get('status')
        include_id = request.args.get('include_id')  # Include specific stok even if not status=R

        query = session.query(StokMotor)

        if type_id:
            type_id_int = int(type_id)
            query = query.filter_by(type_id=type_id_int)

            # If editing, also include the current stok (even if status != R)
            if include_id:
                include_id_int = int(include_id)
                if status:
                    query = query.filter(or_(
                        StokMotor.status == status,
                        StokMotor.id == include_id_int
                    ))
            else:
                if status:
                    query = query.filter_by(status=status)

        stoks = query.order_by(StokMotor.tgl_datang.desc()).all()

        data = []
        for s in stoks:
            type_name = s.type_motor.nama_type if s.type_motor else "N/A"
            dealer_name = s.dealer.nama if s.dealer else "-"

            # Get transfer/tujuan info if exists (active transfer)
            tujuan_name = None
            transfer = session.query(StokTransfer).filter(
                StokTransfer.stok_motor_id == s.id,
                StokTransfer.status == 'A'  # Active only
            ).first()

            if transfer:
                if transfer.dealer_tujuan_id:
                    tujuan = session.query(Dealer).filter_by(id=transfer.dealer_tujuan_id).first()
                    tujuan_name = tujuan.nama if tujuan else None
                elif transfer.broker_tujuan_id:
                    tujuan = session.query(Broker).filter_by(id=transfer.broker_tujuan_id).first()
                    tujuan_name = tujuan.nama if tujuan else None

            data.append({
                'id': s.id,
                'tanggal_datang': s.tgl_datang.isoformat(),
                'no_mesin': s.no_mesin,
                'no_rangka': s.no_rangka,
                'type_id': s.type_id,
                'type_nama': type_name,
                'warna': s.warna,
                'dealer_id': s.dealer_id,
                'dealer_nama': dealer_name,
                'status': s.status,
                'tujuan_nama': tujuan_name,  # Link/Ke Tujuan
            })

        session.close()
        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching stok motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/stok-motor/<int:stok_id>', methods=['GET'])
def get_stok_motor_detail(stok_id):
    """Get stok motor detail"""
    try:
        from database.models import StokMotor
        session = DatabaseManager.get_session()
        stok = session.query(StokMotor).filter_by(id=stok_id).first()

        if not stok:
            session.close()
            return jsonify({'success': False, 'error': 'Stok tidak ditemukan'}), 404

        data = {
            'id': stok.id,
            'tanggal_datang': stok.tgl_datang.isoformat(),
            'no_mesin': stok.no_mesin,
            'no_rangka': stok.no_rangka,
            'type_id': stok.type_id,
            'warna': stok.warna or '',
            'dealer_id': stok.dealer_id,
            'status': stok.status,
        }

        session.close()
        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching stok detail: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/stok-motor', methods=['POST'])
def create_stok_motor():
    """Create new stok motor"""
    try:
        from database.models import StokMotor
        data = request.json

        if not data.get('no_mesin') or not data.get('no_rangka'):
            return jsonify({'success': False, 'error': 'No. Mesin dan No. Rangka required'}), 400

        session = DatabaseManager.get_session()

        stok = StokMotor(
            no_mesin=data['no_mesin'],
            no_rangka=data['no_rangka'],
            type_id=data.get('type_id'),
            warna=data.get('warna'),
            dealer_id=data.get('dealer_id'),
            tgl_datang=datetime.strptime(data.get('tanggal_datang', datetime.now().isoformat()[:10]), '%Y-%m-%d').date(),
            status=data.get('status', 'R'),
        )

        session.add(stok)
        session.commit()
        stok_id = stok.id
        session.close()

        return jsonify({
            'success': True,
            'message': 'Stok motor berhasil dibuat',
            'id': stok_id
        }), 201

    except Exception as e:
        logger.error(f"Error creating stok motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/stok-motor/<int:stok_id>', methods=['PUT'])
def update_stok_motor(stok_id):
    """Update stok motor"""
    try:
        from database.models import StokMotor
        data = request.json
        session = DatabaseManager.get_session()

        stok = session.query(StokMotor).filter_by(id=stok_id).first()
        if not stok:
            session.close()
            return jsonify({'success': False, 'error': 'Stok tidak ditemukan'}), 404

        if 'no_mesin' in data:
            stok.no_mesin = data['no_mesin']
        if 'no_rangka' in data:
            stok.no_rangka = data['no_rangka']
        if 'type_id' in data:
            stok.type_id = data['type_id']
        if 'warna' in data:
            stok.warna = data['warna']
        if 'dealer_id' in data:
            stok.dealer_id = data['dealer_id']
        if 'status' in data:
            stok.status = data['status']
            stok.tgl_status = datetime.utcnow()

        session.commit()
        session.close()

        return jsonify({
            'success': True,
            'message': 'Stok motor berhasil diupdate',
            'id': stok_id
        })

    except Exception as e:
        logger.error(f"Error updating stok motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/stok-motor/<int:stok_id>', methods=['DELETE'])
def delete_stok_motor(stok_id):
    """Delete stok motor"""
    try:
        from database.models import StokMotor
        session = DatabaseManager.get_session()

        stok = session.query(StokMotor).filter_by(id=stok_id).first()
        if not stok:
            session.close()
            return jsonify({'success': False, 'error': 'Stok tidak ditemukan'}), 404

        session.delete(stok)
        session.commit()
        session.close()

        return jsonify({
            'success': True,
            'message': 'Stok motor berhasil dihapus'
        })

    except Exception as e:
        logger.error(f"Error deleting stok motor: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/type-motor/<int:type_id>/update-format', methods=['PUT'])
def update_type_motor_format(type_id):
    """Update type motor format suggestions (prefix for no. mesin dan no. rangka)"""
    try:
        from database.models import TypeMotor
        data = request.json

        session = DatabaseManager.get_session()
        type_motor = session.query(TypeMotor).filter_by(id=type_id).first()
        if not type_motor:
            session.close()
            return jsonify({'success': False, 'error': 'Type motor tidak ditemukan'}), 404

        # Store values before closing session
        old_nomesin = type_motor.prefix_nomesin
        old_norangka = type_motor.prefix_norangka

        # Update format prefixes
        if 'prefix_nomesin' in data:
            type_motor.prefix_nomesin = data['prefix_nomesin']
        if 'prefix_norangka' in data:
            type_motor.prefix_norangka = data['prefix_norangka']

        # Store new values
        new_nomesin = type_motor.prefix_nomesin
        new_norangka = type_motor.prefix_norangka

        session.commit()
        session.close()

        return jsonify({
            'success': True,
            'message': 'Format type motor berhasil diupdate',
            'id': type_id,
            'prefix_nomesin': new_nomesin,
            'prefix_norangka': new_norangka,
        })

    except Exception as e:
        logger.error(f"Error updating type motor format: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/stok-motor/import/excel', methods=['POST'])
def import_stok_motor_excel():
    """Import stok motor from Excel file (Distribusi format)"""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400

        # Validate file extension
        if not file.filename.lower().endswith(('xlsx', 'xls')):
            return jsonify({'success': False, 'error': 'File harus berformat Excel (.xlsx atau .xls)'}), 400

        # Save uploaded file temporarily
        filename = secure_filename(file.filename)
        temp_path = Path(app.config['UPLOAD_FOLDER']) / f"temp_{filename}"
        file.save(str(temp_path))

        # Get tgl_datang from form data if provided
        from datetime import date
        tgl_datang_str = request.form.get('tgl_datang')
        tgl_datang = None
        if tgl_datang_str:
            try:
                tgl_datang = datetime.strptime(tgl_datang_str, '%Y-%m-%d').date()
            except:
                pass

        # Auto-backup database before import (smart: skip if recent backup exists)
        try:
            from pathlib import Path as PathlibPath
            import shutil
            db_path = PathlibPath("data") / "jaya_motor.db"
            if db_path.exists():
                backup_dir = PathlibPath("backups")
                backup_dir.mkdir(exist_ok=True)

                # Check if recent backup exists (within 5 minutes)
                recent_backup_exists = False
                current_time = datetime.now().timestamp()
                for backup in backup_dir.glob("jaya_motor_*.db"):
                    backup_time = backup.stat().st_mtime
                    if current_time - backup_time < 300:  # 5 minutes
                        recent_backup_exists = True
                        logger.info(f"[Import] Recent backup exists, skipping new backup")
                        break

                if not recent_backup_exists:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_path = backup_dir / f"jaya_motor_{timestamp}.db"
                    shutil.copy2(db_path, backup_path)
                    logger.info(f"[Import] Backup created: {backup_path}")

                    # Cleanup old backups - keep only last 5
                    backups = sorted(backup_dir.glob("jaya_motor_*.db"), reverse=True)
                    for old_backup in backups[5:]:  # Delete backups beyond the 5th most recent
                        try:
                            old_backup.unlink()
                            logger.info(f"[Import] Deleted old backup: {old_backup.name}")
                        except:
                            pass
        except Exception as e:
            logger.warning(f"[Import] Backup failed: {e}")
            # Don't fail import if backup fails, just warn

        # Import using service
        import_service = ImportService()
        result = import_service.import_from_excel(str(temp_path), tgl_datang)

        # Clean up temp file
        try:
            temp_path.unlink()
        except:
            pass

        return jsonify(result), (200 if result['success'] else 400)

    except Exception as e:
        logger.error(f"Error importing stok motor: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# API - Laporan (Reports)
# =====================================================================

@app.route('/api/laporan/hutang-sales', methods=['GET'])
def get_hutang_sales_report():
    """Get sales debt report with broker summary and transaction details"""
    try:
        from database.connection import DatabaseManager
        from database.models import Transaksi, TransaksiDetail, Broker, StokMotor, TypeMotor

        broker_id = request.args.get('broker_id', type=int)
        status = request.args.get('status')  # 'paid', 'unpaid'
        start_date_str = request.args.get('start_date')

        session = DatabaseManager.get_session()

        # Build query for transaksi with hutang
        query = session.query(
            Transaksi.id.label('transaksi_id'),
            Transaksi.nota,
            Transaksi.tanggal.label('tanggal_nota'),
            Transaksi.nama_pembeli.label('customer_name'),
            Broker.nama.label('broker_nama'),
            Broker.tipe.label('broker_tipe'),
            TypeMotor.nama_type.label('motor_type'),
            TransaksiDetail.hutang_sales,
            TransaksiDetail.hutang_leasing,
            TransaksiDetail.tgl_hutang_dibayar
        ).join(TransaksiDetail).join(
            Broker, Transaksi.broker_id == Broker.id, isouter=True
        ).join(
            StokMotor, Transaksi.motor_id == StokMotor.id
        ).join(
            TypeMotor, StokMotor.type_id == TypeMotor.id
        ).filter(
            TransaksiDetail.hutang_sales > 0
        )

        if broker_id:
            query = query.filter(Transaksi.broker_id == broker_id)

        if status == 'paid':
            query = query.filter(TransaksiDetail.tgl_hutang_dibayar.isnot(None))
        elif status == 'unpaid':
            query = query.filter(TransaksiDetail.tgl_hutang_dibayar.is_(None))

        if start_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            query = query.filter(Transaksi.tanggal >= start_date)

        transaksi_list = query.order_by(Transaksi.tanggal.desc()).all()

        # Process detail transaksi
        detail_transaksi = []
        for t in transaksi_list:
            detail_transaksi.append({
                'transaksi_id': t.transaksi_id,
                'nota': t.nota,
                'tanggal_nota': t.tanggal_nota.isoformat(),
                'customer_name': t.customer_name,
                'broker_nama': t.broker_nama or '-',
                'motor_type': t.motor_type,
                'hutang_sales': float(t.hutang_sales),
                'hutang_leasing': float(t.hutang_leasing),
                'tgl_hutang_dibayar': t.tgl_hutang_dibayar.isoformat() if t.tgl_hutang_dibayar else None
            })

        # Build broker summary
        broker_summary_dict = {}
        for t in transaksi_list:
            broker_key = t.broker_nama or 'Tanpa Broker'
            if broker_key not in broker_summary_dict:
                broker_summary_dict[broker_key] = {
                    'broker_nama': broker_key,
                    'broker_tipe': t.broker_tipe or '-',
                    'jumlah_transaksi': 0,
                    'total_hutang': 0,
                    'hutang_belum_dibayar': 0,
                    'hutang_sudah_dibayar': 0
                }

            broker_summary_dict[broker_key]['jumlah_transaksi'] += 1
            broker_summary_dict[broker_key]['total_hutang'] += float(t.hutang_sales)

            if t.tgl_hutang_dibayar:
                broker_summary_dict[broker_key]['hutang_sudah_dibayar'] += float(t.hutang_sales)
            else:
                broker_summary_dict[broker_key]['hutang_belum_dibayar'] += float(t.hutang_sales)

        broker_summary = list(broker_summary_dict.values())

        # Calculate totals
        total_hutang = sum(t['total_hutang'] for t in broker_summary)
        hutang_belum_dibayar = sum(t['hutang_belum_dibayar'] for t in broker_summary)
        hutang_sudah_dibayar = sum(t['hutang_sudah_dibayar'] for t in broker_summary)

        summary = {
            'total_hutang': total_hutang,
            'hutang_belum_dibayar': hutang_belum_dibayar,
            'hutang_sudah_dibayar': hutang_sudah_dibayar,
            'total_transaksi': len(detail_transaksi)
        }

        session.close()

        return jsonify({
            'success': True,
            'data': {
                'summary': summary,
                'broker_summary': broker_summary,
                'detail_transaksi': detail_transaksi
            }
        })

    except Exception as e:
        logger.error(f"Error generating hutang sales report: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# API - Pindah Stok (Stock Transfer)
# =====================================================================

@app.route('/api/stok-motor-ready', methods=['GET'])
def get_stok_motor_ready():
    """Get stok motor with status Ready (R)"""
    try:
        from database.connection import DatabaseManager
        from database.models import StokMotor, TypeMotor, Dealer

        session = DatabaseManager.get_session()

        query = session.query(
            StokMotor.id,
            StokMotor.no_mesin,
            StokMotor.no_rangka,
            StokMotor.warna,
            TypeMotor.nama_type.label('motor_type'),
            Dealer.id.label('dealer_id'),
            Dealer.kode_dealer.label('dealer_kode'),
            Dealer.nama.label('dealer_name'),
        ).join(
            TypeMotor, StokMotor.type_id == TypeMotor.id
        ).join(
            Dealer, StokMotor.dealer_id == Dealer.id
        ).filter(
            StokMotor.status == 'R'  # Ready only
        ).order_by(StokMotor.tgl_datang.desc())

        stoks = query.all()

        data = []
        for s in stoks:
            data.append({
                'id': s.id,
                'no_mesin': s.no_mesin,
                'no_rangka': s.no_rangka,
                'warna': s.warna,
                'motor_type': s.motor_type,
                'dealer_id': s.dealer_id,
                'dealer_kode': s.dealer_kode,
                'dealer_name': s.dealer_name,
            })

        session.close()

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching stok ready: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/pindah-stok', methods=['GET'])
def get_pindah_stok():
    """Get stock transfer history"""
    try:
        from database.connection import DatabaseManager
        from database.models import StokTransfer, StokMotor, TypeMotor, Dealer, Broker

        status = request.args.get('status')  # A=Active, K=Kembali

        session = DatabaseManager.get_session()

        query = session.query(
            StokTransfer.id,
            StokTransfer.tgl_transfer,
            StokTransfer.tgl_kembali,
            StokTransfer.tipe_transfer,
            StokTransfer.driver,
            StokTransfer.status,
            StokTransfer.dealer_tujuan_id,
            StokTransfer.broker_tujuan_id,
            StokMotor.no_mesin,
            TypeMotor.nama_type.label('motor_type'),
            Dealer.nama.label('dealer_asal_name'),
        ).outerjoin(
            Dealer, StokTransfer.dealer_asal_id == Dealer.id
        ).join(
            StokMotor, StokTransfer.stok_motor_id == StokMotor.id
        ).join(
            TypeMotor, StokMotor.type_id == TypeMotor.id
        )

        if status:
            query = query.filter(StokTransfer.status == status)

        transfers = query.order_by(StokTransfer.tgl_transfer.desc()).all()

        # Load all dealers and brokers upfront
        dealer_ids = set(t.dealer_tujuan_id for t in transfers if t.dealer_tujuan_id)
        broker_ids = set(t.broker_tujuan_id for t in transfers if t.broker_tujuan_id)

        dealers_map = {}
        if dealer_ids:
            for dealer in session.query(Dealer).filter(Dealer.id.in_(dealer_ids)).all():
                dealers_map[dealer.id] = dealer.nama

        brokers_map = {}
        if broker_ids:
            for broker in session.query(Broker).filter(Broker.id.in_(broker_ids)).all():
                brokers_map[broker.id] = broker.nama

        data = []
        for t in transfers:
            data.append({
                'id': t.id,
                'tgl_transfer': t.tgl_transfer.isoformat(),
                'tgl_kembali': t.tgl_kembali.isoformat() if t.tgl_kembali else None,
                'tipe_transfer': t.tipe_transfer,
                'driver': t.driver,
                'status': t.status,
                'no_mesin': t.no_mesin,
                'motor_type': t.motor_type,
                'dealer_asal_name': t.dealer_asal_name,
                'dealer_tujuan_name': dealers_map.get(t.dealer_tujuan_id),
                'broker_tujuan_name': brokers_map.get(t.broker_tujuan_id),
            })

        session.close()

        return jsonify({'success': True, 'data': data})

    except Exception as e:
        logger.error(f"Error fetching pindah stok: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/pindah-stok', methods=['POST'])
def create_pindah_stok():
    """Create stock transfer record"""
    try:
        from database.connection import DatabaseManager
        from database.models import StokTransfer, StokMotor

        data = request.json

        # Validate required fields
        if not all([data.get('stok_motor_id'), data.get('tgl_transfer'), data.get('tipe_transfer')]):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400

        session = DatabaseManager.get_session()

        # Get motor
        motor = session.query(StokMotor).filter(
            StokMotor.id == data['stok_motor_id']
        ).first()

        if not motor:
            session.close()
            return jsonify({'success': False, 'error': 'Motor tidak ditemukan'}), 404

        if motor.status != 'R':
            session.close()
            return jsonify({'success': False, 'error': 'Motor tidak dalam status ready'}), 400

        # Create transfer record
        transfer = StokTransfer(
            stok_motor_id=motor.id,
            dealer_asal_id=motor.dealer_id,
            dealer_tujuan_id=data.get('dealer_tujuan_id'),
            broker_tujuan_id=data.get('broker_tujuan_id'),
            tgl_transfer=datetime.strptime(data['tgl_transfer'], '%Y-%m-%d').date(),
            tipe_transfer=data['tipe_transfer'],
            driver=data.get('driver'),
            catatan=data.get('catatan'),
            status='A'
        )

        session.add(transfer)
        session.commit()

        # Update motor status to 'T' (transferred)
        motor.status = 'T'
        session.commit()

        logger.info(f"[Pindah Stok] Motor {motor.no_mesin} dipindahkan")

        session.close()

        return jsonify({
            'success': True,
            'message': 'Stok berhasil dipindahkan',
            'id': transfer.id
        }), 201

    except Exception as e:
        logger.error(f"Error creating pindah stok: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/pindah-stok/<int:transfer_id>/kembali', methods=['POST'])
def return_pindah_stok(transfer_id):
    """Return stock to origin dealer"""
    try:
        from database.connection import DatabaseManager
        from database.models import StokTransfer

        data = request.json

        session = DatabaseManager.get_session()

        transfer = session.query(StokTransfer).filter(
            StokTransfer.id == transfer_id
        ).first()

        if not transfer:
            session.close()
            return jsonify({'success': False, 'error': 'Transfer tidak ditemukan'}), 404

        if transfer.status == 'K':
            session.close()
            return jsonify({'success': False, 'error': 'Stok sudah dikembalikan sebelumnya'}), 400

        # Mark as returned
        transfer.tgl_kembali = datetime.strptime(data['tgl_kembali'], '%Y-%m-%d').date()
        transfer.status = 'K'
        if data.get('catatan'):
            transfer.catatan = data['catatan']

        session.commit()

        # Update motor status back to 'R' (ready)
        motor = session.query(StokMotor).filter(
            StokMotor.id == transfer.stok_motor_id
        ).first()
        if motor:
            motor.status = 'R'
            session.commit()

        logger.info(f"[Pindah Stok] Motor (ID {transfer.stok_motor_id}) dikembalikan dari transfer")

        session.close()

        return jsonify({
            'success': True,
            'message': 'Stok berhasil dikembalikan ke dealer asal'
        })

    except Exception as e:
        logger.error(f"Error returning pindah stok: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# Wilayah Autocomplete API
# =====================================================================

@app.route('/api/wilayah/suggest', methods=['GET'])
def suggest_wilayah():
    """
    Suggest kelurahan, kecamatan, kabupaten based on user input
    Usage: /api/wilayah/suggest?type=kelurahan&q=search_text
           /api/wilayah/suggest?type=kecamatan&q=search_text&kelurahan=kelurahan_name
           /api/wilayah/suggest?type=kabupaten&q=search_text&kecamatan=kecamatan_name
    """
    try:
        from database.models import Transaksi

        wilayah_type = request.args.get('type', 'kelurahan')  # kelurahan, kecamatan, kabupaten
        search_q = request.args.get('q', '').lower().strip()
        filter_kelurahan = request.args.get('kelurahan', '').strip()
        filter_kecamatan = request.args.get('kecamatan', '').strip()

        session = DatabaseManager.get_session()

        if wilayah_type == 'kelurahan':
            # Get distinct kelurahan
            results = session.query(Transaksi.kelurahan_pembeli).distinct().filter(
                Transaksi.kelurahan_pembeli.isnot(None),
                Transaksi.kelurahan_pembeli != ''
            ).all()

            suggestions = [r[0] for r in results if search_q in r[0].lower()]

        elif wilayah_type == 'kecamatan':
            # Get kecamatan where kelurahan matches
            query = session.query(Transaksi.kecamatan_pembeli).distinct().filter(
                Transaksi.kecamatan_pembeli.isnot(None),
                Transaksi.kecamatan_pembeli != ''
            )

            if filter_kelurahan:
                query = query.filter(Transaksi.kelurahan_pembeli == filter_kelurahan)

            results = query.all()
            suggestions = [r[0] for r in results if search_q in r[0].lower()]

        elif wilayah_type == 'kabupaten':
            # Get kabupaten where kecamatan (and optionally kelurahan) matches
            query = session.query(Transaksi.kabupaten_pembeli).distinct().filter(
                Transaksi.kabupaten_pembeli.isnot(None),
                Transaksi.kabupaten_pembeli != ''
            )

            if filter_kecamatan:
                query = query.filter(Transaksi.kecamatan_pembeli == filter_kecamatan)

            if filter_kelurahan:
                query = query.filter(Transaksi.kelurahan_pembeli == filter_kelurahan)

            results = query.all()
            suggestions = [r[0] for r in results if search_q in r[0].lower()]
        else:
            suggestions = []

        session.close()
        return jsonify({'success': True, 'data': sorted(suggestions)})

    except Exception as e:
        logger.error(f"Error suggesting wilayah: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# Error Handlers
# =====================================================================

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'success': False, 'error': 'Route not found'}), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    logger.error(f"Server error: {e}")
    return jsonify({'success': False, 'error': 'Internal server error'}), 500


# =====================================================================
# Backup & Restore Routes
# =====================================================================

@app.route('/backup-restore', methods=['GET'])
def backup_restore_page():
    """Render backup/restore page"""
    return render_template('backup_restore.html')


@app.route('/api/backup-database', methods=['POST'])
def backup_database():
    """Manual backup database with custom destination"""
    try:
        data = request.get_json()
        destination = data.get('destination', 'default')
        custom_path = data.get('customPath', '')
        notes = data.get('notes', '')

        import shutil
        from pathlib import Path as PathlibPath

        db_path = PathlibPath("data") / "jaya_motor.db"
        if not db_path.exists():
            return jsonify({'success': False, 'error': 'Database tidak ditemukan'}), 404

        # Determine backup directory
        if destination == 'custom':
            if not custom_path:
                return jsonify({'success': False, 'error': 'Custom path tidak boleh kosong'}), 400
            backup_dir = PathlibPath(custom_path)
        else:
            backup_dir = PathlibPath("backups")

        # Create backup directory if not exists
        backup_dir.mkdir(parents=True, exist_ok=True)

        # Create backup file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        notes_suffix = f"_{notes.replace(' ', '_')}" if notes else ""
        backup_path = backup_dir / f"jaya_motor_{timestamp}{notes_suffix}.db"

        shutil.copy2(db_path, backup_path)
        logger.info(f"[Backup] Created: {backup_path}")

        return jsonify({
            'success': True,
            'backup_file': backup_path.name,
            'message': f'Backup berhasil dibuat: {backup_path.name}'
        }), 200

    except Exception as e:
        logger.error(f"[Backup] Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/list-backups', methods=['GET'])
def list_backups():
    """List 3 most recent backups with info"""
    try:
        from pathlib import Path as PathlibPath
        backup_dir = PathlibPath("backups")

        if not backup_dir.exists():
            return jsonify({'backups': []}), 200

        # Get all backups sorted by modification time (newest first)
        backups = sorted(
            backup_dir.glob("database_*.db"),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )[:3]  # Get only 3 most recent

        backup_list = []
        for backup in backups:
            size_mb = backup.stat().st_size / (1024 * 1024)
            mod_time = datetime.fromtimestamp(backup.stat().st_mtime)
            date_str = mod_time.strftime('%d-%m-%Y %H:%M:%S')

            backup_list.append({
                'filename': backup.name,
                'size': f'{size_mb:.1f} MB',
                'date': date_str,
                'timestamp': mod_time.isoformat()
            })

        return jsonify({'backups': backup_list}), 200

    except Exception as e:
        logger.error(f"[List Backups] Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/restore-database', methods=['POST'])
def restore_database():
    """Restore database from backup"""
    try:
        data = request.get_json()
        backup_filename = data.get('backup_file')

        if not backup_filename:
            return jsonify({'success': False, 'error': 'Backup file tidak ditentukan'}), 400

        import shutil
        from pathlib import Path as PathlibPath

        backup_path = PathlibPath("backups") / backup_filename
        db_path = PathlibPath("data") / "jaya_motor.db"

        if not backup_path.exists():
            return jsonify({'success': False, 'error': 'Backup file tidak ditemukan'}), 404

        # Backup current database before restore
        if db_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            current_backup = PathlibPath("backups") / f"jaya_motor_current_{timestamp}.db"
            current_backup.parent.mkdir(exist_ok=True)
            shutil.copy2(db_path, current_backup)
            logger.info(f"[Restore] Current database backed up to: {current_backup}")

        # Restore from backup
        shutil.copy2(backup_path, db_path)
        logger.info(f"[Restore] Database restored from: {backup_path}")

        # Close all database connections
        DatabaseManager.close_all_connections()

        return jsonify({
            'success': True,
            'message': 'Database berhasil di-restore'
        }), 200

    except Exception as e:
        logger.error(f"[Restore] Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


# =====================================================================
# Main
# =====================================================================

if __name__ == '__main__':
    logger.info(f"Starting {APP_TITLE} Web App v{APP_VERSION}")
    logger.info("Running on http://localhost:5000")
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
