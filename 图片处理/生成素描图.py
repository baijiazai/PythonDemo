import os

from PIL import Image, ImageFilter, ImageOps


def dodge(a, b, alpha):
    return min(int(a * 255 / (256 - b * alpha)), 255)


def draw(filename, save_dir, img, blur=25, alpha=1.0):
    img1 = img.convert('L')  # 图片转换成灰色
    img2 = img1.copy()
    img2 = ImageOps.invert(img2)
    for i in range(blur):  # 模糊度
        img2 = img2.filter(ImageFilter.BLUR)
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), dodge(a, b, alpha))
    # img1.show()
    img1.save('%s/%s' % (save_dir, filename))
    print('%s/%s' % (save_dir, filename))


def draw_images(open_dir, save_dir):
    for root, dirs, files in os.walk(open_dir):
        for file in files:
            if file.split('.')[-1] in ['png', 'jpg', 'jpeg', 'svg']:
                img = Image.open('%s/%s' % (open_dir, file))
                draw(file, save_dir, img)
                
                
draw_images('原图', '素描图')
