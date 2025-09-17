import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False abre o navegador
    page = browser.new_page()
    page.goto("http://www.automationpractice.pl/index.php")
    print(page.title())
    page.click(".login")
    page.wait_for_url(url="http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
    page.fill("#email", "teste@email.com")
    page.fill("#passwd", "password")
    page.click("#SubmitLogin")
    time.sleep(5)
    browser.close()