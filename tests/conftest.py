import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        is_ci = os.environ.get("CI") == "true"
        browser = p.chromium.launch(headless=is_ci)
        page = browser.new_page()
        page.goto("https://demo.guru99.com/V4")
        yield page
        browser.close()