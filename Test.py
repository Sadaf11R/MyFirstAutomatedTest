from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

base_url = "https://play1.automationcamp.ir"
service = Service(executable_path="C:\chromedriver")
driver = webdriver.Chrome(service=service)
# driver.get("https://www.google.com")
# search_field = driver.find_element('name', 'q')
# search_field.send_keys("Hello world!")
# search_field.send_keys(Keys.RETURN)

# driver.find_element('name', 'q').send_keys("hello")
# driver.find_element('name', 'q').send_keys(Keys.RETURN)

driver.get(f"{base_url}/forms.html")
driver.find_element('id', 'check_python').click()
check1 = driver.find_element('id', 'check_validate').text
assert check1 == 'PYTHON'
driver.find_element('id', 'notes').send_keys("Hello world!!!")
check2 = driver.find_element('id', 'area_notes_validate').text
assert check2 == "Hello world!!!"

sleep(2)
driver.quit()
