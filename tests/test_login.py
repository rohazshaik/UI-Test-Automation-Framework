from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_login(driver):

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url