# -*- coding: utf-8 -*-

"""
squenceStyle.py - 절차지향으로 작성한 파이게임 기본실행 
작성일 : 2017-11-07
작성자 : 김건우
"""

import pygame

pygame.init()                               # 파이게임 초기화 
screen_width = 920                          # 화면 가로 길이
screen_height = 400                         # 화면 세로 길이 
screen = pygame.display.set_mode([screen_width, screen_height])

done = False                                # 게임 플레이 변수

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill( (255,255,255) )
    pygame.display.flip()
 
pygame.quit()