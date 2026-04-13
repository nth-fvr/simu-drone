import pygame


#creer une classe pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
      super().__init__()
      self.velocity = 1
      self.image = pygame.image.load("assets/player.png")
      self.rect = self.image.get_rect()
      self.rect.x = 200
      self.rect.y = 650
    
    def move_up(self):
       self.rect.y -= self.velocity
    
    def move_down(self):
       self.rect.y += self.velocity

    