from fastapi import APIRouter
from src.deposit.schemas import Deposit
from src.deposit import service

router = APIRouter()

@router.get("/")
async def home():
    return "message"