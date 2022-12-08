"""create users table

Revision ID: 3f8122d300fc
Revises: 
Create Date: 2022-12-07 12:32:26.290301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f8122d300fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), unique=True),
        sa.Column('first_name', sa.String(100)),
        sa.Column('last_name', sa.String(100)),
        sa.Column('hashed_password', sa.String(500)),
        sa.Column('otp_secret', sa.String(500)),
        sa.Column('disabled', sa.Boolean, default=False),
        sa.Column('user_role', sa.String(50)),
    )


def downgrade():
    pass
