"""
PDF Report Generator
Create PDF reports from transaction data
"""

from datetime import datetime
from pathlib import Path
from typing import List, Any, Tuple

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,
    PageBreak, KeepTogether, Image
)
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

from config import EXPORT_DIR


class PDFReporter:
    """Generate PDF reports from transaction data"""

    PAGE_SIZE = A4
    MARGIN = 0.5 * inch

    @staticmethod
    def generate_transaction_report(
        transactions: List[Any],
        filename: str = None,
        include_summary: bool = True,
        dealer_id: int = None,
    ) -> str:
        """
        Generate PDF report of transactions.

        Args:
            transactions: List of Transaksi objects
            filename: Optional custom filename
            include_summary: Include summary page
            dealer_id: Filter by dealer

        Returns:
            Path to created PDF
        """
        if not filename:
            filename = f"Laporan_Transaksi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        # Ensure export directory exists
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)

        filepath = EXPORT_DIR / filename

        # Create PDF document
        doc = SimpleDocTemplate(
            str(filepath),
            pagesize=PDFReporter.PAGE_SIZE,
            rightMargin=PDFReporter.MARGIN,
            leftMargin=PDFReporter.MARGIN,
            topMargin=PDFReporter.MARGIN,
            bottomMargin=PDFReporter.MARGIN,
        )

        # Build content
        story = []

        # Title page
        story.append(PDFReporter._create_title_page(doc.width))
        story.append(PageBreak())

        # Summary if requested
        if include_summary and transactions:
            story.append(PDFReporter._create_summary_section(doc.width, transactions))
            story.append(PageBreak())

        # Transaction details
        if transactions:
            story.append(PDFReporter._create_transactions_section(doc.width, transactions))

        # Build PDF
        doc.build(story)

        return str(filepath)

    @staticmethod
    def _create_title_page(width: float) -> Paragraph:
        """Create title page"""
        styles = getSampleStyleSheet()

        # Title style
        title_style = ParagraphStyle(
            "CustomTitle",
            parent=styles["Heading1"],
            fontSize=28,
            textColor=colors.HexColor("#1976D2"),
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
        )

        subtitle_style = ParagraphStyle(
            "CustomSubtitle",
            parent=styles["Normal"],
            fontSize=14,
            textColor=colors.HexColor("#666666"),
            spaceAfter=30,
            alignment=TA_CENTER,
        )

        date_style = ParagraphStyle(
            "DateStyle",
            parent=styles["Normal"],
            fontSize=11,
            textColor=colors.HexColor("#999999"),
            alignment=TA_CENTER,
        )

        title = Paragraph("JayaMotor", title_style)
        subtitle = Paragraph("Laporan Transaksi Penjualan Motor", subtitle_style)
        date_para = Paragraph(
            f"Tanggal Laporan: {datetime.now().strftime('%d %B %Y')}",
            date_style
        )

        return KeepTogether([Spacer(width, 1.5 * inch), title, subtitle, Spacer(width, 0.5 * inch), date_para])

    @staticmethod
    def _create_summary_section(width: float, transactions: List[Any]) -> KeepTogether:
        """Create summary section"""
        styles = getSampleStyleSheet()

        # Title
        title_style = ParagraphStyle(
            "SectionTitle",
            parent=styles["Heading2"],
            fontSize=14,
            textColor=colors.HexColor("#1976D2"),
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )

        elements = [Paragraph("RINGKASAN LAPORAN", title_style)]

        # Calculate totals
        total_transactions = len(transactions)
        total_dp = sum(float(t.detail.dp or 0) for t in transactions if t.detail)
        total_subsidi = sum(float(t.detail.subsidi or 0) for t in transactions if t.detail)
        total_diskon = sum(
            float((t.detail.diskon or 0) + (t.detail.diskon_tambahan or 0))
            for t in transactions if t.detail
        )
        total_insentif = sum(float(t.detail.insentif or 0) for t in transactions if t.detail)
        total_pelunasan = sum(float(t.detail.pelunasan or 0) for t in transactions if t.detail)

        # Summary table
        summary_data = [
            ["Keterangan", "Jumlah"],
            ["Total Transaksi", f"{total_transactions}"],
            ["Total DP", f"Rp {total_dp:,.2f}"],
            ["Total Subsidi", f"Rp {total_subsidi:,.2f}"],
            ["Total Diskon", f"Rp {total_diskon:,.2f}"],
            ["Total Insentif", f"Rp {total_insentif:,.2f}"],
            ["Total Pelunasan", f"Rp {total_pelunasan:,.2f}"],
        ]

        table = Table(summary_data, colWidths=[width * 0.6, width * 0.4])
        table.setStyle(TableStyle([
            # Headers
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2196F3")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 11),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

            # Data rows
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 10),
            ("ALIGN", (0, 1), (-1, -1), "LEFT"),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 1), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 8),

            # Borders
            ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#CCCCCC")),
        ]))

        elements.append(table)
        elements.append(Spacer(width, 0.3 * inch))

        return KeepTogether(elements)

    @staticmethod
    def _create_transactions_section(width: float, transactions: List[Any]) -> KeepTogether:
        """Create transaction details section"""
        styles = getSampleStyleSheet()

        # Title
        title_style = ParagraphStyle(
            "SectionTitle",
            parent=styles["Heading2"],
            fontSize=14,
            textColor=colors.HexColor("#1976D2"),
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )

        elements = [Paragraph("DETAIL TRANSAKSI", title_style)]

        # Transaction data
        table_data = [
            [
                "ID", "Tgl", "Nota", "Dealer", "Pembeli",
                "Type", "DP", "Subsidi", "Diskon", "Status"
            ]
        ]

        for trans in transactions:
            row = [
                str(trans.id),
                trans.tanggal.strftime("%d-%m-%y") if trans.tanggal else "",
                trans.nota,
                trans.dealer.nama[:12] if trans.dealer else "",
                trans.nama_pembeli[:15],
                trans.motor.type_motor.nama_type[:8] if trans.motor else "",
                f"Rp {float(trans.detail.dp or 0):,.0f}" if trans.detail else "0",
                f"Rp {float(trans.detail.subsidi or 0):,.0f}" if trans.detail else "0",
                f"Rp {float((trans.detail.diskon or 0) + (trans.detail.diskon_tambahan or 0)):,.0f}" if trans.detail else "0",
                PDFReporter._get_status_text(trans.status_transaksi),
            ]
            table_data.append(row)

        # Create table with column widths
        col_widths = [
            width * 0.06,  # ID
            width * 0.08,  # Date
            width * 0.08,  # Nota
            width * 0.12,  # Dealer
            width * 0.12,  # Pembeli
            width * 0.10,  # Type
            width * 0.10,  # DP
            width * 0.10,  # Subsidi
            width * 0.10,  # Diskon
            width * 0.08,  # Status
        ]

        table = Table(table_data, colWidths=col_widths)
        table.setStyle(TableStyle([
            # Headers
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2196F3")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 9),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

            # Alternating row colors
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),

            # Text alignment
            ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 8),
            ("ALIGN", (0, 1), (0, -1), "CENTER"),  # ID center
            ("ALIGN", (1, 1), (2, -1), "CENTER"),  # Date, Nota center
            ("ALIGN", (6, 1), (8, -1), "RIGHT"),   # Money right
            ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),

            # Padding
            ("TOPPADDING", (0, 1), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),

            # Borders
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
            ("LINEBELOW", (0, 0), (-1, 0), 1, colors.HexColor("#2196F3")),
        ]))

        elements.append(table)
        elements.append(Spacer(width, 0.3 * inch))

        # Footer
        footer_style = ParagraphStyle(
            "Footer",
            parent=styles["Normal"],
            fontSize=8,
            textColor=colors.HexColor("#999999"),
            alignment=TA_CENTER,
        )

        footer_text = f"Laporan dicetak pada {datetime.now().strftime('%d %B %Y %H:%M')}"
        elements.append(Paragraph(footer_text, footer_style))

        return KeepTogether(elements)

    @staticmethod
    def _get_status_text(status_code: str) -> str:
        """Convert status code to text"""
        status_map = {
            "P": "Pending",
            "A": "Approved",
            "L": "Lunas",
            "C": "Cancelled",
        }
        return status_map.get(status_code, status_code)

    @staticmethod
    def generate_summary_report(
        transactions: List[Any],
        filename: str = None,
    ) -> str:
        """
        Generate summary report by dealer.

        Args:
            transactions: List of Transaksi objects
            filename: Optional custom filename

        Returns:
            Path to created PDF
        """
        if not filename:
            filename = f"Ringkasan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        # Ensure export directory exists
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)

        filepath = EXPORT_DIR / filename

        # Create PDF document
        doc = SimpleDocTemplate(
            str(filepath),
            pagesize=PDFReporter.PAGE_SIZE,
            rightMargin=PDFReporter.MARGIN,
            leftMargin=PDFReporter.MARGIN,
            topMargin=PDFReporter.MARGIN,
            bottomMargin=PDFReporter.MARGIN,
        )

        # Build content
        story = []
        story.append(PDFReporter._create_title_page(doc.width))
        story.append(PageBreak())

        # Group by dealer
        dealer_data = {}
        for trans in transactions:
            dealer_name = trans.dealer.nama if trans.dealer else "Unknown"
            if dealer_name not in dealer_data:
                dealer_data[dealer_name] = {
                    "count": 0,
                    "total_dp": 0,
                    "total_subsidi": 0,
                    "total_diskon": 0,
                    "total_insentif": 0,
                }
            dealer_data[dealer_name]["count"] += 1
            if trans.detail:
                dealer_data[dealer_name]["total_dp"] += float(trans.detail.dp or 0)
                dealer_data[dealer_name]["total_subsidi"] += float(trans.detail.subsidi or 0)
                dealer_data[dealer_name]["total_diskon"] += float(
                    (trans.detail.diskon or 0) + (trans.detail.diskon_tambahan or 0)
                )
                dealer_data[dealer_name]["total_insentif"] += float(trans.detail.insentif or 0)

        # Add dealer summary
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "SectionTitle",
            parent=styles["Heading2"],
            fontSize=14,
            textColor=colors.HexColor("#1976D2"),
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )

        story.append(Paragraph("RINGKASAN PER DEALER", title_style))

        # Dealer table
        dealer_table_data = [
            ["Dealer", "Jumlah", "Total DP", "Total Subsidi", "Total Diskon"]
        ]

        for dealer_name, data in sorted(dealer_data.items()):
            row = [
                dealer_name,
                str(data["count"]),
                f"Rp {data['total_dp']:,.0f}",
                f"Rp {data['total_subsidi']:,.0f}",
                f"Rp {data['total_diskon']:,.0f}",
            ]
            dealer_table_data.append(row)

        table = Table(dealer_table_data, colWidths=[doc.width * 0.25, doc.width * 0.15, doc.width * 0.20, doc.width * 0.20, doc.width * 0.20])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2196F3")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("ALIGN", (1, 0), (-1, 0), "CENTER"),
            ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
            ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 9),
            ("ALIGN", (0, 1), (0, -1), "LEFT"),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 1), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 8),

            ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#CCCCCC")),
            ("LINEBELOW", (0, 0), (-1, 0), 2, colors.HexColor("#2196F3")),
        ]))

        story.append(table)

        # Build PDF
        doc.build(story)

        return str(filepath)
