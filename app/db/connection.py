from psycopg_pool import ConnectionPool

from app.core.config import settings


pool = ConnectionPool(
    conninfo=settings.database_url,
    min_size=1,
    max_size=10,
    open=False,
)


def open_pool():
    pool.open()


def close_pool():
    pool.close()


def check_database_connection():
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()