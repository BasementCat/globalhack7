"""Initial models

Revision ID: daa150c72693
Revises: 
Create Date: 2018-10-13 11:25:54.628774

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = 'daa150c72693'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resources',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('created_at', sau.ArrowType(), nullable=False),
    sa.Column('updated_at', sau.ArrowType(), nullable=False),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=False),
    sa.Column('username', sa.Unicode(length=64), nullable=False),
    sa.Column('password', sa.UnicodeText(), nullable=False),
    sa.Column('email', sa.UnicodeText(), nullable=True),
    sa.Column('phone', sa.BigInteger(), nullable=True),
    sa.Column('secondary_phone', sa.BigInteger(), nullable=True),
    sa.Column('bio', sa.UnicodeText(), nullable=False),
    sa.Column('immigration_status', sa.String(length=32), nullable=True),
    sa.Column('primary_role', sa.String(length=32), nullable=True),
    sa.Column('language', sa.String(length=2), nullable=False),
    sa.Column('country', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_index(op.f('ix_users_immigration_status'), 'users', ['immigration_status'], unique=False)
    op.create_index(op.f('ix_users_updated_at'), 'users', ['updated_at'], unique=False)
    op.create_table('user_resources',
    sa.Column('created_at', sau.ArrowType(), nullable=False),
    sa.Column('updated_at', sau.ArrowType(), nullable=False),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('resource_id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('type', sa.String(length=8), nullable=True),
    sa.Column('quantity_available', sa.BigInteger(), nullable=True),
    sa.Column('quantity_needed', sa.BigInteger(), nullable=True),
    sa.Column('fulfilled', sa.Boolean(), server_default='0', nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_resources_created_at'), 'user_resources', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_resources_type'), 'user_resources', ['type'], unique=False)
    op.create_index(op.f('ix_user_resources_updated_at'), 'user_resources', ['updated_at'], unique=False)
    op.create_table('user_resource_fulfillment',
    sa.Column('created_at', sau.ArrowType(), nullable=False),
    sa.Column('updated_at', sau.ArrowType(), nullable=False),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('fulfilling_resource_id', sa.BigInteger(), nullable=False),
    sa.Column('fulfilled_resource_id', sa.BigInteger(), nullable=False),
    sa.Column('fulfilled_quantity', sa.BigInteger(), nullable=False),
    sa.Column('confirmed_by_recipient', sa.Boolean(), server_default='0', nullable=False),
    sa.ForeignKeyConstraint(['fulfilled_resource_id'], ['user_resources.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['fulfilling_resource_id'], ['user_resources.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_resource_fulfillment_created_at'), 'user_resource_fulfillment', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_resource_fulfillment_updated_at'), 'user_resource_fulfillment', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_resource_fulfillment_updated_at'), table_name='user_resource_fulfillment')
    op.drop_index(op.f('ix_user_resource_fulfillment_created_at'), table_name='user_resource_fulfillment')
    op.drop_table('user_resource_fulfillment')
    op.drop_index(op.f('ix_user_resources_updated_at'), table_name='user_resources')
    op.drop_index(op.f('ix_user_resources_type'), table_name='user_resources')
    op.drop_index(op.f('ix_user_resources_created_at'), table_name='user_resources')
    op.drop_table('user_resources')
    op.drop_index(op.f('ix_users_updated_at'), table_name='users')
    op.drop_index(op.f('ix_users_immigration_status'), table_name='users')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    op.drop_table('users')
    op.drop_table('resources')
    # ### end Alembic commands ###
