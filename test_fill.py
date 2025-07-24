import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)
        # context = browser.new_context()
        # page = context.new_page()
        page = browser.new_page()
        yield page

def test_login(page : Page):
    page.goto("http://the-internet.herokuapp.com/login")

    # najdem si v devtools selector pre okienka pre meno
    input_u = page.locator("#username")
    input_u.fill("tomsmith")

# najdem si v devtools selector pre okienka pre HESLO
    input_p = page.locator("#password")
    input_p.fill("SuperSecretPassword!")

#a teraz to odosleme enterom / musim to spustit na inpute ktory je sucast formulara
    input_p.press("Enter")

#kontrola url - ci sa zmeni http://the-internet.herokuapp.com/secure
    assert page.url == "http://the-internet.herokuapp.com/secure"

#spustenie python -m pytest test_fill.py

#trosku sikovnejsia forma
def test_login(page : Page):
    page.goto("http://the-internet.herokuapp.com/login")

    page.fill("#username","tomsmith")
    page.fill("#password","SuperSecretPassword!")

#a teraz to odosleme enterom / musim to spustit na inpute ktory je sucast formulara
    page.press("#password", "Enter")

#kontrola url - ci sa zmeni http://the-internet.herokuapp.com/secure
    assert page.url == "http://the-internet.herokuapp.com/secure"
