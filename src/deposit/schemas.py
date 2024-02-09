from datetime import datetime
from typing import Dict
from pydantic import BaseModel, Field, validator



class Deposit(BaseModel):
    date:str #TODO написать валидацию для даты?
    periods:int = Field(..., ge=1, le=60)
    amount:int = Field(..., ge=10_000, le=3_000_000)
    rate:float = Field(..., ge=1.00, le=8.00)

    @validator('date')
    def validate_str_date(cls, date_input):
        return datetime.strptime(date_input, '%d.%m.%Y').date()  # convert string to date