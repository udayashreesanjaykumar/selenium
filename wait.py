from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.implicitly_wait(4)
driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("udaya")
driver.close()