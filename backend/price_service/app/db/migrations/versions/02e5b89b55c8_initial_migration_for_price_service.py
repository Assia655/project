"""Initial migration for price_service

Revision ID: 02e5b89b55c8
Revises: 
Create Date: 2024-12-27 21:09:42.748032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02e5b89b55c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('market_prices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_market_prices_id'), 'market_prices', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_market_prices_id'), table_name='market_prices')
    op.drop_table('market_prices')
    # ### end Alembic commands ###
