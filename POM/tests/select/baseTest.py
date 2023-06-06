import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_dropdown_menu_from_home(self):
        self.home_page.navigate_to_link_dropdown_menu()

    def select_country_by_index(self, index):
        self.select_page.select_country_index(index=index)

    def select_country_by_text(self, text):
        self.select_page.select_country_text(text=text)

    def select_country_by_value(self, value):
        self.select_page.select_country_value(value=value)
