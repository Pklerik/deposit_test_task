from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from src.deposit import service
from src.deposit.schemas import Deposit

router = APIRouter()

@router.post("/deposit")
async def deposit_calculation(deposit_data:Deposit) -> dict:
    return JSONResponse(status_code=status.HTTP_200_OK, content=service.calculate_deposit(deposit_data))
