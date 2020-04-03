from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

kw = driver.find_element_by_id('kw')
kw.send_keys('python')

su = driver.find_element_by_id('su')
su.click()
