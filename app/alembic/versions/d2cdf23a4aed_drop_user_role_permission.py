"""Drop user role Permission

Revision ID: d2cdf23a4aed
Revises: eff4a07b9fda
Create Date: 2026-07-17 10:00:32.744745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2cdf23a4aed'
down_revision: Union[str, Sequence[str], None] = 'eff4a07b9fda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("user_roles")


def downgrade() -> None:
    """Downgrade schema."""
    pass
