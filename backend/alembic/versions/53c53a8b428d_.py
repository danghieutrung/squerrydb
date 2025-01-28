"""

Revision ID: 53c53a8b428d
Revises: 5a89f99907b6
Create Date: 2025-01-19 22:30:18.956538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53c53a8b428d'
down_revision: Union[str, None] = '5a89f99907b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
