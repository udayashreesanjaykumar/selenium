from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.myntra.com/")
text=driver.find_element(By.XPATH,"(//div[@class='desktop-navLink'])[4]").text
print(text)
#text1=driver.find_elements(By.CSS_SELECTOR,".desktop-main[href='/shop/women']").text1
#print(text1)
driver.close()