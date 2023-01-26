import time

from selenium_base.base import SeleniumBase


class DynamicPropertiesPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.properties_item = 'li[id="item-8"]'
        self.enable_button = 'button[id="enableAfter"]'
        self.color_button = 'button[id="colorChange"]'
        self.visible_button = 'button[id="visibleAfter"]'
        self.expected_color_before = 'rgba(255, 255, 255, 1)'
        self.expected_color_after = 'rgba(220, 53, 69, 1)'

    def find_properties_item(self):
        item = self.is_present('css', self.properties_item)
        self.go_to_element(item)
        item.click()

    def check_enable_button(self):
        try:
            self.element_is_clickable('css', self.enable_button)
        except TimeoutError:
            return False
        return True

    def check_color_button(self):
        color_button = self.is_present('css', self.color_button)
        color_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_after = color_button.value_of_css_property('color')
        return color_before, color_after
