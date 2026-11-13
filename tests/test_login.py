"""UI Tests - Login flow examples."""
import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(page, base_url):
    """Test successful login with valid credentials."""
    login_page = LoginPage(page)
    # Using a demo site - replace with actual credentials
    login_page.navigate("/login")
    
    # Example: fill form (adjust selectors for target site)
    page.fill('input[name="username"]', "demo_user")
    page.fill('input[name="password"]', "demo_pass")
    page.click('button[type="submit"]')
    
    # Wait for navigation
    page.wait_for_load_state("networkidle")
    
    # Assert logged in (adjust for target site)
    assert page.url != f"{base_url}/login"

@pytest.mark.ui
def test_invalid_login(page):
    """Test login with invalid credentials shows error."""
    login_page = LoginPage(page)
    login_page.navigate("/login")
    
    page.fill('input[name="username"]', "invalid")
    page.fill('input[name="password"]', "invalid")
    page.click('button[type="submit"]')
    
    # Should show error
    error = page.locator('.error, .alert-danger, [role="alert"]').first
    assert error.is_visible()

@pytest.mark.ui
@pytest.mark.regression
def test_login_page_elements(page):
    """Test login page has all required elements."""
    page.goto("/login")
    
    # Check form elements exist
    assert page.locator('input[name="username"]').is_visible()
    assert page.locator('input[name="password"]').is_visible()
    assert page.locator('button[type="submit"]').is_visible()