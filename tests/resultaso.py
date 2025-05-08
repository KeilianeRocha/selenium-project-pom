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

# Criar pasta para os screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")


def take_screenshot(name):
    """Função para tirar screenshot e salvar com nome específico"""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot salvo como: {filename}")


try:
    # 1. Acessar a página
    driver.get("https://www.saucedemo.com/")
    take_screenshot("01-pagina_inicial")

    # 2. Fazer login
    driver.find_element(By.ID, "user-name").send_keys(
        "standard_user"
    )  # Mudei para standard_user
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    take_screenshot("02-pre_login")
    driver.find_element(By.ID, "login-button").click()
    take_screenshot("03-pos_login")

    # 3. Selecionar produto
    driver.find_element(
        By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
    ).click()
    take_screenshot("04-detalhes_produto")

    # 4. Adicionar ao carrinho
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    take_screenshot("05-produto_adicionado")

    # 5. Ir para o carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    take_screenshot("06-carrinho")

    # 6. Verificar produto no carrinho
    item_no_carrinho = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']",
            )
        )
    )
    assert item_no_carrinho.is_displayed()
    take_screenshot("07-produto_no_carrinho")

    print("Teste concluído com sucesso!")

except Exception as e:
    take_screenshot("ERRO-teste_falhou")
    print(f"Erro durante o teste: {str(e)}")
    raise  # Re-lança a exceção para interromper a execução

finally:
    time.sleep(2)
    driver.quit()
