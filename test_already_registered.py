import pytest


@pytest.mark.parametrize("email", ["gevaba8747@meeeeesrumart.com"])
def test_conta_ja_existe(page, email):
    page.goto("http://www.automationpractice.pl/index.php")

    # clicar em Sign in
    page.click(".login")
    page.wait_for_url("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

    # preencher email já existente
    page.fill("#email_create", email)
    page.click("#SubmitCreate")

    # esperar erro aparecer
    page.wait_for_selector("#create_account_error")

    # validar mensagem
    mensagem = page.inner_text("#create_account_error").strip()
    assert "already been registered" in mensagem