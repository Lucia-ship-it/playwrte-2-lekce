from playwright.sync_api import Page

def test_3s(page: Page):
    page.goto("http://www.uitestingplayground.com/autowait")
    page.locator("#applyButton3").click()

    assert page.locator("#target").is_visible()
