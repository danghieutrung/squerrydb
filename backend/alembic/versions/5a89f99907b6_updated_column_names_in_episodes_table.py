"""Updated column names in Episodes table

Revision ID: 5a89f99907b6
Revises: f95e7b2fd00b
Create Date: 2025-01-19 22:12:35.711431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a89f99907b6'
down_revision: Union[str, None] = 'f95e7b2fd00b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
