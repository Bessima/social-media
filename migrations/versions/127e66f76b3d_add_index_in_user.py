"""add index in user

Revision ID: 127e66f76b3d
Revises: 1fa392fd3da6
Create Date: 2023-06-12 14:55:15.194925

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '127e66f76b3d'
down_revision = '1fa392fd3da6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(op.f('ind_search'), 'users', ['first_name', 'second_name'], unique=False)


def downgrade() -> None:
    op.drop_index('ind_search', 'users')
