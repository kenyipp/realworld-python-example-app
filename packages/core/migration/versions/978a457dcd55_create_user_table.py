"""Create user table

Revision ID: 978a457dcd55
Revises:
Create Date: 2023-06-10 18:19:54.888545

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "978a457dcd55"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("user_id", sa.String(64), primary_key=True),
        sa.Column("username", sa.String(64), unique=True, nullable=False),
        sa.Column("email", sa.String(250), unique=True, nullable=False),
        sa.Column("bio", sa.Text()),
        sa.Column("image", sa.Text()),
        sa.Column("password_salt", sa.String(64), nullable=False),
        sa.Column("password_hash", sa.String(64), nullable=False),
        sa.Column(
            "record_status",
            sa.Enum("normal", "banned", name="status_enum"),
            nullable=False,
            server_default="normal",
        ),
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
    op.drop_table("user")
