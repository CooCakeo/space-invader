import pygame
# importing the thing cuz it doesnt work if its gone
pygame.init()
# pygame initialized
WIDTH = 700
HEIGHT = 500
# game box
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
# game loop start 
clock = pygame.time.Clock()

player = pygame.Rect(325, 430, 50, 30)
player_speed = 5
running = True

# clock
while running:
    # pygame.event.get is getting events and storing them for later use
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    # tuple: (x, y), (x, y, z)
    screen.fill((12, 24, 38))
    pygame.draw.rect(screen, (80, 220, 120), player)
    # pygame.display updates the screen
    pygame.display.flip()
    clock.tick(120)
    # clock.tick puts the fps of the game to 60
# game loop ends
pygame.quit()

