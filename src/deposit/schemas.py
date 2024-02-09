from fastapi import HTTPException, status
from datetime import datetime, date as date_cl
from pydantic import BaseModel, Field, validator


class Deposit(BaseModel):
    date:str
    periods:int
    amount:int = Field(..., ge=10_000, le=3_000_000)
    rate:float = Field(..., ge=1.00, le=8.00)

    @validator('date')
    @classmethod
    def validate_str_date(cls, date_input:date_cl) -> date_cl: #
        """_summary_

        Args:
            date_input (date): date of request

        Returns:
            date: date of request after validation on format <%d.%m.%Y>
        """
        return datetime.strptime(date_input, '%d.%m.%Y').date()  # convert string to date
    

    #TODO rewrite exception handler to remove detail key from error response
    @validator('periods')
    @classmethod
    def validate_periods(cls, periods:int) -> int:
        if 1 <= periods <= 60:
            return periods
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":"'periods' mast be between 1 and 60"})
        
    @validator('amount')
    @classmethod
    def validate_amount(cls, amount:int) -> int:
        if 10_000 <= amount <= 3_000_000:
            return amount
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":"'amount' mast be between 10 000 and 3 000 000"})
        
    @validator('rate')
    @classmethod
    def validate_rate(cls, rate:float) -> float:
        if 1 <= rate <= 8:
            return rate
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":"'rate' mast be between 1 and 8"})