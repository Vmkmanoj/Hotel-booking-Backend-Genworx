"""add colum propertty

Revision ID: 0031ed273c55
Revises: 6b78a044b042
Create Date: 2026-07-17 16:25:30.625309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '0031ed273c55'
down_revision: Union[str, Sequence[str], None] = '6b78a044b042'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "properties",
        sa.Column(
            "address_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("addresses.id"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_column("properties", "address_id")
