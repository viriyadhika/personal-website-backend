"""001 user table

Revision ID: fd524f8acc32
Revises: 
Create Date: 2024-12-14 12:05:11.717503

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "fd524f8acc32"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "application_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=30), nullable=False),
        sa.Column("password", sa.LargeBinary(length=64), nullable=False),
        sa.Column("salt", sa.LargeBinary(length=64), nullable=False),
        sa.Column("role", sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    op.drop_table("application_user")
