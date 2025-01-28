"""fix column naming

Revision ID: f95e7b2fd00b
Revises: 7e5154fc77bc
Create Date: 2025-01-19 21:45:27.829762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f95e7b2fd00b'
down_revision: Union[str, None] = '7e5154fc77bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
