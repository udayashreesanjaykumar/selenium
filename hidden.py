from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
driver.maximize_window()
ele=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
print(ele)
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
ele1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
print(ele1)