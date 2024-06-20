"""empty message

Revision ID: 137d853777e0
Revises: e38350b8235e
Create Date: 2024-06-20 10:47:57.896714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137d853777e0'
down_revision = 'e38350b8235e'
branch_labels = None
depends_on = None


def upgrade():
    # Commands to remove the unique constraint
    with op.batch_alter_table('subject') as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=16),
               nullable=False)
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=8),
               nullable=False)
        batch_op.drop_constraint("unique_subject_name", "unique")
        batch_op.drop_constraint("unique_subject_code", "unique")

def downgrade():
    # Commands to add the unique constraint back
    with op.batch_alter_table('subject') as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=16),
               nullable=True)
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=8),
               nullable=True)
        batch_op.create_unique_constraint("unique_subject_name", ["name"])
        batch_op.create_unique_constraint("unique_subject_code", ["code"])