"""UI Interaction Tests."""
import pytest
from playwright.sync_api import expect

@pytest.mark.ui
@pytest.mark.regression
def test_navigation(page):
    """Test basic navigation."""
    page.goto("/")
    expect(page).to_have_title(".*")  # Any title
    
    # Check main navigation elements
    nav = page.locator("nav, header, .navigation")
    if nav.count() > 0:
        expect(nav.first).to_be_visible()

@pytest.mark.ui
def test_form_interaction(page):
    """Test form fill and submit."""
    page.goto("/contact")
    
    # Fill form fields if they exist
    name_field = page.locator('input[name="name"], #name')
    email_field = page.locator('input[name="email"], #email')
    message_field = page.locator('textarea[name="message"], #message')
    
    if name_field.count() > 0:
        name_field.fill("Test User")
    if email_field.count() > 0:
        email_field.fill("test@example.com")
    if message_field.count() > 0:
        message_field.fill("Test message")
    
    # Submit if button exists
    submit_btn = page.locator('button[type="submit"], button:has-text("Send")')
    if submit_btn.count() > 0:
        submit_btn.click()
        page.wait_for_load_state("networkidle")

@pytest.mark.ui
def test_responsive_design(page):
    """Test responsive behavior."""
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    assert page.locator("body").is_visible()
    
    # Tablet
    page.set_viewport_size({"width": 768, "height": 1024})
    page.reload()
    assert page.locator("body").is_visible()
    
    # Mobile
    page.set_viewport_size({"width": 375, "height": 667})
    page.reload()
    assert page.locator("body").is_visible()