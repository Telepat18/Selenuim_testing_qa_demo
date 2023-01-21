from selenium_base.base import SeleniumBase


class Buttons(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.button_item = 'li[id="item-4"]'
        self.double_button = 'button[id="doubleClickBtn"]'
        self.right_click_button = 'button[id="rightClickBtn"]'
        self.click_me_button = "//div[3]/button"
        self.success_double = 'p[id="doubleClickMessage"]'
        self.success_right = 'p[id="rightClickMessage"]'
        self.success_click_me = 'p[id="dynamicClickMessage"]'
        self.double_text = 'You have done a double click'
        self.right_text = 'You have done a right click'
        self.click_text = 'You have done a dynamic click'

    def find_button_item(self):
        return self.is_visible('css', self.button_item).click()

    def click_on_different_buttons(self, type_click):
        if type_click == "double":
            self.action_double_click(self.is_visible('css', self.double_button))
            return self.check_clicked_on_button(self.success_double)
        if type_click == "right":
            self.action_right_click(self.is_visible('css', self.right_click_button))
            return self.check_clicked_on_button(self.success_right)
        if type_click == "click":
            self.is_visible('xpath', self.click_me_button).click()
            return self.check_clicked_on_button(self.success_click_me)

    def check_clicked_on_button(self, element):
        return self.is_present('css', element).text
