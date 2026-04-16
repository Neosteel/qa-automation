import pytest 
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto("https://demo.guru99.com/V4")
        yield page
        browser.close()