"""
JayaMotor Configuration Settings
All application settings are centralized here
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# APPLICATION INFO
# ============================================================================
APP_NAME = "JayaMotor"
APP_VERSION = "2.0.0"
APP_TITLE = "JayaMotor - Sistem Manajemen Penjualan Motor"
AUTHOR = "Development Team"
COMPANY = "Jaya Motor"

# ============================================================================
# PATHS
# ============================================================================
# Project root directory
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"
SCRIPTS_DIR = BASE_DIR / "scripts"

# Database file location
DATABASE_PATH = DATA_DIR / "jaya_motor.db"
BACKUP_DIR = DATA_DIR / "backups"
EXPORT_DIR = DATA_DIR / "exports"

# Ensure directories exist
for dir_path in [DATA_DIR, BACKUP_DIR, EXPORT_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================
# Database URL for SQLAlchemy
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{DATABASE_PATH}"
)

# Database settings
DB_ECHO = os.getenv("DB_ECHO", "False").lower() == "true"  # Log SQL queries
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "10"))
DB_MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", "20"))

# Require TLS for the DB connection (needed for TiDB Cloud / most managed MySQL)
DB_SSL_REQUIRED = os.getenv("DB_SSL_REQUIRED", "False").lower() == "true"

# Enable foreign keys in SQLite
DB_ENABLE_FK = True

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================
# Debug mode
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = DATA_DIR / "app.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_MAX_BYTES = 10485760  # 10 MB
LOG_BACKUP_COUNT = 5

# ============================================================================
# GUI SETTINGS
# ============================================================================
# Window dimensions
WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", "1600"))
WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", "900"))
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 700

# Theme
THEME = os.getenv("THEME", "light")  # light or dark
ENABLE_DARK_MODE = os.getenv("ENABLE_DARK_MODE", "True").lower() == "true"

# Font settings
DEFAULT_FONT_FAMILY = "Segoe UI"
DEFAULT_FONT_SIZE = 10
MONOSPACE_FONT_FAMILY = "Courier New"

# Colors (can be overridden by theme)
PRIMARY_COLOR = "#2196F3"
SECONDARY_COLOR = "#17A2B8"
SUCCESS_COLOR = "#28A745"
WARNING_COLOR = "#FFC107"
ERROR_COLOR = "#DC3545"
NEUTRAL_COLOR = "#6C757D"

# ============================================================================
# UI CONFIGURATION
# ============================================================================
# Data grid settings
DATAGRID_ROW_HEIGHT = 25
DATAGRID_HEADER_HEIGHT = 30
DATAGRID_PAGE_SIZE = 100  # Items per page
DATAGRID_ENABLE_PAGINATION = True

# Dialog settings
DIALOG_WIDTH = 900
DIALOG_HEIGHT = 700

# Button sizes
BUTTON_HEIGHT = 35
BUTTON_WIDTH = 120

# ============================================================================
# EXPORT SETTINGS
# ============================================================================
# Excel export
EXCEL_SHEET_NAME = "Transaksi"
EXCEL_INCLUDE_SUMMARY = True
EXCEL_DATE_FORMAT = "DD-MMM-YY"
EXCEL_NUMBER_FORMAT = "#,##0"
EXCEL_CURRENCY_FORMAT = "#,##0.00"

# PDF export
PDF_PAGE_SIZE = "A4"
PDF_ORIENTATION = "landscape"  # portrait or landscape
PDF_MARGIN_TOP = 20
PDF_MARGIN_BOTTOM = 20
PDF_MARGIN_LEFT = 20
PDF_MARGIN_RIGHT = 20

# ============================================================================
# BACKUP SETTINGS
# ============================================================================
# Auto backup
ENABLE_AUTO_BACKUP = os.getenv("ENABLE_AUTO_BACKUP", "True").lower() == "true"
AUTO_BACKUP_INTERVAL = int(os.getenv("AUTO_BACKUP_INTERVAL", "3600"))  # seconds (1 hour)
BACKUP_RETENTION_DAYS = int(os.getenv("BACKUP_RETENTION_DAYS", "30"))

# ============================================================================
# FEATURE FLAGS
# ============================================================================
# Enable/disable features
FEATURE_EXPORT_EXCEL = True
FEATURE_EXPORT_PDF = True
FEATURE_PRINT = True
FEATURE_DARK_MODE = True
FEATURE_AUTO_BACKUP = ENABLE_AUTO_BACKUP
FEATURE_AUDIT_LOG = True

# ============================================================================
# VALIDATION SETTINGS
# ============================================================================
# Field constraints
MAX_TEXT_LENGTH = 255
MAX_NOTES_LENGTH = 1000
MAX_DECIMAL_PLACES = 2
MAX_CURRENCY_VALUE = 9999999999.99

# Date range for transactions
MIN_TRANSACTION_DATE_OFFSET_YEARS = 5  # Can look back 5 years
MAX_TRANSACTION_DATE_OFFSET_DAYS = 30  # Can date transactions up to 30 days in future

# ============================================================================
# IMPORT/EXPORT SETTINGS
# ============================================================================
# MSSQL Migration (for data import from old system)
MSSQL_DSN = os.getenv("MSSQL_DSN", "Softtech")
MSSQL_CONNECTION_STRING = os.getenv(
    "MSSQL_CONNECTION_STRING",
    f"mssql+pyodbc://@{MSSQL_DSN}?driver=ODBC+Driver+17+for+SQL+Server"
)

# ============================================================================
# SECURITY SETTINGS
# ============================================================================
# Password hashing (if implementing authentication later)
PASSWORD_MIN_LENGTH = 8
PASSWORD_REQUIRE_UPPERCASE = True
PASSWORD_REQUIRE_LOWERCASE = True
PASSWORD_REQUIRE_DIGITS = True
PASSWORD_REQUIRE_SPECIAL = False

# Session timeout (in minutes)
SESSION_TIMEOUT_MINUTES = 60

# ============================================================================
# REPORT SETTINGS
# ============================================================================
# Report templates
REPORT_INCLUDE_LOGOS = True
REPORT_INCLUDE_FOOTER = True
REPORT_INCLUDE_PAGE_NUMBERS = True
REPORT_COMPANY_NAME = COMPANY
REPORT_COMPANY_ADDRESS = "Address here"
REPORT_COMPANY_PHONE = "Phone here"

# ============================================================================
# DEBUG & DEVELOPMENT SETTINGS
# ============================================================================
if DEBUG:
    DB_ECHO = True
    LOG_LEVEL = "DEBUG"

# ============================================================================
# VALIDATION & CONSTRAINTS
# ============================================================================
# Transaction status codes
TRANSACTION_STATUS_PENDING = "P"      # Pending approval
TRANSACTION_STATUS_APPROVED = "A"     # Approved
TRANSACTION_STATUS_PAID = "L"         # Lunas (fully paid)
TRANSACTION_STATUS_CANCELLED = "C"    # Cancelled

TRANSACTION_STATUS_CHOICES = {
    TRANSACTION_STATUS_PENDING: "Pending",
    TRANSACTION_STATUS_APPROVED: "Disetujui",
    TRANSACTION_STATUS_PAID: "Lunas",
    TRANSACTION_STATUS_CANCELLED: "Dibatalkan",
}

# Motor status codes
MOTOR_STATUS_READY = "R"      # Ready for sale
MOTOR_STATUS_SOLD = "S"       # Sold
MOTOR_STATUS_TRANSFER = "T"   # Transfer to other dealer
MOTOR_STATUS_DEFECT = "D"     # Defective

MOTOR_STATUS_CHOICES = {
    MOTOR_STATUS_READY: "Siap Jual",
    MOTOR_STATUS_SOLD: "Terjual",
    MOTOR_STATUS_TRANSFER: "Transfer",
    MOTOR_STATUS_DEFECT: "Rusak",
}

# Dealer status codes
DEALER_STATUS_ACTIVE = "A"
DEALER_STATUS_INACTIVE = "I"

DEALER_STATUS_CHOICES = {
    DEALER_STATUS_ACTIVE: "Aktif",
    DEALER_STATUS_INACTIVE: "Tidak Aktif",
}

# Document types
DOC_TYPE_BPKB = "BPKB"              # Vehicle ownership
DOC_TYPE_POLISI = "POLISI"          # License plate
DOC_TYPE_STNK = "STNK"              # Vehicle registration
DOC_TYPE_FAKTUR = "FAKTUR"          # Invoice
DOC_TYPE_SURAT_JALAN = "SURAT_JALAN"  # Delivery note
DOC_TYPE_ASURANSI = "ASURANSI"      # Insurance

DOC_TYPE_CHOICES = {
    DOC_TYPE_BPKB: "BPKB",
    DOC_TYPE_POLISI: "No. Polisi",
    DOC_TYPE_STNK: "STNK",
    DOC_TYPE_FAKTUR: "Faktur",
    DOC_TYPE_SURAT_JALAN: "Surat Jalan",
    DOC_TYPE_ASURANSI: "Asuransi",
}

# Payment method types
PAYMENT_METHOD_CASH = "CASH"
PAYMENT_METHOD_TRANSFER = "TRANSFER"
PAYMENT_METHOD_CHECK = "CHECK"
PAYMENT_METHOD_CARD = "CARD"

PAYMENT_METHOD_CHOICES = {
    PAYMENT_METHOD_CASH: "Tunai",
    PAYMENT_METHOD_TRANSFER: "Transfer Bank",
    PAYMENT_METHOD_CHECK: "Cek",
    PAYMENT_METHOD_CARD: "Kartu Kredit",
}

# ============================================================================
# PRINT SETTINGS
# ============================================================================
# Printer configuration
PRINTER_NAME = os.getenv("PRINTER_NAME", None)  # Default printer
PRINT_TO_PDF = os.getenv("PRINT_TO_PDF", "False").lower() == "true"

# ============================================================================
# API/INTEGRATION SETTINGS (for future use)
# ============================================================================
# External service integrations (if needed)
ENABLE_SMS_NOTIFICATIONS = False
SMS_PROVIDER_API_KEY = os.getenv("SMS_PROVIDER_API_KEY", "")

ENABLE_EMAIL_NOTIFICATIONS = False
SMTP_SERVER = os.getenv("SMTP_SERVER", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL", "noreply@jayamotor.com")

# ============================================================================
# VERIFICATION
# ============================================================================
def verify_configuration():
    """Verify that all required paths exist and configuration is valid"""
    issues = []

    # Check if database directory exists
    if not DATA_DIR.exists():
        issues.append(f"Data directory not found: {DATA_DIR}")

    # Check if database URL is valid
    if not DATABASE_URL:
        issues.append("DATABASE_URL is not configured")

    # Check if window dimensions are reasonable
    if WINDOW_WIDTH < WINDOW_MIN_WIDTH or WINDOW_HEIGHT < WINDOW_MIN_HEIGHT:
        issues.append(
            f"Window dimensions too small. Min: {WINDOW_MIN_WIDTH}x{WINDOW_MIN_HEIGHT}"
        )

    if issues:
        print("⚠️  Configuration Issues:")
        for issue in issues:
            print(f"   - {issue}")
        return False

    return True


# Auto-verify on import
if __name__ == "__main__":
    verify_configuration()
    print("✓ Configuration loaded successfully")
    print(f"  Database: {DATABASE_PATH}")
    print(f"  App Version: {APP_VERSION}")
    print(f"  Debug Mode: {DEBUG}")
