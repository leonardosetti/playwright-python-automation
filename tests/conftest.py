"""Playwright fixtures for pytest."""
import pytest
from playwright.sync_api import Browser, BrowserContext, Page
from utils.config import settings

@pytest.fixture(scope="session")
def browser_type(playwright):
    """Return browser type based on config."""
    return getattr(playwright, settings.browser)

@pytest.fixture(scope="session")
def browser(browser_type):
    """Launch browser once per session."""
    browser = browser_type.launch(headless=settings.headless, slow_mo=settings.slowmo)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser):
    """Create new context for each test."""
    context = browser.new_context(
        base_url=settings.base_url,
        viewport={"width": 1280, "height": 720},
        record_video_dir="test-results/videos/" if not settings.headless else None,
    )
    # Enable tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop()
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create new page for each test."""
    page = context.new_page()
    page.set_default_timeout(settings.timeout)
    yield page
    page.close()

@pytest.fixture(scope="function")
def api_context(playwright):
    """API request context for API testing."""
    request_context = playwright.request.new_context(base_url=settings.base_url)
    yield request_context
    request_context.dispose()