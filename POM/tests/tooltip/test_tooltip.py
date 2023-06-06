import pytest
from GlobalSQA.POM.tests.tooltip.baseTest import BaseTest
from GlobalSQA.TestingData.test_data import text_expected, text_expected1


@pytest.mark.tooltip
class TestTooltip(BaseTest):
    @pytest.mark.image
    def test_tooltip_image(self):
        self.navigate_to_tooltip_from_home()
        self.hover_on_tooltip_image(text_expected)

    @pytest.mark.text
    def test_tooltip_text(self):
        self.navigate_to_tooltip_from_home()
        self.hover_on_tooltip_text("")

    @pytest.mark.inner
    def test_tooltip_inner_text(self):
        self.navigate_to_tooltip_from_home()
        self.hover_on_tooltip_inner_text(text_expected1)
