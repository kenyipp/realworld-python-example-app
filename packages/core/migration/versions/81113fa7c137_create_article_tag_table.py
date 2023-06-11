"""Create article tag table

Revision ID: 81113fa7c137
Revises: 13eae820a4a4
Create Date: 2023-06-10 18:23:18.176937

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "81113fa7c137"
down_revision = "13eae820a4a4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "article_tag",
        sa.Column("article_id", sa.String(64)),
        sa.Column("tag", sa.String(150), index=True),
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
        sa.PrimaryKeyConstraint("article_id", "tag"),
    )


def downgrade() -> None:
    op.drop_table("article_tag")
