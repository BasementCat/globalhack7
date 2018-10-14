"""resource picture field

Revision ID: 08b88db1317a
Revises: 171f43935192
Create Date: 2018-10-13 21:43:08.357403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08b88db1317a'
down_revision = '171f43935192'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resources', sa.Column('picture', sa.UnicodeText(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resources', 'picture')
    # ### end Alembic commands ###