from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "TaskFlow API funcionando"}

def test_register_and_login():
    register_response = client.post("/register", json={
        "username": "testeuser",
        "email": "testeuser@email.com",
        "password": "123456"
    })

    assert register_response.status_code in [200, 400]

    login_response = client.post("/login", json={
        "username": "testeuser",
        "password": "123456"
    })

    assert login_response.status_code == 200
    assert "access_token" in login_response.json()