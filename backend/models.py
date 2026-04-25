from pydantic import BaseModel, Field
from pydantic import constr
from typing import Literal

class ScoreRequest(BaseModel):
    land_area_acres: float = Field(..., gt=0)
    crop_type: constr(min_length=1)
    repayment_history_score: float = Field(..., ge=0, le=100)
    annual_income_band: Literal["<2L", "2-5L", "5-10L", ">10L"]

class ScoreResponse(BaseModel):
    request_id: str
    score: float
    reason_codes: list[str]
    timestamp: str