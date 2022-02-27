from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")
driver.get("https://www.snapdeal.com/search?keyword=mobile%20phone&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
driver.maximize_window()
ele1=driver.find_element(By.CSS_SELECTOR,".price-slider-scroll.left-handle.ui-slider-handle.ui-state-default.ui-corner-all.hashAdded")
ele2=driver.find_element(By.CSS_SELECTOR,".price-slider-scroll.right-handle.ui-slider-handle.ui-state-default.ui-corner-all.hashAdded")
#ActionChains(driver).drag_and_drop_by_offset(ele1,60,0).perform()
#ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(50,0).release().perform()
ActionChains(driver).move_to_element(ele1).pause(1).click_and_hold(ele1).move_by_offset(80,0).release().perform()
time.sleep(3)
driver.close()