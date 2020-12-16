"""empty message

Revision ID: 7396a78972d5
Revises: f311c7474ec5
Create Date: 2020-12-14 15:21:20.286972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7396a78972d5'
down_revision = 'f311c7474ec5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###