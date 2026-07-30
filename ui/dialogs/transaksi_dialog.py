"""
Transaction Dialog
Dialog for creating/editing transactions
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTabWidget,
    QLabel, QLineEdit, QDateEdit, QComboBox, QPushButton,
    QSpinBox, QDoubleSpinBox, QFormLayout, QGroupBox,
    QMessageBox, QSpinBox
)
from PyQt6.QtCore import QDate, pyqtSignal
from datetime import date

from database.repositories import (
    DealerRepository, TypeMotorRepository, StokMotorRepository,
    LeasingRepository, BrokerRepository
)
from business.services import TransaksiService
from business.exceptions import ValidationException, ValidationErrors, RecordNotFound


class TransaksiDialog(QDialog):
    """Dialog for creating/editing transactions"""

    transaksi_saved = pyqtSignal(int)  # Emit transaksi ID when saved

    def __init__(self, parent=None, transaksi_id=None):
        super().__init__(parent)
        self.transaksi_id = transaksi_id
        self.service = TransaksiService()
        self.dealer_repo = DealerRepository()
        self.motor_repo = StokMotorRepository()
        self.type_repo = TypeMotorRepository()
        self.leasing_repo = LeasingRepository()
        self.broker_repo = BrokerRepository()

        self.setWindowTitle("Tambah/Edit Transaksi" if not transaksi_id else "Edit Transaksi")
        self.setGeometry(200, 200, 900, 700)
        self.initUI()

        if transaksi_id:
            self.load_transaksi(transaksi_id)

    def initUI(self):
        """Initialize dialog UI"""
        layout = QVBoxLayout()

        # Create tabs
        tabs = QTabWidget()

        # Tab 1: Data Umum
        tab1 = self.create_tab_umum()
        tabs.addTab(tab1, "Data Umum")

        # Tab 2: Data Kendaraan
        tab2 = self.create_tab_kendaraan()
        tabs.addTab(tab2, "Data Kendaraan")

        # Tab 3: Data Keuangan
        tab3 = self.create_tab_keuangan()
        tabs.addTab(tab3, "Data Keuangan")

        # Tab 4: Data Leasing
        tab4 = self.create_tab_leasing()
        tabs.addTab(tab4, "Data Leasing")

        layout.addWidget(tabs)

        # Buttons
        button_layout = QHBoxLayout()
        btn_save = QPushButton("💾 Simpan")
        btn_save.clicked.connect(self.save_transaksi)
        btn_cancel = QPushButton("❌ Batal")
        btn_cancel.clicked.connect(self.reject)

        button_layout.addStretch()
        button_layout.addWidget(btn_save)
        button_layout.addWidget(btn_cancel)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def create_tab_umum(self):
        """Create 'Data Umum' tab"""
        widget = QGroupBox("Data Umum Transaksi")
        form = QFormLayout()

        # Nota
        self.text_nota = QLineEdit()
        self.text_nota.setPlaceholderText("Misal: TRX-2024-001")
        form.addRow("Nota:", self.text_nota)

        # Tanggal
        self.date_tanggal = QDateEdit()
        self.date_tanggal.setDate(QDate.currentDate())
        self.date_tanggal.setCalendarPopup(True)
        form.addRow("Tanggal:", self.date_tanggal)

        # Dealer
        self.combo_dealer = QComboBox()
        self.load_dealers()
        form.addRow("Dealer:", self.combo_dealer)

        # Nama Pembeli
        self.text_nama = QLineEdit()
        form.addRow("Nama Pembeli:", self.text_nama)

        # Alamat
        self.text_alamat = QLineEdit()
        form.addRow("Alamat:", self.text_alamat)

        # Telepon
        self.text_telp = QLineEdit()
        form.addRow("No Handphone:", self.text_telp)

        # Email
        self.text_email = QLineEdit()
        form.addRow("Email:", self.text_email)

        # Broker
        self.combo_broker = QComboBox()
        self.combo_broker.addItem("Tidak Ada", None)
        self.load_brokers()
        form.addRow("Broker:", self.combo_broker)

        # Status
        self.combo_status = QComboBox()
        self.combo_status.addItems(["Pending (P)", "Approved (A)", "Lunas (L)", "Cancelled (C)"])
        form.addRow("Status:", self.combo_status)

        widget.setLayout(form)
        return widget

    def create_tab_kendaraan(self):
        """Create 'Data Kendaraan' tab"""
        widget = QGroupBox("Data Kendaraan")
        form = QFormLayout()

        # Motor Type
        self.combo_type = QComboBox()
        self.load_motor_types()
        form.addRow("Tipe Motor:", self.combo_type)

        # Motor (Ready Stock)
        self.combo_motor = QComboBox()
        self.load_ready_motors()
        form.addRow("No Mesin (Stok):", self.combo_motor)

        # Color (Read-only, will auto-fill)
        self.text_warna = QLineEdit()
        self.text_warna.setReadOnly(True)
        form.addRow("Warna:", self.text_warna)

        # No Rangka (Read-only)
        self.text_rangka = QLineEdit()
        self.text_rangka.setReadOnly(True)
        form.addRow("No Rangka:", self.text_rangka)

        # Connect motor selection
        self.combo_motor.currentIndexChanged.connect(self.on_motor_changed)

        widget.setLayout(form)
        return widget

    def create_tab_keuangan(self):
        """Create 'Data Keuangan' tab"""
        widget = QGroupBox("Data Keuangan")
        form = QFormLayout()

        # OTR (Read-only)
        self.text_otr = QLineEdit()
        self.text_otr.setReadOnly(True)
        form.addRow("Harga Jual (OTR):", self.text_otr)

        # DP
        self.spin_dp = QDoubleSpinBox()
        self.spin_dp.setMaximum(9999999999)
        self.spin_dp.setDecimals(0)
        form.addRow("Down Payment (DP):", self.spin_dp)

        # Subsidi
        self.spin_subsidi = QDoubleSpinBox()
        self.spin_subsidi.setMaximum(9999999999)
        self.spin_subsidi.setDecimals(0)
        form.addRow("Subsidi:", self.spin_subsidi)

        # Diskon
        self.spin_diskon = QDoubleSpinBox()
        self.spin_diskon.setMaximum(9999999999)
        self.spin_diskon.setDecimals(0)
        form.addRow("Diskon Pokok:", self.spin_diskon)

        # Diskon Tambahan
        self.spin_diskon_tambahan = QDoubleSpinBox()
        self.spin_diskon_tambahan.setMaximum(9999999999)
        self.spin_diskon_tambahan.setDecimals(0)
        form.addRow("Diskon Tambahan:", self.spin_diskon_tambahan)

        # Insentif
        self.spin_insentif = QDoubleSpinBox()
        self.spin_insentif.setMaximum(9999999999)
        self.spin_insentif.setDecimals(0)
        form.addRow("Insentif:", self.spin_insentif)

        # Keterangan DP
        self.text_ket_dp = QLineEdit()
        form.addRow("Ket. DP:", self.text_ket_dp)

        widget.setLayout(form)
        return widget

    def create_tab_leasing(self):
        """Create 'Data Leasing' tab"""
        widget = QGroupBox("Data Leasing/Pembiayaan")
        form = QFormLayout()

        # Leasing Company
        self.combo_leasing = QComboBox()
        self.combo_leasing.addItem("Tidak Ada", None)
        self.load_leasing_companies()
        form.addRow("Leasing:", self.combo_leasing)

        # Tanggal Faktur
        self.date_faktur = QDateEdit()
        self.date_faktur.setCalendarPopup(True)
        form.addRow("Tgl Faktur:", self.date_faktur)

        # Tanggal Lunas
        self.date_lunas = QDateEdit()
        self.date_lunas.setCalendarPopup(True)
        form.addRow("Tgl Lunas:", self.date_lunas)

        # Pelunasan
        self.spin_pelunasan = QDoubleSpinBox()
        self.spin_pelunasan.setMaximum(9999999999)
        self.spin_pelunasan.setDecimals(0)
        form.addRow("Pelunasan:", self.spin_pelunasan)

        # Lain-lain
        self.spin_lain_lain = QDoubleSpinBox()
        self.spin_lain_lain.setMaximum(9999999999)
        self.spin_lain_lain.setDecimals(0)
        form.addRow("Lain-lain:", self.spin_lain_lain)

        widget.setLayout(form)
        return widget

    # =====================================================================
    # LOAD DATA METHODS
    # =====================================================================

    def load_dealers(self):
        """Load dealers into combo"""
        try:
            dealers = self.dealer_repo.get_active()
            for dealer in dealers:
                self.combo_dealer.addItem(dealer.nama, dealer.id)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load dealers: {e}")

    def load_brokers(self):
        """Load brokers into combo"""
        try:
            brokers = self.broker_repo.get_active()
            for broker in brokers:
                self.combo_broker.addItem(broker.nama, broker.id)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load brokers: {e}")

    def load_motor_types(self):
        """Load motor types into combo"""
        try:
            types = self.type_repo.get_active()
            for motor_type in types:
                self.combo_type.addItem(motor_type.nama_type, motor_type.id)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load types: {e}")

    def load_ready_motors(self):
        """Load ready motors into combo"""
        try:
            motors = self.motor_repo.get_ready()
            for motor in motors:
                display = f"{motor.no_mesin} ({motor.type_motor.nama_type})"
                self.combo_motor.addItem(display, motor.id)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load motors: {e}")

    def load_leasing_companies(self):
        """Load leasing companies into combo"""
        try:
            leasings = self.leasing_repo.get_active()
            for leasing in leasings:
                self.combo_leasing.addItem(leasing.nama, leasing.id)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load leasing: {e}")

    def on_motor_changed(self):
        """Handle motor selection change"""
        motor_id = self.combo_motor.currentData()
        if motor_id:
            try:
                motor = self.motor_repo.get_by_id(motor_id)
                if motor:
                    self.text_warna.setText(motor.warna or "")
                    self.text_rangka.setText(motor.no_rangka or "")
                    otr = float(motor.type_motor.otr or 0)
                    self.text_otr.setText(f"{otr:,.0f}")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Gagal load motor: {e}")

    def load_transaksi(self, transaksi_id: int):
        """Load existing transaction for editing"""
        try:
            transaksi = self.service.repo.get_by_id(transaksi_id)
            if not transaksi:
                QMessageBox.warning(self, "Error", "Transaksi tidak ditemukan")
                self.reject()
                return

            # Load data
            self.text_nota.setText(transaksi.nota)
            self.date_tanggal.setDate(QDate.fromString(transaksi.tanggal.isoformat(), "yyyy-MM-dd"))
            self.text_nama.setText(transaksi.nama_pembeli or "")
            self.text_alamat.setText(transaksi.alamat_pembeli or "")
            self.text_telp.setText(transaksi.telp_pembeli or "")
            self.text_email.setText(transaksi.email_pembeli or "")

            # Set dealer
            for i in range(self.combo_dealer.count()):
                if self.combo_dealer.itemData(i) == transaksi.dealer_id:
                    self.combo_dealer.setCurrentIndex(i)
                    break

            # Set broker
            if transaksi.broker_id:
                for i in range(self.combo_broker.count()):
                    if self.combo_broker.itemData(i) == transaksi.broker_id:
                        self.combo_broker.setCurrentIndex(i)
                        break

            # Set motor
            if transaksi.motor:
                for i in range(self.combo_motor.count()):
                    if self.combo_motor.itemData(i) == transaksi.motor_id:
                        self.combo_motor.setCurrentIndex(i)
                        break

                self.text_warna.setText(transaksi.motor.warna or "")
                self.text_rangka.setText(transaksi.motor.no_rangka or "")
                otr = float(transaksi.motor.type_motor.otr or 0)
                self.text_otr.setText(f"{otr:,.0f}")

            # Load financial data
            if transaksi.detail:
                self.spin_dp.setValue(float(transaksi.detail.dp or 0))
                self.spin_subsidi.setValue(float(transaksi.detail.subsidi or 0))
                self.spin_diskon.setValue(float(transaksi.detail.diskon or 0))
                self.spin_diskon_tambahan.setValue(float(transaksi.detail.diskon_tambahan or 0))
                self.spin_insentif.setValue(float(transaksi.detail.insentif or 0))
                self.text_ket_dp.setText(transaksi.detail.ket_dp or "")
                self.spin_pelunasan.setValue(float(transaksi.detail.pelunasan or 0))
                self.spin_lain_lain.setValue(float(transaksi.detail.lain_lain or 0))

                if transaksi.detail.tgl_lunas:
                    self.date_lunas.setDate(QDate.fromString(transaksi.detail.tgl_lunas.isoformat(), "yyyy-MM-dd"))

            # Load leasing
            if transaksi.leasing_id:
                for i in range(self.combo_leasing.count()):
                    if self.combo_leasing.itemData(i) == transaksi.leasing_id:
                        self.combo_leasing.setCurrentIndex(i)
                        break

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal load transaksi: {e}")
            self.reject()

    def get_form_data(self) -> dict:
        """Get form data as dictionary"""
        return {
            "nota": self.text_nota.text(),
            "tanggal": self.date_tanggal.date().toPyDate(),
            "dealer_id": self.combo_dealer.currentData(),
            "nama_pembeli": self.text_nama.text(),
            "alamat_pembeli": self.text_alamat.text(),
            "telp_pembeli": self.text_telp.text(),
            "email_pembeli": self.text_email.text(),
            "motor_id": self.combo_motor.currentData(),
            "broker_id": self.combo_broker.currentData(),
            "leasing_id": self.combo_leasing.currentData(),
            "status_transaksi": self.combo_status.currentText()[0],  # Get first char (P, A, L, C)
            "tgl_faktur": self.date_faktur.date().toPyDate() if self.date_faktur.date().isValid() else None,
        }

    def get_financial_data(self) -> dict:
        """Get financial data"""
        return {
            "dp": self.spin_dp.value(),
            "subsidi": self.spin_subsidi.value(),
            "diskon": self.spin_diskon.value(),
            "diskon_tambahan": self.spin_diskon_tambahan.value(),
            "insentif": self.spin_insentif.value(),
            "ket_dp": self.text_ket_dp.text(),
            "pelunasan": self.spin_pelunasan.value(),
            "lain_lain": self.spin_lain_lain.value(),
            "tgl_lunas": self.date_lunas.date().toPyDate() if self.date_lunas.date().isValid() else None,
        }

    def save_transaksi(self):
        """Save transaction"""
        try:
            data = self.get_form_data()

            if self.transaksi_id:
                # Update existing
                result = self.service.update_transaksi(self.transaksi_id, data)
                transaksi_id = self.transaksi_id
            else:
                # Create new
                result = self.service.create_transaksi(data)
                transaksi_id = result.id

            # Update financial
            financial_data = self.get_financial_data()
            self.service.update_financial(transaksi_id, financial_data)

            QMessageBox.information(self, "Sukses", "Transaksi berhasil disimpan")
            self.transaksi_saved.emit(transaksi_id)
            self.accept()

        except ValidationErrors as e:
            error_msg = "Validasi gagal:\n"
            for error in e.errors:
                error_msg += f"- {error['field']}: {error['message']}\n"
            QMessageBox.warning(self, "Validasi Error", error_msg)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menyimpan: {e}")
