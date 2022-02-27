from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.ajio.com/c/83?query=%3Arelevance%3Adiscount%3A51-80%25&gridColumns=3&gclid=Cj0KCQiA3fiPBhCCARIsAFQ8QzV68jdxrYFkyR9RXK42gdlpxst4BeOV0JiSmVbCKXmNEjK5G5iwrowaAm0SEALw_wcB")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"label[for='Women']").click()
driver.find_element(By.CSS_SELECTOR,"label[for='Women']").click()
#driver.find_element(By.CSS_SELECTOR,"label[for='Women']").is_selected()
var=driver.find_element(By.CSS_SELECTOR,"label[for='Women']").is_selected()
print(var)
time.sleep(3)
driver.close()
