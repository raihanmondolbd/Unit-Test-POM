import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import unittest
from TestData.testdata import Data


class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        # cls.driver.get(Data.BASE_URL)
        # cls.driver.get(Data.DROPDOWN_URL)
        # cls.driver.get(Data.KHASSFOOD_URL)
        print('Test Started')
        cls.driver.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

