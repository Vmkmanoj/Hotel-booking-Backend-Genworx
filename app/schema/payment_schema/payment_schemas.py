# ============================================================
# Standard Library
# ============================================================

from datetime import datetime
from decimal import Decimal
from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

# ============================================================
# Local Imports
# ============================================================

from app.common.enums.payment_enums.payment_enums import (
    InvoiceStatus,
    PaymentGateway,
    PaymentMethod,
    PaymentStatus,
    RefundStatus,
)

# ============================================================
# Create Payment Request
# ============================================================

class CreatePaymentRequest(BaseModel):
    """
    Request schema for creating a payment.
    """

    booking_id: UUID

    payment_method: PaymentMethod

    payment_gateway: PaymentGateway


# ============================================================
# Verify Payment Request
# ============================================================

class VerifyPaymentRequest(BaseModel):
    """
    Request schema for verifying a payment.
    """

    gateway_transaction_id: str = Field(
        min_length=1,
    )

    gateway_response: str | None = None


# ============================================================
# Refund Request
# ============================================================

class RefundRequest(BaseModel):
    """
    Request schema for processing a refund.
    """

    refund_amount: Decimal = Field(
        gt=0,
    )

    reason: str = Field(
        min_length=5,
        max_length=500,
    )

# ============================================================
# Payment Summary Response
# ============================================================

class PaymentSummaryResponse(BaseModel):
    """
    Summary response for a payment.
    """

    id: UUID

    booking_id: UUID

    payment_reference: str

    amount: Decimal

    currency: str

    payment_method: PaymentMethod

    payment_gateway: PaymentGateway

    payment_status: PaymentStatus

    paid_at: datetime | None

    model_config = ConfigDict(
        from_attributes=True,
    )


# ============================================================
# Payment Response
# ============================================================

class PaymentResponse(BaseModel):
    """
    Detailed response for a payment.
    """

    id: UUID

    booking_id: UUID

    payment_reference: str

    amount: Decimal

    currency: str

    payment_method: PaymentMethod

    payment_gateway: PaymentGateway

    payment_status: PaymentStatus

    gateway_transaction_id: str | None

    gateway_response: str | None

    refund_status: RefundStatus

    refund_amount: Decimal

    paid_at: datetime | None

    model_config = ConfigDict(
        from_attributes=True,
    )

# ============================================================
# Invoice Response
# ============================================================

class InvoiceResponse(BaseModel):
    """
    Response schema for an invoice.
    """

    id: UUID

    booking_id: UUID

    invoice_number: str

    invoice_status: InvoiceStatus

    invoice_amount: Decimal

    generated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )

# ============================================================
# Revenue Summary Response
# ============================================================

class RevenueSummaryResponse(BaseModel):
    """
    Revenue summary for a property.
    """

    total_payments: int

    total_revenue: Decimal

    total_refunds: Decimal

    net_revenue: Decimal