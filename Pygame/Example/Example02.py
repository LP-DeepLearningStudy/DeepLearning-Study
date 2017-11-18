# -*- coding: utf-8 -*-

import pygame
import random
import math
 
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

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

pygame.init()
 
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()
 
for i in range(10) :
    block = Block(BLACK, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block.change_x = random.randrange(-3,3)
    block.change_y = random.randrange(-3,3)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = screen_width
    block.bottom_boundary = screen_height
    block_list.add(block)

for i in range(10) :
    ablock = ABlock(RED, 20, 15)
    ablock.rect.x = random.randrange(screen_width)
    ablock.rect.y = random.randrange(screen_height)
    ablock.change_x = random.randrange(-1,1)
    ablock.change_y = random.randrange(-1,1)
    ablock.left_boundary = 0
    ablock.top_boundary = 0
    ablock.right_boundary = screen_width
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
            av = math.sqrt(math.pow(block.change_x,2)+ math.pow(block.change_y,2))
            bv = math.sqrt(math.pow(ablock.change_x,2)+ math.pow(ablock.change_y,2))
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
        
            
    block_list.update()
    block_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()
