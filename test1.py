import time
from selenium import webdriver


test = webdriver.Firefox()

test.get("http://172.28.31.50/mall/login/index")
test.find_element_by_id('names').clear()
test.find_element_by_id('names').send_keys('xinyi')
test.find_element_by_id('password').clear()
test.find_element_by_id('password').send_keys('123456')
test.find_element_by_id('vaildCode').clear()
temp=input(':请输入验证码')
time.sleep(5)
test.find_element_by_id('vaildCode').send_keys(temp)
