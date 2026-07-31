# End-to-End Testing Guide - JayaMotor Transaksi System

Panduan lengkap untuk test integrasi semua komponen sistem transaksi.

---

## 🧪 TEST 1: CREATE TRANSAKSI BARU

### Setup
1. Buka aplikasi di browser: `http://localhost:5000/transaksi`
2. Click button "+ Tambah Transaksi" (atau FAB button)
3. Form modal terbuka

### Test Steps

#### 1.1 Fill Form Dasar
- [ ] **No. Nota:** Isi dengan "TEST-001"
- [ ] **Tanggal Nota:** Pilih tanggal hari ini
- [ ] **Nama Pelanggan:** "Uji Coba Test"
- [ ] **No. HP:** "08123456789"
- [ ] **Alamat:** "Jl. Test No. 123"
- [ ] **Kelurahan:** Ketik "Kelurahan Test" (atau pilih dari autocomplete jika ada)
- [ ] **Kecamatan:** Ketik "Kecamatan Test" (atau pilih dari autocomplete)
- [ ] **Kabupaten:** Ketik "Kabupaten Test" (atau pilih dari autocomplete)

#### 1.2 Select Motor & Leasing
- [ ] **Motor Type:** Pilih tipe motor (contoh: "Honda CB 150")
- [ ] **No. Mesin:** Dropdown muncul dengan motor yang tersedia
  - Verify: Motor list muncul sesuai dengan tipe yang dipilih ✓
  - Select satu motor
- [ ] **Leasing:** Pilih "BCA Finance" atau leasing lain
- [ ] **Broker:** Pilih broker dari dropdown

#### 1.3 Fill Financial Data
- [ ] **Sistem Pembayaran:** Pilih "Cash" atau "Kredit"
  - **Jika Cash:**
    - Ketentuan DP otomatis = OTR ✓
    - Field readonly (abu-abu) ✓
  - **Jika Kredit:**
    - Ketentuan DP bisa di-edit ✓
    - Field editable (putih) ✓

- [ ] **DP (Dibayar):** Isi dengan "1500000"
- [ ] **Subsidi:** Isi dengan "100000"
- [ ] **Diskon AHM:** Isi dengan "200000"
- [ ] **Diskon Dealer:** Isi dengan "100000"
- [ ] **Diskon Leasing:** Isi dengan "50000"

#### 1.4 Verify Calculations
- [ ] **Hutang Sales:** Otomatis hitung
  - **CASH:** Hutang Sales = OTR - DP Dibayar
  - **KREDIT:** Hutang Sales = Ketentuan DP - DP Dibayar
  - Verify nilai muncul ✓

- [ ] **Hutang Leasing:** Otomatis hitung (hanya KREDIT)
  - **KREDIT:** Hutang Leasing = Pokok - Ketentuan DP
  - Verify nilai muncul ✓

- [ ] **Total Hutang:** Hutang Sales + Hutang Leasing
  - Verify display ✓

#### 1.5 Submit Form
- [ ] Click "Simpan Transaksi" button
- [ ] Verify: Toast "Transaksi berhasil dibuat" muncul ✓
- [ ] Verify: Modal tertutup ✓
- [ ] Verify: Data baru muncul di tabel transaksi ✓

### Expected Results ✅
- Transaksi tersimpan di database
- Semua field terinput dengan benar
- Calculations otomatis berjalan
- Status default: "P" (Pending)

---

## 🧪 TEST 2: EDIT TRANSAKSI

### Setup
1. Buka transaksi yang baru dibuat (TEST-001)
2. Click tombol "Edit" di baris transaksi
3. Modal edit terbuka

### Test Steps

#### 2.1 Verify Data Loaded
- [ ] **No. Nota:** Tampil "TEST-001" ✓
- [ ] **Tanggal:** Tampil tanggal yang benar ✓
- [ ] **Nama Pelanggan:** Tampil "Uji Coba Test" ✓
- [ ] **No. HP:** Tampil "08123456789" ✓
- [ ] **Alamat:** Tampil dengan benar ✓
- [ ] **Kelurahan/Kecamatan/Kabupaten:** Tampil dengan benar ✓
- [ ] **Motor Type:** Tampil dengan benar ✓
- [ ] **No. Mesin:** Tampil dengan benar ✓
- [ ] **Leasing:** Tampil "BCA Finance" ✓
- [ ] **Broker:** Tampil dengan benar ✓

#### 2.2 Edit Financial Data
- [ ] Ubah **DP Dibayar** dari "1500000" menjadi "2000000"
- [ ] Verify: **Hutang Sales** otomatis recalculate ✓
  - Hutang Sales baru = Ketentuan DP - 2000000
  - Harus berkurang dari sebelumnya

