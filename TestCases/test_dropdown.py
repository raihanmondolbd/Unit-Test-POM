import time
from TestData.testdata import Data
from Pages.dropdownpage import DropdownPage
from TestCases.basetest import BaseTest


class Dropdown(BaseTest):
    def test_dropdown(self):
        dp = DropdownPage(self.driver)
        self.driver.get(Data.DROPDOWN_URL)
        dp.select_bangladesh()
        time.sleep(5)
        dp.select_america()
        time.sleep(5)
        dp.select_algeria()
        time.sleep(5)
        dp.select_argentina()
        time.sleep(5)

