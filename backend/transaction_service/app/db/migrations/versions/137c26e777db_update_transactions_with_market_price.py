"""Update transactions with market price

Revision ID: 137c26e777db
Revises: 
Create Date: 2024-12-28 21:41:23.377097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '137c26e777db'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('price_at_transaction', sa.Float(), nullable=False))
    op.add_column('transactions', sa.Column('total_price', sa.Float(), nullable=False))
    op.alter_column('transactions', 'seller_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('transactions', 'buyer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('transactions', 'credit_amount',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('transactions', 'status',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.drop_column('transactions', 'market_price_at_time')
    op.drop_column('transactions', 'type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('type', sa.VARCHAR(length=8), autoincrement=False, nullable=False))
    op.add_column('transactions', sa.Column('market_price_at_time', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.alter_column('transactions', 'status',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('transactions', 'credit_amount',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('transactions', 'buyer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('transactions', 'seller_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('transactions', 'total_price')
    op.drop_column('transactions', 'price_at_transaction')
    # ### end Alembic commands ###