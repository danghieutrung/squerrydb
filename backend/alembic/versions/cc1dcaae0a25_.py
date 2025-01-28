"""

Revision ID: cc1dcaae0a25
Revises: 61f8d06549dc
Create Date: 2025-01-19 22:31:41.365439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc1dcaae0a25'
down_revision: Union[str, None] = '61f8d06549dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
