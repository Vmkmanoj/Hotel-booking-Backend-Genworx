"""add column for property

Revision ID: b4e32d5e0fc0
Revises: 0031ed273c55
Create Date: 2026-07-20 14:15:03.339995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'b4e32d5e0fc0'
down_revision: Union[str, Sequence[str], None] = '0031ed273c55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.add_column(
        "properties",
        sa.Column(
            "approval_remarks",
            sa.Text(),
            nullable=True
        )
    )

    op.add_column(
        "properties",
        sa.Column(
            "approved_by",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True
        )
    )

    op.add_column(
        "properties",
        sa.Column(
            "approved_at",
            sa.DateTime(),
            nullable=True
        )
    )

    op.add_column(
        "properties",
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false")
        )
    )


def downgrade():

    op.drop_column("properties", "is_deleted")
    op.drop_column("properties", "approved_at")
    op.drop_column("properties", "approved_by")
    op.drop_column("properties", "approval_remarks")