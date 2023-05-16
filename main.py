from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

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
sleep(2)
Wikipedia_handle = driver.current_window_handle
print('Wikipedia_handle' + str(Wikipedia_handle))
sleep(2)
driver.switch_to.window(driver.window_handles[0])
sleep(2)

# driver.find_element('name', 'q').send_keys("wikipedia")
# sleep(5)
# driver.find_element('name', 'q').send_keys(Keys.RETURN)
# sleep(5)
driver.quit()
