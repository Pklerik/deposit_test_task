from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
from src.deposit.schemas import Deposit
from src.deposit import service

router = APIRouter()

@router.post("/deposit")
async def deposit_calculation(deposit_data:Deposit) -> dict:
    return JSONResponse(status_code=status.HTTP_200_OK, content=service.calculate_deposit(deposit_data))



# @router.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=404)