from selenium_base.base import SeleniumBase


class RadioButton(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.item_two = '#item-2'
        self.yes_option = 'label[class^="custom-control"][for="yesRadio"]'
        self.impressive_option = 'label[class^="custom-control"][for="impressiveRadio"]'
        self.no_option = 'label[class^="custom-control"][for="noRadio"]'
        self.output_result = 'p span[class="text-success"]'

    def find_item(self):
        return self.is_visible('css', self.item_two, 'Radio Button view')

    def find_yes_option(self):
        return self.is_visible('css', self.yes_option, 'Yes Option')

    def find_impressive_option(self):
        return self.is_visible('css', self.impressive_option, 'Impressive Option')

    def find_no_option(self):
        return self.is_visible('css', self.no_option, 'No Option')

    def get_output_result(self):
        return self.is_visible('css', self.output_result).text
