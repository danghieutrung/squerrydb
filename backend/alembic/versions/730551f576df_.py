"""

Revision ID: 730551f576df
Revises: 3eda590179c2
Create Date: 2025-01-20 18:28:34.595713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '730551f576df'
down_revision: Union[str, None] = '3eda590179c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
