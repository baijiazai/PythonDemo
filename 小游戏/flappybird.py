import pygame
import random

W = 800
H = 600
size = (W, H)


class Bird:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.radius = 15
        self.color = (255, 0, 0)

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def fly(self):
        if self.y >= self.radius * 2:
            self.y -= 10

    def fall(self):
        if self.y <= H - self.radius:
            self.y += 3

    def crash(self, obj):
        l1_gt_r2 = self.x - self.radius > obj.left + obj.width
        r1_lt_l2 = self.x + self.radius < obj.left
        t1_gt_b2 = self.y - self.radius > obj.top + obj.height
        b1_lt_t2 = self.y + self.radius < obj.top + obj.height + 100
        return not (l1_gt_r2 or r1_lt_l2 or (t1_gt_b2 and b1_lt_t2))


class Block:
    def __init__(self, id):
        self.id = id
        self.width = 70
        self.height = 400
        self.left = W
        self.top = -(random.randint(0, 200) + 100)
        self.color = (0, 255, 0)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.left, self.top, self.width, self.height))
        pygame.draw.rect(window, self.color, (self.left, self.top + self.height + 100, self.width, self.height))

    def move(self):
        self.left -= 5


pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption('flappybird')
clock = pygame.time.Clock()

bird = Bird()
block_id = 0
blocks = [Block(block_id)]
create_block_time = 0
mark = 0
same = None
run = True
while run:
    pygame.draw.rect(window, (255, 255, 255), (0, 0, W, H))

    bird.draw()
    bird.fall()

    for block in blocks:
        block.draw()
        block.move()
        if bird.crash(block):
            run = False
            print('mark :', mark)
        if block.left - bird.radius <= bird.x <= block.left + block.width + bird.radius:
            if same != block.id:
                same = block.id
                mark += 1
        if block.left + block.width <= -(W / 2):
            blocks.remove(block)

    create_block_time += 1
    if create_block_time >= 30 * 2.5:
        create_block_time = 0
        block_id += 1
        blocks.append(Block(block_id))

    if pygame.mouse.get_pressed()[0]:
        bird.fly()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(30)
