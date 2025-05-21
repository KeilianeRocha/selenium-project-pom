from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import conftest
import pytest
import time
from pages.login_page import LoginPage


"""
# Inicializa o driver e configurações básicas
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
"""
"""
# ------ TRATAMENTO DO SEU POP-UP ESPECÍFICO ------ #
try:
    # Espera pelo botão "Not now" ou "Agora não" do Google
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Not now') or contains(., 'Agora não')]")
        )
    ).click()
    print("Pop-up do Google fechado!")
except:
    print("Nenhum pop-up do Google encontrado - continuando normalmente")
# ------------------------------------------------- #
"""

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        # Fazendo o login
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        """driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
"""
        """# 2. Fecha pop-ups (se existirem)
        try:
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]"))
            ).click()
        except:
            pass  # Ignora se não houver pop-up
        """
        # Adicionando a mochila
        driver.find_element(
            By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']"
        ).click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verificando se a mochila foi adicionada
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(
            By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']"
        ).is_displayed()

        # Volta para produtos
        driver.find_element(By.ID, "continue-shopping").click()

        # Adicionando mais um produto ao carrinho
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

        # time.sleep(3)
        driver.quit()
