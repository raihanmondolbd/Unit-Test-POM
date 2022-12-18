import time
from TestData.testdata import Data
from TestCases.basetest import BaseTest
from Pages.khassfoodpage import KhassfoodPage


class IframeTest(BaseTest):

    def test_iframe(self):
        kf = KhassfoodPage(self.driver)
        self.driver.get(Data.KHASSFOOD_URL)
        try:
            kf.close_advertise()
        except:
            print("Advertise does not visible")


        # time.sleep(2)
        # kf.click_message_icon()
        # time.sleep(2)
        # kf.change_iframe()
        # time.sleep(2)
        # kf.enter_name()
        # time.sleep(2)
        # kf.enter_phone_number()
        # time.sleep(2)
        # kf.enter_message()
        # time.sleep(2)
        # kf.close_message()
        # time.sleep(2)
        # kf.change_default_iframe()
        kf.search_product()
        # time.sleep(5)
        kf.click_search_icon()
        # time.sleep(2)
        kf.select_chicken()
        # time.sleep(2)
        kf.copy_chicken()
        kf.switch_to_new_tab()
        # time.sleep(5)
        kf.paste_chicken()
        # time.sleep(2)
        kf.switch_previus()
        # time.sleep(5)
