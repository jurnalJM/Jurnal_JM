# JayaMotor - Modern Motor Sales Management System

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-Proprietary-red)

## 📋 Overview

JayaMotor adalah aplikasi modern untuk manajemen penjualan dan pembiayaan motor. Aplikasi ini adalah rewrite dari sistem VB6 lama dengan teknologi Python dan SQLite, menghadirkan interface yang modern dan fungsionalitas yang lebih baik.

### Fitur Utama

✨ **Manajemen Transaksi**
- Pencatatan transaksi penjualan motor
- Edit dan hapus data transaksi
- Status tracking (Pending, Approved, Paid, Cancelled)
- Historical notes dan audit trail

📊 **Filtering & Reporting**
- Filter berdasarkan tanggal, dealer, customer
- Search by name atau nomor handphone
- Export ke Excel dengan formatting otomatis
- Print laporan dalam format PDF
- Summary statistics dan totals

🚗 **Vehicle Management**
- Master data type motor
- Inventory tracking
- Vehicle details (chassis, engine, color)

💰 **Financial Tracking**
- Down Payment (DP) management
- Subsidi calculation
- Diskon & diskon tambahan
- Insentif penjual
- Leasing company integration
- Payment schedule & pelunasan

📄 **Document Management**
- BPKB (Ownership certificate)
- License plate number
- STNK & Insurance documents
- Delivery notes

---

## 🛠️ Technology Stack

### Frontend
- **Framework**: PyQt6 (Professional GUI)
- **Styling**: QSS (Qt Style Sheets)
- **Charts**: (Future: PyQtGraph)

### Backend
- **Language**: Python 3.11+
- **ORM**: SQLAlchemy 2.0
- **Database**: SQLite 3

### Data Processing
- **Excel Export**: openpyxl
- **PDF Generation**: ReportLab
- **Data Analysis**: pandas

### Development
- **Testing**: pytest, pytest-qt
- **Code Quality**: pylint, black, flake8
- **Version Control**: Git
- **Package**: PyInstaller (for executable)

---

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Windows 7/10/11 (macOS and Linux support via PyQt6)

### Setup Steps

#### 1. Clone Repository
```bash
cd C:\JayaMotor-Python
# atau clone dari git
git clone <repository-url>
cd JayaMotor-Python
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Setup Configuration
```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env with your settings (optional, defaults work fine)
# edit .env
```

#### 5. Initialize Database
```bash
python -c "from database.schema import initialize_database; initialize_database()"
```

This will:
- Create SQLite database at `data/jaya_motor.db`
- Create all tables with proper schema
- Load initial master data (dealers, leasing companies, etc.)

#### 6. Run Application
```bash
python main.py
```

---

## 📂 Project Structure

```
JayaMotor-Python/
├── database/                 # Database layer
│   ├── models.py            # SQLAlchemy ORM models
│   ├── connection.py        # Database connection management
│   ├── schema.py            # Schema creation & migrations
│   ├── repository.py        # Data access layer
│   └── migrations/          # Database migrations
│
├── business/                 # Business logic layer
│   ├── transaksi_service.py # Transaction services
│   ├── dealer_service.py    # Dealer management
│   ├── report_service.py    # Reporting logic
│   └── validators.py        # Data validation
│
├── ui/                       # User interface layer
│   ├── main_window.py       # Main application window
│   ├── dialogs/             # Dialog windows
│   ├── widgets/             # Custom widgets
│   ├── styles/              # QSS stylesheets
│   └── resources/           # Icons & images
│
├── utils/                    # Utilities
│   ├── excel_export.py      # Excel export
│   ├── pdf_report.py        # PDF generation
│   └── logger.py            # Logging setup
│
├── tests/                    # Unit & integration tests
│   ├── test_models.py
│   ├── test_services.py
│   └── test_ui.py
│
├── docs/                     # Documentation
├── scripts/                  # Utility scripts
├── data/                     # Data files (DB, backups, exports)
├── config.py                 # Central configuration
├── main.py                   # Application entry point
└── requirements.txt          # Python dependencies
```

---

## 🚀 Usage

### Starting the Application

```bash
# Activate virtual environment (if not already active)
.\venv\Scripts\activate

# Run the application
python main.py
```

The main window will open with the following sections:
1. **Toolbar** - Date range picker, search button, print/new buttons
2. **Filter Panel** - Dealer, name/phone search, status filter
3. **Data Grid** - Transaction list with all details
4. **Action Buttons** - Add, edit, delete, export, print, notes

### Common Tasks

#### Creating New Transaction
1. Click "Tambah Data" button
2. Fill in transaction details:
   - General: Nota, Dealer, Customer info
   - Vehicle: Motor type, chassis, engine number
   - Financial: DP, subsidi, diskon
   - Documents: BPKB, license plate, etc.
3. Click "Simpan"

#### Searching Transactions
1. Set date range using date pickers
2. Select dealer from dropdown
3. Enter customer name or phone number
4. Choose status filter
5. Click "Terapkan Filter" button

#### Exporting to Excel
1. Apply desired filters
2. Click "Export Excel" button
3. File will be saved to Documents folder
4. Opens automatically in Excel

#### Printing Reports
1. Select data to print
2. Click "Cetak" (Print) button
3. Choose printer settings
4. Print!

---

## 🧪 Testing

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_transaksi_service.py -v
```

