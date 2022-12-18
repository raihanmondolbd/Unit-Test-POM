import time

from TestCases.basetest import BaseTest
from selenium.webdriver.common.by import By
# from Locators.locators import Locators
from TestData.testdata import Data
from Pages.loginpage import LoginPage


class LoginTest(BaseTest):
    # def test_login(self):
    # self.driver.find_element(*Locators.userNameTextBox).send_keys(Data.USER_NAME)
    # time.sleep(3)
    # self.driver.find_element(*Locators.passWordTextBox).send_keys(Data.PASSWORD)
    # time.sleep(3)
    # self.driver.find_element(*Locators.submitButton).click()
    # time.sleep(5)

    # def test_login(self):
    # login = LoginPage(self.driver)
    # time.sleep(3)
    # login.enter_username()
    # time.sleep(2)
    # login.enter_password()
    # time.sleep(2)
    # login.click_submit()
    # time.sleep(2)

    def test_login(self):
        login = LoginPage(self.driver)
        self.driver.get(Data.BASE_URL)
        login.login()
        login.get_text_employeeList()
        time.sleep(2)
        login.get_color_value()
        login.hover_performance()
        login.get_color_value()
        login.get_class_value()
        login.is_displayed()
        login.is_selected()
        login.click_checkbox()
        login.is_selected()
        login.is_enabled()


