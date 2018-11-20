import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



test = webdriver.Firefox()

test.get("http://172.28.31.50/mall/login/index")
# print('买家开始复制下单')
test.find_element_by_id('names').clear()
test.find_element_by_id('names').send_keys('xinyi')
test.find_element_by_id('password').clear()
test.find_element_by_id('password').send_keys('123456')
#test.find_element_by_id('vaildCode').clear()

# temp=input(':请输入验证码')
#time.sleep(5)
test.find_element_by_id('vaildCode').clear()
test.find_element_by_id('vaildCode').send_keys('1353321_LIBIN@BMSOFT.COM.CN!')
test.find_element_by_xpath('/html/body/div[7]/dl/form/dd/a').click()
#print('正在登陆')
time.sleep(3)
test.find_element_by_xpath('/html/body/div[6]/div[1]/div[3]/dl/dt[1]/a').click()
time.sleep(3)
#print('进入快捷下单界面')
# test.find_element_by_id('sailingDate')
# js = '$(\'input[id=sailingDate]\').removeAttr(\'readonly\')'
# test.execute_script(js)
#print('开始切换窗口')
print (test.current_window_handle) # 输出当前窗口句柄

handles = test.window_handles # 获取当前全部窗口句柄集合
print(handles)# 输出句柄集合


for handle in handles:# 切换窗口
    if handle != test.current_window_handle:
        print ('switch to second window',handle)
        test.close() # 关闭第一个窗口
        test.switch_to.window(handle) #切换到第二个窗口




time.sleep(3)
#期望大船开船时间
test.find_element_by_xpath("//input[@id='sailingDate']").click()
test.find_element_by_id('laydate_ok').click()
#起运港
test.find_element_by_id('select2-startPortId-container').click()
time.sleep(3)
test.find_element_by_xpath('//*[@id="select2-startPortId-results"]/li[1]').click()
#目的港
test.find_element_by_id('select2-endPortId-container').click()
test.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('ny')
time.sleep(3)
test.find_element_by_xpath('//*[@id="select2-endPortId-results"]/li[1]').click()
#船东
test.find_element_by_id('select2-blNo-container').click()
test.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('MOL')
time.sleep(3)
test.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[1]').click()
#放单方式
test.find_element_by_id('select2-actbillType-container').click()
test.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('正本')
time.sleep(3)
test.find_element_by_xpath('//*[@id="select2-actbillType-results"]/li[1]').click()
#提单类型
test.find_element_by_id('select2-ladbillType-container').click()
test.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys('船东提单')
time.sleep(3)
test.find_element_by_xpath('//*[@id="select2-ladbillType-results"]/li[1]').click()

#海运费
test.find_element_by_id('0_price').send_keys('123')
test.find_element_by_id('0_amount').clear()
test.find_element_by_id('0_amount').send_keys('1')
#付款方式
test.find_element_by_id('select2-payType-container').click()
test.find_element_by_xpath('/html/body/span[2]/span/span[1]/input').send_keys('Freight prepaid(预付)')
time.sleep(3)
test.find_element_by_xpath('/html/body/span[2]/span/span[2]/ul/li[1]').click()
#卖家



