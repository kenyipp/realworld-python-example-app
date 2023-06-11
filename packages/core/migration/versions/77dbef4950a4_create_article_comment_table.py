"""Create article comment table

Revision ID: 77dbef4950a4
Revises: 81113fa7c137
Create Date: 2023-06-10 18:23:23.823153

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "77dbef4950a4"
down_revision = "81113fa7c137"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "article_comment",
        sa.Column("article_comment_id", sa.String(64), primary_key=True),
        sa.Column(
            "article_id",
            sa.String(64),
            sa.ForeignKey("article.article_id"),
            index=True
        ),
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
    op.drop_table("article_comment")
