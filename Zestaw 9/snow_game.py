import sys

import pygame
import random

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
dark_gray = (33, 33, 33)
light_gray = (66, 66, 66)

# METHODS
def spawn_snowflake():
    spawn_position_x = random.randrange(10, screen.get_width()-15)
    snowflake = pygame.Rect(spawn_position_x, 0, snowflake_size, snowflake_size)
    snowflakes.append(snowflake)

def move_snowflakes():
    for snowflake in snowflakes[:]:

        snow_pile_fragment = collided_with_snow_pile(snowflake)

        # 1. Collides with snow pile
        if snow_pile_fragment is not None:
            new_y = snow_pile_fragment.top - snowflake_size
            add_to_snow_pile(pygame.Rect(snowflake.x, new_y, snowflake_size, snowflake_size))
            snowflakes.remove(snowflake)
            continue

        # 2. Collides with the ground
        if snowflake.bottom >= screen.get_height():
            new_y = screen.get_height() - snowflake_size
            add_to_snow_pile(pygame.Rect(snowflake.x, new_y, snowflake_size, snowflake_size))
            snowflakes.remove(snowflake)
            continue

        # 3. Normal move
        snowflake.move_ip(speed)


def handle_mouse_click(position):
    global points
    x, y = position
    for snowflake in snowflakes:
        if snowflake.collidepoint(x, y):
            snowflakes.remove(snowflake)
            points += 1
            break

def draw_game():
    screen.fill(dark_gray)

    # Draw snowflakes
    for snowflake in snowflakes:
        pygame.draw.rect(screen, white, snowflake)

    # Draw snow pile
    for snow_pile_fragment in snow_pile:
        pygame.draw.rect(screen, white, snow_pile_fragment)

    # Draw points
    font = pygame.font.SysFont("arial", 60)
    text_surface = font.render(str(points), True, light_gray)
    text_rect = text_surface.get_rect(center=screen.get_rect().center)
    screen.blit(text_surface, text_rect)

def collided_with_snow_pile(snowflake):
    for pile in snow_pile:

        x_overlap = (
            snowflake.right > pile.left and
            snowflake.left < pile.right
        )

        if not x_overlap:
            continue

        touching_top = (
            snowflake.bottom + speed[1] >= pile.top
        )

        if touching_top:
            return pile

    return None

def add_to_snow_pile(snow_pile_position):
    if snow_pile_position.y <= 0:
        pygame.quit()
        sys.exit()
    snow_pile.append(snow_pile_position)

# INITIALIZE THE GAME
pygame.init()
size = width, height = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snow Game')

# CLOCK
FPS = 60
clock = pygame.time.Clock()
spawn_delay = 500
last_spawn = 0

# LOAD ITEMS
speed = [0, 1]
snowflakes = []
snow_pile = []
snowflake_size = 30
points = 0

# MAIN GAME LOOP
while True:
    now = pygame.time.get_ticks()

    if now - last_spawn > spawn_delay:
        spawn_snowflake()
        last_spawn = now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            handle_mouse_click(position)

    move_snowflakes()
    draw_game()

    pygame.display.flip()
    clock.tick(FPS)
