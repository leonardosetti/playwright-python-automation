"""API Tests using Playwright request context."""
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_health_endpoint(api_context):
    """Test health check endpoint."""
    response = api_context.get("/health")
    assert response.ok
    data = response.json()
    assert data.get("status") == "healthy"

@pytest.mark.api
def test_api_get_users(api_context):
    """Test GET users endpoint."""
    response = api_context.get("/api/users")
    assert response.ok
    users = response.json()
    assert isinstance(users, list)

@pytest.mark.api
def test_api_create_user(api_context):
    """Test POST create user."""
    new_user = {"name": "Test User", "email": "test@example.com"}
    response = api_context.post("/api/users", data=new_user)
    assert response.status in (200, 201)
    user = response.json()
    assert user.get("name") == new_user["name"]
    assert "id" in user

@pytest.mark.api
def test_api_invalid_endpoint(api_context):
    """Test 404 for invalid endpoint."""
    response = api_context.get("/api/nonexistent")
    assert response.status == 404