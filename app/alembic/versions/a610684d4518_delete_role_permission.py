"""delete role Permission

Revision ID: a610684d4518
Revises: 97c1d8974da9
Create Date: 2026-07-17 09:48:12.972746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a610684d4518'
down_revision: Union[str, Sequence[str], None] = '97c1d8974da9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("role_permissions")


def downgrade() -> None:
    """Downgrade schema."""
    pass
