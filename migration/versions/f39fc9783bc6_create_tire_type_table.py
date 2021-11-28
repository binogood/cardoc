"""create_rear_tire_table..

Revision ID: f39fc9783bc6
Revises: 833b6a99f8e9
Create Date: 2021-11-26 23:09:02.166170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f39fc9783bc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tire_types',
        sa.Column('tire_type_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint('tire_type_id'),
        sa.UniqueConstraint('name'),
        )


def downgrade():
    op.drop_table('tire_types')
