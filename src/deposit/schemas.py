
from datetime import datetime, date as date_cl
from pydantic import BaseModel, Field, validator


class Deposit(BaseModel):
    date:str
    periods:int = Field(..., ge=1, le=60)
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