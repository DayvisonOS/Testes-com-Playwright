import pytest
import time
#gemini

def test_buscar_produto_e_adicionar_ao_carrinho(page):
    """
    Testa a busca de um produto, a adição ao carrinho e a validação
    da mensagem de sucesso na janela modal.
    """
    # 1. Ir para a página inicial
    page.goto("http://www.automationpractice.pl/index.php")

    # 2. Buscar por um produto (ex: "Blouse")
    produto_busca = "Blouse"
    page.fill("#search_query_top", produto_busca)
    page.click("[name='submit_search']")

    # 3. Esperar a página de resultados carregar
    page.wait_for_selector(".product_list.grid")

    # 4. Passar o mouse sobre o primeiro produto para revelar o botão "Add to cart"
    page.hover(".product_list .product-container:first-child")

    # 5. Clicar no botão "Add to cart"
    # O seletor garante que estamos clicando no botão do primeiro produto
    page.click(".product_list .ajax_add_to_cart_button:first-child")

    # 6. Esperar a janela de confirmação (modal) aparecer
    page.wait_for_selector("#layer_cart", state="visible", timeout=60000)

    # 7. Validar a mensagem de sucesso dentro do modal
    success_message = page.inner_text("#layer_cart .layer_cart_product h2").strip()
    assert "Product successfully added to your shopping cart" in success_message

    # 8. (Opcional) Fechar o modal para finalizar o teste de forma limpa
    page.click("span[title='Close window']")
    time.sleep(2)  # Pequena pausa para observar o fechamento