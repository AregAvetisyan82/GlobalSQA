import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_tooltip_from_home(self):
        self.home_page.navigate_to_link_tooltip()

    def hover_on_tooltip_image(self, expected_result):
        self.tooltip_page.hover_on_image(expected_result=expected_result)

    def hover_on_tooltip_text(self, expected_result):
        self.tooltip_page.hover_on_text(expected_result=expected_result)

    def hover_on_tooltip_inner_text(self, expected_result):
        self.tooltip_page.hover_on_inner_text(expected_result=expected_result)