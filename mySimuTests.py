#import unittest
import os
#import random
#import string

from appium import webdriver
#from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import urllib2
#import json

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



desired_caps = { }
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.2' #10.2 for simu
desired_caps['deviceName'] = 'iPhone 6' #iPhone 7 for simu
#desired_caps['app'] = '//Users//hcltech//Desktop//SafariLauncher//SafariLauncher.ipa'
desired_caps['app'] = '/Users/hcltech/Desktop/SafariLauncher/SafariLauncher.app'   #for Simulator
desired_caps['automationName'] = 'XCUITest'  #reqd for xCode version > 8 
#desired_caps['updatedWDABundleId'] = 'amc1.bundle'
desired_caps['bundleId'] = 'amc1.bundle'
#desired_caps['safariInitialUrl'] = 'www.google.com'  #only works with simu
desired_caps['newCommandTimeout'] = 600



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 
sleep(2)

#Exception handling for unnecessary Popup on Google.com on iPhone
try :
	sleep(4)
	No = driver.find_element_by_name('NO THANKS')
	No.click()
	sleep(2)
except NoSuchElementException : 
	print "No extra pop-ups appeared. Proceeding with test "
	pass	

#To search for Search Bar
try :
	sleep(2)
	first_element = driver.find_element_by_name('Search')
	#first_element = driver.find_element_by_id("lst-ib")
	#first_element = driver.find_element_by_xpath('//*[@id="lst-ib"]')
	#first_element = driver.find_element_by_name('q')
except NoSuchElementException :
	print "Search failed..trying again"
	sleep(6)
	first_element = driver.find_element_by_name('Search')

#Entering Search String and pressing Enter key
first_element.send_keys("Hello")
first_element.send_keys(Keys.RETURN) # hit return after you enter search text
sleep(2)
