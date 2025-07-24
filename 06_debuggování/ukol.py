def test_remove_check(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # najdeme tlačítko "Remove"
    remove_button = page.locator("button")
    remove_button.click()

    # Zkontrolujeme, že checkbox zmizel
    check_box = page.locator("#checkbox")
    assert check_box.is_visible() == False

#zistime ci mame napisany test zle, alebo ta stranka je zle.
# urobime si screenshot page.screenshot(path="cs-png")
# a uvidime co tam je. ci tam nen captcha alebo robot
# do terminalu: PWDEBUG=1 python -m pytest 06_debuggování/ukol.py
