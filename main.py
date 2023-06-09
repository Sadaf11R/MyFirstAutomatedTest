from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os

chrome_option = Options()
chrome_option.add_argument("--incognito")

# driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_option)

driver.get("https://www.google.com")
print(driver.title)
# sleep(2)
# driver.get("https://www.wikipedia.com")
# window_title = driver.title
# print(window_title)
# sleep(2)
# driver.back()
# sleep(3)
# driver.forward()
sleep(2)
driver.switch_to.new_window('window')
driver.get("https://www.wikipedia.com")
print(driver.title)
# driver.refresh()
# sleep(1)
# Wikipedia_handle = driver.current_window_handle
# print('Wikipedia_handle' + str(Wikipedia_handle))
# sleep(1)
# driver.switch_to.window(driver.window_handles[0])
# sleep(2)
driver.maximize_window()
sleep(1)
# Current_path = Path(__file__).parent
# file_name = os.path.join(str(Current_path), 'Session.png')
# driver.save_screenshot(file_name)
# sleep(2)
driver.quit()
