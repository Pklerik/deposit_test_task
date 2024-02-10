from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from src.api import routers

deposit_app = FastAPI(
        title="Deposit calculation FastAPI",
        description="Author - PABUD4",
        version="0.1",)

if __name__ == "__main__":
    deposit_app.include_router(routers.api_router)

    @deposit_app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"error": exc.errors()}),
        )