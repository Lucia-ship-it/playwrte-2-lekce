from playwright.sync_api import Page

# 1. úkol
def test_href(page: Page):
    page.goto("http://the-internet.herokuapp.com/hovers")

    link = page.locator(".large-4  a")
    link.click()
    assert page.url == "https://elementalselenium.com/"

# 2. úkol
def test_hovers(page: Page):
    page.goto("http://the-internet.herokuapp.com/hovers")

    # vybereme první div se třídou .figure
    div = page.locator(".figure").nth(1)

    div.hover()

    # zkontrolujeme, jestli nadpis má správný text
    h5 = div.locator(".figcaption h5")
    assert h5.inner_html() == "name: user2"

# 3. úkol
def test_sign_in_negative(page: Page):
    page.goto("http://the-internet.herokuapp.com/login")
    page.locator("#username").fill("user")
    page.locator("#password").fill("pass")
    page.locator(".radius").click()

    assert page.url == "http://the-internet.herokuapp.com/login"