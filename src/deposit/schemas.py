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
        """validator for 'date' field

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
        """validator for 'periods' field

        Args:
            periods (int): amount of months for deposit

        Raises:
            HTTPException: raises then periods < 1 or periods > 60

        Returns:
            int: amount of periods
        """
        if 1 <= periods <= 60:
            return periods
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":"'periods' must be between 1 and 60"})
        
    @validator('amount')
    @classmethod
    def validate_amount(cls, amount:int) -> int:
        """validator for 'amount' field

        Args:
            amount (int): amount of money for deposit

        Raises:
            HTTPException: raises then amount < 10_000 or amount > 3_000_000

        Returns:
            int: amount of money for deposit
        """
        if 10_000 <= amount <= 3_000_000:
            return amount
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":"'amount' must be between 10 000 and 3 000 000"})
        
    @validator('rate')
    @classmethod
    def validate_rate(cls, rate:float) -> float:
        """validator for 'rate' field

        Args:
            rate (float): deposit rate for current deposit

        Raises:
            HTTPException: raises then rate < 1.00 or rate > 8.00

        Returns:
            float:deposit rate for current deposit
        """
        if 1 <= rate <= 8:
            return rate
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error":"'rate' must be between 1 and 8"})