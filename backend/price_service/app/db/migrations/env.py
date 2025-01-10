import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Importez la base de données et les modèles spécifiques à price_service
from app.db.base import Base  # Base SQLAlchemy
from models.market_prices import MarketPrice  # Importez le modèle pertinent

# Chargement de la configuration Alembic
config = context.config

# Configurer le logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Définir les métadonnées cibles pour Alembic
target_metadata = Base.metadata

def run_migrations_offline():
    """Exécuter les migrations en mode hors ligne."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Exécuter les migrations en mode en ligne."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
