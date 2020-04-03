import os
import time
import requests
from lxml import etree


def fetch(url):
    res = requests.get(url)
    res.encoding = 'gbk'
    return res.text


if __name__ == '__main__':
    # 小说目录
    # book_url = 'http://www.quanshuwang.com/book/9/9055'
    book_url = input('请输入要下载的小说网址：')
    start_url = fetch(book_url)
    html = etree.HTML(start_url)
    book_title = html.xpath('//div[@class="chapName"]/strong/text()')[0]
    # 初始化下载文件目录
    book_dir = os.path.join(os.curdir, book_title)
    if not os.path.isdir(book_dir):
        os.mkdir(book_dir)
    # 小说章节标题和链接
    chapter_title = html.xpath('//div[@class="clearfix dirconone"]/li/a/text()')
    charter_href = html.xpath('//div[@class="clearfix dirconone"]/li/a/@href')
    for i in range(len(chapter_title)):
        chapter_url = fetch(charter_href[i])
        chapter_html = etree.HTML(chapter_url)
        print(chapter_title[i])
        content = chapter_html.xpath('//div[@id="content"]/text()')
        filepath = book_dir + '/' + str(i) + chapter_title[i] + '.txt'
        with open(filepath, 'w', encoding='utf-8') as f:
            for c in content:
                f.write(c)
    print('下载完毕！')
