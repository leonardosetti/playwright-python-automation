"""Base page object with common functionality."""
from playwright.sync_api import Page, Locator
from utils.config import settings

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = settings.base_url
    
    def navigate(self, path: str = "") -> None:
        """Navigate to a page."""
        url = f"{self.base_url}{path}"
        self.page.goto(url, wait_until="networkidle")
    
    def wait_for_element(self, selector: str, timeout: int = 5000) -> Locator:
        """Wait for element to be visible."""
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        return locator
    
    def click(self, selector: str) -> None:
        """Click element."""
        self.page.locator(selector).click()
    
    def fill(self, selector: str, value: str) -> None:
        """Fill input field."""
        self.page.locator(selector).fill(value)
    
    def get_text(self, selector: str) -> str:
        """Get element text."""
        return self.page.locator(selector).inner_text()
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible."""
        return self.page.locator(selector).is_visible()
    
    def wait_for_url(self, url_pattern: str, timeout: int = 5000) -> None:
        """Wait for URL to match pattern."""
        self.page.wait_for_url(url_pattern, timeout=timeout)