"""rename department

Revision ID: 8753ee75061a
Revises: 3f3173bbcd44
Create Date: 2025-06-10 15:00:20.662259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8753ee75061a'
down_revision = '3f3173bbcd44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
