"""

Revision ID: b852309caa87
Revises: 715d2c955704
Create Date: 2025-01-20 17:24:10.204673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b852309caa87'
down_revision: Union[str, None] = '715d2c955704'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
