from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)  

def test_Create_tenant():
    response = client.post(
        "/tenants/",
        json={
            "name": "Desterrrr",
            "email": "Desdertterrrrrder@yopmail.com",
            "plan": "Premium"
        }
    )
    data = response.json()
    print("+++++++++++++++++++++++++++>", data)
    assert response.status_code == 200
    assert response.json()["name"] == "Desterrrr"