- [ ] Ubah **Diskon AHM** dari "200000" menjadi "300000"
- [ ] Verify: Hutang recalculate lagi ✓

#### 2.3 Submit Edit
- [ ] Click "Simpan Perubahan" button
- [ ] Verify: Toast "Transaksi berhasil diupdate" muncul ✓
- [ ] Verify: Modal tertutup ✓
- [ ] Verify: Tabel menampilkan data yang updated ✓

### Expected Results ✅
- Data transaksi terupdate
- Calculations akurat setelah perubahan
- Database konsisten

---

## 🧪 TEST 3: DETAIL MODAL - SEMUA TABS

### Setup
1. Click tombol "👁 Detail" di baris transaksi TEST-001
2. Modal detail terbuka (Tab: Informasi Dasar)

### Test 3.1: Tab INFORMASI DASAR

- [ ] **Header Cards:**
  - No. Nota: "TEST-001" ✓
  - Tanggal: Tampil benar ✓
  - Status: "P" (Pending) dengan badge ✓

- [ ] **Data Pelanggan Section:**
  - Nama: "Uji Coba Test" ✓
  - Telepon: "08123456789" ✓
  - Alamat Lengkap: Alamat + Kelurahan + Kecamatan + Kabupaten ✓

- [ ] **Data Motor Section:**
  - Tipe Motor: "Honda CB 150" ✓
  - Warna: Warna motor tampil ✓

### Test 3.2: Tab MOTOR

- [ ] **Spesifikasi Motor:**
  - Tipe Motor: "Honda CB 150" ✓
  - Warna: Tampil dengan benar ✓
  - No. Mesin: No. mesin yang benar ✓

- [ ] **Identitas Motor:**
  - No. Rangka: No. rangka tampil ✓
  - No. Polisi: Jika ada, tampil dengan highlight hijau ✓

### Test 3.3: Tab FINANSIAL

- [ ] **Sistem Pembayaran:** "Cash" atau "Kredit" ✓

- [ ] **Detail Hutang Section (Card):**
  - OTR Motor: "Rp 24.500.000" ✓
  - DP (Dibayar): "Rp 2.000.000" ✓
  - Subsidi: "Rp 100.000" ✓
  - Diskon AHM: "Rp 300.000" ✓ (updated value)
  - Diskon Dealer: "Rp 100.000" ✓
  - Diskon Leasing: "Rp 50.000" ✓

- [ ] **Hutang Display (Prominent):**
  - Hutang Sales: Merah, nilai besar ✓
  - Hutang Leasing: Kuning (jika kredit), 0 (jika cash) ✓

- [ ] **Ketentuan DP Section:**
  - Ketentuan DP: Tampil nilai ✓

- [ ] **Leasing Section:**
  - Perusahaan Leasing: "BCA Finance" ✓

### Test 3.4: Tab STNK/BPKB

- [ ] **Data BPKB:**
  - No. BPKB: "-" (belum ada, normal untuk transaksi baru) ✓
  - Tgl. Biro Jasa: "-" (belum ada) ✓

- [ ] **Data STNK & Serah Terima:**
  - Nama Pemilik (STNK): "-" atau nama jika sudah diisi ✓
  - Tgl. Serah Terima Motor: "-" atau tanggal jika ada ✓

### Expected Results ✅
- Semua 4 tab menampilkan data dengan benar
- Calculations akurat di tab Finansial
- Styling elegant dengan card-based design

---

## 🧪 TEST 4: LAPORAN HUTANG SALES

### Setup
1. Buka menu "HUTANG SALES" di sidebar
2. Halaman laporan terbuka

### Test Steps

#### 4.1 Filter & Generate
- [ ] **Filter Broker:** Pilih broker jika ada
- [ ] **Filter Status:** Pilih "Semua Status" atau "Belum Dibayar"
- [ ] **Dari Tanggal:** Kosongkan atau isi tanggal awal
- [ ] Click **"Generate Laporan"** button

#### 4.2 Verify Summary Cards
- [ ] **Total Hutang:** Menampilkan total hutang semua transaksi
  - Harus > 0 jika ada transaksi ✓
- [ ] **Hutang Belum Dibayar:** Menampilkan hutang yang belum dibayar
  - Untuk TEST-001 (status P = Pending): Hutang Sales value ✓
- [ ] **Hutang Sudah Dibayar:** 0 (normal, belum ada pembayaran) ✓
- [ ] **Jumlah Transaksi:** Menampilkan jumlah transaksi
  - Minimal 1 (TEST-001) ✓

