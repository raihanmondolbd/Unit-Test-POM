from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    WebDriverException
import time


class HomePage(object):
    def __init__(self, driver, base_url=''):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 90

    def get_element(self, *locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(*locator))
        self.driver.find_element(*locator)

    def get_elements(self, *locator):
        self.driver.find_elements(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()
        # self.get_element(*locator).click()

    def enter_text(self, data, *locator):
        element = self.driver.find_element(*locator)
        element.send_keys(data)

    def get_text(self, *locator):
        text = self.driver.find_element(*locator).text
        print(text)
        return text

    def hover_element(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_css_value(self, *locator):
        element = self.driver.find_element(*locator)
        color = element.value_of_css_property('background-color')
        print(color)
        return color

    def get_attribute_value(self, *locator):
        element = self.driver.find_element(*locator)
        cls = element.get_attribute('class')
        print(cls)
        return cls

    def is_element_displayed(self, *locator):
        element = self.driver.find_element(*locator)
        result = element.is_displayed()
        print(result)
        return result

    def is_element_selected(self, *locator):
        element = self.driver.find_element(*locator)
        result = element.is_selected()
        print(result)
        return result

    def is_element_enabled(self, *locator):
        element = self.driver.find_element(*locator)
        result = element.is_enabled()
        print(result)
        return result

    def select_value_from_dropdown_by_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_value_from_dropdown_by_value(self, value, *locator):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_value(value)

    def select_value_from_dropdown_by_index(self, index, *locator):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_index(index)

    def switch_iframe(self, *locator):
        element = self.driver.find_element(*locator)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def press_ctrl_A(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "A")

    def press_ctrl_C(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "C")

    def press_ctrl_V(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "V")

    def press_Enter(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def open_new_tab(self):
        self.driver.switch_to.new_window('tab')

    def open_new_window(self):
        self.driver.switch_to.new_window('window')

    def switch_to_previus_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])






