"""empty message

Revision ID: 5571a892a384
Revises: 3779e9841155
Create Date: 2020-12-14 09:48:26.149799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5571a892a384'
down_revision = '3779e9841155'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
