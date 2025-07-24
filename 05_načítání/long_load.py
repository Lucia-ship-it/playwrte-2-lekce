from playwright.sync_api import Page


def test_rejstrik(page: Page):
    page.goto("https://www.rzp.cz/verejne-udaje/en/udaje/vyber-subjektu")

    page.locator("#nazev").fill("Anna")
    page.locator("input[type='checkbox'][name='zacinajici']").check()

    page.locator("button[type='submit'].primary").nth(1).click()
    page.wait_for_load_state("networkidle") #cakame pokial sa ta stranka neacita, este  obrazky alebo fonty, css styly atd. networkidle znamena ze ma uz vsetko nachystane

    assert page.locator("#list .plain.cards").is_visible()
