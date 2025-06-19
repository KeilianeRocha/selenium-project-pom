from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.shopping_cart_page import ShoppingCartPage
import pytest
import time

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.smoke
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        shopping_cart_page = ShoppingCartPage()

        # Declarando as variaveis de produtos
        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"

        # Fazendo o login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)
        print("DEBUG: Produto adicionado - Vou verificar o carrinho agora")
        home_page.adicionar_ao_carrinho(produto_2)
        print("DEBUG: Produto adicionado - Vou verificar o carrinho agora")
        time.sleep(2)

        # Verificando se a mochila foi adicionada
        home_page.acessar_carrinho()
        shopping_cart_page.verificar_produto_carrinho_existe(produto_1)
        shopping_cart_page.verificar_produto_carrinho_existe(produto_2)
        time.sleep(2)
"""
        # Clicando para volta para a tela de produtos
        shopping_cart_page.clicar_continuar_comprando()
        time.sleep(2)

        # Adicionando mais um produto ao carrinho

        time.sleep(2)"""


"""
        
        driver.find_element(By.ID, "continue-shopping").click()

        
        driver.find_element(
            By.XPATH,
            "//div[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']",
        ).click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verificando que os dois produtos foram adicionados
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(
            By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']"
        ).is_displayed()
        assert driver.find_element(
            By.XPATH,
            "//div[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']",
        ).is_displayed()

        # Remover um produto do carrinho
        driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']").click()

        # Fazer uma compra com 1 produto no carrinho
        driver.find_element(By.ID, "checkout").click()
        # Dados no chekout
        driver.find_element(By.ID, "first-name").send_keys("Standard")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("1234567")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        assert driver.find_element(By.XPATH, "//*[@class='app_logo']").is_displayed()
        assert driver.find_element(
            By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']"
        )
"""
# time.sleep(3)
# driver.quit()
