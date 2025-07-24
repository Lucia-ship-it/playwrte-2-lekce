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


from playwright.sync_api import sync_playwright
import os


def test_download_file(page: Page):
    page.goto("http://the-internet.herokuapp.com/download")

    # Očekávání stahování souboru
    with page.expect_download() as download_info:
        page.click("a[href='download/bob.jpg']")  # Nahraď správným selektorem odkazu
    download = download_info.value

    # Uložení staženého souboru
    download_path = download.suggested_filename
    download.save_as(download_path)
    print(f"Soubor byl stažen jako: {download_path}")

    # Ověření, že soubor existuje
    assert os.path.exists(download_path)

    # Úklid
    os.remove(download_path)
