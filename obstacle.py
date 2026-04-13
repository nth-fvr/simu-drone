import pygame 

# creer une classe qui va gerer la notion d'obstacle sur le jeu 

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.image = pygame.image.load ("assets/obstacle.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 
        self.rect.y = 550
    
    def forward(self):
        self.rect.x -= self.velocity

        
