from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# Добавляем путь к проекту в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Импортируем Base из вашего приложения
from app.db.database import Base

# Это объект MetaData для autogenerate
target_metadata = Base.metadata

# Конфигурация логгирования
config = context.config
fileConfig(config.config_file_name)

def run_migrations_offline():
    """Запуск миграций в offline режиме."""
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
    """Запуск миграций в online режиме."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()