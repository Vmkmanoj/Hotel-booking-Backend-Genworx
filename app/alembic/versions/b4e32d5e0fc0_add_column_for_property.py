"""add column for property

Revision ID: b4e32d5e0fc0
Revises: 0031ed273c55
Create Date: 2026-07-20 14:15:03.339995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4e32d5e0fc0'
down_revision: Union[str, Sequence[str], None] = '0031ed273c55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
