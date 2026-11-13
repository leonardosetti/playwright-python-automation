# Playwright Python Automation Framework

Proof of work repository demonstrating test automation capabilities with Playwright and Python.

## Stack
- **Playwright** (Python) - Browser automation
- **pytest** - Test runner
- **pytest-playwright** - Playwright integration for pytest
- **Docker** - Containerized execution
- **GitHub Actions** - CI/CD pipeline

## Project Structure
```
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Playwright fixtures
│   ├── test_login.py        # Example: login flow
│   ├── test_api.py          # Example: API testing
│   └── test_ui.py           # Example: UI interactions
├── pages/
│   ├── __init__.py
│   ├── base_page.py         # Page Object Model base
│   └── login_page.py        # Login page object
├── utils/
│   ├── __init__.py
│   ├── config.py            # Configuration management
│   └── helpers.py           # Helper functions
├── docker/
│   ├── Dockerfile           # Test execution container
│   └── docker-compose.yml   # Local development stack
├── .github/
│   └── workflows/
│       └── test.yml         # CI pipeline
├── requirements.txt         # Python dependencies
├── pytest.ini              # pytest configuration
└── playwright.config.py    # Playwright configuration
```

## Quick Start

### Local (with Docker)
```bash
cd docker
docker-compose up --build
```

### Local (without Docker)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
pytest tests/ -v
```

### Run specific test
```bash
pytest tests/test_login.py::test_valid_login -v --headed
```

## CI/CD
GitHub Actions workflow (`.github/workflows/test.yml`) runs on:
- Push to main
- Pull requests
- Schedule (daily)

Generates:
- HTML report (playwright-report)
- JUnit XML (for CI integration)
- Screenshots/videos on failure

## Configuration
Environment variables (`.env`):
```
BASE_URL=https://example.com
HEADLESS=true
BROWSER=chromium
```

## Proof of Competencies Demonstrated
- ✅ Playwright Python API (locators, assertions, auto-waiting)
- ✅ Page Object Model (POM) pattern
- ✅ pytest fixtures for browser/context/page lifecycle
- ✅ API testing with Playwright request context
- ✅ Docker containerization
- ✅ CI/CD with GitHub Actions
- ✅ Cross-browser (chromium, firefox, webkit)
- ✅ Parallel execution
- ✅ Trace viewer, screenshots, videos on failure