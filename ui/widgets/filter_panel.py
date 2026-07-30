"""
Filter Panel Widget
Advanced filtering options for transactions
"""

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QComboBox,
    QLineEdit, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal

from database.repositories import DealerRepository
from config import BUTTON_HEIGHT


class FilterPanel(QWidget):
    """Advanced filter panel"""

    # Signal emitted when filters are applied
    filter_applied = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.dealer_repo = DealerRepository()
        self.initUI()
        self.load_dealers()

    def initUI(self):
        """Initialize filter UI"""
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        # Dealer filter
        layout.addWidget(QLabel("Dealer:"))
        self.combo_dealer = QComboBox()
        self.combo_dealer.setMinimumWidth(150)
        layout.addWidget(self.combo_dealer)

        # Search field
        layout.addWidget(QLabel("Cari Nama/HP:"))
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Masukkan nama atau nomor HP...")
        self.search_field.setMinimumWidth(200)
        layout.addWidget(self.search_field)

        # Status filter
        layout.addWidget(QLabel("Status:"))
        self.combo_status = QComboBox()
        self.combo_status.addItems(["Semua", "Pending (P)", "Approved (A)", "Lunas (L)", "Cancelled (C)"])
        self.combo_status.setMinimumWidth(120)
        layout.addWidget(self.combo_status)

        # Spacer
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)

        # Apply button
        btn_apply = QPushButton("🔍 Terapkan Filter")
        btn_apply.setFixedHeight(BUTTON_HEIGHT)
        btn_apply.setStyleSheet("""
            background-color: #2196F3;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 4px;
            padding: 5px 15px;
        """)
        btn_apply.clicked.connect(self.on_apply_filter)
        layout.addWidget(btn_apply)

        # Reset button
        btn_reset = QPushButton("🔄 Reset")
        btn_reset.setFixedHeight(BUTTON_HEIGHT)
        btn_reset.clicked.connect(self.on_reset_filter)
        layout.addWidget(btn_reset)

        self.setLayout(layout)
        self.setMaximumHeight(50)
        self.setStyleSheet("""
            QWidget {
                background-color: #fafafa;
                border-bottom: 1px solid #ddd;
            }
            QComboBox, QLineEdit {
                padding: 5px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
            }
            QComboBox:focus, QLineEdit:focus {
                border: 2px solid #2196F3;
            }
        """)

    def load_dealers(self):
        """Load dealers into combo box"""
        try:
            dealers = self.dealer_repo.get_active()
            self.combo_dealer.addItem("Semua Dealer", None)

            for dealer in dealers:
                self.combo_dealer.addItem(dealer.nama, dealer.id)
        except Exception as e:
            print(f"Error loading dealers: {e}")

    def on_apply_filter(self):
        """Apply filters"""
        filters = self.get_filters()
        self.filter_applied.emit(filters)

    def on_reset_filter(self):
        """Reset all filters"""
        self.combo_dealer.setCurrentIndex(0)
        self.search_field.clear()
        self.combo_status.setCurrentIndex(0)
        self.on_apply_filter()

    def get_filters(self) -> dict:
        """Get current filter values"""
        dealer_id = self.combo_dealer.currentData()
        search_term = self.search_field.text().strip()
        status = self.combo_status.currentText()

        # Convert status to code
        status_map = {
            "Semua": None,
            "Pending (P)": "P",
            "Approved (A)": "A",
            "Lunas (L)": "L",
            "Cancelled (C)": "C",
        }

        filters = {
            "dealer_id": dealer_id,
            "search_term": search_term,
            "status": status_map.get(status),
        }

        return filters

    def set_search_term(self, term: str):
        """Set search term programmatically"""
        self.search_field.setText(term)
