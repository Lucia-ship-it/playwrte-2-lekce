from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)  # Spusť prohlížeč
        yield browser


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.goto("https://www.google.com/")
    yield page


def test_title(page):
    assert page.title() == "Google"


def test_cookies(page):
    page.locator("#W0wltc").click()

    cookies_bar = page.locator("#CXQnmb")
    assert cookies_bar.is_visible() == False
