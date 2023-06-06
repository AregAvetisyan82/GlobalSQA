from GlobalSQA.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By
# from hamcrest import equal_to
# from GlobalSQA.POM.lib.assertions import assert_that


class SelectPage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    countries_selection = (By.XPATH, "//select")

    def select_country_index(self, index):
        self.select_item(self.countries_selection, index=index, by_index=True)

    def select_country_text(self, text):
        self.select_item(self.countries_selection, text=text, by_text=True)

    def select_country_value(self, value):
        self.select_item(self.countries_selection, value=value, by_value=True)
