# ============================================================
# Standard Library
# ============================================================

from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import (
    func,
    select,
)

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import (
    joinedload,
)

# ============================================================
# Local Imports
# ============================================================

from app.models.booking_models.booking import Booking

from app.modules.properties.models.property_model import Property

from app.models.payment_models.payment import Payment
from app.models.payment_models.invoice import Invoice
# ============================================================
# Payment Repository
# ============================================================

class PaymentRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):

        self.db = db

    # ============================================================
    # Booking Queries
    # ============================================================

    async def get_booking_by_id(
        self,
        booking_id: UUID,
    ) -> Booking | None:

        result = await self.db.execute(
            select(Booking).where(
                Booking.id == booking_id,
            )
        )

        return result.scalar_one_or_none()

    # ============================================================
    # Payment Queries
    # ============================================================

    async def get_payment_by_id(
        self,
        payment_id: UUID,
    ) -> Payment | None:

        result = await self.db.execute(
            select(Payment).where(
                Payment.id == payment_id,
            )
        )

        return result.scalar_one_or_none()
    
    async def get_payment_by_reference(
        self,
        payment_reference: str,
    ) -> Payment | None:

        result = await self.db.execute(
            select(Payment).where(
                Payment.payment_reference == payment_reference,
            )
        )

        return result.scalar_one_or_none()
    

    async def get_payment_by_booking(
        self,
        booking_id: UUID,
    ) -> Payment | None:

        result = await self.db.execute(
            select(Payment).where(
                Payment.booking_id == booking_id,
            )
        )

        return result.scalar_one_or_none()
    
    async def get_invoice_by_booking(
        self,
        booking_id: UUID,
    ) -> Invoice | None:

        result = await self.db.execute(
            select(Invoice).where(
                Invoice.booking_id == booking_id,
            )
        )

        return result.scalar_one_or_none()
    
    # ============================================================
# Payment Commands
# ============================================================

async def create_payment(
    self,
    payment: Payment,
) -> Payment:

    self.db.add(
        payment,
    )

    await self.db.flush()

    await self.db.refresh(
        payment,
    )

    return payment

# ============================================================
# Invoice Commands
# ============================================================

async def create_invoice(
    self,
    invoice: Invoice,
) -> Invoice:

    self.db.add(
        invoice,
    )

    await self.db.flush()

    await self.db.refresh(
        invoice,
    )

    return invoice

# ============================================================
# Payment Commands
# ============================================================

async def update_payment(
    self,
    payment: Payment,
) -> Payment:

    await self.db.flush()

    await self.db.refresh(
        payment,
    )

    return payment


# ============================================================
# Payment Queries
# ============================================================

async def get_my_payments(
    self,
    customer_id: UUID,
) -> list[Payment]:

    result = await self.db.execute(
        select(Payment)
        .join(
            Booking,
            Booking.id == Payment.booking_id,
        )
        .where(
            Booking.customer_id == customer_id,
        )
        .order_by(
            Payment.created_at.desc(),
        )
    )

    return list(
        result.scalars().all(),
    )

# ============================================================
# Property Payment Queries
# ============================================================

async def get_property_payments(
    self,
    owner_id: UUID,
) -> list[Payment]:

    result = await self.db.execute(
        select(Payment)
        .join(
            Booking,
            Booking.id == Payment.booking_id,
        )
        .join(
            Property,
            Property.id == Booking.property_id,
        )
        .where(
            Property.owner_id == owner_id,
        )
        .order_by(
            Payment.created_at.desc(),
        )
    )

    return list(
        result.scalars().all(),
    )


# ============================================================
# Revenue Queries
# ============================================================

async def get_revenue_summary(
    self,
    owner_id: UUID,
):

    result = await self.db.execute(
        select(
            func.count(
                Payment.id,
            ),
            func.coalesce(
                func.sum(
                    Payment.amount,
                ),
                0,
            ),
            func.coalesce(
                func.sum(
                    Payment.refund_amount,
                ),
                0,
            ),
        )
        .join(
            Booking,
            Booking.id == Payment.booking_id,
        )
        .join(
            Property,
            Property.id == Booking.property_id,
        )
        .where(
            Property.owner_id == owner_id,
        )
    )

    return result.one()