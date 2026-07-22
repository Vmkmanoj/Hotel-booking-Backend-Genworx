"""create roomtable

Revision ID: 81c2d6e8a044
Revises: 15ea9051105d
Create Date: 2026-07-22 09:57:23.150800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import  postgresql
import uuid


# revision identifiers, used by Alembic.
revision: str = '81c2d6e8a044'
down_revision: Union[str, Sequence[str], None] = '15ea9051105d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "rooms",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        ),

        sa.Column(
            "room_type_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("room_types.id", ondelete="CASCADE"),
            nullable=False,
        ),

        sa.Column(
            "room_number",
            sa.String(50),
            nullable=False,
        ),

        sa.Column(
            "floor",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "status",
            sa.String(30),
            nullable=False,
            server_default="AVAILABLE",
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),

        sa.Column(
            "availability",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),

        sa.Column(
            "price",
            sa.Numeric(10, 2),
            nullable=False,
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

        # Prevent duplicate room numbers within the same room type
        sa.UniqueConstraint(
            "room_type_id",
            "room_number",
            name="uq_room_type_room_number"
        )
    )

    op.create_index(
        "ix_rooms_room_type_id",
        "rooms",
        ["room_type_id"],
    )

    op.create_index(
        "ix_rooms_status",
        "rooms",
        ["status"],
    )


def downgrade() -> None:
    op.drop_index("ix_rooms_status", table_name="rooms")
    op.drop_index("ix_rooms_room_type_id", table_name="rooms")
    op.drop_table("rooms")
