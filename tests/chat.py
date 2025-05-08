from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configuração inicial
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

# Criar pasta para screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")


def take_screenshot(name):
    """Tira screenshot e salva com timestamp"""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot salvo: {filename}")


try:
    # 1. Acessar o site
    driver.get("https://www.saucedemo.com/")
    take_screenshot("01-pagina_inicial")

    # 2. Fazer login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    take_screenshot("02-pre_login")
    driver.find_element(By.ID, "login-button").click()
    take_screenshot("03-pos_login")

    # 3. Selecionar e adicionar produto ao carrinho
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'inventory_item_name') and text()='Sauce Labs Backpack']",
            )
        )
    )
    product.click()
    take_screenshot("04-detalhes_produto")

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Add to cart')]")
        )
    )
    add_button.click()
    take_screenshot("05-produto_adicionado")

    # 4. Ir para o carrinho
    cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart.click()
    take_screenshot("06-no_carrinho")

    # 5. Verificar produto no carrinho
    item_in_cart = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'inventory_item_name') and text()='Sauce Labs Backpack']",
            )
        )
    )
    assert item_in_cart.is_displayed()
    take_screenshot("07-produto_no_carrinho")

    # 6. Continuar comprando
    continue_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue-shopping"))
    )
    continue_btn.click()
    take_screenshot("08-volta_loja")

    # 7. Verificar que voltou para a página principal
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    take_screenshot("09-pagina_principal")

    print("Fluxo completo executado com sucesso!")

except Exception as e:
    take_screenshot("ERRO-teste_falhou")
    print(f"Erro durante a execução: {str(e)}")
    raise  # Re-lança a exceção para falhar o teste

finally:
    time.sleep(2)
    driver.quit()
