# 1. úkol

Pro následující 2 testy:

```python
from playwright.sync_api import sync_playwright


def test_title():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)  # Spusť prohlížeč
        page = browser.new_page()
        page.goto("https://www.google.com/")
        assert page.title() == "Google"


def test_cookies():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)  # Spusť prohlížeč
        page = browser.new_page()
        page.goto("https://www.google.com/")
        page.locator("#W0wltc").click()

        cookies_bar = page.locator("#CXQnmb")
        assert cookies_bar.is_visible() == False
```

Vytvoř fixture browser() a fixture page(), které nahradí vždy první 3 rádky testu. Test bude jako parametr brát fixture page.
