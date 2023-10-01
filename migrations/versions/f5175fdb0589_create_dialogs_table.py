"""create dialogs table

Revision ID: f5175fdb0589
Revises: aea6c7a80576
Create Date: 2023-09-11 22:22:31.473286

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f5175fdb0589'
down_revision = 'aea6c7a80576'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dialogs',
        sa.Column('user_id', postgresql.UUID(), nullable=False),
        sa.Column('opponent_id', postgresql.UUID(), nullable=False),
        sa.Column('message', sa.String(), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ['opponent_id'],
            ['users.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('user_id', 'opponent_id', 'created_at'),
    )


def downgrade() -> None:
    op.drop_table('dialogs')
