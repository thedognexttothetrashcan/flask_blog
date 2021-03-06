"""empty message

Revision ID: 5a98ef6bd552
Revises: 
Create Date: 2018-09-25 14:46:27.420466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a98ef6bd552'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=12), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('icon', sa.String(length=70), nullable=True),
    sa.Column('role', sa.Boolean(), nullable=True),
    sa.Column('lastLogin', sa.DateTime(), nullable=True),
    sa.Column('registerTime', sa.DateTime(), nullable=True),
    sa.Column('confirm', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
