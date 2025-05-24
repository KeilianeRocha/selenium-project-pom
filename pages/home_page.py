from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        # Padrão para o item do inventário (sem ser tupla ainda)
        self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name' and text()='{0}']")
        # self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name' and text()='{}']")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        # Cria o locator dinamicamente como uma tupla
        # item_locator = (self.item_inventario[0],self.item_inventario[1].replace("{0}", nome_item))
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

