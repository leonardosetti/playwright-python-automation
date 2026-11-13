# Docker for Playwright Python tests
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create test results directories
RUN mkdir -p test-results/screenshots test-results/videos test-results/traces

# Default command
CMD ["pytest", "tests/", "-v", "--html=test-results/report.html", "--self-contained-html"]