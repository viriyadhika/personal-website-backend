"""002 crawler table

Revision ID: 8a67177ddb76
Revises: fd524f8acc32
Create Date: 2024-12-14 16:44:43.952727

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.crawler.model.base import CrawlerBase
from app.db.engine import engine

# revision identifiers, used by Alembic.
revision: str = "8a67177ddb76"
down_revision: Union[str, None] = "fd524f8acc32"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    CrawlerBase.metadata.create_all(engine)


def downgrade() -> None:
    CrawlerBase.metadata.drop_all(engine)
