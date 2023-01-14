import random

from selenium_base_new.base import SeleniumBase


class CheckBox(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.item_one = '#item-1'
        self.expand_all = 'button[title="Expand all"]'
        self.collapse_all = 'button[title="Collapse all"]'
        self.home_checkbox = 'label[for="tree-node-home"]'
        self.checkboxes_list = 'span[class="rct-title"]'
        self.EXPECTED_TEXT = ['Home', 'Desktop', 'Notes', 'Commands', 'Documents', 'WorkSpace', 'React',
                              'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General',
                              'Downloads', 'Word File.doc', 'Excel File.doc']
        self.CHECKED_ITEMS = 'svg[class="rct-icon rct-icon-check"]'
        self.TITLE_ITEM = './/ancestor::span[@class="rct-title"]'


    def find_item(self):
        return self.is_visible('css', self.item_one, 'Check Box Item View')

    def find_expand_all(self):
        return self.is_visible('css', self.expand_all, 'Expand All Button')

    def find_collapse_all(self):
        return self.is_visible('css', self.collapse_all, 'Collapse All Button')

    def find_home_checkbox(self):
        return self.is_visible('css', self.home_checkbox, 'Home CheckBox')

    def find_text(self):
        item_list = self.are_visible('css', self.checkboxes_list, 'Check Box List')
        data = []
        for item in item_list:
            data.append(item.text)
        return data

    def click_random_checkbox(self):
        checkbox = self.are_visible('css', self.checkboxes_list, 'Check Box List')
        count = 21
        while count != 0:
            item = checkbox[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_items(self):
        checked_list = self.are_present('css', self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element_by_xpath(self.TITLE_ITEM)
            data.append(title_item.text)
        return data

