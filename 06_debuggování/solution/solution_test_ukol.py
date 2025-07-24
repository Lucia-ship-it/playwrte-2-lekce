def test_remove_check(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # najdeme tlačítko "Remove" - chyba v lokátoru pro tlačítko
    remove_button = page.locator("#checkbox-example > button")
    remove_button.click()

    # přidáme chvíli čekání, než se akce provede
    page.wait_for_timeout(5000)

    # Zkontrolujeme, že checkbox zmizel
    check_box = page.locator("#checkbox")
    assert check_box.is_visible() == False
