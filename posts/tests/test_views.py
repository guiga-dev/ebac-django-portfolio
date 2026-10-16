def test_home_returns_hello_world(client):
    response = client.get("/home")
    assert response.status_code == 200
    assert response.content == b"Hello World"

def test_unknown_route_is_404(client):
    assert client.get("/rota-inexistente/").status_code == 404
