import random

from selenium_base.base import SeleniumBase


class TestFormPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.radio_button = f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1, 3)}"]'

    def find_radio_button(self):
        button = self.is_visible('css', self.radio_button)
        self.click_on_element(button)
