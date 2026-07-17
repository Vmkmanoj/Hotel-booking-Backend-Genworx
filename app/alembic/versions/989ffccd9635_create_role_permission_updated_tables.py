"""create role permission updated  tables

Revision ID: 989ffccd9635
Revises: a79a27ea78bd
Create Date: 2026-07-16 16:14:56.189308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '989ffccd9635'
down_revision: Union[str, Sequence[str], None] = 'a79a27ea78bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("role_permissions")

def downgrade() -> None:
    """Downgrade schema."""
    pass
