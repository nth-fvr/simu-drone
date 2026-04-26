import pygame
import random

pygame.init()

fenetre = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Drone Runner")
horloge = pygame.time.Clock()
police = pygame.font.SysFont(None, 40)

# Chargement des images
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (800, 500))

img_joueur = pygame.image.load("player.png")
img_joueur = pygame.transform.scale(img_joueur, (70, 50))

img_obstacle_sol = pygame.image.load("obstacle.png")
img_obstacle_volant = pygame.image.load("flying_obstacl.png")

img_goal = pygame.image.load("goal.png")
img_goal = pygame.transform.scale(img_goal, (70, 100))


# ÉCRAN DE DÉMARRAGE

def ecran_demarrage():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False

        fenetre.blit(bg, (0, 0))
        texte = police.render("Appuie sur ENTREE pour jouer", True, (255, 255, 255))
        fenetre.blit(texte, (180, 230))
        pygame.display.flip()
        horloge.tick(60)



# JEU PRINCIPAL

def lancer_jeu():

    # Position du joueur
    joueur_y = 220
    joueur_rect = pygame.Rect(100, joueur_y, 70, 50)

    # Création des obstacles
    # Chaque obstacle est une liste : [rect, image]
    # On place 20 obstacles espacés aléatoirement hors de l'écran
    obstacles = []
    x = 900
    for i in range(20):
        x += random.randint(220, 380)
        choix = random.randint(0, 1)

        if choix == 0:
            # Obstacle au sol
            hauteur = random.randint(60, 160)
            rect = pygame.Rect(x, 500 - hauteur, 60, hauteur)
            img = pygame.transform.scale(img_obstacle_sol, (60, hauteur))
        else:
            # Obstacle volant
            y = random.randint(30, 350)
            rect = pygame.Rect(x, y, 60, 60)
            img = pygame.transform.scale(img_obstacle_volant, (60, 60))

        obstacles.append([rect, img])

    # But final, placé après le dernier obstacle
    goal_rect = pygame.Rect(obstacles[-1][0].x + 350, 380, 70, 100)

    resultat = ""
    en_jeu = True

    while en_jeu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Déplacement du joueur avec les flèches haut et bas
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP] and joueur_rect.y > 10:
            joueur_rect.y -= 5
        if touches[pygame.K_DOWN] and joueur_rect.y < 430:
            joueur_rect.y += 5

        # Déplacement des obstacles et du but vers la gauche
        for obs in obstacles:
            obs[0].x -= 4
        goal_rect.x -= 4

        # Dessin du fond, des obstacles, du but et du joueur
        fenetre.blit(bg, (0, 0))
        for obs in obstacles:
            fenetre.blit(obs[1], obs[0].topleft)
        fenetre.blit(img_goal, goal_rect.topleft)
        fenetre.blit(img_joueur, joueur_rect.topleft)

        # Collision avec un obstacle → perdu
        for obs in obstacles:
            if joueur_rect.colliderect(obs[0]):
                resultat = "perdu"
                en_jeu = False

        # Collision avec le but → gagné
        if joueur_rect.colliderect(goal_rect):
            resultat = "gagne"
            en_jeu = False

        pygame.display.flip()
        horloge.tick(60)

    return resultat


# ÉCRAN DE FIN

def ecran_fin(resultat):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False

        fenetre.blit(bg, (0, 0))

        if resultat == "gagne":
            texte = police.render("BRAVO ! Appuie sur ENTREE pour rejouer", True, (0, 255, 0))
        else:
            texte = police.render("PERDU ! Appuie sur ENTREE pour rejouer", True, (255, 0, 0))

        fenetre.blit(texte, (80, 230))
        pygame.display.flip()
        horloge.tick(60)



# LANCEMENT DU JEU

ecran_demarrage()

while True:
    resultat = lancer_jeu()
    ecran_fin(resultat)