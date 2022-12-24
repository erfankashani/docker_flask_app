from app.main import app

def test_index_page():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"<h1>This Flask App is Running Healthy</h1>" in response.data