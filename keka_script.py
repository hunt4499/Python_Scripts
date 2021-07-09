from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://app.keka.com/account/login?returnUrl=%2F")
# assert "Python" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys("USERNAME")
driver.find_element_by_class_name('login-from-btn').click();
elemNew = driver.find_element_by_id("password")
elemNew.send_keys("PASSWORD")
driver.find_element_by_class_name('login-from-btn').click();
# driver.find_element_by_class_name('btn-white').click();
time.sleep(2.7)
driver.find_element_by_css_selector('button.btn-white').click();
messages=["Hey","Good Morning","Hey there","Hi"]
time.sleep(1)
selectedMessage=messages[random.randrange(3)]
elemMessages = driver.find_element_by_name("reason")
elemMessages.send_keys(selectedMessage)
driver.find_element_by_xpath("//div[@class='modal-footer']//button[@class='btn btn-primary btn-sm']").click()

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
