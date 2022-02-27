from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.facebook.com/r.php?locale=en_GB&display=page")
driver.maximize_window()
dropdown=driver.find_element(By.ID,"month")
dd=Select(dropdown)
dd.select_by_value("4")
time.sleep(3)
dd.select_by_visible_text("Aug")
time.sleep(4)
dd.select_by_index(6)
time.sleep(3)
driver.quit()