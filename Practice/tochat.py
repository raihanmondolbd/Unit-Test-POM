import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl


class Selenium(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        # cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.khaasfood.com/')
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        # print("Test Finished!")

    def test_login(self):
        # try:
        #     self.driver.find_element(By.XPATH, '//button[@class="bld-el   snp-close-link snp-cursor-pointer"]').click()
        # except:
        #     print('There is no add')
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, '//div[@id="webchat"]/div[2]/div').click()
        # time.sleep(2)
        # self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//iframe[@class="cwidsk16-styled-frame"]'))
        # self.driver.find_element(By.XPATH, '(// input[ @ type = "text"][ @ placeholder = "Name*"])').send_keys('Dola')
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, '//input[@placeholder="Phone Number*"]').send_keys('01712111111')
        # time.sleep(5)
        # self.driver.switch_to.default_content()

        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = 'Product price'
        sheet.append(['product_name', 'price'])

        self.driver.find_element(By.XPATH, '//button[@class="bld-el   snp-close-link snp-cursor-pointer"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '(//input[@name="s"][@type="text"])[1]').send_keys('chicken')
        time.sleep(5)
        self.driver.find_element(By.XPATH, '(//button [@type="submit"][@class="searchsubmit"])[1]').click()
        time.sleep(5)
        for i in range(1, 13):
            productName = self.driver.find_element(By.XPATH, f'(//h3[@class="product-title"]/a)[{i}]').text
            price = self.driver.find_element(By.XPATH, f'(//span[@class="price"]/span)[{i}]').text
            print(f'{i}: {productName} price is : {price}')
            sheet.append([productName, price])

        excel.save('../price.xlsx')
