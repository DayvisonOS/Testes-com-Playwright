import pytest
#gemini
# Usaremos um e-mail válido, mas uma senha incorreta
VALID_EMAIL = "gevaba8747@meeeeesrumart.com"
INVALID_PASSWORD = "wrongpassword123"

def test_login_com_senha_invalida(page):
    """
    Testa o fluxo de login com uma senha inválida e valida a mensagem de erro.
    """
    # 1. Navegar para a página de autenticação
    page.goto("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

    # 2. Preencher credenciais inválidas
    page.fill("#email", VALID_EMAIL)
    page.fill("#passwd", INVALID_PASSWORD)
    page.click("#SubmitLogin")

    # 3. Esperar pela mensagem de erro
    # O seletor '.alert.alert-danger' identifica a caixa de erro que aparece
    page.wait_for_selector(".alert.alert-danger")

    # 4. Validar o conteúdo da mensagem de erro
    mensagem_erro = page.inner_text(".alert.alert-danger li").strip()
    assert mensagem_erro == "Authentication failed."