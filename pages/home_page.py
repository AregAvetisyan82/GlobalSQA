from selenium.webdriver.common.by import By
from lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    shoes_btn = (By.XPATH, "//*[@href='/shoes']")

    def click_on_shoes_btn(self):
        self.find_and_click(self.shoes_btn)


