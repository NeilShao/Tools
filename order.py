# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time


BrowserObj_dirver = webdriver.Chrome("D:\\SBD\\tool\\chromedriver.exe")

BrowserObj_dirver.get("http://10.206.131.12/media/page/index.html")

Login_element = BrowserObj_dirver.find_element_by_id('user-pick-identity')
Login_element.send_keys("Baodong Shao")
Login_element.send_keys(Keys.RETURN)

time.sleep(1)

Add_element = BrowserObj_dirver.find_element_by_xpath('//*[@id="food_evening"]/div/div[3]/input')
Add_element.clear()
Add_element.send_keys('1')
Add_element.send_keys(Keys.RETURN)

Button_element = BrowserObj_dirver.find_element_by_id('place_order')
#Button_element.send_keys(Keys.RETURN)
time.sleep(1)
try:
    alert = BrowserObj_dirver.switch_to_alert()
    alert.dismiss()
except:
    pass