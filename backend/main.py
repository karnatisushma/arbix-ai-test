from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (mandatory)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    income: float
    land_size: float

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: InputData):
    score = data.income * 0.6 + data.land_size * 0.4
    
    return {
        "score": score,
        "explanation": {
            "income_contribution": data.income * 0.6,
            "land_contribution": data.land_size * 0.4
        }
    }