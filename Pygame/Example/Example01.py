# -*- coding: utf-8 -*-

import pygame
import random
import math
import matplotlib
 
matplotlib.use("Agg")
 
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
aVelocity = []
bVelocity = []
 
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
 
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        self.rect.x += self.change_x
 
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
 
 
class ABlock(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
 
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
 
def plot(a, b) :
    ax.plot(a, b)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    return pygame.image.fromstring(raw_data, size, "RGB")
 
fig = plt.figure(figsize=[5,5])
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)
 
 
pygame.init()
screen_width = 920
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
block_list = pygame.sprite.Group()
 
for i in range(5):
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randrange(500)
    block.rect.y = random.randrange(screen_height)
    block.change_x = random.randrange(-7, 5)
    block.change_y = random.randrange(-7, 5)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = 500
    block.bottom_boundary = screen_height
    block_list.add(block)
 
for i in range(5):
    ablock = ABlock(RED, 20, 15)
    ablock.rect.x = random.randrange(500)
    ablock.rect.y = random.randrange(screen_height)
    ablock.change_x = random.randrange(-1, 1)
    ablock.change_y = random.randrange(-1, 1)
    ablock.left_boundary = 0
    ablock.top_boundary = 0
    ablock.right_boundary = 500
    ablock.bottom_boundary = screen_height
    block_list.add(ablock)
 
done = False
clock = pygame.time.Clock()
score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)
 
    block_list.update()
 
    for block in block_list:
        block_list.remove(block)
        if pygame.sprite.spritecollide(block, block_list, False):
            av = math.sqrt(math.pow(block.change_x, 2) + math.pow(block.change_y, 2))
            bv = math.sqrt(math.pow(ablock.change_x, 2) + math.pow(ablock.change_y, 2))
            aVelocity.append(av)
            bVelocity.append(bv)
 
            temp_x = ablock.change_x
            ablock.change_x = block.change_x
            block.change_x = temp_x
            temp_y = ablock.change_y
            ablock.change_y = block.change_y
            block.change_y = temp_y
 
        block_list.add(ablock)
        block_list.add(block)
 
    surf = plot(aVelocity, bVelocity)
    plt.pause(0.05)
    screen.blit(surf, (520,0))
 
    block_list.update()
    block_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()

