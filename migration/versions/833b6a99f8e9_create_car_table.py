"""create_car_table..

Revision ID: 833b6a99f8e9
Revises: e367fdeb9e18
Create Date: 2021-11-26 23:08:55.022888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '833b6a99f8e9'
down_revision = 'c77c0ea5fbbd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cars',
        sa.Column('car_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('trimId', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('car_id'),
    )


def downgrade():
    op.drop_table('cars')
