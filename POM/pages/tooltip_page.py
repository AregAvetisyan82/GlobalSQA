from GlobalSQA.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By
from hamcrest import equal_to
from GlobalSQA.POM.lib.assertions import assert_that


class TooltipPage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    iframe = (By.XPATH, "(//iframe[@class='demo-frame lazyloaded'])[1]")
    st_stephens_image = (By.XPATH, "//img[@src='images/st-stephens.jpg']")
    vienna_austria_txt = (By.XPATH, "//*[@href='https://maps.google.com/maps?q=vienna,+austria&z=11']")
    inner_txt = (By.XPATH, "//*[@href='http://creativecommons.org/licenses/by-sa/3.0/deed.en']")
    tooltip = (By.XPATH, "//*[@class='ui-tooltip-content']")

    def hover_on_image(self, expected_result):
        self.wait.until(self.switch_to_iframe(self.iframe))
        element = self.find(self.st_stephens_image)
        self.scroll_to(element)
        self.focus_on_element(element)
        actual_result = self.find(self.tooltip, get_text=True)
        assert_that(actual_result, equal_to(expected_result))

    def hover_on_text(self, expected_result):
        self.wait.until(self.switch_to_iframe(self.iframe))
        element = self.find(self.vienna_austria_txt)
        self.focus_on_element(element)
        actual_result = self.find(self.tooltip, get_text=True)
        assert_that(actual_result, equal_to(expected_result))

    def hover_on_inner_text(self, expected_result):
        self.wait.until(self.switch_to_iframe(self.iframe))
        element = self.find(self.inner_txt)
        self.focus_on_element(element)
        actual_result = self.find(self.tooltip, get_text=True)
        assert_that(actual_result, equal_to(expected_result))
