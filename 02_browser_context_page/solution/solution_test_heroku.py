from playwright.sync_api import sync_playwright
import pytest


def test_hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/hovers")

        users = page.locator(".figure").all()

        for user in users:
            user.hover()

            div = user.locator(".figcaption")
            assert div.is_visible()


@pytest.mark.parametrize("browser_type", ["chromium", "firefox"])
def test_different_browsers(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)  # Spusť prohlížeč
        page = browser.new_page()
        page.goto("https://www.google.com/")
        assert page.title() == "Google"
