"""Create article table

Revision ID: 13eae820a4a4
Revises: a373039c17ea
Create Date: 2023-06-10 18:23:02.550863

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "13eae820a4a4"
down_revision = "a373039c17ea"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "article",
        sa.Column("article_id", sa.String(64), primary_key=True),
        sa.Column("title", sa.String(120)),
        sa.Column(
            "slug", sa.String(120), unique=True, index=True
        ),
        sa.Column("description", sa.String(250)),
        sa.Column("body", sa.Text()),
        sa.Column(
            "user_id",
            sa.String(64),
            sa.ForeignKey("user.user_id"),
            index=True
        ),
        sa.Column("record_status", sa.String(1), server_default="normal"),
        sa.Column(
            "created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            server_onupdate=sa.func.now(),
        ),
    )


def downgrade() -> None:
    op.drop_table("article")
