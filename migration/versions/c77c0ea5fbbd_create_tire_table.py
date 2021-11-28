"""create_front_tire_table..

Revision ID: c77c0ea5fbbd
Revises: f39fc9783bc6
Create Date: 2021-11-26 23:09:06.147743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c77c0ea5fbbd'
down_revision = 'e367fdeb9e18'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tires',
        sa.Column('tire_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('value', sa.String(length=20), nullable=False),
        sa.Column('tire_type_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['tire_type_id'], ['tire_types.tire_type_id'], ),
        sa.PrimaryKeyConstraint('tire_id'),
        sa.UniqueConstraint('value'),
    )


def downgrade():
    op.drop_table('tires')
