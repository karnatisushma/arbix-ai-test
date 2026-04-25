from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from datetime import datetime

from models import ScoreRequest, ScoreResponse
from scoring import calculate_score
from logger import logger

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Arbix API Running"}

@app.post("/score", response_model=ScoreResponse)
def score(data: ScoreRequest):
    request_id = str(uuid4())
    timestamp = datetime.utcnow().isoformat()

    score_value, reasons = calculate_score(data)

    logger.info({
        "request_id": request_id,
        "input": data.dict(),
        "score": score_value,
        "reasons": reasons,
        "timestamp": timestamp
    })

    return {
        "request_id": request_id,
        "score": score_value,
        "reason_codes": reasons,
        "timestamp": timestamp
    }