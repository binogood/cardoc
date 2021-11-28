"""create_car_tire_table..

Revision ID: 9641370b0435
Revises: eb85c17cf651
Create Date: 2021-11-27 14:11:44.538831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9641370b0435'
down_revision = 'eb85c17cf651'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('car_tires',
        sa.Column('car_tire_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('car_id', sa.Integer(), nullable=False),
        sa.Column('tire_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['car_id'],['cars.car_id'], ),
        sa.ForeignKeyConstraint(['tire_id'], ['tires.tire_id'], ),
        sa.PrimaryKeyConstraint('car_tire_id'),
    )


def downgrade():
    pass
