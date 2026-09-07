from app.db.connection import pool


CREATE_URLS_TABLE = """
CREATE TABLE IF NOT EXISTS urls (
    id BIGSERIAL PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_urls_short_code
ON urls(short_code);
"""


def initialize_database():
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_URLS_TABLE)
            connection.commit()