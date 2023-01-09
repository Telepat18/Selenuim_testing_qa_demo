from selenium.webdriver.remote.webelement import WebElement
from typing import List, Tuple

from generator.generator import generated_person
from selenium_base_new.base import SeleniumBase


class Elements(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.name_field = '#userName'
        self.email = '#userEmail'
        self.current_address = '#currentAddress'
        self.permanent_address = '#permanentAddress'
        self.submit = '#submit'
        self.name_text = 'p[id="name"]'
        self.email_text = 'p[id="email"]'
        self.current_address_text = 'p[id="currentAddress"]'
        self.permanent_address_text = 'p[id="permanentAddress"]'

    def full_name_field(self):
        return self.is_visiable('css', self.name_field, 'Full name field')

    def email_field(self):
        return self.is_visiable('css', self.email, 'Email field')

    def current_address_field(self):
        return self.is_visiable('css', self.current_address, 'Current address field')

    def permanent_address_field(self):
        return self.is_visiable('css', self.permanent_address, 'Permanent address field')

    def submit_button(self):
        return self.element_is_clickable('css', self.submit, 'Submit button')

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.full_name_field().send_keys(full_name)
        self.email_field().send_keys(email)
        self.current_address_field().send_keys(current_address)
        self.permanent_address_field().send_keys(permanent_address)
        self.submit_button().click()
        return full_name, email, current_address, permanent_address

    def text_name(self):
        return self.is_visiable('css', self.name_text, "Name Text")

    def text_email(self):
        return self.is_visiable('css', self.email_text, "Email Text")

    def text_current_address(self):
        return self.is_visiable('css', self.current_address_text, "Current Address Text")

    def text_permanent_address(self):
        return self.is_visiable('css', self.permanent_address_text)

    def entered_data(self):
        output_name = self.text_name().text.split(':')[1]
        output_email = self.text_email().text.split(':')[1]
        output_current_address = self.text_current_address().text.split(':')[1]
        output_permanent_address = self.text_permanent_address().text.split(':')[1]
        return output_name, output_email, output_current_address, output_permanent_address

