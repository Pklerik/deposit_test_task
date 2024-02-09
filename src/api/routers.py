from fastapi import APIRouter

from src.api.endpoint import deposit, home

api_router = APIRouter()
api_router.include_router(deposit.router, tags=["deposit"])
api_router.include_router(home.router, tags=["home"])

