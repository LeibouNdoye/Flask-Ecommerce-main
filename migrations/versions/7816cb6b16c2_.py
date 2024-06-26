"""empty message

Revision ID: 7816cb6b16c2
Revises: 
Create Date: 2024-04-19 02:34:08.620583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7816cb6b16c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_product_category', 'category', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_category', type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
