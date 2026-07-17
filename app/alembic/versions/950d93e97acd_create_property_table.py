"""create property table

Revision ID: 950d93e97acd
Revises: d2cdf23a4aed
Create Date: 2026-07-17 16:18:05.189532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
# revision identifiers, used by Alembic.
revision: str = '950d93e97acd'
down_revision: Union[str, Sequence[str], None] = 'd2cdf23a4aed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "properties",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
        ),

        sa.Column(
            "owner_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id"),
            nullable=False,
        ),

        # sa.Column(
        #     "address_id",
        #     postgresql.UUID(as_uuid=True),
        #     sa.ForeignKey("addresses.id"),
        #     nullable=False,
        # ),

        sa.Column("property_name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("property_type", sa.String(length=255), nullable=False),
        sa.Column("star_rating", sa.Integer(), nullable=True),
        sa.Column("contact_email", sa.String(length=255), nullable=False),
        sa.Column("contact_number", sa.String(length=20), nullable=False),
        sa.Column("cancellation_policy", sa.Text(), nullable=True),
        sa.Column("house_rules", postgresql.JSONB(), nullable=True),
        sa.Column("child_policy", sa.Text(), nullable=True),
        sa.Column("pet_policy", sa.Text(), nullable=True),
        sa.Column("smoking_policy", sa.Text(), nullable=True),
        sa.Column("status", sa.String(length=100), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("avg_rating", sa.DECIMAL(2, 1), nullable=True),
        sa.Column("total_reviews", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("check_in_time", sa.Time(), nullable=False),
        sa.Column("check_out_time", sa.Time(), nullable=False),
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
        sa.Column("created_by", sa.String(length=100), nullable=True),
        sa.Column("updated_by", sa.String(length=100), nullable=True),
    )


def downgrade():
    op.drop_table("properties")
