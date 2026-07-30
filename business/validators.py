"""
Data Validators
Handles validation of input data before database operations
"""

import re
from datetime import date, datetime
from typing import Any, Dict, List

from config import (
    MAX_TEXT_LENGTH,
    MAX_NOTES_LENGTH,
    MAX_CURRENCY_VALUE,
    MIN_TRANSACTION_DATE_OFFSET_YEARS,
    MAX_TRANSACTION_DATE_OFFSET_DAYS,
)
from business.exceptions import ValidationErrors, ValidationException


class BaseValidator:
    """Base validator class with common validation methods"""

    def __init__(self):
        self.errors = []

    def reset(self):
        """Clear errors"""
        self.errors = []

    def add_error(self, field: str, message: str):
        """Add validation error"""
        self.errors.append({"field": field, "message": message})

    def has_errors(self) -> bool:
        """Check if there are validation errors"""
        return len(self.errors) > 0

    def get_errors(self) -> List[Dict[str, str]]:
        """Get all errors"""
        return self.errors

    def raise_if_errors(self):
        """Raise exception if there are errors"""
        if self.has_errors():
            raise ValidationErrors(self.errors)

    # =====================================================================
    # COMMON VALIDATORS
    # =====================================================================

    def validate_required(self, value: Any, field_name: str) -> bool:
        """Validate that value is not empty"""
        if value is None or (isinstance(value, str) and value.strip() == ""):
            self.add_error(field_name, f"{field_name} tidak boleh kosong")
            return False
        return True

    def validate_string_length(
        self,
        value: str,
        field_name: str,
        min_length: int = 1,
        max_length: int = MAX_TEXT_LENGTH,
    ) -> bool:
        """Validate string length"""
        if not isinstance(value, str):
            self.add_error(field_name, f"{field_name} harus string")
            return False

        length = len(value.strip())

        if length < min_length:
            self.add_error(
                field_name,
                f"{field_name} minimal {min_length} karakter"
            )
            return False

        if length > max_length:
            self.add_error(
                field_name,
                f"{field_name} maksimal {max_length} karakter"
            )
            return False

        return True

    def validate_numeric(
        self,
        value: Any,
        field_name: str,
        min_value: float = None,
        max_value: float = None,
    ) -> bool:
        """Validate numeric value"""
        try:
            num_value = float(value)
        except (ValueError, TypeError):
            self.add_error(field_name, f"{field_name} harus angka")
            return False

        if min_value is not None and num_value < min_value:
            self.add_error(
                field_name,
                f"{field_name} minimal {min_value}"
            )
            return False

        if max_value is not None and num_value > max_value:
            self.add_error(
                field_name,
                f"{field_name} maksimal {max_value}"
            )
            return False

        return True

    def validate_currency(
        self,
        value: Any,
        field_name: str,
        allow_zero: bool = True,
    ) -> bool:
        """Validate currency value"""
        if not self.validate_numeric(value, field_name, 0, MAX_CURRENCY_VALUE):
            return False

        if not allow_zero and float(value) == 0:
            self.add_error(field_name, f"{field_name} tidak boleh 0")
            return False

        return True

    def validate_date(self, value: Any, field_name: str) -> bool:
        """Validate date value"""
        if isinstance(value, date):
            return True

        if isinstance(value, str):
            for fmt in ["%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"]:
                try:
                    datetime.strptime(value, fmt)
                    return True
                except ValueError:
                    continue

        self.add_error(field_name, f"{field_name} format tanggal tidak valid")
        return False

    def validate_date_range(
        self,
        date_from: date,
        date_to: date,
        field_name: str = "Tanggal",
    ) -> bool:
        """Validate date range (from <= to)"""
        if date_from > date_to:
            self.add_error(
                field_name,
                f"Tanggal mulai harus <= tanggal akhir"
            )
            return False
        return True

    def validate_email(self, value: str, field_name: str) -> bool:
        """Validate email format"""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if value and not re.match(email_pattern, value):
            self.add_error(field_name, f"{field_name} format email tidak valid")
            return False

        return True

    def validate_phone(self, value: str, field_name: str) -> bool:
        """Validate phone number format"""
        if not value:
            return True  # Phone is optional

        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)]', '', value)

        if not cleaned.isdigit() or len(cleaned) < 10:
            self.add_error(
                field_name,
                f"{field_name} harus minimal 10 angka"
            )
            return False

        return True

    def validate_in_list(
        self,
        value: str,
        field_name: str,
        allowed_values: list,
    ) -> bool:
        """Validate value is in allowed list"""
        if value not in allowed_values:
            self.add_error(
                field_name,
                f"{field_name} harus salah satu dari: {', '.join(allowed_values)}"
            )
            return False

        return True


