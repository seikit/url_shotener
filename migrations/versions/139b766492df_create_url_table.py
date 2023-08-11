"""create url table

Revision ID: 139b766492df
Revises:
Create Date: 2023-08-10 20:55:38.263118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "139b766492df"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "url",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("short_url", sa.String(6), nullable=False),
        sa.Column("long_url", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("url")
