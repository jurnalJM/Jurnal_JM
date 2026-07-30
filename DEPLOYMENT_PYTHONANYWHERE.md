# Deployment Guide - PythonAnywhere

## Setup Steps

### 1. Login ke PythonAnywhere
- Buka https://www.pythonanywhere.com
- Login dengan account JurnalJM
- Akses Bash console

### 2. Clone Repository
```bash
cd /home/JurnalJM
git clone https://github.com/jurnalJM/Jurnal_JM.git
cd Jurnal_JM
```

### 3. Create Virtual Environment
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements-web.txt
```

### 5. Setup Environment Variables
```bash
# Copy example dan edit
cp .env.example .env

# Edit .env dengan nano/vim
nano .env
```

Pastikan isi:
```
FLASK_APP=app.py
FLASK_ENV=production
DATABASE_URL=sqlite:////home/JurnalJM/Jurnal_JM/jayamotor.db
SECRET_KEY=your-secret-key-here
```

### 6. Create WSGI Configuration
Buat file: `/home/JurnalJM/Jurnal_JM/wsgi.py`

```python
import sys
import os

# Add project folder to path
sys.path.insert(0, '/home/JurnalJM/Jurnal_JM')

# Set environment
os.environ['FLASK_ENV'] = 'production'

# Import and create app
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

**TAPI:** Cek apakah `app.py` sudah punya `create_app()` function. Jika langsung `app = Flask(__name__)`, edit WSGI:

```python
import sys
sys.path.insert(0, '/home/JurnalJM/Jurnal_JM')

from app import app
```

### 7. Configure Web App di PythonAnywhere Dashboard

1. Buka **Web** tab di dashboard
2. Click **Add a new web app**
3. Pilih **Manual configuration**
4. Pilih Python 3.11
5. Di WSGI configuration file, set path ke:
   ```
   /home/JurnalJM/Jurnal_JM/wsgi.py
   ```

6. Di **Virtualenv** section, set:
   ```
   /home/JurnalJM/Jurnal_JM/venv
   ```

7. Di **Source code** section, set:
   ```
   /home/JurnalJM/Jurnal_JM
   ```

8. Click **Reload** web app

### 8. Configure Static & Media Files (Optional)
Jika ada static files:

1. Di Web tab, cari **Static files** section
2. Add mapping:
   - URL: `/static/`
   - Directory: `/home/JurnalJM/Jurnal_JM/static`

### 9. Test Aplikasi
- Buka https://JurnalJM.pythonanywhere.com
- Cek apakah loading OK

### 10. Troubleshooting

**Error: ModuleNotFoundError**
```bash
# Re-check virtual env active
source venv/bin/activate
pip list  # Cek apakah semua dependency terinstall
```

**Error: Database not found**
```bash
# Database path di .env harus absolute path
DATABASE_URL=sqlite:////home/JurnalJM/Jurnal_JM/jayamotor.db
```

**Error: Import app failed**
- Check app.py apakah ada syntax error
- Run: `python app.py` untuk test

**Reload tidak berubah**
- Cek error log di Web tab → Error log
- Clear cache browser (Ctrl+Shift+Delete)

## Database Migration

Jika perlu initialize database:
```bash
cd /home/JurnalJM/Jurnal_JM
source venv/bin/activate
python
>>> from database.connection import DatabaseManager
>>> from database.models import Base
>>> engine = DatabaseManager.get_engine()
>>> Base.metadata.create_all(engine)
```

## Update Code dari GitHub

```bash
cd /home/JurnalJM/Jurnal_JM
git pull origin main
# Reload web app di dashboard
```

## Useful Commands

```bash
# View web app error log
tail -f /var/log/JurnalJM.pythonanywhere.com.error.log

# Restart web app
# (Use dashboard Web tab → Reload)

# SSH into app
# ssh JurnalJM@ssh.pythonanywhere.com
```

---

**Support:**
- PythonAnywhere Help: https://help.pythonanywhere.com
- Flask Docs: https://flask.palletsprojects.com
