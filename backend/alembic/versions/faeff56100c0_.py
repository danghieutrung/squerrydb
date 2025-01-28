"""

Revision ID: faeff56100c0
Revises: ba19854445d7
Create Date: 2025-01-20 17:02:54.073016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'faeff56100c0'
down_revision: Union[str, None] = 'ba19854445d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
