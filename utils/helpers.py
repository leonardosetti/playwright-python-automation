"""Helper utilities for tests."""
import json
from typing import Any, Dict
from playwright.sync_api import Page, APIResponse

def take_screenshot(page: Page, name: str) -> None:
    """Take a screenshot with timestamp."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"test-results/screenshots/{name}_{timestamp}.png"
    page.screenshot(path=path, full_page=True)

def save_trace(page: Page, name: str) -> None:
    """Save Playwright trace."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"test-results/traces/{name}_{timestamp}.zip"
    page.context.tracing.stop(path=path)

def log_response(response: APIResponse) -> None:
    """Log API response for debugging."""
    print(f"[{response.status}] {response.url}")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception:
        print(response.text()[:500])

def wait_for_network_idle(page: Page, timeout: int = 5000) -> None:
    """Wait for network to be idle."""
    page.wait_for_load_state("networkidle", timeout=timeout)