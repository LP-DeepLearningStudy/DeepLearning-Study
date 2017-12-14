# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""
기초적인 오브젝트 그리기 
작성일 : 2017-11-07
작성자 : 김건우
"""

import pygame

class Main :
    
    def __init__(self) :
        
        self.BLACK = (0, 0, 0)                  # 검은색 
        self.WHITE = (255, 255, 255)            # 흰색
        self.RED   = (255, 0, 0)                # 붉은색
        
        self.screen_width   = 500               # 화면 가로 길이
        self.screen_height  = 500               # 화면 세로 길이
        
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
            
            self.drawBlock()                    # 상자 그리기
            self.drawCircle00()                   # 원 그리기
            self.drawCircle01()
            self.drawCircle02()
            self.drawLine()                     # 선 그리기

            pygame.display.flip()               # 화면 업데이트
            
    def drawBlock(self) :
        pygame.draw.rect(self.screen,self.BLACK,(238,240,35,35))
         
    def drawCircle00(self) :
        pygame.draw.circle(self.screen,self.BLACK,(250,250), 200, 2)
        
    def drawCircle01(self) :
        pygame.draw.circle(self.screen,self.BLACK,(150,200), 50, 2)
        
    def drawCircle02(self) :
        pygame.draw.circle(self.screen,self.BLACK,(350,200), 50, 2)
        
    def drawLine(self) :
        pygame.draw.line(self.screen, self.BLACK, [150,350], [350,350], 5)

        
if __name__ == "__main__": 
    pygame.init()                               # 파이게임 모듈 초기화
    game = Main()                               # Main 인스턴스 생성 
    game.initializeGame()                       # 게임화면 실행 ! 