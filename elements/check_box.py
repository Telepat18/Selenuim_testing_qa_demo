from selenium_base_new.base import SeleniumBase


class CheckBox(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check_box = '#item-1'
        self.expand_all_button = 'button[title="Expand-all"]'
        self.item_list = 'span[class="rct-title"]'
        'ul[class ="header__gender"]'

    def submit_button(self):
        return self.element_is_clickable('css', self.check_box, 'Submit button')

    def open_full_list(self):
        return self.is_visiable('css', self.expand_all_button, 'Expand All').click()

    # def click_random_checkbox(self):
    #     return self.are_visiable('css' self.item_list, 'item list')
