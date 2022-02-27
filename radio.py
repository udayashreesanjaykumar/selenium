
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"label[for='gender-radio-1']").click()
WebElement var=driver.find_element(By.CSS_SELECTOR,"label[for='gender-radio-1']").is_selected()
print(var)
time.sleep(4)
driver.close()
