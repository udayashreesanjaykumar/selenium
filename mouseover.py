from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.yatra.com/")
driver.maximize_window()
button=driver.find_element(By.CSS_SELECTOR,".more-arr").click()
time.sleep(3)
account=driver.find_element(By.CSS_SELECTOR,"li[id='userLoginBlock'] a[class='dropdown-toggle']").click()
achains=ActionChains(driver)
achains.move_to_element(button).perform()
achains.move_to_element(account).perform()
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#SignUpBtn").click()
time.sleep(3)
driver.quit()