import pygame
# importing the thing cuz it doesnt work if its gone
pygame.init()
# pygame initialized
WIDTH = 700
HEIGHT = 500
# game box
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# before the game loop
bullets = []
bullet_speed = 7


clock = pygame.time.Clock()

player = pygame.Rect(325, 430, 100, 80)
player_speed = 5
running = True

player_image = pygame.image.load("assets/alien_spaceship_sprite.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (100, 80))

enemies = []
for row in range(3):
    for col in range(8):
        enemy = pygame.Rect(80 + col * 60, 60 + row * 45, 40, 25)
        enemies.append(enemy)

enemy_speed = 1
enemy_direction = 1


# clocko
# game loop start 
while running:
    # pygame.event.get is getting events and storing them for later use
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # In the event loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx -3, player.top, 6, 15) 
                bullets.append(bullet)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed
    player.left = max(player.left, 0)
    player.right = min(player.right, WIDTH)
    screen.fill((12, 24, 38))
    
    move_down = False
    for enemy in enemies:
        # equivalent to enemy.x = enemy.x + enemy_speed * enemy_direction
        enemy.x += enemy_speed * enemy_direction 
        if enemy.right >= WIDTH or enemy.left <= 0:
            move_down = True
    if move_down:
        enemy_direction *= -1
        for enemy in enemies:
            enemy.y += 20


    # Update bullet
    for bullet in bullets[:]:
        bullet.y -= bullet_speed 
        if bullet.bottom < 0:
            bullets.remove(bullet)
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 80), bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, (220, 80, 80), enemy)

    # tuple: (x, y), (x, y, z)
    
    # Put this in the draw section 
    screen.blit(player_image, player)
    # pygame.draw.rect(screen, (255, 255, 80), player)

    # pygame.display updates the screen
    pygame.display.flip()
    clock.tick(120)
    # clock.tick puts the fps of the game to 60
# game loop ends
pygame.quit()
