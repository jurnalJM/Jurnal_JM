"""
Main Application Window
Central hub for the JayaMotor application
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QMessageBox, QStatusBar, QLabel
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QPainter
import subprocess
import os

from ui.widgets.toolbar import MainToolbar
from ui.widgets.filter_panel import FilterPanel
from ui.widgets.data_grid import DataGrid
from ui.dialogs.transaksi_dialog import TransaksiDialog
from business.services import TransaksiService
from business.exceptions import ValidationErrors, RecordNotFound
from config import APP_TITLE, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT
from utils import ExcelExporter, PDFReporter


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{APP_TITLE} v{APP_VERSION}")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.service = TransaksiService()
        self.current_transactions = []

        self.initUI()
        self.load_initial_data()

    def initUI(self):
        """Initialize user interface"""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # =====================================================================
        # TOOLBAR
        # =====================================================================
        self.toolbar = MainToolbar()
        self.toolbar.search_clicked.connect(self.on_search)
        self.toolbar.new_clicked.connect(self.on_new_transaction)
        self.toolbar.export_clicked.connect(self.on_export)
        self.toolbar.print_clicked.connect(self.on_print)
        self.toolbar.exit_clicked.connect(self.close)
        main_layout.addWidget(self.toolbar)

        # =====================================================================
        # FILTER PANEL
        # =====================================================================
        self.filter_panel = FilterPanel()
        self.filter_panel.filter_applied.connect(self.on_filter_applied)
        main_layout.addWidget(self.filter_panel)

        # =====================================================================
        # DATA GRID
        # =====================================================================
        self.data_grid = DataGrid()
        self.data_grid.row_selected.connect(self.on_row_selected)
        main_layout.addWidget(self.data_grid)

        # =====================================================================
        # ACTION BUTTONS
        # =====================================================================
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(5, 5, 5, 5)
        button_layout.setSpacing(10)

        btn_add = QPushButton("➕ Tambah Data")
        btn_add.clicked.connect(self.on_new_transaction)
        button_layout.addWidget(btn_add)

        btn_edit = QPushButton("✏️ Edit")
        btn_edit.clicked.connect(self.on_edit_transaction)
        button_layout.addWidget(btn_edit)

        btn_delete = QPushButton("🗑️ Hapus")
        btn_delete.clicked.connect(self.on_delete_transaction)
        button_layout.addWidget(btn_delete)

        btn_detail = QPushButton("📋 Detail")
        btn_detail.clicked.connect(self.on_view_detail)
        button_layout.addWidget(btn_detail)

        btn_notes = QPushButton("📝 Catatan")
        btn_notes.clicked.connect(self.on_view_notes)
        button_layout.addWidget(btn_notes)

        button_layout.addStretch()

        btn_refresh = QPushButton("🔄 Refresh")
        btn_refresh.clicked.connect(self.on_refresh)
        button_layout.addWidget(btn_refresh)

        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

        # =====================================================================
        # STATUS BAR
        # =====================================================================
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.status_label = QLabel("Siap")
        self.statusBar.addWidget(self.status_label)

        self.count_label = QLabel("Total: 0")
        self.statusBar.addPermanentWidget(self.count_label)

        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #1565C0;
            }
            QStatusBar {
                background-color: #f5f5f5;
                border-top: 1px solid #ddd;
            }
        """)

    def load_initial_data(self):
        """Load initial data on startup"""
        try:
            self.on_search(QDate.currentDate().addMonths(-1), QDate.currentDate())
            self.set_status("Data loaded successfully")
        except Exception as e:
            self.set_status(f"Error loading data: {e}")

    # =====================================================================
    # SEARCH & FILTER
    # =====================================================================

    def on_search(self, date_from: QDate, date_to: QDate):
        """Handle search by date range"""
        try:
            self.set_status("Searching...")

            transaksis = self.service.repo.get_by_date_range(
                date_from.toPyDate(),
                date_to.toPyDate()
            )

            self.current_transactions = transaksis
            self.data_grid.load_data(transaksis)
            self.update_count(len(transaksis))

            self.set_status(f"Found {len(transaksis)} transactions")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Search failed: {e}")
            self.set_status("Search failed")

    def on_filter_applied(self, filters: dict):
        """Handle filter applied"""
        try:
            self.set_status("Applying filters...")

            date_from, date_to = self.toolbar.get_date_range()
            transaksis = self.service.search_transaksi(
                date_from=date_from.toPyDate(),
                date_to=date_to.toPyDate(),
                dealer_id=filters.get("dealer_id"),
                customer_name=filters.get("search_term"),
                status=filters.get("status")
            )

            self.current_transactions = transaksis
            self.data_grid.load_data(transaksis)
            self.update_count(len(transaksis))

            self.set_status(f"Filter applied: {len(transaksis)} transactions")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Filter failed: {e}")
            self.set_status("Filter failed")

    # =====================================================================
    # TRANSACTION MANAGEMENT
    # =====================================================================

    def on_new_transaction(self):
        """Open dialog to create new transaction"""
        dialog = TransaksiDialog(self)
        if dialog.exec() == 1:  # QDialog.Accepted
            self.on_refresh()
            self.set_status("Transaction created successfully")

    def on_edit_transaction(self):
        """Edit selected transaction"""
        selected_ids = self.data_grid.get_selected_row_ids()
        if not selected_ids:
            QMessageBox.warning(self, "Warning", "Pilih transaksi untuk diubah")
            return

        transaksi_id = selected_ids[0]
        dialog = TransaksiDialog(self, transaksi_id)
        if dialog.exec() == 1:
            self.on_refresh()
            self.set_status("Transaction updated successfully")

    def on_delete_transaction(self):
        """Delete selected transaction"""
        selected_ids = self.data_grid.get_selected_row_ids()
        if not selected_ids:
            QMessageBox.warning(self, "Warning", "Pilih transaksi untuk dihapus")
            return

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Hapus {len(selected_ids)} transaksi?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                for transaksi_id in selected_ids:
                    self.service.cancel_transaksi(transaksi_id, "Deleted by user")

                QMessageBox.information(self, "Success", "Transaction(s) deleted")
                self.on_refresh()
                self.set_status("Transaction(s) deleted")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Delete failed: {e}")

    def on_view_detail(self):
        """View transaction detail"""
        selected_ids = self.data_grid.get_selected_row_ids()
        if not selected_ids:
            QMessageBox.warning(self, "Warning", "Pilih transaksi untuk dilihat")
            return

        try:
            transaksi_id = selected_ids[0]
            status = self.service.get_transaction_status(transaksi_id)

            detail_text = f"""
DETAIL TRANSAKSI
================

Nota: {status['nota']}
Status: {status['status']}
Customer: {status['customer']}

KENDARAAN
Motor: {status['motor']['type']}
No Mesin: {status['motor']['no_mesin']}

KEUANGAN
Harga Jual: Rp {status['financial']['otr']:,.0f}
Diskon: Rp {status['financial']['discount']:,.0f}
Harus Bayar: Rp {status['financial']['due']:,.0f}
DP Diterima: Rp {status['financial']['dp_received']:,.0f}
Total Bayar: Rp {status['financial']['total_paid']:,.0f}
Sisa Hutang: Rp {status['financial']['remaining']:,.0f}

Pembayaran: {status['payments']} kali
            """

            QMessageBox.information(self, "Detail Transaksi", detail_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load detail: {e}")

    def on_view_notes(self):
        """View transaction notes"""
        selected_ids = self.data_grid.get_selected_row_ids()
        if not selected_ids:
            QMessageBox.warning(self, "Warning", "Pilih transaksi untuk dilihat catatannya")
            return

        try:
            transaksi_id = selected_ids[0]
            notes = self.service.get_notes(transaksi_id)

            notes_text = "CATATAN TRANSAKSI\n" + "=" * 40 + "\n\n"
            for note in notes:
                notes_text += f"[{note.tgl_catatan.strftime('%d-%b-%y %H:%M')}] {note.konten}\n"

            QMessageBox.information(self, "Catatan", notes_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load notes: {e}")

    def on_row_selected(self, transaksi_id: int):
        """Handle row selection"""
        pass  # Can be used for preview or other actions

    # =====================================================================
    # EXPORT & PRINT
    # =====================================================================

    def on_export(self):
        """Export data to Excel"""
        try:
            if not self.current_transactions:
                QMessageBox.warning(self, "Warning", "Tidak ada data untuk diexport")
                return

            filepath = ExcelExporter.export_transactions(
                self.current_transactions,
                include_summary=True
            )

            QMessageBox.information(
                self,
                "Export Sukses",
                f"Berhasil export {len(self.current_transactions)} transaksi\n\n"
                f"File: {os.path.basename(filepath)}"
            )
            self.set_status(f"Exported {len(self.current_transactions)} transactions to Excel")

            # Open file
            if os.name == 'nt':  # Windows
                os.startfile(filepath)
            else:
                subprocess.Popen(['xdg-open', filepath])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Export failed: {e}")
            self.set_status("Export failed")

    def on_print(self):
        """Print report"""
        try:
            if not self.current_transactions:
                QMessageBox.warning(self, "Warning", "Tidak ada data untuk diprint")
                return

            # Generate PDF first
            pdf_path = PDFReporter.generate_transaction_report(
                self.current_transactions,
                include_summary=True
            )

            # Open PDF with default viewer
            if os.name == 'nt':  # Windows
                os.startfile(pdf_path, 'print')
            else:
                subprocess.Popen(['xdg-open', pdf_path])

            QMessageBox.information(
                self,
                "Print Laporan",
                f"Laporan PDF telah dibuat:\n{os.path.basename(pdf_path)}\n\n"
                f"Silahkan cetak dari PDF viewer"
            )
            self.set_status(f"Generated PDF report: {os.path.basename(pdf_path)}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Print failed: {e}")
            self.set_status("Print failed")

    # =====================================================================
    # UTILITIES
    # =====================================================================

    def on_refresh(self):
        """Refresh data"""
        self.load_initial_data()

    def update_count(self, count: int):
        """Update transaction count"""
        self.count_label.setText(f"Total: {count}")

    def set_status(self, message: str):
        """Set status bar message"""
        self.status_label.setText(message)


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
