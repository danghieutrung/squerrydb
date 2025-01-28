"""

Revision ID: 3eda590179c2
Revises: b852309caa87
Create Date: 2025-01-20 18:19:34.284050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3eda590179c2'
down_revision: Union[str, None] = 'b852309caa87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
