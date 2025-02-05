"""jwt_tokens_black_list

Revision ID: 3d84abb65ddb
Revises: 85551320403f
Create Date: 2023-07-28 19:31:59.863874

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3d84abb65ddb'
down_revision = '85551320403f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jwt_tokens_blacklist',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('jwt_token', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jwt_tokens_blacklist')
    # ### end Alembic commands ###
