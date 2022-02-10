"""user table information changed

Revision ID: 4f91a490e6fa
Revises: e4e5f2697188
Create Date: 2022-02-10 21:11:01.144958

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4f91a490e6fa'
down_revision = 'e4e5f2697188'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=50), nullable=False))
    op.drop_column('users', 'gender')
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('users', sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('users', sa.Column('is_superuser', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('gender', mysql.ENUM('male', 'female', 'other'), nullable=False))
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###