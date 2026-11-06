"""Database access helpers."""

import psycopg

from app.config import DATABASE_URL


def database_is_reachable() -> bool:
    """Return True if a connection to PostgreSQL can be opened and queried."""
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=2) as conn:
            conn.execute("SELECT 1")
        return True
    except psycopg.Error:
        return False
