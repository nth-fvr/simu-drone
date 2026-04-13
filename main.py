import pygame 
from game import Game

pygame.init()


#generer la fenetre du jeu 
pygame.display.set_caption("drone soccer game")
screen = pygame.display.set_mode((1080,720)) 

#importer l'arriere plan 
background = pygame.image.load("assets/bg.jpg")

#charger le jeu
game = Game()



running = True
while running:

    #appliquer l'arriere plan du jeu 
    screen.blit(background, (-75,-20))

    #appliquer l'image du joueur 
    screen.blit(game.player.image, game.player.rect)

    #appliquer l'ensemble des images du groupe d'obstacles
    game.all_obstacles.draw(screen)

    # récuperer les obstacles du jeu
    for obstacle in game.all_obstacles:
        obstacle.forward()




    #verifier si le joueur veut aller en haut ou en bas 
    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get (pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()


    #metre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    #detecter si le joueur utilise le clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
     
        

