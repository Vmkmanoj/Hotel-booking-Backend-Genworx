"""create userTable tables

Revision ID: 8d23c673ab2c
Revises: aae42522abe8
Create Date: 2026-07-16 10:32:02.341492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '8d23c673ab2c'
down_revision: Union[str, Sequence[str], None] = 'aae42522abe8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
        ),
        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "password_hash",
            sa.String(length=255),
            nullable=False
        ),
        sa.Column(
            "first_name",
            sa.String(length=100),
            nullable=False
        ),
        sa.Column(
            "last_name",
            sa.String(length=100),
            nullable=True
        ),
        sa.Column(
            "phone",
            sa.String(length=20),
            nullable=True
        ),
        sa.Column(
            "avatar_url",
            sa.String(length=500),
            nullable=True
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true")
        ),
        sa.Column(
            "last_login_at",
            sa.DateTime(),
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
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
