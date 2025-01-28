"""

Revision ID: 61f8d06549dc
Revises: 53c53a8b428d
Create Date: 2025-01-19 22:30:58.573042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61f8d06549dc'
down_revision: Union[str, None] = '53c53a8b428d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
