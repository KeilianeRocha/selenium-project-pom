from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//*[@class='app_logo']")
        
    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)
