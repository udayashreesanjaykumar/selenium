from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
#driver.find_element(By.XPATH,"//span[normalize-space()='Create account']").click()
#driver.find_element(By.XPATH,"(//li[@role='menuitem'])[1]").click()
driver.maximize_window()
time.sleep(4)
#driver.minimize_window()
driver.quit()
#driver.close()


