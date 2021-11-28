"""create_user_car_table..

Revision ID: eb85c17cf651
Revises: e367fdeb9e18
Create Date: 2021-11-27 01:58:12.829209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb85c17cf651'
down_revision = '833b6a99f8e9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_cars',
    sa.Column('user_car_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['car_id'], ['cars.car_id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('user_car_id'),
    )


def downgrade():
    op.drop_table('user_cars')
