"""Add slack to participant

Revision ID: b3338f2ae582
Revises: e77f6676bf8a
Create Date: 2020-04-05 17:19:46.056559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b3338f2ae582"
down_revision = "e77f6676bf8a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "participant", sa.Column("slack", sa.String(length=21), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("participant", "slack")
    # ### end Alembic commands ###
