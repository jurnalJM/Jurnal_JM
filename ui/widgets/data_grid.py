"""
Data Grid Widget
Display transaction data in table format
"""

from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt, pyqtSignal, QDate
from PyQt6.QtGui import QFont, QColor

from database.models import Transaksi


class DataGrid(QTableWidget):
    """Table widget for displaying transactions"""

    # Signal when row is selected
    row_selected = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.selected_rows_data = []
        self.initUI()

    def initUI(self):
        """Initialize table UI"""
        # Setup columns
        columns = [
            "ID", "Tanggal", "Nota", "Dealer", "Nama Pembeli",
            "HP", "No Mesin", "Type Motor", "Warna",
            "DP", "Subsidi", "Diskon", "Insentif", "Leasing",
            "Tgl Lunas", "Pelunasan", "Status"
        ]

        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

        # Setup header
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # ID
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # Tanggal
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Nota
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)  # Dealer
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)  # Nama

        # Style
        header_font = QFont()
        header_font.setBold(True)
        header.setFont(header_font)

        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                gridline-color: #ddd;
                background-color: white;
                alternate-background-color: #f9f9f9;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #bbdefb;
            }
        """)

        # Connect selection
        self.itemSelectionChanged.connect(self.on_row_selected)

    def load_data(self, transaksis: list):
        """Load transaction data into grid"""
        self.setRowCount(len(transaksis))
        self.selected_rows_data = []

        for row, trans in enumerate(transaksis):
            # ID
            item = QTableWidgetItem(str(trans.id))
            item.setData(Qt.ItemDataRole.UserRole, trans.id)
            self.setItem(row, 0, item)

            # Tanggal
            self.setItem(row, 1, QTableWidgetItem(trans.tanggal.strftime("%d-%b-%y")))

            # Nota
            self.setItem(row, 2, QTableWidgetItem(trans.nota))

            # Dealer
            dealer_name = trans.dealer.nama if trans.dealer else "-"
            self.setItem(row, 3, QTableWidgetItem(dealer_name))

            # Nama Pembeli
            self.setItem(row, 4, QTableWidgetItem(trans.nama_pembeli))

            # HP
            self.setItem(row, 5, QTableWidgetItem(trans.telp_pembeli or "-"))

            # No Mesin
            no_mesin = trans.motor.no_mesin if trans.motor else "-"
            self.setItem(row, 6, QTableWidgetItem(no_mesin))

            # Type Motor
            type_name = trans.motor.type_motor.nama_type if trans.motor else "-"
            self.setItem(row, 7, QTableWidgetItem(type_name))

            # Warna
            warna = trans.motor.warna if trans.motor else "-"
            self.setItem(row, 8, QTableWidgetItem(warna))

            # Financial data (from detail)
            if trans.detail:
                # DP
                dp_item = QTableWidgetItem(f"{float(trans.detail.dp):,.0f}")
                dp_item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.setItem(row, 9, dp_item)

                # Subsidi
                subsidi_item = QTableWidgetItem(f"{float(trans.detail.subsidi):,.0f}")
                subsidi_item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.setItem(row, 10, subsidi_item)

                # Diskon
                diskon_total = float(trans.detail.diskon or 0) + float(trans.detail.diskon_tambahan or 0)
                diskon_item = QTableWidgetItem(f"{diskon_total:,.0f}")
                diskon_item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.setItem(row, 11, diskon_item)

                # Insentif
                insentif_item = QTableWidgetItem(f"{float(trans.detail.insentif):,.0f}")
                insentif_item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.setItem(row, 12, insentif_item)

                # Tgl Lunas
                tgl_lunas = trans.detail.tgl_lunas.strftime("%d-%b-%y") if trans.detail.tgl_lunas else "-"
                self.setItem(row, 14, QTableWidgetItem(tgl_lunas))

                # Pelunasan
                pelunasan_item = QTableWidgetItem(f"{float(trans.detail.pelunasan):,.0f}")
                pelunasan_item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                self.setItem(row, 15, pelunasan_item)
            else:
                # Fill with dashes
                for col in [9, 10, 11, 12, 14, 15]:
                    self.setItem(row, col, QTableWidgetItem("-"))

            # Leasing
            leasing_name = trans.leasing.nama if trans.leasing else "-"
            self.setItem(row, 13, QTableWidgetItem(leasing_name))

            # Status
            status_text = self.get_status_text(trans.status_transaksi)
            status_item = QTableWidgetItem(status_text)
            status_item.setBackground(self.get_status_color(trans.status_transaksi))
            self.setItem(row, 16, status_item)

    def on_row_selected(self):
        """Handle row selection"""
        selected_items = self.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            id_item = self.item(row, 0)
            if id_item:
                transaksi_id = id_item.data(Qt.ItemDataRole.UserRole)
                self.row_selected.emit(transaksi_id)

    def get_selected_row_ids(self) -> list:
        """Get IDs of selected rows"""
        selected_ranges = self.selectedRanges()
        ids = []

        for range_item in selected_ranges:
            for row in range(range_item.topRow(), range_item.bottomRow() + 1):
                id_item = self.item(row, 0)
                if id_item:
                    ids.append(id_item.data(Qt.ItemDataRole.UserRole))

        return ids

    def get_status_text(self, status_code: str) -> str:
        """Convert status code to text"""
        status_map = {
            "P": "Pending",
            "A": "Approved",
            "L": "Lunas",
            "C": "Cancelled",
        }
        return status_map.get(status_code, status_code)

    def get_status_color(self, status_code: str) -> QColor:
        """Get color for status"""
        color_map = {
            "P": QColor("#FFF3CD"),  # Yellow
            "A": QColor("#D1ECF1"),  # Light blue
            "L": QColor("#D4EDDA"),  # Green
            "C": QColor("#F8D7DA"),  # Red
        }
        return color_map.get(status_code, QColor("white"))

    def clear_data(self):
        """Clear all data from grid"""
        self.setRowCount(0)
