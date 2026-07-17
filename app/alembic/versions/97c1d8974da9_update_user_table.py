"""update user table

Revision ID: 97c1d8974da9
Revises: a6706bc89676
Create Date: 2026-07-17 09:41:18.045204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '97c1d8974da9'
down_revision: Union[str, Sequence[str], None] = 'a6706bc89676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
     op.add_column(
        "users",
        sa.Column(
            "roleId",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("roles.id"),
            nullable=True,
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
