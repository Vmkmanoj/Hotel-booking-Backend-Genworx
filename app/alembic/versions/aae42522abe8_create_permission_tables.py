"""create permission tables

Revision ID: aae42522abe8
Revises: 844c215a123b
Create Date: 2026-07-16 10:29:36.148800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'aae42522abe8'
down_revision: Union[str, Sequence[str], None] = '844c215a123b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "permissions",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            server_default=sa.text("gen_random_uuid()")
        ),
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False,
            unique=True
        ),
        sa.Column(
            "modules",
            sa.String(length=100),
            nullable=False
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True
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
    op.drop_table("permissions")
