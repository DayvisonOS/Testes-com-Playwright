import pytest
#gemini
# E-mail de uma conta que sabemos que existe
EXISTING_EMAIL = "gevaba8747@meeeeesrumart.com"

def test_recuperar_senha(page):
    """
    Testa o fluxo de recuperação de senha para um e-mail registrado.
    """
    # 1. Ir para a página de login
    page.goto("http://www.automationpractice.pl/index.php?controller=authentication")

    # 2. Clicar no link "Forgot your password?"
    page.click("a[title='Recover your forgotten password']")

    # 3. Esperar a página de recuperação de senha carregar
    page.wait_for_url("http://www.automationpractice.pl/index.php?controller=password")

    # 4. Preencher o e-mail e solicitar a recuperação
    page.fill("#email", EXISTING_EMAIL)
    page.click("button.button-medium") # Clica no botão 'Retrieve Password'

    # 5. Esperar pela mensagem de confirmação
    page.wait_for_selector(".alert.alert-success")

    # 6. Validar a mensagem de sucesso
    confirmation_message = page.inner_text(".alert.alert-success").strip()
    assert "A confirmation email has been sent to your address" in confirmation_message