import pytest
from tests.base_test import BaseTest
from TestingData import test_data


@pytest.mark.date_picker
class TestExam(BaseTest):
    def test_6pm_heels_items_count(self):
        self.navigate_to_shoes_page()
        self.navigate_to_heels_page()
        self.heels_count_data_info(test_data.heels_count_text)
