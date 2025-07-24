Stránky vhodné pro testování:

- www.uitestingplayground.com
- the-internet.herokuapp.com
- https://ecommerce-playground.lambdatest.io/
- https://demoqa.com/

Dokumentace playwrightu:

- https://playwright.dev/python/docs/api/class-locator

# Úkol č. 1

Na stránce http://the-internet.herokuapp.com/hovers najdete Nápis "Powered by Elemental Selenium". Klikně na odkaz Elemental Selenium a zkontrolujte, jestli jste byly přesměrováni na stránku https://elementalselenium.com/.

```python
from playwright.sync_api import Page
```

# Úkol č. 2

Na stránce http://the-internet.herokuapp.com/hovers vyzkoušejte najet myší na 2. obrázek a vyzkoušejte, jestli se objeví nápis "name: user2".

# Úkol č. 3
Na stránce http://the-internet.herokuapp.com/login vyzkoušejte nevalidní login (tedy, že zadáte špatné přihlašovací jmné, nebo heslo) a otestujte, že jste zůstali na stránce `http://the-internet.herokuapp.com/login`.