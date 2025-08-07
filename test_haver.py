import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # context = browser.new_context()
        # page = context.new_page()
        page = browser.new_page()
        yield page

def test_hover(page : Page):
    page.goto("http://the-internet.herokuapp.com/hovers")

    # najet mysi na obrazok
    # napsat lokator pre obrazok
    div = page.locator("div.figure").nth(2)
    #najet mysi
    div.hover()
    #kontrola ze bude videt text, najdem si ho
    h5 = div.locator("h5")
    #assert ci je vidiet
    assert h5.is_visible()

    # python -m pytest test_haver.py
    # spustenie funguje, test prejde

    # ked je lokatorov viac, urobi nam z toho zoznam a mi zadame, ktoru z toho zoznamu ma spracovat
def test_hover_2(page : Page):
    page.goto("http://the-internet.herokuapp.com/hovers")

    # najet mysi na obrazok
    # napsat lokator pre obrazok
    div = page.locator("div.figure").nth(0)
    #najet mysi
    div.hover()
    #kontrola ze bude videt text, najdem si ho
    h5 = page.locator("div.figure:nth-child(3) > div:nth-child(2) > h5:nth-child(1)")
    #assert ci je vidiet
    assert h5.is_visible()


#nepotrebujem aby program hladal na celej stranke. ale len v ramci konkretneho divu
def test_hover_3(page : Page):
    page.goto("http://the-internet.herokuapp.com/hovers")

    # najet mysi na obrazok
    # napsat lokator pre obrazok
    div = page.locator("div.figure").nth(0)
    #najet mysi
    div.hover()
    #kontrola ze bude videt text, najdem si ho
    h5 = div.locator("h5")
    #assert ci je vidiet
    assert h5.is_visible()

#PREPISTE TO TAK, ABY SME KONTROLOVALI POSLEDNY OBRAZOK
def test_hover_4(page : Page):
    page.goto("http://the-internet.herokuapp.com/hovers")

    # najet mysi na obrazok
    # napsat lokator pre obrazok
    div = page.locator("div.figure").nth(2)
    #najet mysi
    div.hover()
    #kontrola ze bude videt text, najdem si ho
    h5 = div.locator("h5")
    #assert ci je vidiet
    assert h5.is_visible()

# SPUSTIT KONKRETNY TEST: pytest test_haver.py::test_hover_4