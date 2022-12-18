import time

from Locators.locators import Locators
from Pages.homepage import HomePage
from TestData.testdata import Data


class DropdownPage(HomePage):
    def __init__(self, driver):
        self.locator = Locators
        self.driver = driver
        super(DropdownPage, self).__init__(driver)

    def select_bangladesh(self):
        self.select_value_from_dropdown_by_text('Bangladesh', *self.locator.select_dropdown)

    def select_america(self):
        self.select_value_from_dropdown_by_value('USA', *self.locator.select_dropdown)

    def select_algeria(self):
        self.select_value_from_dropdown_by_index(3, *self.locator.select_dropdown)

    def select_argentina(self):
        self.click_element(*self.locator.select_dropdown)
        time.sleep(5)
        self.click_element(*self.locator.arg)