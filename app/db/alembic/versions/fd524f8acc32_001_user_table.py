"""001 user table

Revision ID: fd524f8acc32
Revises: 
Create Date: 2024-12-14 12:05:11.717503

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.db.engine import engine
from app.auth.db.models.User import Base

# revision identifiers, used by Alembic.
revision: str = "fd524f8acc32"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    Base.metadata.create_all(engine)


def downgrade() -> None:
    Base.metadata.drop_all(engine)
