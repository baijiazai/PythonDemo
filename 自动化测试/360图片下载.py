import time
import os
import sys

import requests
from PIL import Image
from selenium import webdriver

# 用户输入
keyword = input('输入搜索关键词：')
while True:
    try:
        count = int(input('下载多少张：'))
        break
    except:
        print('请输入数字')
filename = input('下载图片文件名前缀：')
while True:
    try:
        width, height = [int(i) for i in input('是否修改图片像素，是：w h，否：0 0，以空格为间隔：').split()]
        break
    except:
        print('请按照要求输入')
# 打开浏览器
driver = webdriver.Chrome()
# 请求地址
driver.get('https://image.so.com/')
driver.find_element_by_id('search_kw').send_keys(keyword)
driver.find_element_by_tag_name('form').find_element_by_tag_name('button').click()
# 浏览图片
print('正在浏览图片请稍等……')
scroll_y = 0
page = 0
while page < count // 10:
    scroll_y += 2000
    driver.execute_script("window.scrollTo(0,%d);" % scroll_y)
    page += 1
    img_count = len(driver.find_elements_by_class_name('img'))
    if img_count > count:
        break
    print(str(page) + '次')
    print(str(img_count) + '张')
    time.sleep(1)
# 图片url列表
img_url_list = [item.find_element_by_tag_name('img').get_attribute('src') for item in driver.find_elements_by_class_name('img')]
driver.close()
# 创建文件夹
filename += '_360'
if not os.path.exists(filename):
    os.mkdir(filename)
# 下载图片并修改图片像素
print('正在下载图片……')
for i in range(len(img_url_list)):
    img_name = '%s/%s_%d.jpg' % (filename, filename, i)
    try:
        response = requests.get(img_url_list[i], timeout=3)
        if response.status_code == 200:
            with open(img_name, 'wb') as fp:
                fp.write(response.content)
            if width and height:
                img = Image.open(img_name)
                new_img = img.resize((width, height), Image.BILINEAR)
                new_img.save(img_name)
            print('下载进度：%d/%d' % (i, len(img_url_list)))
    except:
        continue
print('全部下载完成')
# 删除非图片文件
for file in os.listdir(filename):
    try:
        Image.open('%s/%s' % (filename, file))
    except:
        os.remove('%s/%s' % (filename, file))
# 关闭窗口
for i in range(3):
    print('%d秒后自动关闭窗口' % (3 - i))
    time.sleep(1)
sys.exit(0)




