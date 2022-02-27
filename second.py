from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")

driver.get("https://www.flipkart.com/")
driver.find_element(By.CSS_SELECTOR,"input[class='_2IX_2- VJZDxU']").send_keys("8123011653")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Udaya@1993")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
driver.find_element(By.XPATH,"//div[2]//div[1]//a[1]//div[1]//img[2]").click()
#driver.find_element(By.CSS_SELECTOR,"._14Me7y").click()
#driver.find_element(By.XPATH,"//input[@class='_2IX_2- VJZDxU']").send_keys("8234567890")
#driver.find_element(By.CSS_SELECTOR,"button[type='submit'] span").click()
driver.close()