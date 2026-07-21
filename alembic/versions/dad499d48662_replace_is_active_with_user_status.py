"""replace_is_active_with_user_status

Revision ID: dad499d48662
Revises: 0365292165ad
Create Date: 2026-07-20 22:08:02.887346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dad499d48662'
down_revision: Union[str, Sequence[str], None] = '0365292165ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    user_status_enum = sa.Enum(
        "ACTIVE",
        "SUSPENDED",
        "DEACTIVATED",
        name="user_status_enum",
    )

    user_status_enum.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "users",
        sa.Column(
            "user_status",
            user_status_enum,
            nullable=False,
            server_default="ACTIVE",
        ),
    )

    op.drop_column(
        "users",
        "is_active",
    )

    op.alter_column(
        "users",
        "user_status",
        server_default=None,
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.add_column(
        "users",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),
    )

    op.drop_column(
        "users",
        "user_status",
    )

    user_status_enum = sa.Enum(
        "ACTIVE",
        "SUSPENDED",
        "DEACTIVATED",
        name="user_status_enum",
    )

    user_status_enum.drop(
        op.get_bind(),
        checkfirst=True,
    )