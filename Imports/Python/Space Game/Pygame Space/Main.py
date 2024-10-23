import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game')
BG = pygame.transform.scale(pygame.image.load('Space.jpg'), (WIDTH, HEIGHT))
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

FONT = pygame.font.SysFont('comicsans', 30)

def Draw(Player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, 'white')
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (255, 0, 0), Player)

    for star in stars:
        pygame.draw.rect(WIN, 'white', star)



    pygame.display.update()



def main():
    run = True

    Player = pygame.Rect(480, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False

    while run:

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and Player.x - PLAYER_VEL >=0  or keys[pygame.K_a] and Player.x - PLAYER_VEL >=0:
            Player.x -= PLAYER_VEL       
        if keys[pygame.K_RIGHT] and Player.x + PLAYER_VEL + Player.width <= WIDTH or keys[pygame.K_d] and Player.x + PLAYER_VEL + Player.width <= WIDTH:
            Player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= Player.y and star.colliderect(Player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render('You Lost! You lasted ' + str(elapsed_time // 1)+'s',1,'grey')
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        Draw(Player, elapsed_time, stars)

    pygame.quit()

if __name__ == '__main__':
    main()