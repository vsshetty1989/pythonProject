import re
import pytest
import time
from selenium import webdriver
import helper

inputList=list()
driver=webdriver.Chrome(executable_path='/Users/sinisasi/PycharmProjects/pythonProject/Drivers/chromedriver')
# driver.get('http://automationpractice.com/index.php')
driver.get('https://www.google.com')
driver.maximize_window()
# driver.find_element_by_xpath('//a[contains(text(),"Sign in")]').click()
time.sleep(5)
driver.find_element_by_partial_link_text('Nest').click()