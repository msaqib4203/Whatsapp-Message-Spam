
#This script is for education purposes only.
#Use it at your own risk...!
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
location = 'Chrome driver or any web driver location goes here'
driver =  webdriver.Chrome(location)
driver.get("http://web.whatsapp.com")
#Scan qr code on whatsapp web and open chat to be spammed
confirm = raw_input("Continue?")
input = driver.find_element_by_xpath("//div[@data-tab='1']")
c = 0;
while(1>0):
	input.send_keys(str(c))
	c = c+1
	time.sleep(1.500)
	submit = driver.find_element_by_xpath("//button[@class='icon btn-icon icon-send send-container']")
	submit.click()