### Run with Coverage
```bash
pytest --cov=. --cov-report=html
```

Coverage report will be in `htmlcov/index.html`

### Run UI Tests
```bash
pytest tests/test_ui.py -v
```

---

## 📊 Database

### SQLite Database Location
- **Development**: `data/jaya_motor.db`
- **Backups**: `data/backups/` (auto-created daily)
- **Exports**: `data/exports/` (user exports)

### Database Tables
- `dealer` - Dealer/cabang master data
- `broker` - Broker/intermediary data
- `leasing` - Leasing company data
- `type_motor` - Motor type master
- `stok_motor` - Vehicle inventory
- `transaksi` - Main transactions
- `transaksi_detail` - Transaction financial details
- `dokumen` - Transaction documents
- `catatan` - Historical notes
- `pembayaran` - Payment records
- `admin_log` - Audit trail

See `docs/DATABASE_SCHEMA.md` for detailed schema documentation.

---

## 🔧 Configuration

### Key Settings (in `config.py`)

| Setting | Default | Description |
|---------|---------|-------------|
| `DEBUG` | False | Enable debug logging |
| `THEME` | "light" | UI theme (light/dark) |
| `WINDOW_WIDTH` | 1600 | Main window width |
| `WINDOW_HEIGHT` | 900 | Main window height |
| `ENABLE_AUTO_BACKUP` | True | Auto backup database |
| `AUTO_BACKUP_INTERVAL` | 3600 | Backup interval (seconds) |

Override defaults by setting environment variables in `.env` file.

---

## 🐛 Troubleshooting

### Database Lock Error
**Problem**: "Database is locked"

**Solution**:
1. Close all instances of the application
2. Delete `.db-wal` file in data folder if exists
3. Restart application

### Missing Dependencies
**Problem**: "ModuleNotFoundError: No module named 'PyQt6'"

**Solution**:
```bash
pip install -r requirements.txt --upgrade
```

### Port Already in Use
**Problem**: Application won't start, port error

**Solution**: (Only if using network features)
1. Check what's using the port: `netstat -ano | findstr :PORT`
2. Kill the process: `taskkill /PID <PID> /F`

---

## 📈 Performance Tips

1. **Database Queries**
   - Use filters to reduce data loaded
   - Enable pagination for large datasets
   - Create indexes on frequently searched fields

2. **UI Responsiveness**
   - Long operations run in background threads
   - Progress indicators for bulk operations
   - Lazy loading for data grids

3. **Memory Usage**
   - Close unused dialogs
   - Clear export cache regularly
   - Monitor with Task Manager

---

## 🔐 Security

### Features
- ✅ Database encryption (optional)
- ✅ Audit trail for all changes
- ✅ No hardcoded credentials
- ✅ Parameterized queries (SQL injection prevention)
- ✅ Input validation on all forms

### Best Practices
1. **Backup Regularly**
   - Enable auto-backup in config
   - Backup location: `data/backups/`

2. **Access Control** (if multi-user)
   - Use strong passwords
   - Regularly audit logs

3. **Data Protection**
   - Encrypt sensitive fields
   - Restrict database file permissions

---

## 📝 Development

### Code Style
Follow PEP 8 guidelines. Enforce with:
```bash
black .           # Auto-format code
pylint business   # Check code quality
flake8 .          # Lint check
```

### Adding Features
1. Create feature branch: `git checkout -b feature/my-feature`
2. Implement feature with tests
3. Ensure all tests pass: `pytest`
4. Submit pull request

### Creating Executable
```bash
pyinstaller --onefile --windowed main.py
```

Executable will be in `dist/main.exe`

---

## 📚 Documentation

- [API Documentation](docs/API.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [Architecture Guide](docs/ARCHITECTURE.md)
- [User Manual](docs/USER_GUIDE.md)

---

## 🐛 Known Issues

- [ ] Dark mode not fully implemented (UI redesign in progress)
- [ ] PDF export fonts may vary by system
- [ ] Large datasets (>100k) may need optimization

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

---

## 📞 Support

For issues, questions, or suggestions:
1. Check FAQ in documentation
2. Review existing issues
3. Create new issue with details

---

## 📄 License

This project is proprietary software owned by Jaya Motor.
Unauthorized copying, modification, or distribution is prohibited.

---

## 🙏 Acknowledgments

- Original VB6 application development team
- PyQt6 community
- SQLAlchemy developers

---

## 📈 Project Status

**Current Version**: 2.0.0 (Development)

**Changelog**:
- 2.0.0 (2024) - Python rewrite, SQLite migration
- 1.0.0 (2017) - Original VB6 version

---

**Last Updated**: 2024-01-XX  
**Maintained by**: Development Team

