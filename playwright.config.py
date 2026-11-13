import os
from playwright.sync_api import Playwright

def pytest_configure(config):
    config.option.playwright_browsers = ["chromium", "firefox", "webkit"]
    config.option.playwright_headless = os.getenv("HEADLESS", "true").lower() == "true"
    config.option.playwright_slowmo = int(os.getenv("SLOWMO", "0"))

# Custom markers
def pytest_configure(config):
    config.addinivalue_line("markers", "ui: UI tests")
    config.addinivalue_line("markers", "api: API tests")
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")