#### 4.3 Verify Broker Summary Table
- [ ] **Nama Broker:** Tampil broker dari TEST-001 ✓
- [ ] **Tipe:** Tampil tipe broker (Broker/Sales/Leasing) ✓
- [ ] **Jumlah Transaksi:** 1 ✓
- [ ] **Total Hutang:** Sama dengan Hutang Sales dari TEST-001 ✓
- [ ] **Belum Dibayar:** Sama dengan Total Hutang ✓
- [ ] **Sudah Dibayar:** 0 ✓

#### 4.4 Verify Detail Transaksi Table
- [ ] **Nota:** "TEST-001" ✓
- [ ] **Tanggal:** Tanggal transaksi ✓
- [ ] **Pelanggan:** "Uji Coba Test" ✓
- [ ] **Broker/Sales:** Nama broker ✓
- [ ] **Motor:** "Honda CB 150" ✓
- [ ] **Hutang Sales:** Nilai hutang dengan warna merah ✓
- [ ] **Status:** "⏳ Belum Dibayar" dengan badge ✓
- [ ] **Aksi Buttons:** 
  - "👁 Detail" button ✓
  - "💰 Bayar" button ✓

### Expected Results ✅
- Laporan muncul dengan data yang benar
- Summary cards menampilkan nilai akurat
- Tables terisi dengan data transaksi

---

## 🧪 TEST 5: JURNAL INFORMASI

### Setup
1. Buka menu "JURNAL INFO" di sidebar
2. Halaman jurnal informasi terbuka

### Test Steps

#### 5.1 Search Transaksi
- [ ] Di field "No. Mesin / Nota" cari "TEST-001"
- [ ] Click "Cari Data" button
- [ ] Verify: Data TEST-001 muncul di tabel ✓

#### 5.2 Verify Jurnal Table Columns
- [ ] **No. Mesin:** No. mesin motor tampil ✓
- [ ] **No. Rangka:** No. rangka tampil ✓
- [ ] **Nota:** "TEST-001" ✓
- [ ] **Tipe Motor:** "Honda CB 150" ✓
- [ ] **Warna:** Warna motor ✓
- [ ] **Pelanggan:** "Uji Coba Test" ✓
- [ ] **DP:** "Rp 2.000.000" ✓
- [ ] **Subsidi:** "Rp 100.000" ✓
- [ ] **Diskon AHM:** "Rp 300.000" ✓
- [ ] **Diskon Dealer:** "Rp 100.000" ✓
- [ ] **Diskon Leasing:** "Rp 50.000" ✓
- [ ] **Insentif:** "0" atau nilai ✓
- [ ] **Leasing:** "BCA Finance" ✓ (PENTING: Tidak N/A)
- [ ] **Tgl Hutang Dibayar:** "-" (belum dibayar) ✓
- [ ] **Status:** "P" (Pending) ✓

#### 5.3 Click Detail Jurnal
- [ ] Click row TEST-001 untuk buka detail
- [ ] Verify modal detail terbuka dengan data ✓
- [ ] Verify semua field terisi dengan benar ✓
- [ ] Close modal

### Expected Results ✅
- Jurnal Informasi menampilkan semua kolom
- Leasing name muncul (tidak N/A)
- Data lengkap dan akurat

---

## 🧪 TEST 6: CALCULATIONS VERIFICATION

### Setup
Gunakan TEST-001 dengan nilai:
- OTR: 24.500.000
- DP: 2.000.000 (updated)
- Ketentuan DP (CASH): 24.500.000
- Subsidi: 100.000
- Diskon AHM: 300.000
- Diskon Dealer: 100.000
- Diskon Leasing: 50.000

### Test CASH Calculation
```
Total Diskon = 100.000 + 300.000 + 100.000 + 50.000 = 550.000
Pokok = 24.500.000 - 550.000 = 23.950.000
Hutang Sales (CASH) = OTR - DP = 24.500.000 - 2.000.000 = 22.500.000
Hutang Leasing = 0
```

- [ ] **Frontend Calculate:** 
  - Open edit form, verify Hutang Sales = 22.500.000 ✓
  - Verify Hutang Leasing = 0 ✓

- [ ] **Detail Modal:**
  - Verify Hutang Sales = 22.500.000 ✓

- [ ] **Laporan Hutang:**
  - Verify Hutang Sales = 22.500.000 ✓

### Test KREDIT Calculation (jika ada transaksi kredit)
```
Ketentuan DP (manual): contoh 5.000.000
Hutang Sales (KREDIT) = Ketentuan DP - DP Dibayar = 5.000.000 - 2.000.000 = 3.000.000
Hutang Leasing = Pokok - Ketentuan DP = 23.950.000 - 5.000.000 = 18.950.000
```

- [ ] Verify calculations konsisten di semua tempat ✓

### Expected Results ✅
- Calculations akurat & konsisten
- CASH vs KREDIT logic bekerja benar
- Database menyimpan nilai yang benar

---

## 🧪 TEST 7: WILAYAH AUTOCOMPLETE

