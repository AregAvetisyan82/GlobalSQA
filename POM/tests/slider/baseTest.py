import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_demo_site(self):
        self.home_page.navigate_to_demo_testing_site()

    def slider_move_to_left(self, x_offset, colour_number):
        self.slider_page.slider_red_color_move(x_offset, colour_number)
