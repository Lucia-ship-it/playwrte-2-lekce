from playwright.sync_api import Page


def test_dynamic(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.click("text=Start")
    assert page.locator("#finish").is_visible() == True
