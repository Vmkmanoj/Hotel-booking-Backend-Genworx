# ============================================================
# Third Party
# ============================================================

from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.database.session import get_db

from app.dependencies.auth import get_current_user

from app.modules.users.models.users import User

from app.services.booking_services.booking_service import (
    BookingService,
)

from app.schema.booking_schema.booking_schemas import (
    BookingResponse,
    BookingSummaryResponse,
    CancelBookingRequest,
    CreateBookingRequest,
)

# ============================================================
# Booking Router
# ============================================================

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


# ============================================================
# Create Booking
# ============================================================

@router.post(
    "",
    response_model=BookingResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_booking(
    request: CreateBookingRequest,
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
) -> BookingResponse:
    """
    Creates a new booking for the authenticated customer.
    """

    service = BookingService(
        db,
    )

    return await service.create_booking(
        request=request,
        current_user=current_user,
    )



# ============================================================
# Get My Bookings
# ============================================================

@router.get(
    "/me",
    response_model=list[BookingSummaryResponse],
    status_code=status.HTTP_200_OK,
)
async def get_my_bookings(
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
) -> list[BookingSummaryResponse]:
    """
    Retrieves all bookings for the authenticated customer.
    """

    service = BookingService(
        db,
    )

    return await service.get_my_bookings(
        current_user=current_user,
    )

# ============================================================
# Get Upcoming Bookings
# ============================================================

@router.get(
    "/me/upcoming",
    response_model=list[BookingSummaryResponse],
    status_code=status.HTTP_200_OK,
)
async def get_upcoming_bookings(
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
) -> list[BookingSummaryResponse]:
    """
    Retrieves all upcoming bookings for the authenticated customer.
    """

    service = BookingService(
        db,
    )

    return await service.get_upcoming_bookings(
        current_user=current_user,
    )


# ============================================================
# Get Completed Bookings
# ============================================================

@router.get(
    "/me/completed",
    response_model=list[BookingSummaryResponse],
    status_code=status.HTTP_200_OK,
)
async def get_completed_bookings(
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
) -> list[BookingSummaryResponse]:
    """
    Retrieves all completed bookings for the authenticated customer.
    """

    service = BookingService(
        db,
    )

    return await service.get_completed_bookings(
        current_user=current_user,
    )


# ============================================================
# Get Booking By ID
# ============================================================

@router.get(
    "/{booking_id}",
    response_model=BookingResponse,
    status_code=status.HTTP_200_OK,
)
async def get_booking_by_id(
    booking_id: UUID,
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
) -> BookingResponse:
    """
    Retrieves a booking by its ID.
    """

    service = BookingService(
        db,
    )

    return await service.get_booking_by_id(
        booking_id=booking_id,
        current_user=current_user,
    )


# ============================================================
# Cancel Booking
# ============================================================

@router.patch(
    "/{booking_id}/cancel",
    status_code=status.HTTP_200_OK,
)
async def cancel_booking(
    booking_id: UUID,
    request: CancelBookingRequest,
    db: AsyncSession = Depends(
        get_db,
    ),
    current_user: User = Depends(
        get_current_user,
    ),
) -> dict[str, str]:
    """
    Cancels an existing booking.
    """

    service = BookingService(
        db,
    )

    await service.cancel_booking(
        booking_id=booking_id,
        request=request,
        current_user=current_user,
    )

    return {
        "message": "Booking cancelled successfully.",
    }