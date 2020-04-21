from PIL import Image

img = Image.open('小程序图标.png')
bg = Image.new(mode='RGBA' ,size=(200, 200), color=(255, 255, 255, 0))

img2 = img.resize((144, 144))
bg.paste(img2, (28, 28))

bg.save('out.png')