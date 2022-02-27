from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")

driver.get("https://www.zomato.com/bangalore/restaurants?utm_source=google&utm_medium=cpc&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-PanIndia&utm_term=zomato&gclid=Cj0KCQiAraSPBhDuARIsAM3Js4rgVBSASFpyVqMWyRP7yEZ7NbDYINQxW2ZwzbDQ1Xo7Tp4Twm92dJgaAjtVEALw_wcB")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/header[1]/nav[1]/ul[2]/li[2]/a[1]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[1]/div[2]/section[2]/section[1]/div[1]/div[1]/input[1]").send_keys("9123456782")
time.sleep(4)
driver.close()

