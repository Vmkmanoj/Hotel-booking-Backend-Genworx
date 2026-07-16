"""create role_permission tables

Revision ID: a79a27ea78bd
Revises: 8d23c673ab2c
Create Date: 2026-07-16 10:37:22.776131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'a79a27ea78bd'
down_revision: Union[str, Sequence[str], None] = '8d23c673ab2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "role_permissions",

        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            primary_key=True,
            nullable=False
        ),

        sa.Column(
            "permission_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("permissions.id", ondelete="CASCADE"),
            primary_key=True,
            nullable=False
        ),

        sa.Column(
            "created_by",
            sa.String(length=100),
            nullable=True
        ),

        sa.Column(
            "updated_by",
            sa.String(length=100),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
