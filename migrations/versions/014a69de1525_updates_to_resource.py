"""Updates to resource

Revision ID: 014a69de1525
Revises: 2d8b71248ae4
Create Date: 2018-10-13 13:13:51.457705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '014a69de1525'
down_revision = '2d8b71248ae4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('fontaweseome_icon', sa.UnicodeText(), nullable=True))
    op.add_column('categories', sa.Column('parent_id', sa.BigInteger(), nullable=True))
    op.alter_column('categories', 'name',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.create_foreign_key('fk_cat_parent', 'categories', 'categories', ['parent_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_cat_parent', 'categories', type_='foreignkey')
    op.alter_column('categories', 'name',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.drop_column('categories', 'parent_id')
    op.drop_column('categories', 'fontaweseome_icon')
    # ### end Alembic commands ###
