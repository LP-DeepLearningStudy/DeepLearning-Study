# -*- coding: utf-8 -*-

"""
main.py - 기본적인 파이게임 실행모듈
작성일 : 2017-11-07
작성자 : 김건우
"""

import pygame

class Main :
    
    def __init__(self) :
        
        self.BLACK = (0, 0, 0)                  # 검은색 
        self.WHITE = (255, 255, 255)            # 흰색
        self.RED   = (255, 0, 0)                # 붉은색
        
        self.screen_width   = 640               # 화면 가로 길이
        self.screen_height  = 400               # 화면 세로 길이
        
        self.done = False                       # 게임 플레이 변수 
        
        # 파이게임 화면 설정
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
               
    def initializeGame(self) :
        
        # 종료 이벤트가 발생할 때까지 업데이트 !
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
 
            self.screen.fill(self.WHITE)        # 배경은 흰색
            pygame.display.flip()               # 화면 업데이트
        
pygame.init()                                   # 파이게임 모듈 초기화
game = Main()                                   # Main 인스턴스 생성 
game.initializeGame()                           # 게임화면 실행 ! 
