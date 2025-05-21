#from selenium import webdriver
#from selenium.webdriver.common.by import By
import pytest
#import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_fazer_login_valido(self):
        #driver = conftest.driver
        
        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()
        
        # faz o login
        login_page.fazer_login("standard_user", "secret_sauce")
        
        # verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()
        
        #assert driver.find_element(By.XPATH, "//*[@class='app_logo']").is_displayed()
