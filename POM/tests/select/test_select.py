import pytest
from GlobalSQA.POM.tests.select.baseTest import BaseTest


@pytest.mark.select
class TestSelect(BaseTest):
    @pytest.mark.index
    @pytest.mark.parametrize("index", [3, 4, 5])
    def test_select_by_index(self, index):
        self.navigate_to_dropdown_menu_from_home()
        self.select_country_by_index(index=index)

    @pytest.mark.text1
    @pytest.mark.parametrize("text", ["Armenia", "Aruba", "Belgium"])
    def test_select_by_text(self, text):
        self.navigate_to_dropdown_menu_from_home()
        self.select_country_by_text(text=text)

    @pytest.mark.value
    @pytest.mark.parametrize("value", ["BEN", "BMU", "BTN"])
    def test_select_by_value(self, value):
        self.navigate_to_dropdown_menu_from_home()
        self.select_country_by_value(value=value)