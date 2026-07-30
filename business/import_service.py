"""
Import Service for Excel-based Stok Motor import
Handles parsing and validation of distribusi Excel files
"""

from datetime import date
from typing import List, Dict, Any, Tuple
import openpyxl

from database.connection import DatabaseManager
from database.models import StokMotor, TypeMotor
from database.import_config import get_dealer_id
from business.exceptions import ValidationException


class ImportService:
    """Service for importing stok motor from Excel files"""

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.validated_rows = []
        self.type_motor_suggestions = {}  # Suggestions for type motor format

    def import_from_excel(self, file_path: str, tgl_datang: date = None) -> Dict[str, Any]:
        """
        Import stok motor from Excel file

        Args:
            file_path: Path to Excel file
            tgl_datang: Default tanggal masuk (if not in Excel)

        Returns:
            Dict with results, errors, warnings
        """
        self.errors = []
        self.warnings = []
        self.validated_rows = []

        if tgl_datang is None:
            tgl_datang = date.today()

        try:
            # Read Excel file
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active

            # Parse and validate rows
            for row_num, row in enumerate(ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=False), 1):
                values = [cell.value for cell in row]

                # Skip empty rows
                if not any(values):
                    continue

                result = self._parse_row(row_num, values, tgl_datang)
                if result:
                    self.validated_rows.append(result)

            # Import validated rows
            imported_count = 0
            if self.validated_rows and not self.errors:
                imported_count = self._insert_to_database(self.validated_rows)

            # Enhance suggestions with type motor info
            suggestions_enhanced = []
            if self.type_motor_suggestions:
                suggestion_session = DatabaseManager.get_session()
                for type_id, suggestion in self.type_motor_suggestions.items():
                    type_motor = suggestion_session.query(TypeMotor).filter_by(id=type_id).first()
                    if type_motor:
                        suggestions_enhanced.append({
                            'type_id': type_id,
                            'type_kode': type_motor.kode_type,
                            'type_nama': type_motor.nama_type,
                            'prefix_norangka': suggestion['prefix_norangka'],
                            'prefix_nomesin': suggestion['prefix_nomesin'],
                        })
                suggestion_session.close()

            return {
                'success': len(self.errors) == 0,
                'imported': imported_count,
                'total': len(self.validated_rows),
                'errors': self.errors,
                'warnings': self.warnings,
                'preview': self.validated_rows[:5],  # First 5 rows for preview
                'type_motor_suggestions': suggestions_enhanced,  # Format suggestions for master type
            }

        except Exception as e:
            self.errors.append(f"Failed to read Excel file: {str(e)}")
            return {
                'success': False,
                'imported': 0,
                'total': 0,
                'errors': self.errors,
                'warnings': self.warnings,
            }

    def _parse_row(self, row_num: int, values: List, tgl_datang: date) -> Dict[str, Any]:
        """
        Parse and validate a single row from Excel

        Excel columns:
        A: Nama Dealer
        B: Nomor Rangka (tanpa prefix)
        C: Nomor Mesin
        D: Kode Type (ML1F, MJ1E, dll)
        E: Kode Warna (BW, BL, BK, dll atau nama warna)
        F: Kode Dealer (A0035, A0105, dll)
        """
        if len(values) < 6:
            self.errors.append(f"Row {row_num}: Tidak cukup kolom (harus 6)")
            return None

        nama_dealer = values[0]
        no_rangka_base = values[1]
        no_mesin = values[2]
        kode_type = values[3]
        warna = values[4]
        kode_dealer = values[5]

        # Validate required fields
        if not no_rangka_base:
            self.errors.append(f"Row {row_num}: Nomor Rangka kosong")
            return None
        if not no_mesin:
            self.errors.append(f"Row {row_num}: Nomor Mesin kosong")
            return None
        if not kode_type:
            self.errors.append(f"Row {row_num}: Kode Type kosong")
            return None
        if not kode_dealer:
            self.errors.append(f"Row {row_num}: Kode Dealer kosong")
            return None

        # Map dealer
        dealer_id = get_dealer_id(str(kode_dealer).strip())
        if not dealer_id:
            self.errors.append(f"Row {row_num}: Kode Dealer '{kode_dealer}' tidak dikenali")
            return None

        # Get or create type motor based on kode_type
        type_id = self._get_or_create_type_motor(str(kode_type).strip())
        if not type_id:
            self.errors.append(f"Row {row_num}: Gagal memproses Type '{kode_type}'")
            return None

        # Use warna value directly from Excel (no mapping needed)
        warna_value = str(warna).strip() if warna else ''

        # Format nomor rangka (tambah MH1 prefix)
        no_rangka = f"MH1{no_rangka_base.strip()}"

        return {
            'row_num': row_num,
            'nama_dealer': nama_dealer,
            'no_mesin': no_mesin.strip(),
            'no_rangka': no_rangka,
            'type_id': type_id,
            'warna': warna_value,
            'dealer_id': dealer_id,
            'tgl_datang': tgl_datang,
            'status': 'R',  # Ready
        }

    def _get_or_create_type_motor(self, kode_type: str) -> int:
        """
        Get TypeMotor ID if exists, or create new one if not exists

        Returns type_id or None if failed
        """
        session = DatabaseManager.get_session()
        try:
            # Check if type already exists
            existing = session.query(TypeMotor).filter_by(kode_type=kode_type).first()
            if existing:
                return existing.id

            # Create new type motor with basic info
            new_type = TypeMotor(
                kode_type=kode_type,
                nama_type=kode_type,  # Use kode as nama if not found
                status='A',
            )
            session.add(new_type)
            session.commit()
            type_id = new_type.id
            session.close()

            self.warnings.append(f"Type motor baru dibuat: {kode_type}")
            return type_id

        except Exception as e:
            self.errors.append(f"Error processing type motor '{kode_type}': {str(e)}")
            session.close()
            return None

    def _insert_to_database(self, rows: List[Dict]) -> int:
        """Insert validated rows to database and collect type motor suggestions"""
        session = DatabaseManager.get_session()
        imported = 0

        try:
            for row_data in rows:
                # Check if already exists
                existing = session.query(StokMotor).filter_by(
                    no_mesin=row_data['no_mesin'],
                    no_rangka=row_data['no_rangka']
                ).first()

                if existing:
                    self.warnings.append(
                        f"Row {row_data['row_num']}: "
                        f"Unit {row_data['no_mesin']} sudah ada di database"
                    )
                    continue

                # Collect suggestions for type motor format
                type_id = row_data['type_id']
                if type_id not in self.type_motor_suggestions:
                    self.type_motor_suggestions[type_id] = {
                        'prefix_nomesin': row_data['no_mesin'][:5],      # First 5 digits
                        'prefix_norangka': row_data['no_rangka'][:7],    # First 7 digits
                    }

                # Create new stok motor
                stok = StokMotor(
                    no_mesin=row_data['no_mesin'],
                    no_rangka=row_data['no_rangka'],
                    type_id=row_data['type_id'],
                    warna=row_data['warna'],
                    dealer_id=row_data['dealer_id'],
                    tgl_datang=row_data['tgl_datang'],
                    status=row_data['status'],
                )
                session.add(stok)
                imported += 1

            session.commit()
        except Exception as e:
            session.rollback()
            self.errors.append(f"Database error: {str(e)}")
        finally:
            session.close()

        return imported
