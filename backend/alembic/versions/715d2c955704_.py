"""

Revision ID: 715d2c955704
Revises: faeff56100c0
Create Date: 2025-01-20 17:23:01.267905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '715d2c955704'
down_revision: Union[str, None] = 'faeff56100c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
