from playwright.sync_api import Page

#vdaka evaluate mozeme zavolat hociaky java skript
#playwrite ma veela knihoven, vela je napsano, staci uz len vyuzit

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
