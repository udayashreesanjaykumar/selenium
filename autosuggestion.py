from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
value=driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
value.click()
value.send_keys("bags")
time.sleep(1)
value.send_keys(Keys.ENTER)
time.sleep(1)
driver.quit()
