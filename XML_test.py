from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.wikipedia.com")

# ID >
search_input1 = driver.find_element('id', 'searchInput')
sleep(1)
search_input1.send_keys("Hello world!")
# search_input1.send_keys(Keys.RETURN)
print(search_input1)
sleep(2)

# Absolute XPATH >
# driver.find_element('xpath', "/html/body/div[3]/input")
# sleep(2)

# Relative XPATH >
search_input2 = driver.find_element('xpath', "//input[@type='search']")
sleep(1)
search_input2.send_keys("Hello world!")
# search_input2.send_keys(Keys.RETURN)
print(search_input2)
sleep(1)
assert search_input1 == search_input2
search_input3 = driver.find_element('xpath', "//*[text()='MediaWiki']")
search_input3.click()
print(search_input3)
sleep(2)

driver.quit()
