"""

Revision ID: 4a871a11b02b
Revises: cc1dcaae0a25
Create Date: 2025-01-19 22:38:12.864229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a871a11b02b'
down_revision: Union[str, None] = 'cc1dcaae0a25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
