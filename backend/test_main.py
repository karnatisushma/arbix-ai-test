from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_happy_path():
    response = client.post("/score", json={
        "land_area_acres": 3,
        "crop_type": "Rice",
        "repayment_history_score": 80,
        "annual_income_band": "2-5L"
    })
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert len(data["reason_codes"]) == 3

def test_invalid_input():
    response = client.post("/score", json={
        "land_area_acres": -1,
        "crop_type": "",
        "repayment_history_score": 200,
        "annual_income_band": "wrong"
    })
    assert response.status_code != 200