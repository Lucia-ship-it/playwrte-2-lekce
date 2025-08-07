from playwright.sync_api import Page
from datetime import datetime

#pytest test_projekt.py
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def test_title_lekarna(page: Page):
    page.goto("https://www.lekarnalemon.cz/?srsltid=AfmBOooEQ8c3jgvq-BJtH48oN3GY7-c4_KsYt6MVQ4JPhedXCQ4LGWCp")
    title = page.title()
    print("Page title is:", title)
    
    assert "Profesionální péče o Vaše zdraví a krásu" in title

# cookies
def test_cookies_click(page: Page):
    page.goto("https://www.lekarnalemon.cz/?srsltid=AfmBOooEQ8c3jgvq-BJtH48oN3GY7-c4_KsYt6MVQ4JPhedXCQ4LGWCp")
    button = page.locator("#cookiescript_accept") #page.locator("text=Léto").click()
    print("before click")
    page.screenshot(path="before_click.png")
    assert button.is_visible() == True

    button.click()

    print("after click")
    page.screenshot(path="after_click.png")
    page.wait_for_timeout(2000)
    # overim, ze sa mi nezobrazuje
    cookies_square = page.locator("#cookiescript_injected")
    
    assert cookies_square.is_visible() == False
