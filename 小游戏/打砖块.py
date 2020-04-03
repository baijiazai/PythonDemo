import pygame
import random

W = 800
H = 600
size = (W, H)


class Ball:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.radius = 10
        self.color = (255, 0, 0)
        self.speed_x = 5
        self.speed_y = 5

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= W:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= H:
            self.speed_y = -self.speed_y
        self.x += self.speed_x
        self.y += self.speed_y

    def crash(self, obj):
        l1_gt_r2 = self.x - self.radius > obj.left + obj.width
        r1_lt_l2 = self.x + self.radius < obj.left
        t1_gt_b2 = self.y - self.radius > obj.top + obj.height
        b1_lt_t2 = self.y + self.radius < obj.top
        return not (l1_gt_r2 or r1_lt_l2 or t1_gt_b2 or b1_lt_t2)


class Bat:
    def __init__(self):
        self.width = 100
        self.height = 30
        self.left = (W - self.width) / 2
        self.top = (H - self.height) - 20
        self.color = (0, 0, 255)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.left, self.top, self.width, self.height))

    def move(self):
        self.left = pygame.mouse.get_pos()[0] - self.width / 2
        if self.left <= 0:
            self.left = 0
        elif self.left >= W - self.width:
            self.left = W - self.width


class Brick:
    def __init__(self, left, top):
        self.left = left
        self.top = top
        self.width = 78
        self.height = 28
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.rect(window, self.color, (self.left, self.top, self.width, self.height))


def create_brick(row, col):
    arr = []
    for r in range(row):
        for c in range(col):
            arr.append(Brick(c * 80, r * 30))
    return arr


pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption('打砖块')
clock = pygame.time.Clock()

ball = Ball()
bat = Bat()
bricks = create_brick(5, 10)

run = True
while run:
    pygame.draw.rect(window, (255, 255, 255), (0, 0, W, H))

    ball.draw()
    bat.draw()
    for brick in bricks:
        brick.draw()
        if ball.crash(brick):
            bricks.remove(brick)
            ball.speed_y = -ball.speed_y

    ball.move()
    bat.move()

    if ball.crash(bat):
        ball.speed_y = -ball.speed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)
