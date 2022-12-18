import time

from selenium.webdriver.common.by import By

from Locators.locators import Locators
from Pages.homepage import HomePage
from TestData.testdata import Data


class KhassfoodPage(HomePage):
    def __init__(self, driver):
        self.locator = Locators
        self.driver = driver
        super(KhassfoodPage, self).__init__(driver)

    def close_advertise(self):
        self.click_element(*self.locator.addvertise)

    def click_message_icon(self):
        self.click_element(*self.locator.messageIcon)

    def change_iframe(self):
        self.switch_iframe(*self.locator.iframe)

    def enter_name(self):
        self.click_element(*self.locator.nameTextBox)
        time.sleep(2)
        self.enter_text(Data.NAME, *self.locator.nameTextBox)

    def enter_phone_number(self):
        self.click_element(*self.locator.phoneNumberTextBox)
        time.sleep(2)
        self.enter_text('0123456789', *self.locator.phoneNumberTextBox)

    def enter_message(self):
        self.click_element(*self.locator.messageTextArea)
        time.sleep(2)
        self.enter_text('Hi, I want to by chicken', *self.locator.messageTextArea)

    def close_message(self):
        self.click_element(*self.locator.chatClose)

    def change_default_iframe(self):
        self.switch_to_default_content()

    def search_product(self):
        self.enter_text("Chicken", *self.locator.searchTextbox)

    def click_search_icon(self):
        self.click_element(*self.locator.searchIcon)

    def select_chicken(self):
        self.press_ctrl_A(*self.locator.searchTextbox)

    def copy_chicken(self):
        self.press_ctrl_C(*self.locator.searchTextbox)

    def switch_to_new_tab(self):
        # global original_window
        # original_window = self.driver.current_window_handle
        # print(original_window)
        self.open_new_tab()
        self.driver.get("https://www.google.com/")

    def paste_chicken(self):
        self.press_ctrl_V(*self.locator.googleSearchTextbox)
        time.sleep(2)
        self.press_Enter(*self.locator.googleSearchTextbox)

    def switch_previus(self):
        self.switch_to_previus_tab()



