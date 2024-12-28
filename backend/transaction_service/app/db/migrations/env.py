from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Importer la base et le moteur depuis votre projet
from app.db.base import Base
from app.db.session import engine

# Ce fichier est généré par Alembic et utilise les variables de configuration de alembic.ini
config = context.config

# Configurer le logging à partir du fichier ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Ajouter ici vos modèles SQLAlchemy
# Exemple : from app.models import Transaction, Announcement
#           Vous pouvez importer autant de modèles que nécessaire
from app.models.transactions import Transaction
from app.models.announcements import Announcement

# Attribuer la base pour 'target_metadata'
target_metadata = Base.metadata

def run_migrations_offline():
    """
    Exécuter les migrations en mode "offline" (hors connexion).
    Cela configure l'environnement pour utiliser une chaîne de connexion.
    """
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
    """
    Exécuter les migrations en mode "online".
    Cela crée un moteur et associe une connexion au contexte.
    """
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
