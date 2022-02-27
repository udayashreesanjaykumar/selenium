from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.facebook.com/login/")
driver.maximize_window()
value=driver.find_element(By.CSS_SELECTOR,"#loginbutton")
value.screenshot(".\\test.png")
value.click()
time.sleep(2)
driver.get_screenshot_as_file("C:\\python-selenium\\error.png")
driver.save_screenshot(".\\test1.png")
driver.quit()