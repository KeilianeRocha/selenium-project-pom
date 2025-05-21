from selenium import webdriver
import conftest
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "123456")