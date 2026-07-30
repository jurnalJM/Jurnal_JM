"""
Tests for export and reporting functionality
"""

import pytest
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import Mock

from utils.excel_export import ExcelExporter
from utils.pdf_report import PDFReporter


class MockMotor:
    """Mock motor object"""
    def __init__(self):
        self.no_mesin = "TRX123456"
        self.warna = "Merah"
        self.type_motor = Mock(nama_type="PCX 160")


class MockLeasing:
    """Mock leasing company"""
    def __init__(self):
        self.nama = "Mandiri"


class MockDealer:
    """Mock dealer object"""
    def __init__(self, name="PT Jaya Motor"):
        self.nama = name


class MockTransaksiDetail:
    """Mock transaction detail"""
    def __init__(self):
        self.dp = 10000000.0
        self.subsidi = 2000000.0
        self.diskon = 500000.0
        self.diskon_tambahan = 100000.0
        self.insentif = 200000.0
        self.tgl_lunas = datetime.now().date() + timedelta(days=30)
        self.pelunasan = 5000000.0


class MockTransaksi:
    """Mock transaction object"""
    def __init__(self, trans_id=1, nota="TRX-001"):
        self.id = trans_id
        self.nota = nota
        self.tanggal = datetime.now().date()
        self.dealer = MockDealer()
        self.nama_pembeli = "John Doe"
        self.telp_pembeli = "081212345678"
        self.motor = MockMotor()
        self.leasing = MockLeasing()
        self.detail = MockTransaksiDetail()
        self.status_transaksi = "A"


@pytest.fixture
def sample_transactions():
    """Create sample mock transactions for testing"""
    transactions = []
    for i in range(5):
        trans = MockTransaksi(
            trans_id=i + 1,
            nota=f"TRX-{i+1:03d}"
        )
        trans.dealer.nama = f"Dealer {i+1}"
        trans.detail.dp = 10000000 + (i * 1000000)
        transactions.append(trans)
    return transactions


class TestExcelExport:
    """Test Excel export functionality"""

    def test_export_transactions_creates_file(self, sample_transactions, tmp_path):
        """Test that export creates an Excel file"""
        import utils.excel_export as export_module

        # Mock EXPORT_DIR
        original_export_dir = export_module.EXPORT_DIR
        export_module.EXPORT_DIR = tmp_path

        try:
            result_path = ExcelExporter.export_transactions(
                sample_transactions,
                filename="test.xlsx",
                include_summary=True
            )

            assert Path(result_path).exists()
            assert Path(result_path).suffix == ".xlsx"
            assert Path(result_path).stat().st_size > 0
        finally:
            export_module.EXPORT_DIR = original_export_dir

    def test_export_with_default_filename(self, sample_transactions, tmp_path):
        """Test export with auto-generated filename"""
        import utils.excel_export as export_module

        original_export_dir = export_module.EXPORT_DIR
        export_module.EXPORT_DIR = tmp_path

        try:
            result_path = ExcelExporter.export_transactions(
                sample_transactions,
                include_summary=True
            )

            assert Path(result_path).exists()
            assert "Transaksi_" in Path(result_path).name
            assert Path(result_path).suffix == ".xlsx"
        finally:
            export_module.EXPORT_DIR = original_export_dir

    def test_export_empty_transactions(self, tmp_path):
        """Test export with empty transaction list"""
        import utils.excel_export as export_module

        original_export_dir = export_module.EXPORT_DIR
        export_module.EXPORT_DIR = tmp_path

        try:
            result_path = ExcelExporter.export_transactions(
                [],
                filename="empty.xlsx",
                include_summary=True
            )

            assert Path(result_path).exists()
            assert Path(result_path).suffix == ".xlsx"
        finally:
            export_module.EXPORT_DIR = original_export_dir

    def test_status_text_conversion(self):
        """Test status code to text conversion"""
        assert ExcelExporter._get_status_text("P") == "Pending"
        assert ExcelExporter._get_status_text("A") == "Approved"
        assert ExcelExporter._get_status_text("L") == "Lunas"
        assert ExcelExporter._get_status_text("C") == "Cancelled"


class TestPDFReport:
    """Test PDF report functionality"""

    def test_generate_transaction_report_creates_file(self, sample_transactions, tmp_path):
        """Test that PDF report is created"""
        import utils.pdf_report as pdf_module

        original_export_dir = pdf_module.EXPORT_DIR
        pdf_module.EXPORT_DIR = tmp_path

        try:
            result_path = PDFReporter.generate_transaction_report(
                sample_transactions,
                filename="test_report.pdf",
                include_summary=True
            )

            assert Path(result_path).exists()
            assert Path(result_path).suffix == ".pdf"
            assert Path(result_path).stat().st_size > 0
        finally:
            pdf_module.EXPORT_DIR = original_export_dir

    def test_generate_with_default_filename(self, sample_transactions, tmp_path):
        """Test PDF generation with auto-generated filename"""
        import utils.pdf_report as pdf_module

        original_export_dir = pdf_module.EXPORT_DIR
        pdf_module.EXPORT_DIR = tmp_path

        try:
            result_path = PDFReporter.generate_transaction_report(
                sample_transactions,
                include_summary=True
            )

            assert Path(result_path).exists()
            assert "Laporan_Transaksi_" in Path(result_path).name
            assert Path(result_path).suffix == ".pdf"
        finally:
            pdf_module.EXPORT_DIR = original_export_dir

    def test_generate_summary_report(self, sample_transactions, tmp_path):
        """Test summary report by dealer"""
        import utils.pdf_report as pdf_module

        original_export_dir = pdf_module.EXPORT_DIR
        pdf_module.EXPORT_DIR = tmp_path

        try:
            result_path = PDFReporter.generate_summary_report(
                sample_transactions,
                filename="summary.pdf"
            )

            assert Path(result_path).exists()
            assert Path(result_path).suffix == ".pdf"
        finally:
            pdf_module.EXPORT_DIR = original_export_dir

    def test_pdf_with_empty_transactions(self, tmp_path):
        """Test PDF generation with empty list"""
        import utils.pdf_report as pdf_module

        original_export_dir = pdf_module.EXPORT_DIR
        pdf_module.EXPORT_DIR = tmp_path

        try:
            result_path = PDFReporter.generate_transaction_report(
                [],
                filename="empty_report.pdf",
                include_summary=True
            )

            assert Path(result_path).exists()
            assert Path(result_path).suffix == ".pdf"
        finally:
            pdf_module.EXPORT_DIR = original_export_dir

    def test_status_text_conversion(self):
        """Test status code conversion in PDF"""
        assert PDFReporter._get_status_text("P") == "Pending"
        assert PDFReporter._get_status_text("A") == "Approved"
        assert PDFReporter._get_status_text("L") == "Lunas"
        assert PDFReporter._get_status_text("C") == "Cancelled"
