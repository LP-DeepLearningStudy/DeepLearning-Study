
# -*- coding: utf-8 -*-

import pygame

class Main :
    
    def __init__(self) :
        
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED   = (255, 0, 0)
        
        self.screen_width   = 640
        self.screen_height  = 400
        
        self.done = False
        
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
               
    def initializeGame(self) :
        
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
 
            self.screen.fill(self.WHITE)
            pygame.display.flip()
        
pygame.init()
game = Main()        
game.initializeGame()
