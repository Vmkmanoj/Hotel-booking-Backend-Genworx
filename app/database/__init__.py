from app.database.base import Base
from app.database.base_table import BaseModel
from app.database.session import AsyncSessionLocal, engine, get_db

# Import ORM models so Alembic can discover them
from app.modules.users.models import (
    Permission,
    Role,
    RolePermission,
    User,
)

from app.modules.properties.models import Property

from app.modules.bookings.models import (
    Booking,
    BookingRoom,
    BookingHistory,
    BookingCancellation,
)

from app.modules.payments.models import (
    Invoice,
    Payment,
)


__all__ = [
    "Base",
    "BaseModel",
    "engine",
    "AsyncSessionLocal",
    "get_db",

    "User",
    "Role",
    "Permission",
    "RolePermission",

    "Property",


    "Booking",
    "BookingRoom",
    "BookingHistory",
    "BookingCancellation",

    "Payment",
    "Invoice",
]