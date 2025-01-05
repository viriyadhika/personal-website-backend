"""002 crawler table

Revision ID: 8a67177ddb76
Revises: fd524f8acc32
Create Date: 2024-12-14 16:44:43.952727

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "8a67177ddb76"
down_revision: Union[str, None] = "fd524f8acc32"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "batch",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("batch_id", sa.String(length=100), nullable=False),
        sa.Column("location", sa.String(length=100), nullable=False),
        sa.Column("keywords", sa.String(length=100), nullable=False),
        sa.Column(
            "last_updated",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("batch_id"),
    )
    op.create_table(
        "company",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("company_id", sa.String(length=25), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("link", sa.String(length=300), nullable=False),
        sa.Column("employee", sa.String(length=25), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("company_id"),
    )
    op.create_table(
        "job",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("job_id", sa.String(length=25), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("link", sa.String(length=300), nullable=False),
        sa.Column("company_id", sa.String(length=25), nullable=False),
        sa.Column("description", sa.String(length=3000), nullable=True),
        sa.ForeignKeyConstraint(
            ["company_id"],
            ["company.company_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("job_id"),
    )
    op.create_table(
        "batch_relationship",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("batch_id", sa.String(length=100), nullable=False),
        sa.Column("job_id", sa.String(length=25), nullable=False),
        sa.Column(
            "timestamp",
            sa.Date(),
            server_default=sa.text("CURRENT_DATE"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["batch_id"],
            ["batch.batch_id"],
        ),
        sa.ForeignKeyConstraint(
            ["job_id"],
            ["job.job_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("batch_id", "job_id", "timestamp", name="unique_index"),
    )


def downgrade() -> None:
    op.drop_table("batch_relationship")
    op.drop_table("job")
    op.drop_table("company")
    op.drop_table("batch")
