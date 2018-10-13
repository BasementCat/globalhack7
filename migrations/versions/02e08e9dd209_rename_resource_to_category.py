"""Rename resource to category

Revision ID: 02e08e9dd209
Revises: daa150c72693
Create Date: 2018-10-13 13:06:38.575269

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '02e08e9dd209'
down_revision = 'daa150c72693'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('user_resources_ibfk_1', 'user_resources', type_='foreignkey')
    op.drop_table('resources')
    op.add_column('user_resources', sa.Column('category_id', sa.BigInteger(), nullable=False))
    op.create_foreign_key('fk_user_resources_categories', 'user_resources', 'categories', ['category_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.drop_column('user_resources', 'resource_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_resources', sa.Column('resource_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False))
    op.drop_constraint('fk_user_resources_categories', 'user_resources', type_='foreignkey')
    op.create_foreign_key('user_resources_ibfk_1', 'user_resources', 'resources', ['resource_id'], ['id'], onupdate='CASCADE')
    op.drop_column('user_resources', 'category_id')
    op.create_table('resources',
    sa.Column('id', mysql.BIGINT(display_width=20), nullable=False),
    sa.Column('name', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('categories')
    # ### end Alembic commands ###