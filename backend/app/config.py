"""Configuration read from environment variables."""

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://musicid:musicid@localhost:5432/musicid")
