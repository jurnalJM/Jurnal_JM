"""
SQLAlchemy ORM Models
Defines all database tables and relationships
"""

from datetime import datetime, date
from typing import Optional, List

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Numeric,
    DateTime,
    Date,
    Text,
    Boolean,
    ForeignKey,
    UniqueConstraint,
    CheckConstraint,
    Index,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Dealer(Base):
    """Master data for dealers/branches"""

    __tablename__ = "dealer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode_dealer = Column(String(10), unique=True, index=True)  # A0035, A0105, etc
    nama = Column(String(100), nullable=False, unique=True, index=True)
    alamat = Column(String(100))
    kota = Column(String(50))
    telp = Column(String(25))
    kontak_person = Column(String(100))
    email = Column(String(100))
    status = Column(String(1), default="A", nullable=False)  # A=Active, I=Inactive
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    transaksis = relationship("Transaksi", back_populates="dealer")
    stok_motors = relationship("StokMotor", back_populates="dealer")

    __table_args__ = (
        CheckConstraint("status IN ('A', 'I')", name="check_dealer_status"),
        Index("idx_dealer_nama", "nama"),
        Index("idx_dealer_status", "status"),
    )

    def __repr__(self):
        return f"<Dealer(id={self.id}, nama='{self.nama}')>"


