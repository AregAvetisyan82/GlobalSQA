from GlobalSQA.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class DatePickerPage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    iframe = (By.XPATH, "(//iframe[@class='demo-frame lazyloaded'])[1]")
    date_picker = (By.ID, "datepicker")

    def select_date(self, date):
        self.wait.until(self.switch_to_iframe(self.iframe))
        self.find_and_send_keys(self.date_picker, date)
