"""Update Transaction model

Revision ID: 135c0e406662
Revises: 561433eafa4b
Create Date: 2025-01-01 14:30:24.667706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '135c0e406662'
down_revision: Union[str, None] = '561433eafa4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Ajout des nouvelles colonnes
    op.add_column('transactions', sa.Column('currency', sa.String(length=255), nullable=False))
    op.add_column('transactions', sa.Column('type', sa.String(length=255), nullable=False))
    
    # Rendre `seller_id` optionnel
    op.alter_column('transactions', 'seller_id', nullable=True)

    # Rendre `price_at_transaction` et `total_price` optionnels
    op.alter_column('transactions', 'price_at_transaction', nullable=True)
    op.alter_column('transactions', 'total_price', nullable=True)

    # Mettre une valeur par défaut pour `status`
    op.alter_column('transactions', 'status', server_default='pending', nullable=True)

    # Vous pouvez ajouter ici des transformations de données si nécessaire, comme des mises à jour de valeurs existantes


def downgrade() -> None:
    # Suppression des colonnes ajoutées
    op.drop_column('transactions', 'currency')
    op.drop_column('transactions', 'type')
    
    # Réversion des colonnes modifiées
    op.alter_column('transactions', 'seller_id', nullable=False)
    op.alter_column('transactions', 'price_at_transaction', nullable=False)
    op.alter_column('transactions', 'total_price', nullable=False)

    # Supprimer la valeur par défaut pour `status`
    op.alter_column('transactions', 'status', server_default=None, nullable=True)
