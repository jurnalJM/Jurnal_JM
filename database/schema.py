"""
Database Schema Initialization
Creates all tables and initializes with seed data
"""

from datetime import datetime, date

from database.connection import DatabaseManager
from database.models import Base, Dealer, TypeMotor, Leasing, Broker, StokMotor


def initialize_database(database_url: str = None):
    """
    Initialize the database with tables and seed data.

    Args:
        database_url: SQLAlchemy database URL (optional)

    Returns:
        True if successful
    """
    print("🔧 Initializing database...")

    # Initialize connection
    DatabaseManager.initialize(database_url)
    print("✓ Database connection established")

    # Drop all tables first
    print("📊 Dropping existing tables...")
    DatabaseManager.drop_all_tables()
    print("✓ All tables dropped")

    # Create all tables
    print("📊 Creating tables...")
    DatabaseManager.create_all_tables()
    print("✓ All tables created")

    # Seed initial data
    print("🌱 Seeding initial data...")
    seed_master_data()
    print("✓ Initial data seeded")

    print("✅ Database initialization complete!\n")
    return True


def seed_master_data():
    """Seed master data (dealers, types, leasing, brokers)"""

    with DatabaseManager.session_context() as session:
        # =====================================================================
        # DEALERS
        # =====================================================================
        dealers = [
            Dealer(
                kode_dealer="A0035",
                nama="Jaya Motor 1",
                alamat="Jl. Merdeka No. 123",
                kota="Jakarta",
                telp="021-123-4567",
                kontak_person="Budi Santoso",
                email="pusat@jayamotor.com",
                status="A",
            ),
            Dealer(
                kode_dealer="A0105",
                nama="Jaya Motor 2",
                alamat="Jl. Serpong No. 45",
                kota="Tangerang Selatan",
                telp="021-789-0123",
                kontak_person="Siti Nurhaliza",
                email="bsd@jayamotor.com",
                status="A",
            ),
            Dealer(
                kode_dealer="A0210",
                nama="Jaya Motor Bekasi",
                alamat="Jl. Harapan No. 67",
                kota="Bekasi",
                telp="021-456-7890",
                kontak_person="Ahmad Wijaya",
                email="bekasi@jayamotor.com",
                status="A",
            ),
        ]

        for dealer in dealers:
            existing = session.query(Dealer).filter_by(nama=dealer.nama).first()
            if not existing:
                session.add(dealer)
                print(f"  ✓ Added dealer: {dealer.nama}")

        session.commit()

        # =====================================================================
        # MOTOR TYPES
        # =====================================================================
        types = [
            TypeMotor(
                kode_type="H-CB150",
                nama_type="Honda CB 150",
                merek="Honda",
                cc=150,
                tahun_produksi=2024,
                otr=24500000,
                harga_dasar=23500000,
                harga_beli=21000000,
                warna_tersedia="Merah, Hitam, Putih, Biru",
                prefix_nomesin="MH1JMF217",
                prefix_norangka="JMF2F182",
                status="A",
            ),
            TypeMotor(
                kode_type="Y-MX130",
                nama_type="Yamaha MX 130",
                merek="Yamaha",
                cc=130,
                tahun_produksi=2024,
                otr=18900000,
                harga_dasar=18000000,
                harga_beli=16000000,
                warna_tersedia="Merah, Hitam, Putih",
                prefix_nomesin="5Y1JE236",
                prefix_norangka="JYM4NF18",
                status="A",
            ),
            TypeMotor(
                kode_type="S-AX100",
                nama_type="Suzuki Axelo 100",
                merek="Suzuki",
                cc=100,
                tahun_produksi=2024,
                otr=16500000,
                harga_dasar=15800000,
                harga_beli=14000000,
                warna_tersedia="Merah, Hitam, Putih, Biru, Emas",
                prefix_nomesin="RS2JE219",
                prefix_norangka="JSMTME18",
                status="A",
            ),
            TypeMotor(
                kode_type="K-REVO100",
                nama_type="Kawasaki Revo 100",
                merek="Kawasaki",
                cc=100,
                tahun_produksi=2024,
                otr=15800000,
                harga_dasar=15000000,
                harga_beli=13500000,
                warna_tersedia="Hitam, Putih, Merah",
                prefix_nomesin="KE140FR",
                prefix_norangka="JKAVNF18",
                status="A",
            ),
        ]

        for motor_type in types:
            existing = (
                session.query(TypeMotor)
                .filter_by(kode_type=motor_type.kode_type)
                .first()
            )
            if not existing:
                session.add(motor_type)
                print(f"  ✓ Added type: {motor_type.nama_type}")

        session.commit()

        # =====================================================================
        # LEASING COMPANIES
        # =====================================================================
        leasings = [
            Leasing(
                kode="BCA",
                nama="BCA Finance",
                alamat="Jl. MH Thamrin, Jakarta",
                kota="Jakarta",
                telp="021-111-2222",
                kontak_person="Ibu Sinta",
                email="bca@finance.com",
                max_tenor=60,
                bunga_default=7.5,
                status="A",
            ),
            Leasing(
                kode="MANDIRI",
                nama="Mandiri Finance",
                alamat="Jl. Sudirman, Jakarta",
                kota="Jakarta",
                telp="021-333-4444",
                kontak_person="Bapak Hanif",
                email="mandiri@finance.com",
                max_tenor=60,
                bunga_default=8.0,
                status="A",
            ),
            Leasing(
                kode="PERMATA",
                nama="Permata Finance",
                alamat="Jl. Gatot Subroto, Jakarta",
                kota="Jakarta",
                telp="021-555-6666",
                kontak_person="Ibu Rani",
                email="permata@finance.com",
                max_tenor=60,
                bunga_default=8.5,
                status="A",
            ),
            Leasing(
                kode="FIF",
                nama="Federal International Finance",
                alamat="Jl. Pancasila, Jakarta",
                kota="Jakarta",
                telp="021-777-8888",
                kontak_person="Pak Adi",
                email="fif@finance.com",
                max_tenor=60,
                bunga_default=8.2,
                status="A",
            ),
        ]

        for leasing in leasings:
            existing = session.query(Leasing).filter_by(kode=leasing.kode).first()
            if not existing:
                session.add(leasing)
                print(f"  ✓ Added leasing: {leasing.nama}")

        session.commit()

        # =====================================================================
        # BROKERS
        # =====================================================================
        brokers = [
            Broker(
                nama="PT Mitra Bisnis Sukses",
                alamat="Jl. Raya Bogor No. 100",
                kota="Jakarta",
                telp="021-999-0000",
                kontak_person="Pak Hendra",
                email="mitrabs@broker.com",
                tipe="B",
                status="A",
            ),
            Broker(
                nama="CV Jaya Perkasa",
                alamat="Jl. Kemang No. 50",
                kota="Jakarta",
                telp="021-888-7777",
                kontak_person="Ibu Dewi",
                email="jayaperkasa@broker.com",
                tipe="B",
                status="A",
            ),
            Broker(
                nama="PT Sentosa Jaya",
                alamat="Jl. Cipete No. 25",
                kota="Jakarta Selatan",
                telp="021-777-6666",
                kontak_person="Pak Wono",
                email="sentosajaya@broker.com",
                tipe="B",
                status="A",
            ),
        ]

        for broker in brokers:
            existing = session.query(Broker).filter_by(nama=broker.nama).first()
            if not existing:
                session.add(broker)
                print(f"  ✓ Added broker: {broker.nama}")

        session.commit()

        # =====================================================================
        # STOK MOTOR (Inventory)
        # =====================================================================
        stoks = [
            StokMotor(
                no_mesin="MH1JMF217TK23372",
                no_rangka="JMF2F18236291",
                type_id=1,  # Honda CB 150
                warna="Merah",
                dealer_id=1,
                tgl_datang=date(2026, 7, 15),
                status="R",
            ),
            StokMotor(
                no_mesin="MH1JMF217TK23373",
                no_rangka="JMF2F18236292",
                type_id=1,  # Honda CB 150
                warna="Hitam",
                dealer_id=1,
                tgl_datang=date(2026, 7, 15),
                status="R",
            ),
            StokMotor(
                no_mesin="5Y1JE236AB45678",
                no_rangka="JYM4NF18AB12345",
                type_id=2,  # Yamaha MX 130
                warna="Putih",
                dealer_id=2,
                tgl_datang=date(2026, 7, 18),
                status="R",
            ),
            StokMotor(
                no_mesin="RS2JE219CD89012",
                no_rangka="JSMTME18CD56789",
                type_id=3,  # Suzuki Axelo 100
                warna="Biru",
                dealer_id=2,
                tgl_datang=date(2026, 7, 20),
                status="R",
            ),
            StokMotor(
                no_mesin="KE140FREF34567",
                no_rangka="JKAVNF18EF01234",
                type_id=4,  # Kawasaki Revo 100
                warna="Merah",
                dealer_id=3,
                tgl_datang=date(2026, 7, 10),
                status="R",
            ),
        ]

        for stok in stoks:
            existing = session.query(StokMotor).filter_by(no_mesin=stok.no_mesin).first()
            if not existing:
                session.add(stok)
                print(f"  ✓ Added stok: {stok.no_mesin}")

        session.commit()

        print("\n✅ All seed data loaded successfully!")


def drop_all_tables():
    """
    Drop all tables from database.
    WARNING: This is destructive and only for development/testing!
    """
    print("⚠️  WARNING: Dropping all database tables...")
    response = input("Are you sure? Type 'yes' to confirm: ")

    if response.lower() == "yes":
        DatabaseManager.drop_all_tables()
        print("✓ All tables dropped")
    else:
        print("❌ Operation cancelled")


def reset_database(database_url: str = None):
    """
    Reset database - drop all tables and recreate from scratch.

    Args:
        database_url: SQLAlchemy database URL (optional)
    """
    print("🔄 Resetting database...")
    drop_all_tables()
    initialize_database(database_url)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        reset_database()
    else:
        initialize_database()
