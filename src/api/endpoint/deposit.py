from fastapi import APIRouter
from src.deposit.schemas import Deposit
from src.deposit import service

router = APIRouter()

@router.post("/deposit")
async def deposit_calculation(deposit_data:Deposit) -> dict:
    return service.calculate_deposit(deposit_data)