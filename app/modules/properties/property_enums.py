# ============================================================
# Standard Library
# ============================================================

from enum import Enum

# ============================================================
# Property Type
# ============================================================

class PropertyType(str, Enum):
    """
    Types of properties supported by the platform.
    """

    HOTEL = "HOTEL"
    APARTMENT = "APARTMENT"
    VILLA = "VILLA"
    RESORT = "RESORT"
    HOMESTAY = "HOMESTAY"


# ============================================================
# Property Status
# ============================================================

class PropertyStatus(str, Enum):
    """
    Lifecycle status of a property.
    """

    DRAFT = "DRAFT"

    PENDING_VERIFICATION = "PENDING_VERIFICATION"

    PUBLISHED = "PUBLISHED"

    SUSPENDED = "SUSPENDED"

    ARCHIVED = "ARCHIVED"


# ============================================================
# Verification Status
# ============================================================

class VerificationStatus(str, Enum):
    """
    Verification state assigned by the Super Admin.
    """

    PENDING = "PENDING"

    APPROVED = "APPROVED"

    REJECTED = "REJECTED"