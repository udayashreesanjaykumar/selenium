from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
parent_handle=driver.current_window_handle
print(parent_handle)
driver.find_element(By.CSS_SELECTOR,"img[alt='AC| Best sellers']").click()
all_handles=driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle!=parent_handle:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH,"(//div[@class='a-section aok-relative s-image-square-aspect'])[2]").click()
        time.sleep(4)
        driver.close()
        time.sleep(3)
        break
driver.switch_to.window(parent_handle)
driver.find_element(By.CSS_SELECTOR,"img[alt='AC| Best sellers']")


