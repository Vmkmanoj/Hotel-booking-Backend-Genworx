"""create room images

Revision ID: 4522db696dbb
Revises: 81c2d6e8a044
Create Date: 2026-07-22 09:59:10.422920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

# revision identifiers, used by Alembic.
revision: str = '4522db696dbb'
down_revision: Union[str, Sequence[str], None] = '81c2d6e8a044'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "room_images",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4,
        ),

        sa.Column(
            "room_type_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("room_types.id", ondelete="CASCADE"),
            nullable=False,
        ),

        sa.Column(
            "image_url",
            sa.String(500),
            nullable=False,
        ),

        sa.Column(
            "caption",
            sa.String(255),
            nullable=True,
        ),

        sa.Column(
            "display_order",
            sa.Integer(),
            nullable=False,
            server_default="1",
        ),

        sa.Column(
            "is_cover",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
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
        "ix_room_type_images_room_type_id",
        "room_images",
        ["room_type_id"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_room_type_images_room_type_id",
        table_name="room_images",
    )

    op.drop_table("room_images")
