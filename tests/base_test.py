import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_shoes_page(self):
        self.home_page.click_on_shoes_btn()

    def navigate_to_heels_page(self):
        self.shoes_page.click_on_heels_btn()

    def heels_count_data_info(self, expected_result):
        self.shoes_page.get_heels_count_data(expected_result)
