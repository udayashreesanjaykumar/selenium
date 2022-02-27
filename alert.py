from selenium import webdriver
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.hyrtutorials.com/p/alertsdemo.html")
driver.maximize_window()
# to accept alert
#driver.find_element(By.ID,"confirmBox").click()
#time.sleep(2)
#driver.switch_to.frame(0)
#driver.switch_to.alert()
#driver.switch_to.alert().accept()
#time.sleep(2)
#to dismiss alert
driver.find_element(By.ID,"confirmBox").click()
time.sleep(2)
driver.switch_to.frame(0)
driver.switch_to.alert()
driver.switch_to.alert().dismiss()

#to send the values in alert
#driver.find_element(By.CSS_SELECTOR,"#promptBox").click()
#time.sleep(2)
#driver.switch_to.frame(0)
#driver.switch_to_alert()
#time.sleep(2)
#var=driver.switch_to_alert().send_keys("udaya")
#driver.switch_to.alert().accept()
#print(var.gettext())
#time.sleep(2)

#Alert(driver).accept()
#driver.switch_to_alert().send_keys("udaya")
#driver.switch_to_alert().accept()
#time.sleep(2)

