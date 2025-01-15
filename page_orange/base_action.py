from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:
    basic_wait_time = 30


    def __init__(self,driver=None):
        self.driver = driver
        self.wait_for_60_second = 60

    def open_browser(self,browser):
        if browser=="chrome":
            self.driver=webdriver.Chrome()

        elif browser=="firefox":
            self.driver=webdriver.Firefox()

        elif browser=="edge":
            self.driver=webdriver.Edge()

        return self.driver

    def open_url(self,url):
        self.driver.get(url)

    def maximize_window_screen(self):
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.quit()

    def get_web_element(self, locator):
        element = self.driver.find_element(locator[0],locator[1])
        return element

    def click_me(self, locator):
        element = self.get_web_element(locator)
        element.click()

    def type_input(self, locator, value):
        element = self.get_web_element(locator)
        element.send_keys(value)

    def verify_element_displayed(self, locator):
        element= self.get_web_element(locator)
        return element.is_displayed()

    def wait_for_element(self, locator, default_timeout=20):
        if default_timeout is None:
            default_timeout = self.basic_wait_time
            WebDriverWait(self.driver,default_timeout).until(EC.presence_of_element_located(locator))
