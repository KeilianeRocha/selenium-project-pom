from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_fazer_login_valido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "//*[@class='app_logo']").is_displayed()