### Setup
Buka form edit transaksi TEST-001

### Test Steps

- [ ] **Kelurahan Field:**
  - Clear field
  - Ketik "Kelurahan" (2-3 karakter)
  - Verify: Dropdown muncul dengan suggestions ✓
  - Klik satu suggestion
  - Verify: Kelurahan terisi, Kecamatan & Kabupaten ter-clear ✓

- [ ] **Kecamatan Field:**
  - Ketik "Kec" (2-3 karakter)
  - Verify: Dropdown muncul dengan kecamatan yang match kelurahan ✓
  - Klik satu suggestion
  - Verify: Kecamatan terisi, Kabupaten ter-clear ✓

- [ ] **Kabupaten Field:**
  - Ketik "Kab" (2-3 karakter)
  - Verify: Dropdown muncul dengan kabupaten yang match ✓
  - Klik satu suggestion
  - Verify: Kabupaten terisi ✓

### Expected Results ✅
- Autocomplete bekerja untuk semua 3 field
- Dependencies berfungsi (clear field yang tergantung)
- Suggestions berdasarkan data yang sudah terinput

---

## 🧪 TEST 8: PAYMENT TRACKING

### Setup
1. Buka Laporan Hutang Sales
2. Click "💰 Bayar" button pada transaksi TEST-001

### Test Steps

#### 8.1 Bayar Hutang Modal
- [ ] **Info Transaksi:**
  - No. Transaksi: "TEST-001" ✓
  - Pelanggan: "Uji Coba Test" ✓

- [ ] **Perhitungan Hutang:**
  - OTR Motor: "Rp 24.500.000" ✓
  - DP (Dibayar): "Rp 2.000.000" ✓
  - Subsidi: "Rp 100.000" ✓
  - Diskon: "Rp 450.000" ✓
  - Hutang Beban Sales: "Rp 22.500.000" ✓

- [ ] **Hutang Status:**
  - Sudah Dibayar: "Rp 0" ✓
  - Sisa Hutang: "Rp 22.500.000" ✓
  - Status: "Belum Dibayar" (red badge) ✓

#### 8.2 Input Pembayaran
- [ ] **Nominal Pembayaran:** "5000000"
- [ ] **Tanggal Pembayaran:** Hari ini
- [ ] **Metode Pembayaran:** Pilih "Transfer"
- [ ] **Keterangan:** "Pembayaran cicilan"
- [ ] Click **"Catat Pembayaran"** button

#### 8.3 Verify Payment Recorded
- [ ] Verify: Toast "Pembayaran berhasil dicatat" muncul ✓
- [ ] Modal tertutup ✓
- [ ] Buka laporan hutang sales lagi
- [ ] Verify: 
  - Hutang Belum Dibayar = 22.500.000 - 5.000.000 = 17.500.000 ✓
  - Hutang Sudah Dibayar = 5.000.000 ✓
  - Status: "Cicilan" (yellow badge) ✓

### Expected Results ✅
- Payment recorded di database
- Calculations update otomatis
- Status berubah dari "Belum Dibayar" → "Cicilan"

---

## ✅ SUMMARY CHECKLIST

### Database Integrity
- [ ] Semua transaksi tersimpan dengan field lengkap
- [ ] Foreign keys (motor, leasing, broker) valid
- [ ] Calculations (hutang_sales, hutang_leasing) tersimpan benar

### API Endpoints
- [ ] POST /api/transaksi - create dengan calculations
- [ ] PUT /api/transaksi/{id} - update dengan recalculations
- [ ] GET /api/transaksi/{id} - return data dengan calculations
- [ ] GET /api/laporan/hutang-sales - return data akurat
- [ ] POST /api/transaksi/{id}/bayar-hutang - payment tracking

### Frontend Integration
- [ ] Form create/edit - semua field bekerja
- [ ] Dropdowns - motor, leasing, broker loading
- [ ] Autocomplete - wilayah dependencies bekerja
- [ ] Modal detail - all 4 tabs display correctly
- [ ] Calculations - live update saat input berubah

### Business Logic
- [ ] CASH vs KREDIT - calculations berbeda benar
- [ ] Hutang calculations - akurat di semua tempat
- [ ] Payment tracking - status update otomatis
- [ ] Leasing display - tidak N/A, menampilkan nama

### Data Consistency
- [ ] Data sama di form, modal, laporan
- [ ] Calculations konsisten across all views
- [ ] Payment history tersimpan dengan benar

---

## 🎯 Kesimpulan

Jika semua test di atas PASS ✅, maka sistem transaksi **FULLY INTEGRATED** dan siap untuk production.

Jika ada yang FAIL ❌, dokumentasi di issue dengan detail:
- Screenshot
- Expected vs Actual
- Steps to reproduce
