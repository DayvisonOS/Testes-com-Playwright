import pytest

#gemini
def test_enviar_mensagem_pelo_fale_conosco(page):
    """
    Testa o envio de uma mensagem através do formulário de "Contact us".
    """
    # 1. Ir para a página de contato
    page.goto("http://www.automationpractice.pl/index.php?controller=contact")

    # 2. Preencher os campos do formulário
    # Selecionar um assunto
    page.select_option("#id_contact", label="Customer service")

    # Preencher o e-mail
    page.fill("#email", "cliente.teste@email.com")

    # Preencher a referência do pedido (opcional para o teste)
    page.fill("#id_order", "12345")

    # Anexar um arquivo (exemplo, cria um arquivo falso para o teste)
    # page.set_input_files("#fileUpload", "path/to/your/file.txt") # Descomente se quiser testar upload

    # Preencher a mensagem
    page.fill("#message", "Esta é uma mensagem de teste enviada por um script automatizado.")

    # 3. Clicar em "Send"
    page.click("#submitMessage")

    # 4. Esperar pela mensagem de sucesso
    page.wait_for_selector(".alert.alert-success")

    # 5. Validar a mensagem de confirmação
    success_alert = page.inner_text(".alert.alert-success").strip()
    assert "Your message has been successfully sent to our team." in success_alert