"""
Main Toolbar Widget
Contains date range selectors and main action buttons
"""

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton,
    QDateEdit, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal, QDate
from PyQt6.QtGui import QIcon

from config import BUTTON_HEIGHT


class MainToolbar(QWidget):
    """Toolbar with date range selector and action buttons"""

    # Signals
    search_clicked = pyqtSignal(QDate, QDate)
    new_clicked = pyqtSignal()
    print_clicked = pyqtSignal()
    export_clicked = pyqtSignal()
    exit_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize toolbar UI"""
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        # Date range section
        label1 = QLabel("Dari Tanggal:")
        label1.setStyleSheet("font-weight: bold;")
        layout.addWidget(label1)

        self.date_from = QDateEdit()
        self.date_from.setDate(QDate.currentDate().addMonths(-1))
        self.date_from.setCalendarPopup(True)
        self.date_from.setDate(QDate.currentDate().addMonths(-1))
        layout.addWidget(self.date_from)

        label2 = QLabel("Sampai Tanggal:")
        label2.setStyleSheet("font-weight: bold;")
        layout.addWidget(label2)

        self.date_to = QDateEdit()
        self.date_to.setDate(QDate.currentDate())
        self.date_to.setCalendarPopup(True)
        layout.addWidget(self.date_to)

        # Search button
        btn_search = QPushButton("🔍 Cari")
        btn_search.setFixedHeight(BUTTON_HEIGHT)
        btn_search.clicked.connect(self.on_search)
        layout.addWidget(btn_search)

        # Spacer
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)

        # Action buttons
        btn_new = QPushButton("➕ Baru")
        btn_new.setFixedHeight(BUTTON_HEIGHT)
        btn_new.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        btn_new.clicked.connect(self.new_clicked.emit)
        layout.addWidget(btn_new)

        btn_export = QPushButton("📊 Export")
        btn_export.setFixedHeight(BUTTON_HEIGHT)
        btn_export.clicked.connect(self.export_clicked.emit)
        layout.addWidget(btn_export)

        btn_print = QPushButton("🖨️ Cetak")
        btn_print.setFixedHeight(BUTTON_HEIGHT)
        btn_print.clicked.connect(self.print_clicked.emit)
        layout.addWidget(btn_print)

        btn_exit = QPushButton("❌ Keluar")
        btn_exit.setFixedHeight(BUTTON_HEIGHT)
        btn_exit.setStyleSheet("background-color: #f44336; color: white; font-weight: bold;")
        btn_exit.clicked.connect(self.exit_clicked.emit)
        layout.addWidget(btn_exit)

        self.setLayout(layout)
        self.setMaximumHeight(60)
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                border-bottom: 1px solid #ddd;
            }
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #1565C0;
            }
            QDateEdit {
                padding: 5px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
            }
        """)

    def on_search(self):
        """Emit search signal"""
        self.search_clicked.emit(self.date_from.date(), self.date_to.date())

    def get_date_range(self):
        """Get selected date range"""
        return self.date_from.date(), self.date_to.date()

    def set_date_range(self, date_from, date_to):
        """Set date range"""
        self.date_from.setDate(date_from)
        self.date_to.setDate(date_to)
