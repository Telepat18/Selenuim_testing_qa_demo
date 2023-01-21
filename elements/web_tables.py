import random

from generator.generator import create_person
from selenium_base.base import SeleniumBase


class WebTablesPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.item_three = '#item-3'
        self.add_button = 'button[id="addNewRecordButton"]'
        self.first_name_field = 'input[id="firstName"]'
        self.last_name_field = 'input[id="lastName"]'
        self.email_field = 'input[id="userEmail"]'
        self.age_field = 'input[id="age"]'
        self.salary_field = 'input[id="salary"]'
        self.department_field = 'input[id="department"]'
        self.submit_button = 'button[id="submit"]'
        self.table_item = 'div[class="rt-tr-group"]'
        self.search_box = 'input[id="searchBox"]'
        self.delete_icon = 'span[title="Delete"]'
        self.row_parent = ".//ancestor::div[@class='rt-tr-group']"
        self.update_button = 'span[title="Edit"]'
        self.not_found = 'div[class="rt-noData"]'
        self.no_rows_found_text = 'No rows found'

    def find_item_three(self):
        return self.is_visible('css', self.item_three)

    def find_add_button(self):
        return self.is_visible('css', self.add_button)

    def find_first_name_field(self):
        return self.is_visible('css', self.first_name_field)

    def find_last_name_field(self):
        return self.is_visible('css', self.last_name_field)

    def find_email_field(self):
        return self.is_visible('css', self.email_field)

    def find_age_field(self):
        return self.is_visible('css', self.age_field)

    def find_salary_field(self):
        return self.is_visible('css', self.salary_field)

    def find_department_field(self):
        return self.is_visible('css', self.department_field)

    def find_submit_button(self):
        return self.is_visible('css', self.submit_button)

    def add_new_person(self):
        count = random.randint(1, 3)
        while count != 0:
            person_info = next(create_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.find_first_name_field().send_keys(first_name)
            self.find_last_name_field().send_keys(last_name)
            self.find_email_field().send_keys(email)
            self.find_age_field().send_keys(age)
            self.find_salary_field().send_keys(salary)
            self.find_department_field().send_keys(department)
            self.find_submit_button().click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def find_table_element(self):
        table_element = self.are_visible('css', self.table_item)
        data = []
        for item in table_element:
            data.append(item.text.splitlines())
        return data

    def search_person(self, key_word):
        return self.is_visible('css', self.search_box).send_keys(key_word)

    def check_person(self):
        delete_button = self.is_visible('css', self.delete_icon)
        row = delete_button.find_element("xpath", self.row_parent)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(create_person())
        age = person_info.age
        self.is_visible('css', self.update_button).click()
        self.is_visible('css', self.age_field).clear()
        self.is_visible('css', self.age_field).send_keys(age)
        self.is_visible('css', self.submit_button).click()
        return str(age)

    def delete_person(self):
        self.is_visible('css', self.delete_icon).click()

    def check_deleted(self):
        return self.is_present('css', self.not_found).text
