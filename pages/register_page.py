import time

from pages.base_action import BaseAction
from selenium.webdriver.common.by import By

class Register(BaseAction):
    register_text = (By.XPATH,'//h2[text()="Register"]')
    first_name = (By.XPATH,'//input[@placeholder="First Name"]')
    last_name = (By.XPATH,'//input[@placeholder="Last Name"]')
    adress = (By.XPATH,'//textarea[@ng-model="Adress"]')
    email_id = (By.XPATH,'//input[@type="email"]')
    phone_no = (By.XPATH,'//input[@type="tel"]')
    gender = (By.XPATH,'//div[@class="col-md-4 col-xs-4 col-sm-4"]/label/input')
    hobbies = (By.XPATH,'//div[@class="col-md-4 col-xs-4 col-sm-4"]/div/input')
    languages_click = (By.XPATH,'//div[@id="msdd"]')
    language_dropdown = (By.XPATH,'//ul[@class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all"]')
    login_flipcart_text = (By.XPATH,"//span[text()='Login']")



    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    # def validate_register_page(self):
    #     text = self.wait_for_element(self.register_text).text()
    #     assert text=="Register", "Page not veryfied"

    def enter_first_name(self):
        self.type_input(self.first_name,"Suvam")

    def enter_last_name(self):
        self.type_input(self.last_name,"Nayak")

    def enter_adress(self):
        self.type_input(self.adress,"Bhadrak")

    def enter_email_id(self):
        self.type_input(self.email_id,"suvamnayakbdk@gmail.com")

    def phone_number(self):
        self.type_input(self.phone_no,"9876543210")

    def gender_select(self):
        elements = self.get_web_elements(self.gender)
        for each in elements:
            self.click_me(each)
            print(f'gender name- {each.get_attribute("value")},check is selected {each.is_selected()}')
            time.sleep(2)

    def hobbies_select(self):
        elements = self.get_web_elements(self.hobbies)
        for i in elements:
            self.click_me(i)
            print(f'hobby name- {i.get_attribute("value")},check is selected {i.is_selected()}')
            time.sleep(2)

    def language_select(self):
        self.get_web_element(self.languages_click).click()
        self.wait_for_element(self.language_dropdown)
        self.click_me('//a[text()="English"]')

    def login_text_validation(self):
        # excepted_text='Login'
        self.wait_for_element(self.login_flipcart_text)
        outcome_text = self.get_text(self.login_flipcart_text)
        print(outcome_text)





