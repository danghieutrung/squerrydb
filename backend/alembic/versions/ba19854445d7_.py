"""

Revision ID: ba19854445d7
Revises: 4a871a11b02b
Create Date: 2025-01-19 22:38:57.936697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba19854445d7'
down_revision: Union[str, None] = '4a871a11b02b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
