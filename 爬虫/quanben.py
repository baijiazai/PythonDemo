import os
import requests
from lxml import etree


def fetch(url, header):
    html = requests.get(url, headers=header, timeout=10)
    # html.encoding = 'utf-8'
    return html.text


def download_chapter(filename, content):
    with open(filename, 'w', encoding='utf-8') as fp:
        for c in content:
            fp.write(c + '\n')


if __name__ == '__main__':
    user_header = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3941.4Safari / 537.36'
    }
    home_url = 'https://www.quanben.net'
    book_url = home_url + '/2/2719/'

    html = etree.HTML(fetch(book_url, user_header))
    book_title = html.xpath('//div[@class="btitle"]/h1/text()')[0]

    book_dir = os.path.join(os.curdir, book_title)
    if not os.path.isdir(book_dir):
        os.mkdir(book_dir)

    chapter_title = html.xpath('//div[@id="main"]//dd/a/text()')
    chapter_href = html.xpath('//div[@id="main"]//dd/a/@href')
    for ct, ch in zip(chapter_title, chapter_href):
        filepath = book_dir + '/' + ct + '.txt'
        if os.path.exists(filepath):
            continue
        else:
            while True:
                try:
                    chapter_html = etree.HTML(fetch(home_url + ch, user_header))
                    chapter_content = chapter_html.xpath('//div[@id="BookText"]/text()')

                    download_chapter(filepath, chapter_content)
                    print(ct, home_url + ch)
                    break
                except Exception as e:
                    print(e)
    print('下载完毕！')
