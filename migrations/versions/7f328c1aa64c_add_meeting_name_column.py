"""add Meeting.name column

Revision ID: 7f328c1aa64c
Revises: 137d853777e0
Create Date: 2024-06-20 12:29:00.350442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f328c1aa64c'
down_revision = '137d853777e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meeting', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=16), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meeting', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
