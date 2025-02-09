from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.db.base import Base
# from app.models.user import User  # Import explicite des modèles
# from app.models.wallet import Wallet  # Import explicite des modèles

# Configurer Alembic
config = context.config
config.set_main_option('sqlalchemy.url', 'postgresql://postgres:1234@localhost:5431/carbonmarket')

# Configurer les logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Ajouter les métadonnées des modèles
target_metadata = Base.metadata

def run_migrations_offline():
    """Mode hors ligne."""
    context.configure(
        url=config.get_main_option('sqlalchemy.url'),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Mode en ligne."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