class TransaksiValidator(BaseValidator):
    """Validator for Transaksi (Transactions)"""

    def validate_create(self, data: Dict[str, Any], existing_repo=None) -> bool:
        """Validate transaction creation"""
        self.reset()

        # Required fields
        self.validate_required(data.get("nota"), "Nota")
        self.validate_required(data.get("tanggal"), "Tanggal")
        self.validate_required(data.get("dealer_id"), "Dealer")
        self.validate_required(data.get("nama_pembeli"), "Nama Pembeli")
        self.validate_required(data.get("motor_id"), "Motor")

        # Nota - alphanumeric
        nota = data.get("nota")
        if nota and not re.match(r'^[A-Z0-9-]+$', nota):
            self.add_error("Nota", "Nota harus huruf besar dan angka")

        # Nota - must be unique
        if nota and existing_repo:
            if existing_repo.get_by_nota(nota):
                self.add_error("Nota", f"Nota '{nota}' sudah terdaftar")

        # Tanggal
        tanggal = data.get("tanggal")
        if tanggal:
            self.validate_date(tanggal, "Tanggal")
            # Check date not too far in past or future
            today = date.today()
            if isinstance(tanggal, str):
                try:
                    tanggal = datetime.strptime(tanggal, "%Y-%m-%d").date()
                except:
                    tanggal = None

            if tanggal:
                days_diff = abs((tanggal - today).days)
                if days_diff > MAX_TRANSACTION_DATE_OFFSET_DAYS:
                    self.add_error(
                        "Tanggal",
                        f"Tanggal maksimal {MAX_TRANSACTION_DATE_OFFSET_DAYS} hari"
                    )

        # Nama Pembeli
        nama = data.get("nama_pembeli")
        if nama:
            self.validate_string_length(nama, "Nama Pembeli", 3, 100)

        # Telepon
        telp = data.get("telp_pembeli")
        if telp:
            self.validate_phone(telp, "Telepon")

        # Email
        email = data.get("email_pembeli")
        if email:
            self.validate_email(email, "Email")

        # Status
        status = data.get("status_transaksi")
        if status:
            self.validate_in_list(status, "Status", ["P", "A", "L", "C"])

        self.raise_if_errors()
        return not self.has_errors()

    def validate_update(self, data: Dict[str, Any]) -> bool:
        """Validate transaction update"""
        self.reset()

        # Only validate fields that are being updated
        if "nama_pembeli" in data:
            self.validate_string_length(data["nama_pembeli"], "Nama Pembeli", 3, 100)

        if "telp_pembeli" in data:
            self.validate_phone(data["telp_pembeli"], "Telepon")

        if "email_pembeli" in data:
            self.validate_email(data["email_pembeli"], "Email")

        if "status_transaksi" in data:
            self.validate_in_list(
                data["status_transaksi"],
                "Status",
                ["P", "A", "L", "C"]
            )

        self.raise_if_errors()
        return not self.has_errors()


class TransaksiDetailValidator(BaseValidator):
    """Validator for TransaksiDetail (Financial Details)"""

    def validate(self, data: Dict[str, Any]) -> bool:
        """Validate transaction detail"""
        self.reset()

        # All financial amounts should be >= 0
        for field in ["dp", "subsidi", "diskon", "diskon_tambahan", "insentif", "pelunasan", "lain_lain"]:
            if field in data and data[field] is not None:
                self.validate_currency(data[field], field, allow_zero=True)

        # If tgl_lunas provided, should be valid date
        if "tgl_lunas" in data and data["tgl_lunas"]:
            self.validate_date(data["tgl_lunas"], "Tgl Lunas")

        self.raise_if_errors()
        return not self.has_errors()


class DealerValidator(BaseValidator):
    """Validator for Dealer"""

    def validate_create(self, data: Dict[str, Any]) -> bool:
        """Validate dealer creation"""
        self.reset()

        # Required
        self.validate_required(data.get("nama"), "Nama Dealer")

        # Nama
        nama = data.get("nama")
        if nama:
            self.validate_string_length(nama, "Nama", 3, 100)

        # Telepon
        telp = data.get("telp")
        if telp:
            self.validate_phone(telp, "Telepon")

        # Email
        email = data.get("email")
        if email:
            self.validate_email(email, "Email")

        # Status
        status = data.get("status")
        if status:
            self.validate_in_list(status, "Status", ["A", "I"])

        self.raise_if_errors()
        return not self.has_errors()


class StokMotorValidator(BaseValidator):
    """Validator for StokMotor (Vehicle Inventory)"""

    def validate_create(self, data: Dict[str, Any]) -> bool:
        """Validate vehicle creation"""
        self.reset()

        # Required
        self.validate_required(data.get("no_mesin"), "No Mesin")
        self.validate_required(data.get("no_rangka"), "No Rangka")
        self.validate_required(data.get("type_id"), "Tipe Motor")
        self.validate_required(data.get("tgl_datang"), "Tgl Datang")

        # No Mesin
        no_mesin = data.get("no_mesin")
        if no_mesin:
            self.validate_string_length(no_mesin, "No Mesin", 10, 25)

        # No Rangka
        no_rangka = data.get("no_rangka")
        if no_rangka:
            self.validate_string_length(no_rangka, "No Rangka", 10, 25)

        # Tgl Datang
        tgl = data.get("tgl_datang")
        if tgl:
            self.validate_date(tgl, "Tgl Datang")

        # Status
        status = data.get("status")
        if status:
            self.validate_in_list(status, "Status", ["R", "S", "T", "D"])

        self.raise_if_errors()
        return not self.has_errors()


class PriceValidator(BaseValidator):
    """Validator for price-related operations"""

    def validate_calculation(
        self,
        otr: float,
        dp: float,
        subsidi: float,
        diskon: float,
    ) -> bool:
        """Validate pricing calculation"""
        self.reset()

        # OTR should be positive
        self.validate_currency(otr, "OTR (Harga Jual)", allow_zero=False)

        # DP should not exceed OTR
        if dp > otr:
            self.add_error("DP", "DP tidak boleh melebihi harga jual")

        # Total discount should not exceed OTR
        total_discount = subsidi + diskon
        if total_discount > otr:
            self.add_error(
                "Diskon",
                "Total subsidi + diskon tidak boleh melebihi harga jual"
            )

        self.raise_if_errors()
        return not self.has_errors()
