import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from api.app import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "service" in response.json()

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()

def test_predict_endpoint(sample_application):
    response = client.post("/predict", json=sample_application)
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "risk_category" in data
    assert "approved" in data
