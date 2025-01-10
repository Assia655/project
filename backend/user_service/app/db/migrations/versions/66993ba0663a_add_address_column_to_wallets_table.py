"""Add address column to wallets table

Revision ID: 66993ba0663a
Revises: 3f0715feaee0
Create Date: 2025-01-07 15:45:44.334995

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '66993ba0663a'
down_revision: Union[str, None] = '3f0715feaee0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Ajouter la colonne 'address'
    op.add_column('wallets', sa.Column('address', sa.String(), nullable=True))

    # Modifier la colonne 'currency' pour utiliser le nouveau type 'walletcurrency'
    op.alter_column('wallets', 'currency',
                    existing_type=postgresql.ENUM('USD', 'ETH', 'CARBON', name='wallettype'),
                    type_=sa.Enum('USD', 'ETH', 'CARBON', name='walletcurrency'),
                    existing_nullable=False,
                    postgresql_using='currency::text::walletcurrency') 

def downgrade() -> None:
    # Revenir à l'ancien type 'wallettype' pour la colonne 'currency'
    op.alter_column('wallets', 'currency',
                    existing_type=sa.Enum('USD', 'ETH', 'CARBON', name='walletcurrency'),
                    type_=postgresql.ENUM('USD', 'ETH', 'CARBON', name='wallettype'),
                    existing_nullable=False,
                    postgresql_using='currency::text::wallettype') 

    # Supprimer la colonne 'address'
    op.drop_column('wallets', 'address')

