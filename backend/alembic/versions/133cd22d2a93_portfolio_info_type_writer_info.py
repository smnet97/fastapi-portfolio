"""portfolio_info_type_writer_info

Revision ID: 133cd22d2a93
Revises: 3d84abb65ddb
Create Date: 2023-08-01 00:46:28.414134

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '133cd22d2a93'
down_revision = '3d84abb65ddb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio_info',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('owner_name', sa.String(length=40), nullable=False),
    sa.Column('socials', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_writer_info',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('info', sa.String(length=150), nullable=False),
    sa.Column('portfolio_info_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_info_id'], ['portfolio_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('type_writer_info')
    op.drop_table('portfolio_info')
    # ### end Alembic commands ###
