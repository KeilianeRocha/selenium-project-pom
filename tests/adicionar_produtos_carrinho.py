from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o driver e configurações básicas
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Fazendo o login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Após o login (logo depois do click no "login-button"):
try:
    driver.find_element(By.XPATH, "//div[text()='Not now']").click()  # Fecha a pop-up
except:
    print("Pop-up não apareceu. Continuando...")

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

# Volta para produtos (aqui estava o erro original - agora corrigido com ID)
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


time.sleep(10)
driver.quit()
