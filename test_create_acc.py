import time

from playwright.sync_api import sync_playwright
email_address = "gevaba8747@meeeeesrumart.com"
with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)  # headless=False abre o navegador
    page = browser.new_page()
    page.goto("http://www.automationpractice.pl/index.php")
    print(page.title())
    page.click(".login")
    page.wait_for_url(url="http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
    page.fill("#email_create", email_address)
    page.click("#SubmitCreate")
    page.wait_for_url(url="http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    page.click("#uniform-id_gender1")
    page.fill("#customer_firstname", "Joaozin")
    page.fill("#customer_lastname", "Silva")
    valor_email = page.input_value("#email")
    assert valor_email == email_address
    page.fill("#passwd", "password")
    page.select_option("#days","10")
    page.select_option("#months","10")
    page.select_option("#years","1998")
    page.click("#submitAccount")
    page.wait_for_selector(".alert.alert-success", timeout=60000)
    msg = page.inner_text(".alert.alert-success").strip()
    time.sleep(5)
    assert msg == "Your account has been created."
