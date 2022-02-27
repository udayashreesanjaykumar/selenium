from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")

driver.get("https://www.flipkart.com/")
abc=driver.find_elements(By.TAG_NAME,'div')
print(len(abc))

driver.close()