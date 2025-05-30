"""refactor tasks

Revision ID: 1b4856363d4d
Revises: 6c672de1878a
Create Date: 2025-05-30 18:07:15.704288

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "1b4856363d4d"
down_revision: Union[str, None] = "6c672de1878a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("tasks", sa.Column("isCompleted", sa.Boolean(), nullable=False))
    op.drop_column("tasks", "is_completed")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "tasks", sa.Column("is_completed", sa.BOOLEAN(), autoincrement=False, nullable=False)
    )
    op.drop_column("tasks", "isCompleted")
