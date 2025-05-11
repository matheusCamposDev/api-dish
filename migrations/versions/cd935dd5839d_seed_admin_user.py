"""seed admin user

Revision ID: cd935dd5839d
Revises:
Create Date: 2025-04-23 16:33:05.245344

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cd935dd5839d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    user_table = sa.Table(
        "role",
        sa.MetaData(),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.bulk_insert(
        user_table,
        [
            {"name": "admin"},
            {"name": "normal"},
        ],
    )


def downgrade():
    pass
