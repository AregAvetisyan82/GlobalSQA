import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument("--disable-popup-blocking")
options.add_argument("--window-size=1920,1080")
options.add_argument("-- disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
prefs = {'download.default_directory': '/Users/areg.avetisyan/Downloads',
         "download.prompt_for_download": False,
         "download.directory_upgrade": True,
         "safebrowsing_for_trusted_sources_enabled": False,
         "safebrowsing.enabled": False,
         "profile.default_content_setting_values.notifications": 1, "block-new-web-contents": False}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
driver = webdriver.Chrome(options=options)
driver.execute_script("window.alert = function() {};")

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
driver.maximize_window()

driver.get("https://www.6pm.com/women-heels/CK_XARC41wHAAQHiAgMBAhg.zso?s=recentSalesStyle%2Fdesc%2F&pf_rd_p=a362bd56-bb96-4568-ae5e-0252e8ebb25e&pf_rd_r=YVFY8YTQKWGCTWQS6MAJ")

heels_count = (By.XPATH, "//*[@class='zu-z']")


def find(loc, timeout=10, get_text=False, get_attribute=False):
    elem = WebDriverWait(driver, timeout).until(ec.presence_of_element_located(loc))
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem


wait.until(ec.visibility_of_element_located(heels_count))

text = find(heels_count, get_text=True)
print(text)
print(type(text))
# time.sleep(5)
driver.quit()
