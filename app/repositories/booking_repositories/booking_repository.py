# ============================================================
# Standard Library
# ============================================================

from datetime import date
from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import (
    and_,
    select,
)

from sqlalchemy.orm import (
    joinedload,
)

from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.models.booking_models.booking import Booking
from app.models.booking_models.booking_room import BookingRoom
from app.models.booking_models.booking_history import BookingHistory
from app.models.booking_models.booking_cancellation import BookingCancellation

from app.modules.properties.models.property_model import Property
from app.modules.rooms.models.room_model import Room

from app.common.enums.booking_enums.booking_enums import (
    BookingStatus,
)

# ============================================================
# Booking Repository
# ============================================================

class BookingRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):

        self.db = db
    # ============================================================
    # Property Queries
    # ============================================================

    async def get_property_by_id(
        self,
        property_id: UUID,
    ) -> Property | None:

        result = await self.db.execute(
            select(Property).where(
                Property.id == property_id,
            )
        )

        return result.scalar_one_or_none()
    
    # ============================================================
    # Room Queries
    # ============================================================

    async def get_room_by_id(
        self,
        room_id: UUID,
    ) -> Room | None:

        result = await self.db.execute(
            select(Room).where(
                Room.id == room_id,
            )
        )

        return result.scalar_one_or_none()
    

    # ============================================================
    # Booking Commands
    # ============================================================

    async def create_booking(
        self,
        booking: Booking,
    ) -> Booking:

        self.db.add(booking)

        await self.db.flush()

        await self.db.refresh(booking)

        return booking
    
    # ============================================================
    # Room Queries
    # ============================================================

    async def get_rooms_by_ids(
        self,
        room_ids: list[UUID],
    ) -> list[Room]:

        result = await self.db.execute(
            select(Room).where(
                Room.id.in_(room_ids),
            )
        )

        return list(result.scalars().all())
    

    # ============================================================
    # Booking Room Commands
    # ============================================================

    async def create_booking_rooms(
        self,
        booking_rooms: list[BookingRoom],
    ) -> None:

        self.db.add_all(
            booking_rooms,
        )

        await self.db.flush()

    # ============================================================
    # Booking History Commands
    # ============================================================

    async def create_booking_history(
        self,
        booking_history: BookingHistory,
    ) -> None:

        self.db.add(
            booking_history,
        )

        await self.db.flush()


    # ============================================================
    # Booking Queries
    # ============================================================

    async def get_booking_by_id(
        self,
        booking_id: UUID,
    ) -> Booking | None:

        result = await self.db.execute(
            select(Booking)
            .options(
                joinedload(
                    Booking.booking_rooms,
                )
            )
            .where(
                Booking.id == booking_id,
            )
        )

        return result.scalar_one_or_none()


    async def get_customer_bookings(
        self,
        customer_id: UUID,
    ) -> list[Booking]:

        result = await self.db.execute(
            select(Booking)
            .where(
                Booking.customer_id == customer_id,
            )
            .order_by(
                Booking.created_at.desc(),
            )
        )

        return list(result.scalars().all())
    

    # ============================================================
    # Booking Cancellation Commands
    # ============================================================

    async def create_booking_cancellation(
        self,
        booking_cancellation: BookingCancellation,
    ) -> None:

        self.db.add(
            booking_cancellation,
        )

        await self.db.flush()

    # ============================================================
    # Availability Queries
    # ============================================================

    async def check_room_availability(
        self,
        room_id: UUID,
        check_in_date: date,
        check_out_date: date,
    ) -> bool:

        result = await self.db.execute(
            select(BookingRoom)
            .join(
                Booking,
                Booking.id == BookingRoom.booking_id,
            )
            .where(
                BookingRoom.room_id == room_id,
                Booking.booking_status.notin_(
                    [
                        "CANCELLED",
                        "COMPLETED",
                    ]
                ),
                and_(
                    Booking.check_in_date < check_out_date,
                    Booking.check_out_date > check_in_date,
                ),
            )
        )

        booking_room = result.scalar_one_or_none()

        return booking_room is None
    

    # ============================================================
    # Booking Queries
    # ============================================================

    async def get_upcoming_bookings(
        self,
        customer_id: UUID,
        today: date,
    ) -> list[Booking]:

        result = await self.db.execute(
            select(Booking)
            .where(
                Booking.customer_id == customer_id,
                Booking.check_in_date >= today,
                Booking.booking_status != BookingStatus.CANCELLED,
            )
            .order_by(
                Booking.check_in_date.asc(),
            )
        )

        return list(result.scalars().all())
    

    async def get_completed_bookings(
        self,
        customer_id: UUID,
    ) -> list[Booking]:

        result = await self.db.execute(
            select(Booking)
            .where(
                Booking.customer_id == customer_id,
                Booking.booking_status == BookingStatus.COMPLETED,
            )
            .order_by(
                Booking.check_out_date.desc(),
            )
        )

        return list(result.scalars().all())