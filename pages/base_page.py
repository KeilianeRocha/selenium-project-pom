import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import (expected_conditions as EC,)  # abreviação de 'expected_conditions'
from selenium.webdriver import ActionChains, Keys

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento"
        f"'{locator}' não foi encontrado na tela"

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text
    
    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f"Elemento '{locator}' não existe,mas é esperado que exista."
    
    def verificar_se_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elemento(locator)) == 0, f"Elemento '{locator}' existe, é esperado que não exista."
        
    def clicar_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()
    
    def clique_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()

    def precionara_teclas(self, locator, key):
        elem = self.encontrar_elemento(locator)
        if key == "ENTER": # mesma foram que vai ser chamada
            elem.send_keys(Keys.ENTER)
        elif key == "SPACE":
            elem.send_keys(Keys.SPACE)
        elif key == "F1":
            elem.send_keys(Keys.F1)
            
            
        
        
    