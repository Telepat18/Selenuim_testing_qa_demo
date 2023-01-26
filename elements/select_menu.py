from selenium.webdriver import Keys

from selenium_base.base import SeleniumBase


class SelectMenuPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.dropdown = 'div[id="withOptGroup"]'

    def find_dropdown(self):
        return self.is_visible('css', self.dropdown).send_keys(Keys.ENTER)
