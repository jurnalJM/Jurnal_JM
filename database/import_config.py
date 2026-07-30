"""
Import Configuration for Stok Motor
Maps dealer codes and handles dynamic type/warna creation
"""

# Dealer mapping: Kode dealer (dari Excel) → Dealer ID
DEALER_MAPPING = {
    'A0035': 1,  # Jaya Motor Pusat
    'A0105': 2,  # Jaya Motor BSD (Jaya Motor II)
}

def get_dealer_id(kode_dealer):
    """Get dealer ID from kode dealer"""
    return DEALER_MAPPING.get(kode_dealer)
