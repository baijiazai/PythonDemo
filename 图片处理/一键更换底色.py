import os

from PIL import Image
from removebg import RemoveBg

# API KEY获取官方网站：https://www.remove.bg/zh/api
API_KEY = ''
OPEN_DIR = '原图/'
SAVE_DIR = '证件照/'


# 给去除了背景的图像添加背景颜色
def change_img_bg(img, size, color, save_dir):
    try:
        # 填充红色背景255，0，0  白色是255，255，255
        bg = Image.new('RGBA', size, color)
        bg.paste(img, (0, 0, size[0], size[1]), img)
        # 保存填充后的图片
        bg.save(save_dir)
    except:
        print('图片底色更换失败')


def generate_no_bg(filename, save_dir):
    remove_bg = RemoveBg(API_KEY, "error.log")  # API密钥
    remove_bg.remove_background_from_img_file(OPEN_DIR + filename)  # 输入图片，jpg格式，试过bmp未成功
    # 输入已经去除背景的图像
    filename = filename[:filename.rfind('.')]
    img_no_bg = Image.open(OPEN_DIR + filename + '.jpg_no_bg.png')
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    change_img_bg(img_no_bg, img_no_bg.size, (255, 255, 255), save_dir + filename + '_白.png')
    change_img_bg(img_no_bg, img_no_bg.size, (255, 0, 0), save_dir + filename + '_红.png')
    change_img_bg(img_no_bg, img_no_bg.size, (0, 0, 255), save_dir + filename + '_蓝.png')


def generate():
    for root, dirs, files in os.walk(OPEN_DIR):
        for file in files:
            if file.split('.')[-1] in ['png', 'jpg', 'jpeg', 'svg']:
                generate_no_bg(file, SAVE_DIR)


if __name__ == '__main__':
    generate()
    print('图片底色更换完毕')
