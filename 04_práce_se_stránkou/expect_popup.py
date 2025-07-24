from playwright.sync_api import sync_playwright, Page
import pytest


@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)  # Spusť prohlížeč
        yield browser


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.goto("https://www.google.com/")
    yield page


def test_title(page: Page):
    page.goto("https://engeto.cz/")

    with page.expect_popup() as popup:
        button = page.locator(".ci-facebook")
        button.click()

    new_page = popup.value
    assert new_page.url == "https://www.facebook.com/engetocom/"
