"""Remove immigration status

Revision ID: 7032046b3486
Revises: 08b88db1317a
Create Date: 2018-10-13 22:41:01.718177

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7032046b3486'
down_revision = '08b88db1317a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_immigration_status', table_name='users')
    op.drop_column('users', 'immigration_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('immigration_status', mysql.VARCHAR(length=32), nullable=True))
    op.create_index('ix_users_immigration_status', 'users', ['immigration_status'], unique=False)
    # ### end Alembic commands ###