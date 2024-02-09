from fastapi import FastAPI
from src.api import routers

deposit_app = FastAPI(
    title="Deposit calculation FastAPI",
    description="Author - PABUD4",
    version="0.1",)

deposit_app.include_router(routers.api_router)
