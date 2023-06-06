from GlobalSQA.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By
from hamcrest import equal_to
from GlobalSQA.POM.lib.assertions import assert_that


class SliderPage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    first_step = (By.XPATH, "(//*[@class='price_column_title'])[1]")
    slider_btn = (By.XPATH, "//*[@href='https://www.globalsqa.com/demo-site/sliders/']")
    iframe = (By.XPATH, "(//iframe[@class='demo-frame lazyloaded'])[1]")
    slider_element = (By.XPATH, "(//*[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
    color = (By.ID, "swatch")

    def slider_red_color_move(self, x_offset, colour_number):
        self.scroll_to(self.find(self.first_step))
        self.actions.click(self.find(self.slider_btn)).perform()
        self.wait.until(self.switch_to_iframe(self.iframe))
        self.actions.click_and_hold(self.find(self.slider_element)).move_by_offset(x_offset, 0).release().perform()
        actual_result = self.find(self.color).value_of_css_property('background-color')
        assert_that(actual_result, equal_to(colour_number))
