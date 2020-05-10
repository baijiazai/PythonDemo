import os

import pytesseract
from PIL import Image

OPEN_DIR = '原图/'


def img_to_str(path):
    img = Image.open(path)
    # 图片灰度
    img = img.convert('L')
    # 图片黑白转换，使图片黑白分明
    data = img.load()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            data[i, j] = 255 if data[i, j] > 127 else 0
    # 图片转字符串
    return pytesseract.image_to_string(img)


if __name__ == '__main__':
    for root, dirs, files in os.walk(OPEN_DIR):
        for file in files:
            if file.split('.')[-1] in ['png', 'jpg', 'jpeg', 'svg', 'gif']:
                result = img_to_str(OPEN_DIR + file)
                print(result)
