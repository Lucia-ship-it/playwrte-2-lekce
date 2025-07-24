from playwright.sync_api import Page

#ak je playwright rychly az moc.

def test_dynamic(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.click("text=Start")
    # page.wait_for_timeout(5000) - ale mozno zbytocne dlho cakame
    #assert page.locator("#finish").is_visible() == True
    assert page.wait_for_selector("#finish",timeout=10000).is_visible() == True #ze maximalne 10 s
