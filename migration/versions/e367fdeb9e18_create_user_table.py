"""create_user_table..

Revision ID: e367fdeb9e18
Revises: 
Create Date: 2021-11-26 23:08:01.674114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e367fdeb9e18'
down_revision = 'f39fc9783bc6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=30), nullable=False),
        sa.Column('password', sa.String(length=200), nullable=False),
        sa.Column('is_admin', sa.Boolean(), default=False, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('name'),
    )


def downgrade():
    op.drop_table('users')
