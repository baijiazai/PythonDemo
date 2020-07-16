import random
import string

import pygame

PANEL_WIDTH = 400
PANEL_HEIGHT = 500
FONT_PX = 15

def rain(content):
    pygame.init()
    # 创建一个窗口
    win_sur = pygame.display.set_mode((PANEL_WIDTH, PANEL_HEIGHT))
    font = pygame.font.SysFont('fangsong', 20)
    bg_suface = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT), flags=pygame.SRCALPHA)
    pygame.Surface.convert(bg_suface)
    bg_suface.fill(pygame.Color(0, 0, 0, 13))
    win_sur.fill((0, 0, 0))
    # 文本
    texts = [font.render(str(content[i]), True, (0, 255, 0)) for i in range(10)]
    # 按窗口的宽度来计算可以在画板上放几列坐标并生成一个列表
    colums = int(PANEL_WIDTH / FONT_PX)
    drops = [0 for i in range(colums)]
    while True:
        # 从列表中获取事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                chang = pygame.key.get_pressed()
                if chang[32]:
                    exit()
        # 暂停给定的毫秒数
        pygame.time.delay(30)
        # 重新编辑图像
        win_sur.blit(bg_suface, (0, 0))
        for i in range(len(drops)):
            text = random.choice(texts)
            # 重新编辑每一个坐标点的图像
            win_sur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
            drops[i] += 1
            if drops[i] * 10 > 600 or random.random() > 0.95:
                drops[i] = 0
        pygame.display.flip()
        

if __name__ == '__main__':
    rain([str(i) for i in range(10)])
    # rain(string.ascii_lowercase)