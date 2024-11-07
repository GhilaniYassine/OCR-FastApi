# the goal of it is to test the api endpoints
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_home():
    response = client.get("/") # python request
    assert response.status_code == 200
    assert "text/html" in  response.headers['content-type']
def test_post_home():
    response = client.post("/") # python request
    assert response.status_code == 200
    assert "application/json" in  response.headers['content-type']
    assert response.json() == {"hello": "world"}
