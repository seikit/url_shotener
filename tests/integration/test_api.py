from fastapi.testclient import TestClient


def test_shorten(client: TestClient, data: dict) -> None:
    response = client.post("/shorten", params={"long_url": data["long"]})
    assert response.status_code == 200


def test_short_url(client: TestClient, data: dict) -> None:
    response = client.post("/shorten", params={"long_url": data["long"]})
    assert response.status_code == 200
    resp_data: dict = response.json()

    response = client.get("/short-url", params={"short_url": resp_data["short_url"]})
    assert response.status_code == 200
    resp_data: dict = response.json()

    assert resp_data["long_url"] == data["long"]
