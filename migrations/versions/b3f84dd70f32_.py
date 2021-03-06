"""empty message

Revision ID: b3f84dd70f32
Revises: fc09c3beef0e
Create Date: 2021-06-28 19:07:58.555683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3f84dd70f32'
down_revision = 'fc09c3beef0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###
