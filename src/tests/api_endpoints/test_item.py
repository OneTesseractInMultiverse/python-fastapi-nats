from fastapi.testclient import TestClient
from app.main import app


# -----------------------------------------------------------------------------
# GET APPLICATION TEST CLIENT
# -----------------------------------------------------------------------------
def get_application_test_client() -> TestClient:
    return TestClient(app=app)


# -----------------------------------------------------------------------------
# TEST WHEN VALID ITEM ID IS PROVIDED STATUS CODE IS 200
# -----------------------------------------------------------------------------
def test_when_valid_item_id_is_provided_status_code_is_200():

    # Prepare
    client = get_application_test_client()
    expected = 200

    # Act
    actual = client.get('/api/v1/item/1')

    # Assert
    assert actual.status_code == expected


# -----------------------------------------------------------------------------
# TEST WHEN VALID ITEM ID IS PROVIDED STATUS CODE IS 200
# -----------------------------------------------------------------------------
def test_when_invalid_item_id_is_provided_status_code_is_404():
    # Prepare
    client = get_application_test_client()
    expected = 404

    # Act
    actual = client.get('/api/v1/item/2')

    # Assert
    assert actual.status_code == expected


# -----------------------------------------------------------------------------
# TEST WHEN VALID ITEM ID IS PROVIDED STATUS CODE IS 200
# -----------------------------------------------------------------------------
def test_when_valid_item_id_is_provided_valid_response_is_produced():
    # Prepare
    client = get_application_test_client()
    expected = {
        "id": "1",
        "title": "test item"
    }

    # Act
    actual = client.get('/api/v1/item/1')

    # Assert
    assert actual.json() == expected


# -----------------------------------------------------------------------------
# TEST WHEN VALID ITEM ID IS PROVIDED STATUS CODE IS 200
# -----------------------------------------------------------------------------
def test_when_valid_item_id_is_provided_consistent_id_is_produced_in_the_response():
    # Prepare
    client = get_application_test_client()
    expected = '1'

    # Act
    actual = client.get('/api/v1/item/1')

    # Assert
    assert actual.json()['id'] == expected
