import pytest
from GlobalSQA.POM.tests.date_picker.baseTest import BaseTest


@pytest.mark.date_picker
class TestDatePicker(BaseTest):
    @pytest.mark.parametrize("date", ["06/02/2023", "06/01/2023", "05/31/2023"])
    def test_date_picker_icon(self, date):
        self.navigate_to_date_picker_from_home()
        self.select_any_date(date)
