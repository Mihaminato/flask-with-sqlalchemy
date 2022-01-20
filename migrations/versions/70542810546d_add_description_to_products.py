"""add description to products

Revision ID: 70542810546d
Revises: b792377bd55c
Create Date: 2022-01-20 11:27:10.888562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70542810546d'
down_revision = 'b792377bd55c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'description')
    # ### end Alembic commands ###
