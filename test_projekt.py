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
    page.screenshot(path=f"screenshot_{timestamp}.png")
    button.click()

    cookies_square = page.locator("#cookiescript_injected")
    page.wait_for_timeout(2000)
    page.screenshot(path=f"screenshot_{timestamp}.png")

    assert cookies_square.is_visible() == False

def test_new_page(page: Page):
    page.goto("https://www.lekarnalemon.cz/?srsltid=AfmBOooEQ8c3jgvq-BJtH48oN3GY7-c4_KsYt6MVQ4JPhedXCQ4LGWCp")
    # na stranke najdi v menu leto a klikni nan
    button = page.locator("#desktop-a8ab5f3c-86fa-414f-999e-4601782baaec-dropdown")
    button.click()

# rozbali sa mi ponuka, screenshot  
    page.screenshot(path=f"screenshot_{timestamp}.png")
    page.locator("body > header > div.page-header__navigation > div > nav > div.menu-item.menu-item-dropdown.show > div > div").wait_for(state="visible")

# chcem kliknut na text s doplnkami stravy:
    h_text = page.locator("text=Doplňky stravy na opalování")
    # # <a href="/leto/doplnky-stravy-na-opalovani" class="dropdown-menu__content-list--item--title">Doplňky stravy na opalování</a>
    new_page = h_text.click()

    assert new_page == page.goto"https://www.lekarnalemon.cz/leto/doplnky-stravy-na-opalovani"

def test_chart(page: Page):
    page.goto("https://www.lekarnalemon.cz/leto/doplnky-stravy-na-opalovani")
    # otvor si produkt s nazvom:
    select = page.locator("h3.box__product-title:has-text('Gs Betakaroten gold 15 mg 30 kapslí')")
    new_page = select.click()


    assert new_page ==  "https://www.lekarnalemon.cz/leto/doplnky-stravy-na-opalovani/gs-betakaroten-gold-15mg-cps-30-8595693300541"

    #najdem tlacitko koupit, kliknem
    button = new_page.locator("button.btn.btn-md.js-add-to-cart:has-text('Koupit')")
    button.click()

    #najedem na ikonku kosik a necham si zobrazit text, cliknem 
    chart_icon = new_page.locator('body > header > div.container > div > div.page-header__top-nav > a:nth-child(3) > span.page-header__top-link--icon > svg')
    chart_page = chart_icon.click()

    #na novej stranke overim, ze sa mi tam produkt s nazvom....nachadza - nebude tam, lebo sme v anonimnom okne


    LEPSIE BUDE PRIHLASENIE
    najedem na prihlasenie, click, do emailu vyplnim neexist email, do hesla nieco a entrom odoslem. kontrola ze sa zobrazi chybova hlaska.