"""refactor tasks

Revision ID: 53c64ee2ebf6
Revises: 1b4856363d4d
Create Date: 2025-05-30 18:26:15.349994

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "53c64ee2ebf6"
down_revision: Union[str, None] = "1b4856363d4d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("tasks", sa.Column("completed", sa.Boolean(), nullable=False))
    op.drop_column("tasks", "isCompleted")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "tasks", sa.Column("isCompleted", sa.BOOLEAN(), autoincrement=False, nullable=False)
    )
    op.drop_column("tasks", "completed")
