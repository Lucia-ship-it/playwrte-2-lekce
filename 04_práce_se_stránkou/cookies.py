from playwright.sync_api import sync_playwright


def test_w3schools_cookie_setting():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Otevři cílovou stránku
        page.goto("https://www.w3schools.com/js/js_cookies.asp")

        # odklikni cookies:
        page.click("#accept-choices")

        # Klikni na tlačítko "Set Cookie"
        page.click("button:has-text('Create Cookie 1')")

        # Získání cookies
        cookies = page.context.cookies()

        # Vyhledání požadované cookie
        target_cookie = next(
            (cookie for cookie in cookies if cookie["name"] == "firstname"), None
        )

        # Ověření
        assert target_cookie is not None, "Cookie 'firstname' nebyla nastavena."
        assert (
            target_cookie["value"] == "John"
        ), f"Očekávána hodnota 'John', ale byla: {target_cookie['value']}"

        print("✅ Test cookies na W3Schools proběhl úspěšně.")

        browser.close()
