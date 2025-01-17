from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={"username": "user4", "email": "user4@example.com", "password": "password123", "tenant_id": 3})
    assert response.status_code == 200
    assert response.json()["email"] == "user4@example.com"
    
    
def test_login():
    reposonse = client.post("/users/login", json={"email":"user4@example.com", "password": "password123"})
    assert reposonse.status_code == 200
    