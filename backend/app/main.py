"""FastAPI application entry point (the "api" process)."""

from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(title="Music ID API", version="0.1.0")
app.include_router(health_router, prefix="/api")
