"""added password column

Revision ID: 48734176150d
Revises: 82cba7e49af6
Create Date: 2022-07-30 22:19:32.261216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48734176150d'
down_revision = '82cba7e49af6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
