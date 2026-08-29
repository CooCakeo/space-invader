import pygame
game_state = "start"
def create_enemies():
    enemies = []
    for row in range(3):
        for col in range(8):
            enemy = pygame.Rect(80 + col * 60, 60 + row * 45, 40, 25)
            enemies.append(enemy)

    return enemies

def reset_game():
    global score, lives, bullets, enemies, game_state
    score = 0
    lives = 3
    bullets = []
    enemies = []
    for row in range(3):
        for col in range(8):
            enemies.append(pygame.Rect(80 + col * 60, 60 + row + 45, 40, 25))
    game_state = "playing"

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


enemy_speed = 7
enemy_direction = 1

score = 0
font = pygame.font.Font(None, 36)
# Before game loop
for bullet in bullets[:]:
    for enemy in enemies[:]:
        if bullet.colliderect(enemy):
            bullets.remove(bullet)
            enemies.remove(enemy)
            score += 10
            break
lives = 3

# clocko
# START OF GAME LOOP
while running:
   # START OF EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # In the event loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == "playing":
                bullet = pygame.Rect(player.centerx -3, player.top, 6, 15) 
                bullets.append(bullet)
            if event.key == pygame.K_RETURN:
                if game_state in ["start", "game_over"]:
                    reset_game()

    # END OF EVENT LOOP

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and game_state == "playing":
        player.x -= player_speed
    if keys[pygame.K_d] and game_state == "playing":
        player.x += player_speed
    player.left = max(player.left, 0)
    player.right = min(player.right, WIDTH)
    screen.fill((12, 24, 38))

    if game_state == "playing":
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
    
        #collision update
        for bullet in bullets[:]:
            for enemy in enemies[:]:    
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break
        # Enemy danger check
        for enemy in enemies:
            if enemy.bottom >= player.top:
                lives -= 1

                # reset
                enemies.clear()
                enemies = create_enemies()
                
                if lives <= 0:
                    game_state = "game_over"

    # Draw HUD
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (560, 10))
    if game_state == "game_over":
        text = font.render("GAME OVER", True, (255, 80, 80))
        screen.blit(text, (270, 230))

    if game_state == "start":
        screen.fill((5, 5, 25,))
        title = font.render("SPACE INVADERS" , True, (255, 255, 255))
        screen.blit(title, (230, 200))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    # Update bullet
    for bullet in bullets[:]:
        bullet.y -= bullet_speed 
        if bullet.bottom < 0:
            bullets.remove(bullet)
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 80), bullet)
    if game_state == "playing":
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


# END OF GAME LOOP
pygame.quit()
