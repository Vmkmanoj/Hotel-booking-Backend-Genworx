"""create room type

Revision ID: 15ea9051105d
Revises: 7dc776c44eda
Create Date: 2026-07-22 09:55:32.054668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid


# revision identifiers, used by Alembic.
revision: str = '15ea9051105d'
down_revision: Union[str, Sequence[str], None] = '7dc776c44eda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "room_types",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        ),

        sa.Column(
            "property_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("properties.id", ondelete="CASCADE"),
            nullable=False,
        ),

        sa.Column(
            "name",
            sa.String(150),
            nullable=False,
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "base_price",
            sa.Numeric(10, 2),
            nullable=False,
        ),

        sa.Column(
            "max_adults",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "max_child",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "bed_configuration",
            postgresql.JSONB,
            nullable=True,
        ),

        sa.Column(
            "size_sqm",
            sa.Numeric(10, 2),
            nullable=True,
        ),

        sa.Column(
            "created_by",
            sa.String(100),
            nullable=True,
        ),

        sa.Column(
            "updated_by",
            sa.String(100),
            nullable=True,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now(),
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    op.create_index(
        "ix_room_types_property_id",
        "room_types",
        ["property_id"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_room_types_property_id",
        table_name="room_types",
    )

    op.drop_table("room_types")
