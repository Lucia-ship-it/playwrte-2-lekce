import pytest
from playwright.sync_api import Page, sync_playwright
def test_click(page: Page):
    # přejít na stránku http://the-internet.herokuapp.com
    page.goto("http://the-internet.herokuapp.com")
    # kliknout na tlačítko "Hovers"
    # #content > ul:nth-child(4) > li:nth-child(25) > a:nth-child(1)
    # a[href='/hovers']

    link = page.locator("a[href='/hovers']")
    link.click()
    # zkontrolovat, že nové url je http://the-internet.herokuapp.com/hovers
    assert page.url == "http://the-internet.herokuapp.com/hovers"

def test_click_2():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=5000)
        # context = browser.new_context()
        # page = context.new_page()
        page = browser.new_page()

        page.goto("http://the-internet.herokuapp.com")
        link = page.locator("a[href='/hovers']")
        link.click()
        assert page.url == "http://the-internet.herokuapp.com/hovers"


def test_click_3():
    # přepiště tak, abyste využili vlastní page - webkit, headless = False, slow_mo
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=4000)
        page = browser.new_page()
    
        page.goto("http://the-internet.herokuapp.com")

        link = page.locator("a[href='/inputs']")
        link.click()
        assert page.url == "http://the-internet.herokuapp.com/inputs"


from playwright.sync_api import Page, sync_playwright
def test_click():
    # přepiště tak, abyste využili vlastní page - webkit, headless = False, slow_mo
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
    
        page.goto("http://the-internet.herokuapp.com")

        link = page.locator("a[href='/inputs']")
        link.click()
        assert page.url == "http://the-internet.herokuapp.com/inputs"

from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)
        # context = browser.new_context()
        # page = context.new_page()
        page = browser.new_page()
        yield page

def test_click(page: Page):
    page.goto("http://the-internet.herokuapp.com")
    link = page.locator("a[href='/hovers']")
    link.click()
    assert page.url == "http://the-internet.herokuapp.com/hovers"

def test_click_2(page: Page):
    page.goto("http://the-internet.herokuapp.com")
    link = page.locator("a[href='/inputs']")
    link.click()
    assert page.url == "http://the-internet.herokuapp.com/inputs"

