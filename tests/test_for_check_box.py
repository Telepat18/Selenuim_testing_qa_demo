import pytest

from elements.check_box import CheckBox


@pytest.mark.usefixtures('setup')
class TestCheckBox:

    def text_check_box(self):
        check_box_page = CheckBox(self.driver)

