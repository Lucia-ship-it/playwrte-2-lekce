# 1. úkol

Testu `test_hovers(page)` z předchozího úkolu přidej vlastní `page`, která se otevře ve chromiu a testy nebudou probíhat na pozadí (ale uvidíme je na obrazovce).

# několik prohlížečů
```python
def test_different_browsers():
    with sync_playwright() as p:
        browsers = ["chromium", "firefox"]
        for browser_type in browsers:
            browser = getattr(p, browser_type).launch(headless=False)  # Spusť prohlížeč
            page = browser.new_page()
            page.goto("https://www.google.com/")
            assert page.title() == "Google"
```

