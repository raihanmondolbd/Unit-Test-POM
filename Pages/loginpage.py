import time

from Locators.locators import Locators
from Pages.homepage import HomePage
from TestData.testdata import Data


class LoginPage(HomePage):
    def __init__(self, driver):
        self.locator = Locators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def enter_username(self):
        self.enter_text(Data.USER_NAME, *self.locator.userNameTextBox)

    def enter_password(self):
        self.enter_text(Data.PASSWORD, *self.locator.passWordTextBox)

    def click_submit(self):
        self.click_element(*self.locator.submitButton)

    def login(self):
        self.enter_text(Data.USER_NAME, *self.locator.userNameTextBox)
        time.sleep(2)
        self.enter_text(Data.PASSWORD, *self.locator.passWordTextBox)
        time.sleep(2)
        self.click_element(*self.locator.submitButton)
        time.sleep(2)

    def get_text_employeeList(self):
        self.get_text(*self.locator.employeeList)

    def hover_performance(self):
        self.hover_element(*self.locator.performance)

    def get_color_value(self):
        self.get_css_value(*self.locator.performance)

    def get_class_value(self):
        self.get_attribute_value(*self.locator.pim)

    def is_displayed(self):
        self.is_element_displayed(*self.locator.orangeImg)

    def is_selected(self):
        self.is_element_selected(*self.locator.secondCheckbox)

    def click_checkbox(self):
        self.click_element(*self.locator.secondCheckbox2)

    def is_enabled(self):
        self.is_element_enabled(*self.locator.employee_id)
