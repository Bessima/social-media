"""add friends tables

Revision ID: 0612a9dae6c9
Revises: 127e66f76b3d
Create Date: 2023-07-05 11:42:47.769192

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0612a9dae6c9'
down_revision = '127e66f76b3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'friends',
        sa.Column('user_id', postgresql.UUID(), nullable=False),
        sa.Column('friend_id', postgresql.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ['friend_id'],
            ['users.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('user_id', 'friend_id'),
    )


def downgrade() -> None:
    op.drop_table('friends')
