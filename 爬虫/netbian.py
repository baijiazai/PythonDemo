# 彼岸网爬虫 v1.0.2
import os
import requests
from lxml import etree


def fetch(url, header):
    html = requests.get(url, headers=header, timeout=10)
    html.encoding = 'gbk'
    return html.text


def download_img(filename, content):
    with open(filename, 'wb') as fp:
        fp.write(content)


if __name__ == '__main__':
    user_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36'
    }
    home_url = 'http://pic.netbian.com'
    class_url = home_url + '/4kdongman'

    class_html = etree.HTML(fetch(class_url, user_header))
    class_title = class_html.xpath('//div[@class="loaction"]//h1/text()')[0]
    # 初始化图片下载目录
    img_dir = 'D:/电脑壁纸/' + class_title
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)

    page = int(input('请输入要下载的页数：'))
    # 翻页
    for i in range(page):
        if i == 0:
            page_url = class_url
        else:
            page_url = class_url + '/index_%d.html' % (i + 1)
        while True:
            try:
                page_html = etree.HTML(fetch(page_url,user_header))
                break
            except Exception as e:
                print(e)
        # 获取每张缩略图的 href 和 title
        img_list = page_html.xpath('//div[@class="slist"]/ul/li/a/@href')
        img_tits = page_html.xpath('//div[@class="slist"]/ul/li/a/b/text()')
        for img_href, img_tit in zip(img_list, img_tits):
            # 如果文件存在就跳过
            filepath = img_dir + '/' + img_tit + '.jpg'
            if os.path.exists(filepath):
                continue
            else:
                # 超时重试
                while True:
                    try:
                        # 获取大图的 src
                        img_html = etree.HTML(fetch(home_url + img_href, user_header))
                        img_src = img_html.xpath('//a[@id="img"]/img/@src')[0]
                        img = requests.get(home_url + img_src).content
                        # 下载图片
                        download_img(filepath, img)
                        print(img_tit, home_url + img_src)
                        break
                    except Exception as e:
                        print(e)
        print('第%d页下载完成。' % (i + 1))
    print('全部下载完毕！')