from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest
import pytest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        # 1. Preenche login com senha ERRADA
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("123456")  # Senha incorreta
        driver.find_element(By.ID, "login-button").click()

        # 2. Fecha pop-ups (se existirem)
        try:
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]"))
            ).click()
        except:
            pass  # Ignora se não houver pop-up

        # 3. Verifica a MENSAGEM DE ERRO ESPECÍFICA
        try:
            error_message = (
                WebDriverWait(driver, 10)
                .until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
                .text
            )
            assert (
                "Epic sadface: Username and password do not match any user in this service"
                in error_message
            )  # Mensagem exata
            print("✅ Teste de falha no login PASSOU! (Erro exibido corretamente)")
        except Exception as e:
            print(f"❌ Falha no teste: {e}")
            raise  # Força o teste a falhar com o erro original

        driver.quit()

        # Pedi ajuda da IA, MAS 90% FOI DOR E SOFRIMENTO MEU.