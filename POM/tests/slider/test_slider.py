import pytest
from GlobalSQA.POM.tests.slider.baseTest import BaseTest


# DEFAULT - background-color: rgb(255, 140, 60);
@pytest.mark.select
class TestSlider(BaseTest):
    @pytest.mark.slider
    @pytest.mark.parametrize("x, y", [(-100, "rgba(170, 140, 60, 1)"), (-200, "rgba(85, 140, 60, 1)")])
    def test_slider_by_x_offset(self, x, y):
        self.navigate_to_demo_site()
        self.slider_move_to_left(x, y)
