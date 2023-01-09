import time

import pytest

from elements.check_box import CheckBox
from elements.elements import Elements


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


