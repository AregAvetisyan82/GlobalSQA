from GlobalSQA.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    testers_hub_link = (By.XPATH, "(//*[@href='https://www.globalsqa.com/testers-hub/'])[1]")
    demo_testing_hub_link = (By.XPATH, "(//*[@href='https://www.globalsqa.com/demo-site/'])[1]")
    tooltip_link = (By.XPATH, "(//*[@href='https://www.globalsqa.com/demo-site/tooltip/'])[1]")
    date_picker_link = (By.ID, "menu-item-2827")
    dropdown_menu_link = (By.ID, "menu-item-2825")
    bottom_iframe = (By.XPATH, "//*[@class='down']")

    def navigate_to_demo_testing_site(self):
        self.focus_on_element(self.find(self.testers_hub_link))
        self.find_and_click(self.demo_testing_hub_link)

    def navigate_to_link_tooltip(self):
        self.focus_on_element(self.find(self.testers_hub_link))
        self.focus_on_element(self.find(self.demo_testing_hub_link))
        self.find_and_click(self.tooltip_link)

    def navigate_to_link_date_picker(self):
        self.focus_on_element(self.find(self.testers_hub_link))
        self.focus_on_element(self.find(self.demo_testing_hub_link))
        self.find_and_click(self.date_picker_link)

    def navigate_to_link_dropdown_menu(self):
        self.focus_on_element(self.find(self.testers_hub_link))
        self.focus_on_element(self.find(self.demo_testing_hub_link))
        self.find_and_click(self.dropdown_menu_link)
