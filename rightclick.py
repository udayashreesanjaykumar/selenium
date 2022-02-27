from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
#right click
#achains=ActionChains(driver)
#ele=driver.find_element(By.CSS_SELECTOR,".context-menu-one.btn.btn-neutral")
#copyele=driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-copy']")
#achains.context_click(ele).perform()
#time.sleep(3)
#copyele.click()
#time.sleep(3)

#double click
achains=ActionChains(driver)
ele1=driver.find_element(By.CSS_SELECTOR,"button[ondblclick='myFunction()']")
achains.double_click(ele1).perform()
time.sleep(3)
