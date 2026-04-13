import pygame
from obstacle import  Obstacle
from player import Player

#creer une seconde classe qui va representer notre jeu 
class Game:
    def __init__(self):
      #generer notre joueur
      self.player = Player()
      #groupe d'obstacle
      self.all_obstacles = pygame.sprite.Group()
      self.pressed  = {}
      self.spawn_obstacle()

    def check_collision(self, sprite, group):
       return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_obstacle(self):
       obstacle = Obstacle()
       self.all_obstacles.add (obstacle)