"""Create user follow table

Revision ID: a373039c17ea
Revises: 978a457dcd55
Create Date: 2023-06-10 18:22:35.873103

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a373039c17ea"
down_revision = "978a457dcd55"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_follow",
        sa.Column(
            "user_follow_id",
            sa.String(64),
            primary_key=True,
            comment="Unique identifier for each following record",
        ),
        sa.Column(
            "follower_id", sa.String(64), comment="ID of the user who is following"
        ),
        sa.Column(
            "following_id",
            sa.String(64),
            comment="ID of the user who is being followed",
        ),
        sa.Column("record_status", sa.String(10), server_default="normal"),
        sa.Column(
            "created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now()
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            server_onupdate=sa.func.now(),
        ),
        sa.UniqueConstraint(
            "follower_id",
            "following_id"
        ),
    )


def downgrade() -> None:
    op.drop_table("user_follow")
