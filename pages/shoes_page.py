import time
from selenium.webdriver.common.by import By
from lib.helpers import Helpers
from hamcrest import equal_to
from lib.assertions import assert_that


class ShoesPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    heels_btn = (By.XPATH, "//*[@data-eventvalue='S-TOPCAT-Heels']")
    heels_count = (By.XPATH, "//*[@class='zu-z']")

    def click_on_heels_btn(self):
        self.find_and_click(self.heels_btn)

    def get_heels_count_data(self, expected_result):
        actual_result = self.find(self.heels_count, check_visibility=True, get_text=True)
        assert_that(actual_result, equal_to(expected_result))
