import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_date_picker_from_home(self):
        self.home_page.navigate_to_link_date_picker()

    def select_any_date(self, date):
        self.date_picker_page.select_date(date)