class Broker(Base):
    """Master data for brokers/intermediaries"""

    __tablename__ = "broker"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(100), nullable=False, unique=True, index=True)
    alamat = Column(String(100))
    kota = Column(String(50))
    telp = Column(String(25))
    kontak_person = Column(String(100))
    email = Column(String(100))
    tipe = Column(String(1), default="B", nullable=False)  # B=Broker, S=Sales/Mitra, L=Leasing Partner
    status = Column(String(1), default="A", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    transaksis = relationship("Transaksi", back_populates="broker")

    __table_args__ = (
        CheckConstraint("tipe IN ('B', 'S', 'L')", name="check_broker_tipe"),
        CheckConstraint("status IN ('A', 'I')", name="check_broker_status"),
        Index("idx_broker_nama", "nama"),
    )

    def __repr__(self):
        return f"<Broker(id={self.id}, nama='{self.nama}')>"


class Leasing(Base):
    """Master data for leasing companies"""

    __tablename__ = "leasing"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode = Column(String(25), unique=True, nullable=False, index=True)
    nama = Column(String(100), nullable=False, index=True)
    alamat = Column(String(100))
    kota = Column(String(50))
    telp = Column(String(25))
    kontak_person = Column(String(100))
    email = Column(String(100))
    max_tenor = Column(Integer, default=60)  # Max financing period in months
    bunga_default = Column(Numeric(5, 2), default=8.5)  # Default interest rate
    status = Column(String(1), default="A", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships

    __table_args__ = (
        CheckConstraint("status IN ('A', 'I')", name="check_leasing_status"),
        Index("idx_leasing_kode", "kode"),
        Index("idx_leasing_nama", "nama"),
    )

    def __repr__(self):
        return f"<Leasing(id={self.id}, kode='{self.kode}', nama='{self.nama}')>"


class TypeMotor(Base):
    """Master data for motor types"""

    __tablename__ = "type_motor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode_type = Column(String(20), unique=True, nullable=False)
    nama_type = Column(String(100), nullable=False, index=True)
    merek = Column(String(50), index=True)  # Honda, Yamaha, Suzuki, etc
    cc = Column(Integer)  # Engine size
    tahun_produksi = Column(Integer)
    otr = Column(Numeric(15, 2))  # On The Road price (selling price)
    harga_dasar = Column(Numeric(15, 2))  # Base price (without subsidy)
    harga_beli = Column(Numeric(15, 2))  # Buying price from supplier
    warna_tersedia = Column(String(200))  # Comma-separated list
    prefix_nomesin = Column(String(50))  # Format awal nomor mesin (prefix)
    prefix_norangka = Column(String(50))  # Format awal nomor rangka (prefix)
    tgl_expired_harga = Column(Date)  # Tanggal expired harga OTR
    status = Column(String(1), default="A", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    stok_motors = relationship("StokMotor", back_populates="type_motor")

    __table_args__ = (
        CheckConstraint("status IN ('A', 'I')", name="check_type_motor_status"),
        Index("idx_type_motor_nama", "nama_type"),
        Index("idx_type_motor_merek", "merek"),
    )

    def __repr__(self):
        return f"<TypeMotor(id={self.id}, nama='{self.nama_type}')>"


class StokMotor(Base):
    """Vehicle inventory/stock"""

    __tablename__ = "stok_motor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    no_mesin = Column(String(25), unique=True, nullable=False, index=True)
    no_rangka = Column(String(25), unique=True, nullable=False, index=True)
    type_id = Column(Integer, ForeignKey("type_motor.id"), nullable=False)
    warna = Column(String(50))
    tahun_produksi = Column(Integer)
    tgl_datang = Column(Date, nullable=False)
    dealer_id = Column(Integer, ForeignKey("dealer.id"))
    status = Column(String(1), default="R", nullable=False, index=True)  # R=Ready, S=Sold, T=Transfer, D=Defect
    tgl_status = Column(DateTime)
    catatan = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    type_motor = relationship("TypeMotor", back_populates="stok_motors")
    dealer = relationship("Dealer", back_populates="stok_motors")
    transaksi = relationship("Transaksi", back_populates="motor", uselist=False)
    transfer_history = relationship("StokTransfer", back_populates="stok_motor")

    __table_args__ = (
        CheckConstraint("status IN ('R', 'S', 'T', 'D')", name="check_stok_status"),
        Index("idx_stok_no_mesin", "no_mesin"),
        Index("idx_stok_no_rangka", "no_rangka"),
        Index("idx_stok_status", "status"),
        Index("idx_stok_dealer", "dealer_id"),
    )

    def __repr__(self):
        return f"<StokMotor(id={self.id}, no_mesin='{self.no_mesin}')>"


class Transaksi(Base):
    """Main transaction table - sales of motors"""

    __tablename__ = "transaksi"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota = Column(String(50), unique=True, nullable=False, index=True)  # Transaction number
    tanggal = Column(Date, nullable=False, index=True)  # Transaction date
    dealer_id = Column(Integer, ForeignKey("dealer.id"), nullable=False, index=True)

    # Customer data
    nama_pembeli = Column(String(100), nullable=False)
    alamat_pembeli = Column(String(100))
    kelurahan_pembeli = Column(String(100))  # Kel.
    kecamatan_pembeli = Column(String(100))  # Kec.
    kabupaten_pembeli = Column(String(100))  # Kab.
    telp_pembeli = Column(String(25))
    email_pembeli = Column(String(100))

    # Notification letter (after delivery) - for BPKB/STNK document
    no_surat_pemberitahuan = Column(String(50))  # Notification letter number (e.g., "SU-2026-001")
    tgl_surat_pemberitahuan = Column(Date)  # Notification letter date

    # BPKB/STNK document name & address (if different from pembeli)
    nama_surat = Column(String(100))  # Name on BPKB/STNK (if different from nama_pembeli)
    alamat_surat = Column(String(100))  # Address on BPKB/STNK (if different)
    kelurahan_surat = Column(String(100))  # Kel. on BPKB/STNK
    kecamatan_surat = Column(String(100))  # Kec. on BPKB/STNK
    kabupaten_surat = Column(String(100))  # Kab. on BPKB/STNK

    # Vehicle reference
    motor_id = Column(Integer, ForeignKey("stok_motor.id"), nullable=False)

    # Broker data
    broker_id = Column(Integer, ForeignKey("broker.id"))

    # Invoice from Main Dealer
    no_faktur = Column(String(50))  # Invoice number from main dealer
    tgl_faktur = Column(Date)  # Invoice date
    file_faktur = Column(String(255))  # Path to uploaded invoice file (PDF, PNG, JPG)

    # STNK/Vehicle Registration Data
    no_polisi = Column(String(20))  # License plate number
    tgl_biro = Column(Date)  # Date received from Biro Jasa (license plate processing agency)
    no_bpkb = Column(String(50))  # BPKB (vehicle registration) number
    tgl_terima_bpkb = Column(Date)  # Date BPKB received (STNK & BPKB may arrive separately)
    tgl_serah_terima = Column(Date)  # Motor handover/delivery date to customer

    # Leasing data
    leasing_id = Column(Integer, ForeignKey("leasing.id"))

    # Status
    status_transaksi = Column(
        String(1), default="D", nullable=False, index=True
    )  # D=Draft, P=Pending Approval, A=Approved/Posted, L=Paid, C=Cancelled
    tanggal_po = Column(String(25))  # "Acc" or PO date

    # Audit
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    dealer = relationship("Dealer", back_populates="transaksis")
    motor = relationship("StokMotor", back_populates="transaksi")
    broker = relationship("Broker", back_populates="transaksis")
    detail = relationship(
        "TransaksiDetail",
        back_populates="transaksi",
        uselist=False,
        cascade="all, delete-orphan",
    )
    dokumens = relationship(
        "Dokumen", back_populates="transaksi", cascade="all, delete-orphan"
    )
    catatan_list = relationship(
        "Catatan", back_populates="transaksi", cascade="all, delete-orphan"
    )
    pembayaran_list = relationship(
        "Pembayaran", back_populates="transaksi", cascade="all, delete-orphan"
    )
    pembayaran_hutang_list = relationship(
        "PembayaranHutang", cascade="all, delete-orphan", foreign_keys="PembayaranHutang.transaksi_id"
    )

    __table_args__ = (
        CheckConstraint(
            "status_transaksi IN ('D', 'P', 'A', 'L', 'C')", name="check_transaksi_status"
        ),
        Index("idx_transaksi_nota", "nota"),
        Index("idx_transaksi_tanggal", "tanggal"),
        Index("idx_transaksi_dealer", "dealer_id"),
        Index("idx_transaksi_status", "status_transaksi"),
    )

    def __repr__(self):
        return f"<Transaksi(id={self.id}, nota='{self.nota}')>"


class TransaksiDetail(Base):
    """Financial details of transaction"""

    __tablename__ = "transaksi_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaksi_id = Column(Integer, ForeignKey("transaksi.id"), nullable=False, unique=True)

    # Pricing
    harga_dasar = Column(Numeric(15, 2), default=0)
    otr = Column(Numeric(15, 2), default=0)  # On-The-Road price from master type motor

    # Payment method
    sistem_pembayaran = Column(String(20), default="Cash")  # Cash or Kredit
    ketentuan_dp = Column(Numeric(15, 2), default=0)  # Cash: auto from OTR, Kredit: manual

    # Down Payment
    dp = Column(Numeric(15, 2), default=0)
    tgl_bayar_dp = Column(Date)  # Date when DP is paid
    ket_dp = Column(Text)

    # Subsidi
    subsidi = Column(Numeric(15, 2), default=0)

    # Discount (AHM/Dealer/Leasing)
    diskon_ahm = Column(Numeric(15, 2), default=0)  # AHM / Main Dealer discount
    diskon_dealer = Column(Numeric(15, 2), default=0)  # Dealer discount
    diskon_leasing = Column(Numeric(15, 2), default=0)  # Leasing / AHM discount

    # Incentive
    insentif = Column(Numeric(15, 2), default=0)

    # Leasing info
    leasing_id = Column(Integer, ForeignKey("leasing.id"))  # Selected leasing company

    # Debt tracking
    hutang_sales = Column(Numeric(15, 2), default=0)  # Sales/Broker debt = Ketentuan DP (Cash=0, Kredit=DP amount)
    hutang_leasing = Column(Numeric(15, 2), default=0)  # Leasing debt = OTR - Ketentuan DP (Cash=0, Kredit=sisa)
    total_terbayar = Column(Numeric(15, 2), default=0)  # Total amount paid so far
    status_hutang = Column(String(20), default="Belum")  # Belum/Cicilan/Lunas
    tgl_hutang_dibayar = Column(Date)  # When debt to sales is FULLY paid

    # Payment
    tgl_lunas = Column(Date)
    pelunasan = Column(Numeric(15, 2), default=0)

    # Misc
    lain_lain = Column(Numeric(15, 2), default=0)

    # Audit
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    transaksi = relationship("Transaksi", back_populates="detail")
    leasing = relationship("Leasing", foreign_keys=[leasing_id])

    def __repr__(self):
        return f"<TransaksiDetail(id={self.id}, transaksi_id={self.transaksi_id})>"


class PembayaranHutang(Base):
    """Payment history for sales debt (hutang_sales)"""

    __tablename__ = "pembayaran_hutang"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaksi_id = Column(Integer, ForeignKey("transaksi.id"), nullable=False, index=True)

    # Payment details
    nominal = Column(Numeric(15, 2), nullable=False)  # Payment amount
    tgl_pembayaran = Column(Date, nullable=False)  # Payment date
    metode = Column(String(50))  # Method: Cash, Transfer, Check, etc
    keterangan = Column(Text)  # Notes

    # Status after this payment
    sisa_hutang = Column(Numeric(15, 2), default=0)  # Remaining debt after this payment
    status = Column(String(20), default="A")  # A=Active/Recorded, K=Cancelled

    # Audit
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String(100))  # Who recorded this payment

    __table_args__ = (
        Index("idx_pembayaran_hutang_transaksi", "transaksi_id"),
        Index("idx_pembayaran_hutang_tgl", "tgl_pembayaran"),
    )

    def __repr__(self):
        return f"<PembayaranHutang(id={self.id}, transaksi_id={self.transaksi_id}, nominal={self.nominal})>"


class Dokumen(Base):
    """Transaction documents (BPKB, license plate, etc)"""

    __tablename__ = "dokumen"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaksi_id = Column(Integer, ForeignKey("transaksi.id"), nullable=False)
    tipe_dokumen = Column(
        String(50)
    )  # BPKB, POLISI, STNK, FAKTUR, SURAT_JALAN, ASURANSI
    nomor_dokumen = Column(String(50))
    tgl_terbit = Column(Date)
    tgl_berlaku = Column(Date)
    path_file = Column(String(255))  # File location
    catatan = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    transaksi = relationship("Transaksi", back_populates="dokumens")

    __table_args__ = (
        Index("idx_dokumen_transaksi", "transaksi_id"),
        Index("idx_dokumen_tipe", "tipe_dokumen"),
    )

    def __repr__(self):
        return f"<Dokumen(id={self.id}, tipe='{self.tipe_dokumen}')>"


class Catatan(Base):
    """Historical notes for transaction"""

    __tablename__ = "catatan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaksi_id = Column(Integer, ForeignKey("transaksi.id"), nullable=False)
    tgl_catatan = Column(DateTime, default=datetime.utcnow)
    konten = Column(Text, nullable=False)
    tipe_catatan = Column(
        String(50)
    )  # HISTORIS, FOLLOW_UP, MASALAH, PEMBAYARAN, etc
    dibuat_oleh = Column(String(100))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    transaksi = relationship("Transaksi", back_populates="catatan_list")

    __table_args__ = (
        Index("idx_catatan_transaksi", "transaksi_id"),
        Index("idx_catatan_tgl", "tgl_catatan"),
    )

    def __repr__(self):
        return f"<Catatan(id={self.id}, transaksi_id={self.transaksi_id})>"


class Pembayaran(Base):
    """Payment records for transactions"""

    __tablename__ = "pembayaran"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaksi_id = Column(Integer, ForeignKey("transaksi.id"), nullable=False)
    no_cicilan = Column(Integer)  # 0 = lump sum, 1,2,3 = installments
    tgl_pembayaran = Column(Date, index=True)
    jumlah = Column(Numeric(15, 2), nullable=False)
    tipe_pembayaran = Column(String(50))  # DP, CICILAN, LUNAS, etc
    metode = Column(String(50))  # TUNAI, TRANSFER, CEK, CARD
    referensi = Column(String(100))  # Transfer reference, check number, etc
    status = Column(String(1), default="C", nullable=False, index=True)  # C=Confirmed, P=Pending
    catatan = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    transaksi = relationship("Transaksi", back_populates="pembayaran_list")

    __table_args__ = (
        CheckConstraint("status IN ('C', 'P')", name="check_pembayaran_status"),
        Index("idx_pembayaran_transaksi", "transaksi_id"),
        Index("idx_pembayaran_tgl", "tgl_pembayaran"),
        Index("idx_pembayaran_status", "status"),
    )

    def __repr__(self):
        return f"<Pembayaran(id={self.id}, transaksi_id={self.transaksi_id})>"


class StokTransfer(Base):
    """Stock transfer history between dealers/brokers"""

    __tablename__ = "stok_transfer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stok_motor_id = Column(Integer, ForeignKey("stok_motor.id"), nullable=False, index=True)
    dealer_asal_id = Column(Integer, ForeignKey("dealer.id"), nullable=False)
    dealer_tujuan_id = Column(Integer, ForeignKey("dealer.id"), nullable=True)
    broker_tujuan_id = Column(Integer, ForeignKey("broker.id"), nullable=True)

    tgl_transfer = Column(Date, nullable=False, index=True)
    tipe_transfer = Column(String(20), nullable=False)  # PINDAH (transfer), PINJAM (loan), SERAH (handover)
    driver = Column(String(100))
    catatan = Column(Text)

    # Return/reversal info
    tgl_kembali = Column(Date)  # When returned to origin
    status = Column(String(1), default="A", nullable=False, index=True)  # A=Active (transferred), K=Kembali (returned)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    stok_motor = relationship("StokMotor", back_populates="transfer_history")
    dealer_asal = relationship("Dealer", foreign_keys=[dealer_asal_id])
    dealer_tujuan = relationship("Dealer", foreign_keys=[dealer_tujuan_id])
    broker_tujuan = relationship("Broker")

    __table_args__ = (
        CheckConstraint("status IN ('A', 'K')", name="check_transfer_status"),
        CheckConstraint("tipe_transfer IN ('PINDAH', 'PINJAM', 'SERAH')", name="check_transfer_type"),
        Index("idx_transfer_motor", "stok_motor_id"),
        Index("idx_transfer_asal", "dealer_asal_id"),
        Index("idx_transfer_tgl", "tgl_transfer"),
    )

    def __repr__(self):
        return f"<StokTransfer(id={self.id}, motor_id={self.stok_motor_id})>"


class AdminLog(Base):
    """Audit trail for all changes"""

    __tablename__ = "admin_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tgl_aksi = Column(DateTime, default=datetime.utcnow, index=True)
    user_id = Column(String(100))
    tabel = Column(String(50), index=True)
    tipe_aksi = Column(String(10))  # INSERT, UPDATE, DELETE
    record_id = Column(Integer)
    nilai_lama = Column(Text)  # JSON format
    nilai_baru = Column(Text)  # JSON format
    ip_address = Column(String(50))
    user_agent = Column(String(255))

    __table_args__ = (
        Index("idx_log_tgl", "tgl_aksi"),
        Index("idx_log_tabel", "tabel"),
    )

    def __repr__(self):
        return f"<AdminLog(id={self.id}, tabel='{self.tabel}', tipe='{self.tipe_aksi}')>"
