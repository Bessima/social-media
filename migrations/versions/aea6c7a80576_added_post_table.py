"""Added post table

Revision ID: aea6c7a80576
Revises: 0612a9dae6c9
Create Date: 2023-08-31 19:59:32.011393

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = 'aea6c7a80576'
down_revision = '0612a9dae6c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('author_id', postgresql.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ['author_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id', 'author_id'),
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
