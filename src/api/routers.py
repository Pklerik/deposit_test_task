from fastapi import APIRouter

from src.api.endpoint import deposit

api_router = APIRouter()
api_router.include_router(deposit.router, tags=["deposit"])

