"""test_views.py"""
# test_views.py

def test_index_ok(client):
    """simple 200 response test"""
    response = client.get('/')
    assert response.status_code == 200
