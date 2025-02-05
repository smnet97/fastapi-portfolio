"""postcategory

Revision ID: 5b805317c167
Revises: f591ea526a70
Create Date: 2023-08-27 15:15:11.747814

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5b805317c167'
down_revision = 'f591ea526a70'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('name', sa.String(length=150), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column('posts', sa.Column('category_id', sa.UUID(), nullable=False))
    op.create_foreign_key(None, 'posts', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'category_id')
    op.drop_table('categories')
    # ### end Alembic commands ###
