def test_remove_check(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # najdeme tlačítko "Remove"
    remove_button = page.locator("button")
    remove_button.click()

    # Zkontrolujeme, že checkbox zmizel
    check_box = page.locator("#checkbox")
    assert check_box.is_visible() == False
