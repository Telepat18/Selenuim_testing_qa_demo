import random
import time

import pytest

from elements.check_box import CheckBox
from elements.elements import Elements
from elements.radio_button import RadioButton
from elements.web_tables import WebTablesPage


@pytest.mark.usefixtures('setup')
class TestElements:

    def test_text_box(self):
        text_box_page = Elements(self.driver)
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_current_address, output_permanent_address = text_box_page.entered_data()
        assert full_name == output_name
        assert email == output_email
        assert current_address == output_current_address
        assert permanent_address == output_permanent_address
        time.sleep(5)

    def test_check_box(self):
        check_box_page = CheckBox(self.driver)
        check_box_page.find_item().click()
        check_box_page.find_expand_all().click()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        actual_result_text = check_box_page.find_text()
        expected_result_text = check_box_page.expected_text
        assert actual_result_text == expected_result_text
        assert input_checkbox == output_result
        time.sleep(5)

    def test_radio_button(self):
        radio_button_page = RadioButton(self.driver)
        radio_button_page.find_item().click()
        radio_button_page.find_yes_option().click()
        output_yes = radio_button_page.get_output_result()
        radio_button_page.find_impressive_option().click()
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.find_no_option().click()
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes'
        assert output_impressive == 'Impressive'
        assert output_no == 'No'

    def test_web_tables(self):
        web_tables_page = WebTablesPage(self.driver)
        web_tables_page.find_item_three().click()
        web_tables_page.find_add_button().click()
        new_person = web_tables_page.add_new_person()
        table_result = web_tables_page.find_table_element()
        assert new_person in table_result

    def test_web_table_search_person(self):
        web_tables_page = WebTablesPage(self.driver)
        web_tables_page.find_item_three().click()
        web_tables_page.find_add_button().click()
        key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
        web_tables_page.search_person(key_word)
        table_result = web_tables_page.check_person()
        assert key_word in table_result

    def test_web_table_update_info(self):
        web_tables_page = WebTablesPage(self.driver)
        web_tables_page.find_item_three().click()
        web_tables_page.find_add_button().click()
        lastname = web_tables_page.add_new_person()[1]
        web_tables_page.search_person(lastname)
        age = web_tables_page.update_person_info()
        row = web_tables_page.check_person()
        assert age in row

    def test_web_table_delete_info(self):
        web_tables_page = WebTablesPage(self.driver)
        web_tables_page.find_item_three().click()
        web_tables_page.find_add_button().click()
        email = web_tables_page.add_new_person()[3]
        web_tables_page.search_person(email)
        web_tables_page.delete_person()
        text = web_tables_page.check_deleted()
        assert text == web_tables_page.no_rows_found_text
