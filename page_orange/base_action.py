from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:
    basic_wait_time = 30        #dought----------------------


    def __init__(self,driver=None):
        self.driver = driver
        self.wait_for_60_second = 60

    def open_browser(self,browser):
        """it is used open the browser like chrome, firefox, edge"""

        if browser=="chrome":
            self.driver=webdriver.Chrome()

        elif browser=="firefox":
            self.driver=webdriver.Firefox()

        elif browser=="edge":
            self.driver=webdriver.Edge()

        return self.driver

    def open_url(self,url):
        """it is used to open url"""

        self.driver.get(url)

    def maximize_window_screen(self):
        """it is used to maximize the browser window....."""
        self.driver.maximize_window()

    def close_browser(self):
        """it is used for close the browser"""
        self.driver.quit()

    def get_web_element(self, locator):
        """it is used for get the web element........ """
        element = self.driver.find_element(locator[0],locator[1])
        return element

    def get_web_elements(self,locator):
        """it is used for get the web elements or a list of elements....... """
        elements = self.driver.find_elements(locator[0],locator[1])
        return elements

    def click_me(self, locator):
        """it is used for click action only....... """
        element = self.get_web_element(locator)
        element.click()

    def type_input(self, locator, value):
        """it is used for send the user input.... """
        element = self.get_web_element(locator)
        element.send_keys(value)

    def verify_element_displayed(self, locator):
        element= self.get_web_element(locator)
        return element.is_displayed()

    def wait_for_element(self, locator, default_timeout=20):
        """it is  wait for a specific element ........ """
        if default_timeout is None:     #dought---------
            default_timeout = self.basic_wait_time
            WebDriverWait(self.driver,default_timeout).until(EC.presence_of_element_located(locator))


    def clear_text_box(self,locator):
        """it is used for clear the existing text in a text box...... """
        element = self.get_web_element(locator)
        element.clear()


    def check_is_enabled(self,locator):
        """it is used to determine whether a web element is enabled or not.
         This is particularly useful when working with form elements like buttons, input fields, or dropdowns.
         If an element is enabled, it means it can be interacted with, such as clicking or typing."""
        element = self.get_web_element(locator)
        element.is_enabled()


    def check_is_selected(self,locator):
        """it is used to check if a web element is currently selected. This method is typically used with elements like:
        Checkboxes
        Radio buttons
        Options in a dropdown menu (when implemented using <select> and <option>)"""

        element = self.get_web_element(locator)
        element.is_selected()





