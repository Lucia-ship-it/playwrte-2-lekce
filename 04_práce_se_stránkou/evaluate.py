from playwright.sync_api import Page


def test_cookies_local_storace(page: Page):
    page.goto(
        "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_localstorage"
    )
    localStorageValue = page.evaluate(
        """() => {
    return localStorage.getItem('lastname');
    }
    """
    )
    assert localStorageValue == "Smith"
