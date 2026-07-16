"""create roles tables

Revision ID: 844c215a123b
Revises: 
Create Date: 2026-07-16 09:44:54.635788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = '844c215a123b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False
        ),
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true")
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
    op.drop_table("roles")
