"""
Custom Exceptions for Business Logic
"""


class BusinessLogicException(Exception):
    """Base exception for all business logic errors"""

    def __init__(self, message: str, code: str = None):
        self.message = message
        self.code = code or "BUSINESS_ERROR"
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.code}] {self.message}"


class ValidationException(BusinessLogicException):
    """Exception raised for validation errors"""

    def __init__(self, message: str, field: str = None, code: str = "VALIDATION_ERROR"):
        super().__init__(message, code)
        self.field = field

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "field": self.field,
        }


class ValidationErrors(BusinessLogicException):
    """Exception for multiple validation errors"""

    def __init__(self, errors: list, code: str = "VALIDATION_ERRORS"):
        self.errors = errors  # List of dicts: {field, message}
        message = f"{len(errors)} validation error(s)"
        super().__init__(message, code)

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "errors": self.errors,
            "count": len(self.errors),
        }

    def add_error(self, field: str, message: str):
        """Add another error"""
        self.errors.append({"field": field, "message": message})

    def has_errors(self):
        """Check if there are any errors"""
        return len(self.errors) > 0


class DuplicateRecordException(ValidationException):
    """Exception raised when trying to create duplicate record"""

    def __init__(self, message: str, field: str = None):
        super().__init__(message, field, "DUPLICATE_RECORD")


class RecordNotFound(BusinessLogicException):
    """Exception raised when record not found"""

    def __init__(self, model_name: str, id: any = None, field: str = None, value: str = None):
        if id:
            message = f"{model_name} with ID {id} not found"
        elif field and value:
            message = f"{model_name} with {field}='{value}' not found"
        else:
            message = f"{model_name} not found"
        super().__init__(message, "RECORD_NOT_FOUND")


class InvalidOperationException(BusinessLogicException):
    """Exception raised for invalid operations"""

    def __init__(self, message: str):
        super().__init__(message, "INVALID_OPERATION")


class InsufficientDataException(BusinessLogicException):
    """Exception raised when required data is missing"""

    def __init__(self, message: str, missing_fields: list = None):
        super().__init__(message, "INSUFFICIENT_DATA")
        self.missing_fields = missing_fields or []

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "missing_fields": self.missing_fields,
        }


class InventoryException(BusinessLogicException):
    """Exception raised for inventory-related errors"""

    def __init__(self, message: str):
        super().__init__(message, "INVENTORY_ERROR")


class PricingException(BusinessLogicException):
    """Exception raised for pricing calculation errors"""

    def __init__(self, message: str):
        super().__init__(message, "PRICING_ERROR")


class FinancialException(BusinessLogicException):
    """Exception raised for financial operation errors"""

    def __init__(self, message: str):
        super().__init__(message, "FINANCIAL_ERROR")
