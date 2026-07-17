"""role Permission

Revision ID: eff4a07b9fda
Revises: a610684d4518
Create Date: 2026-07-17 09:54:10.901689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'eff4a07b9fda'
down_revision: Union[str, Sequence[str], None] = 'a610684d4518'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
        op.create_table(
        "role_permissions",

        sa.Column(
            "rolesId",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("roles.id", ondelete="CASCADE"),
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
