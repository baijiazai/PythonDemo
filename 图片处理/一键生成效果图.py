import os

from PIL import Image, ImageFilter, ImageOps

OPEN_DIR = '原图/'

BLUR_DIR = '模糊/'
CONTOUR_DIR = '轮廓/'
DETAIL_DIR = '细节增强/'
EDGE_ENHANCE_DIR = '边缘增强/'
EDGE_ENHANCE_MORE_DIR = '深度边缘增强/'
EMBOSS_DIR = '浮雕/'
FIND_EDGES_DIR = '边缘查找/'
SMOOTH_DIR = '平滑/'
SMOOTH_MORE_DIR = '深度平滑/'
SHARPEN_DIR = '锐化/'

SKETCH_DIR = '素描/'

TIPS = """
0: 生成所有效果图
1: 模糊滤镜，会使图片较原先的模糊一些。
2: 轮廓滤波，将图像中的轮廓信息提取出来
3: 细节增强滤波，它会显化图片中细节。
4: 边缘增强滤波，突出、加强和改善图像中不同灰度区域之间的边界和轮廓的图像增强方法。
5: 深度边缘增强滤波，会使得图像中边缘部分更加明显。
6: 浮雕滤波，会使图像呈现出浮雕效果。
7: 边缘查找，寻找边缘信息的滤波，会找出图像中的边缘信息。
8: 平滑滤波，突出图像的宽大区域、低频成分、主干部分或抑制图像噪声和干扰高频成分，使图像亮度平缓渐变，减小突变梯度，改善图像质量。
9: 深度平滑滤波，会使得图像变得更加平滑。
10: 锐化滤波，补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰。
11: 素描
"""


# 生成滤镜效果
def image_filter(filename, open_dir, save_dir, filter):
    img = Image.open(open_dir + filename)
    img_out = img.filter(filter)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    img_out.save(save_dir + filename)
    print(save_dir + filename)


def dodge(a, b, alpha):
    return min(int(a * 255 / (256 - b * alpha)), 255)


# 生成素描图
def sketch(filename, open_dir, save_dir, blur=25, alpha=1.0):
    img = Image.open(open_dir + filename)
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
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    img1.save(save_dir + filename)
    print(save_dir + filename)


# 主方法
def generate():
    print(TIPS)
    action = int(input('输入你需要生成效果图的编号：'))

    for root, dirs, files in os.walk(OPEN_DIR):
        for file in files:
            if file.split('.')[-1] in ['png', 'jpg', 'jpeg', 'svg']:
                img = Image.open(OPEN_DIR + file)
                if action == 0:
                    image_filter(file, OPEN_DIR, BLUR_DIR, ImageFilter.BLUR)
                    image_filter(file, OPEN_DIR, CONTOUR_DIR, ImageFilter.CONTOUR)
                    image_filter(file, OPEN_DIR, DETAIL_DIR, ImageFilter.DETAIL)
                    image_filter(file, OPEN_DIR, EDGE_ENHANCE_DIR, ImageFilter.EDGE_ENHANCE)
                    image_filter(file, OPEN_DIR, EDGE_ENHANCE_MORE_DIR, ImageFilter.EDGE_ENHANCE_MORE)
                    image_filter(file, OPEN_DIR, EMBOSS_DIR, ImageFilter.EMBOSS)
                    image_filter(file, OPEN_DIR, FIND_EDGES_DIR, ImageFilter.FIND_EDGES)
                    image_filter(file, OPEN_DIR, SMOOTH_DIR, ImageFilter.SMOOTH)
                    image_filter(file, OPEN_DIR, SMOOTH_MORE_DIR, ImageFilter.SMOOTH_MORE)
                    image_filter(file, OPEN_DIR, SHARPEN_DIR, ImageFilter.SHARPEN)
                    sketch(file, OPEN_DIR, SKETCH_DIR)
                elif action == 1:
                    image_filter(file, OPEN_DIR, BLUR_DIR, ImageFilter.BLUR)
                elif action == 2:
                    image_filter(file, OPEN_DIR, CONTOUR_DIR, ImageFilter.CONTOUR)
                elif action == 3:
                    image_filter(file, OPEN_DIR, DETAIL_DIR, ImageFilter.DETAIL)
                elif action == 4:
                    image_filter(file, OPEN_DIR, EDGE_ENHANCE_DIR, ImageFilter.EDGE_ENHANCE)
                elif action == 5:
                    image_filter(file, OPEN_DIR, EDGE_ENHANCE_MORE_DIR, ImageFilter.EDGE_ENHANCE_MORE)
                elif action == 6:
                    image_filter(file, OPEN_DIR, EMBOSS_DIR, ImageFilter.EMBOSS)
                elif action == 7:
                    image_filter(file, OPEN_DIR, FIND_EDGES_DIR, ImageFilter.FIND_EDGES)
                elif action == 8:
                    image_filter(file, OPEN_DIR, SMOOTH_DIR, ImageFilter.SMOOTH)
                elif action == 9:
                    image_filter(file, OPEN_DIR, SMOOTH_MORE_DIR, ImageFilter.SMOOTH_MORE)
                elif action == 10:
                    image_filter(file, OPEN_DIR, SHARPEN_DIR, ImageFilter.SHARPEN)
                elif action == 11:
                    sketch(file, OPEN_DIR, SKETCH_DIR)


if __name__ == '__main__':
    generate()
    print('所有图片处理完毕！')
