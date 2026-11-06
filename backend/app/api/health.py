"""Health check endpoint, used by the front end and by Docker."""

from fastapi import APIRouter

from app import db

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    database = "ok" if db.database_is_reachable() else "unavailable"
    return {"status": "ok", "database": database}
