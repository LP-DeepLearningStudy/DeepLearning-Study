import pygame

class Box :
    def __init__(self, _x=50, _y=150):
        self.x = _x
        self.y = _y
        
        self.velocity = 0.05
        self.acceleration = 0.2
        
    def move(self, screen):
        t = 1
        self.x = self.x + self.velocity * t + 0.5 * self.acceleration * t * t      
        if self.x > 600 or self.x < 50 :
            self.acceleration *= -1           
            self.velocity *= -1
        pygame.draw.rect(screen, (255,0,0) ,(self.x, self.y,10,10))
        t += 1