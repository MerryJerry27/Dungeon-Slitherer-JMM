import sys
import os
import pygame
import copy
from snake import Snake
from entities import Entity
from layout import Layout

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# FONT SET UP
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# CAPTION / ICON SETUP
icon = os.path.join("Dungeon Slitherer", "assets", "door.png")
icon = pygame.image.load(icon).convert_alpha()
pygame.display.set_caption("Dungeon Slitherer - JMM")
pygame.display.set_icon(icon)

# SNAKE SETUP
snake = Snake(-40, -40, 100, 2000, 10)
snakes = pygame.sprite.Group()
snakes.add(snake)

snake_health = Snake(-40, -40, 0, 0, 10)
snakes_health = pygame.sprite.Group()
snakes_health.add(snake_health)

snake_body_collisions = []

# LEVEL / MENU SETUP
menus = (
    Layout("Menu", -40, -40, 1,
        (
            Entity("Panel", 80, 120, 400, 280, 400, 280, True, ("Normal", "Title")),
            Entity("Panel", 520, 40, 40, 40, 400, 440, True, ("Normal", "Normal")),
            Entity("Button", 560, 80, 80, 80, 80, 80, True, ("Level", 1)),
            Entity("Button", 680, 80, 80, 80, 80, 80, True, ("Level", 2)),
            Entity("Button", 800, 80, 80, 80, 80, 80, True, ("Level", 3)),
            Entity("Button", 560, 200, 80, 80, 80, 80, True, ("Level", 4)),
            Entity("Button", 680, 200, 80, 80, 80, 80, True, ("Level", 5)),
            Entity("Button", 800, 200, 80, 80, 80, 80, True, ("Level", 6)),
        )
    ),
    Layout("Menu", -40, -40, 1,
        (
            Entity("Panel", 320, 160, 360, 200, 360, 200, True, ("Normal", "Pause")),
            Entity("Button", 360, 200, 120, 40, 120, 40, True, ("Resume", "Normal")),
            Entity("Button", 360, 240, 120, 40, 120, 40, True, ("Restart", "Normal")),
            Entity("Button", 360, 280, 120, 40, 120, 40, True, ("Exit", "Normal"))
        )
    ),
    Layout("Menu", -40, -40, 1,
        (
            Entity("Panel", 320, 160, 360, 200, 360, 200, True, ("Normal", "Complete")),
            Entity("Button", 360, 200, 120, 40, 120, 40, True, ("Next", "Normal")),
            Entity("Button", 360, 240, 120, 40, 120, 40, True, ("Restart", "Normal")),
            Entity("Button", 360, 280, 120, 40, 120, 40, True, ("Exit", "Normal"))
        )
    ),
    Layout("Menu", -40, -40, 1,
        (
            Entity("Panel", 320, 160, 360, 200, 360, 200, True, ("Normal", "Died")),
            Entity("Button", 360, 200, 120, 40, 120, 40, True, ("Restart", "Normal")),
            Entity("Button", 360, 280, 120, 40, 120, 40, True, ("Exit", "Normal"))
        )
    )
)

levels = (
    Layout("Level", -40, -40, 1,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
        )
    ),
    Layout("Level", 120, 240, 1,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
            Entity("Button", 840, 560, 80, 80, 80, 80, True, ("Pause", "Normal")),
            Entity("Panel", 80, 560, 40, 40, 440, 80, True, ("Normal", "Normal")),
            Entity("Number", 560, 560, 40, 40, 80, 80, True, ("Snake_Length")),

            Entity("Wall", 40, 40, 40, 40, 920, 160, True, ("Normal")),
            Entity("Wall", 40, 320, 40, 40, 920, 160, True, ("Normal")),
            Entity("Door", 840, 240, 40, 40, 40, 40, True, (1, "Equal"))
        )
    ),
    Layout("Level", 840, 240, 1,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
            Entity("Button", 840, 560, 80, 80, 80, 80, True, ("Pause", "Normal")),
            Entity("Panel", 80, 560, 40, 40, 440, 80, True, ("Normal", "Normal")),
            Entity("Number", 560, 560, 40, 40, 80, 80, True, ("Snake_Length")),

            Entity("Wall", 760, 40, 40, 40, 40, 320, True, ("Normal")),
            Entity("Wall", 600, 160, 40, 40, 40, 320, True, ("Normal")),
            Entity("Wall", 440, 40, 40, 40, 40, 320, True, ("Normal")),
            Entity("Wall", 280, 160, 40, 40, 40, 320, True, ("Normal")),
            Entity("Door", 120, 400, 40, 40, 40, 40, True, (1, "Equal"))
        )
    ),
    Layout("Level", 120, 400, 1,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
            Entity("Button", 840, 560, 80, 80, 80, 80, True, ("Pause", "Normal")),
            Entity("Panel", 80, 560, 40, 40, 440, 80, True, ("Normal", "Normal")),
            Entity("Number", 560, 560, 40, 40, 80, 80, True, ("Snake_Length")),

            Entity("Wall", 200, 320, 40, 40, 40, 160, True, ("Normal")),
            Entity("Wall", 80, 320, 40, 40, 120, 40, True, ("Normal")),
            Entity("Wall", 40, 240, 40, 40, 120, 40, True, ("Normal")),
            Entity("Wall", 200, 240, 40, 40, 240, 40, True, ("Normal")),
            Entity("Wall", 280, 320, 40, 40, 40, 80, True, ("Normal")),
            Entity("Wall", 320, 320, 40, 40, 200, 40, True, ("Normal")),
            Entity("Wall", 280, 440, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 360, 400, 40, 40, 40, 80, True, ("Normal")),
            Entity("Wall", 400, 400, 40, 40, 120, 40, True, ("Normal")),
            Entity("Wall", 560, 280, 40, 40, 40, 160, True, ("Normal")),
            Entity("Wall", 440, 200, 40, 40, 40, 80, True, ("Normal")),
            Entity("Wall", 240, 120, 40, 40, 40, 120, True, ("Normal")),
            Entity("Wall", 80, 80, 40, 40, 240, 40, True, ("Normal")),
            Entity("Wall", 360, 40, 40, 40, 40, 160, True, ("Normal")),
            Entity("Wall", 320, 160, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 640, 280, 40, 40, 280, 40, True, ("Normal")),
            Entity("Wall", 800, 400, 40, 40, 120, 80, True, ("Normal")),
            Entity("Wall", 600, 400, 40, 40, 160, 40, True, ("Normal")),
            Entity("Wall", 880, 360, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 640, 320, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 720, 360, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 800, 320, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 480, 200, 40, 40, 280, 40, True, ("Normal")),
            Entity("Wall", 840, 200, 40, 40, 80, 40, True, ("Normal")),
            Entity("Wall", 720, 80, 40, 40, 40, 120, True, ("Normal")),
            Entity("Wall", 840, 80, 40, 40, 40, 120, True, ("Normal")),
            Entity("Wall", 920, 80, 40, 40, 40, 40, True, ("Normal")),
            Entity("Door", 600, 120, 40, 40, 40, 40, True, (1, "Equal"))
        )
    ),
    Layout("Level", 600, 120, 1,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
            Entity("Button", 840, 560, 80, 80, 80, 80, True, ("Pause", "Normal")),
            Entity("Panel", 80, 560, 40, 40, 440, 80, True, ("Normal", "Normal")),
            Entity("Number", 560, 560, 40, 40, 80, 80, True, ("Snake_Length")),

            Entity("Wall", 40, 40, 40, 40, 520, 160, True, ("Normal")),
            Entity("Wall", 680, 40, 40, 40, 280, 160, True, ("Normal")),
            Entity("Wall", 680, 320, 40, 40, 280, 160, True, ("Normal")),
            Entity("Wall", 40, 320, 40, 40, 520, 160, True, ("Normal")),
            Entity("Wall", 560, 40, 40, 40, 120, 40, True, ("Normal")),
            Entity("Wall", 560, 440, 40, 40, 120, 40, True, ("Normal")),
            Entity("Food", 120, 240, 40, 40, 40, 40, True, (1)),
            Entity("Food", 240, 240, 40, 40, 40, 40, True, (1)),
            Entity("Food", 360, 240, 40, 40, 40, 40, True, (1)),
            Entity("Door", 840, 240, 40, 40, 40, 40, True, (4, "Equal"))
        )
    ),
    Layout("Level", 840, 240, 4,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
            Entity("Button", 840, 560, 80, 80, 80, 80, True, ("Pause", "Normal")),
            Entity("Panel", 80, 560, 40, 40, 440, 80, True, ("Normal", "Normal")),
            Entity("Number", 560, 560, 40, 40, 80, 80, True, ("Snake_Length")),

            Entity("Wall", 720, 40, 40, 40, 240, 160, True, ("Normal")),
            Entity("Wall", 800, 320, 40, 40, 160, 160, True, ("Normal")),
            Entity("Wall", 920, 200, 40, 40, 40, 120, True, ("Normal")),
            Entity("Wall", 240, 80, 40, 40, 440, 120, True, ("Normal")),
            Entity("Wall", 240, 200, 40, 40, 160, 120, True, ("Normal")),
            Entity("Wall", 520, 200, 40, 40, 160, 80, True, ("Normal")),
            Entity("Wall", 440, 240, 40, 40, 40, 40, True, ("Normal")),
            Entity("Wall", 240, 320, 40, 40, 240, 40, True, ("Normal")),
            Entity("Wall", 520, 320, 40, 40, 280, 40, True, ("Normal")),
            Entity("Wall", 40, 320, 40, 40, 160, 40, True, ("Normal")),
            Entity("Wall", 240, 400, 40, 40, 120, 80, True, ("Normal")),
            Entity("Wall", 80, 160, 40, 40, 160, 40, True, ("Normal")),
            Entity("Wall", 120, 240, 40, 40, 40, 80, True, ("Normal")),
            Entity("Wall", 80, 40, 40, 40, 40, 40, True, ("Normal")),
            Entity("Food", 320, 360, 40, 40, 40, 40, True, (3)),
            Entity("Food", 160, 360, 40, 40, 40, 40, True, (1)),
            Entity("Food", 40, 280, 40, 40, 40, 40, True, (1)),
            Entity("Food", 40, 40, 40, 40, 40, 40, True, (1)),
            Entity("Food", 200, 120, 40, 40, 40, 40, True, (1)),
            Entity("One_Way", 680, 160, 40, 40, 40, 40, True, (((0, 1), ("Single")), ((0, 1), ("Single")))),
            Entity("One_Way", 480, 240, 40, 40, 40, 40, True, (((0, 1), ("Single")), ((0, 1), ("Single")))),
            Entity("One_Way", 480, 320, 40, 40, 40, 40, True, (((0, 1), ("Single")), ((0, 1), ("Single")))),
            Entity("One_Way", 240, 360, 40, 40, 40, 40, True, (((-1, 0), ("Single")), ((-1, 0), ("Single")))),
            Entity("One_Way", 200, 320, 40, 40, 40, 40, True, (((0, -1), ("Single")), ((0, -1), ("Single")))),
            Entity("One_Way", 40, 160, 40, 40, 40, 40, True, (((0, -1), ("Single")), ((0, -1), ("Single")))),
            Entity("One_Way", 160, 120, 40, 40, 40, 40, True, (((-1, 0), ("Single")), ((-1, 0), (0, -1)))),
            Entity("Door", 720, 400, 40, 40, 40, 40, True, (10, "Equal"))
        )
    ),
    Layout("Level", 720, 440, 10,
        (
            Entity("Border", 0, 0, 40, 40, 1000, 40, True, ("Normal")),
            Entity("Border", 960, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 0, 0, 40, 40, 40, 720, True, ("Normal")),
            Entity("Border", 40, 480, 40, 40, 920, 40, True, ("Normal")),
            Entity("Border", 40, 680, 40, 40, 920, 40, True, ("Normal")),
            Entity("Button", 840, 560, 80, 80, 80, 80, True, ("Pause", "Normal")),
            Entity("Panel", 80, 560, 40, 40, 440, 80, True, ("Normal", "Normal")),
            Entity("Number", 560, 560, 40, 40, 80, 80, True, ("Snake_Length")),

            Entity("Wall", 640, 80, 40, 40, 40, 400, True, ("Normal")),
            Entity("Wall", 320, 40, 40, 40, 40, 400, True, ("Normal")),
            Entity("Enemy", 680, 360, 40, 40, 40, 40, True, [-1, False, 40, 500, 1000, [0, 0], (680, 360), (((1, 0), 6), ((-1, 0), 6))]),
            Entity("Enemy", 920, 240, 40, 40, 40, 40, True, [-1, False, 40, 500, 1000, [0, 0], (920, 240), (((-1, 0), 6), ((1, 0), 6))]),
            Entity("Enemy", 680, 120, 40, 40, 40, 40, True, [-1, False, 40, 500, 1000, [0, 0], (680, 120), (((1, 0), 6), ((-1, 0), 6))]),
            Entity("Enemy", 360, 40, 40, 40, 40, 40, True, [-1, False, 10, 75, 500, [0, 0], (360, 40), (((0, 1), 20), ((1, 0), 24), ((-1, 0), 24), ((0, -1), 20))]),
            Entity("Enemy", 600, 440, 40, 40, 40, 40, True, [-1, False, 10, 75, 500, [0, 0], (600, 440), (((0, -1), 20), ((-1, 0), 24), ((1, 0), 24), ((0, 1), 20))]),
            Entity("Enemy", 600, 240, 40, 40, 40, 40, True, [-1, False, 10, 75, 500, [0, 0], (600, 240), (((-1, 0), 24), ((0, -1), 20), ((0, 1), 20), ((1, 0), 24))]),
            Entity("Enemy", 360, 240, 40, 40, 40, 40, True, [-1, False, 10, 75, 500, [0, 0], (360, 240), (((1, 0), 24), ((0, 1), 20), ((0, -1), 20), ((-1, 0), 24))]),
            Entity("Enemy", 40, 160, 40, 40, 40, 40, True, [-1, False, 2, 1, 1000, [0, 0], (40, 160), (((1, 0), 120), ((0, 1), 80), ((-1, 0), 120), ((0, -1), 80))]),
            Entity("Enemy", 280, 160, 40, 40, 40, 40, True, [-1, False, 2, 1, 1000, [0, 0], (280, 160), (((-1, 0), 120), ((0, 1), 80), ((1, 0), 120), ((0, -1), 80))]),
            Entity("Enemy", 160, 240, 40, 40, 40, 40, True, [-1, False, 40, 500, 1000, [0, 0], (160, 240), (((0, 0), 0), ((0, 0), 0))]),
            Entity("One_Way", 640, 40, 40, 40, 40, 40, True, (((-1, 0), ("Single")), ((-1, 0), ("Single")))),
            Entity("One_Way", 320, 440, 40, 40, 40, 40, True, (((-1, 0), ("Single")), ((-1, 0), ("Single")))),
            Entity("Door", 80, 80, 40, 40, 40, 40, True, (1, "Higher"))
        )
    )
)
menu_num = 0
control_in_menu = True
level_num = 0
control_in_level = False
stored_time = 0
snake.rect.x = levels[level_num].starting_x
snake.rect.y = levels[level_num].starting_y
snake.last_pos = (snake.rect.x, snake.rect.y)
snake.set_length(levels[level_num].starting_length)

for entity in levels[level_num].entity_list:
    if entity.type == "Enemy":
        entity.last_move = entity.speed * 2

# PRODUCTION TOOL / ENTITY COORD GATHERER FUNCTIONS
part = ""
coords = [(0, 0), (0, 0)]

def entity_builder():
        if part == "One":
            coords[0] = (snake.rect.x, snake.rect.y)
        if part == "Two":
            coords[1] = (snake.rect.x, snake.rect.y)
        if part == "Solve":
            print(str(coords[0][0]) + ", " + str(coords[0][1]) + ", " + str(coords[1][0] - coords[0][0] + 40) + ", " + str(coords[1][1] - coords[0][1] + 40) + ", ")



while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # LEVEL LOGIC
    if control_in_level:
        # COLLISIONS SETUP
        head_collision = pygame.sprite.spritecollide(snake, levels[level_num].entity_list, False)

        snake_body_collisions.clear()
        for body_part in snake.snake_body:
            snake_body_collisions.append(pygame.sprite.spritecollide(body_part, levels[level_num].entity_list, False))

        body_east_collision = pygame.sprite.spritecollide(snake.east_hitbox.sprites()[0], snake.snake_body, False)
        body_west_collision = pygame.sprite.spritecollide(snake.west_hitbox.sprites()[0], snake.snake_body, False)
        body_south_collision = pygame.sprite.spritecollide(snake.south_hitbox.sprites()[0], snake.snake_body, False)
        body_north_collision = pygame.sprite.spritecollide(snake.north_hitbox.sprites()[0], snake.snake_body, False)
        
        entity_east_collision = pygame.sprite.spritecollide(snake.east_hitbox.sprites()[0], levels[level_num].entity_list, False)
        entity_west_collision = pygame.sprite.spritecollide(snake.west_hitbox.sprites()[0], levels[level_num].entity_list, False)
        entity_south_collision = pygame.sprite.spritecollide(snake.south_hitbox.sprites()[0], levels[level_num].entity_list, False)
        entity_north_collision = pygame.sprite.spritecollide(snake.north_hitbox.sprites()[0], levels[level_num].entity_list, False)

        # Keyboard events / MOVEMENT COLLISION
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            snake.move(head_collision, body_north_collision, entity_north_collision, 0, -1)
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            snake.move(head_collision, body_west_collision, entity_west_collision, -1, 0)
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            snake.move(head_collision, body_south_collision, entity_south_collision, 0, 1)
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            snake.move(head_collision, body_east_collision, entity_east_collision, 1, 0)

        # PRODUCTION TOOL / ENTITY COORD GATHERER KEYS
        # if keys_pressed[pygame.K_i]:
        #     part = "One"
        #     entity_builder()
        # if keys_pressed[pygame.K_o]:
        #     part = "Two"
        #     entity_builder()
        # if keys_pressed[pygame.K_p]:
        #     part = "Solve"
        #     entity_builder()

    # ALWAYS DETECT THE MOUSE
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the (x, y) coordinates

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if control_in_level:
                    for entity in levels[level_num].entity_list:
                        if entity.rect.collidepoint(mouse_pos):
                            if entity.type == "Button":
                                if entity.event == "Pause":
                                    control_in_level = False
                                    control_in_menu = True
                                    stored_time = pygame.time.get_ticks()
                                    menu_num = 1
                if control_in_menu:
                    for entity in menus[menu_num].entity_list:
                        if entity.rect.collidepoint(mouse_pos):
                            if entity.type == "Button":
                                if entity.event == "Level":
                                    control_in_level = True
                                    control_in_menu = False
                                    level_num = entity.level
                                    snake.rect.x = levels[level_num].starting_x
                                    snake.rect.y = levels[level_num].starting_y
                                    snake.set_length(levels[level_num].starting_length)
                                    snake.direction = (1, 0)
                                    for body_part in snake.snake_body:
                                        body_part.rect.x = snake.rect.x
                                        body_part.rect.y = snake.rect.y
                                        body_part.front_direction = snake.direction
                                        body_part.back_direction = snake.direction
                                    for entity_2 in levels[level_num].entity_list:
                                        entity_2.display = True
                                        if entity_2.type == "Enemy":
                                            entity_2.rect.x = entity_2.starting_position[0]
                                            entity_2.rect.y = entity_2.starting_position[1]
                                            entity_2.last_move = pygame.time.get_ticks()
                                            entity_2.move_stages = [0, 0]
                                    head_collision = pygame.sprite.spritecollide(snake, levels[level_num].entity_list, False)
                                if entity.event == "Next":
                                    if level_num < 6:
                                        control_in_level = True
                                        control_in_menu = False
                                        level_num += 1
                                        for body_part in snake.snake_body:
                                            body_part.rect.x = snake.rect.x
                                            body_part.rect.y = snake.rect.y
                                            body_part.front_direction = snake.direction
                                            body_part.back_direction = snake.direction
                                    else:
                                        control_in_level = False
                                        control_in_menu = True
                                        level_num = 0
                                        menu_num = 0
                                        snake.rect.x = levels[level_num].starting_x
                                        snake.rect.y = levels[level_num].starting_y
                                        snake.set_length(levels[level_num].starting_length)
                                        snake.direction = (1, 0)
                                        snake_health.rect.x = -40
                                        snake_health.rect.y = -40
                                        for body_part_health in snake_health.snake_body:
                                            body_part_health.rect.x = -40
                                            body_part_health.rect.y = -40
                                    if level_num != 0:
                                        for entity_2 in levels[level_num].entity_list:
                                            entity_2.display = True
                                            if entity_2.type == "Enemy":
                                                entity_2.rect.x = entity_2.starting_position[0]
                                                entity_2.rect.y = entity_2.starting_position[1]
                                                entity_2.last_move = pygame.time.get_ticks()
                                                entity_2.move_stages = [0, 0]
                                    head_collision = pygame.sprite.spritecollide(snake, levels[level_num].entity_list, False)
                                if entity.event == "Resume":
                                    control_in_level = True
                                    control_in_menu = False
                                    snake.last_moved = pygame.time.get_ticks() - (stored_time - snake.last_moved)
                                    snake.last_damage = pygame.time.get_ticks() - (stored_time - snake.last_damage)
                                    for entity_2 in levels[level_num].entity_list:
                                        if entity_2.display:
                                            if entity_2.type == "Enemy":
                                                entity_2.last_move = pygame.time.get_ticks() - (stored_time - entity_2.last_move)
                                    head_collision = pygame.sprite.spritecollide(snake, levels[level_num].entity_list, False)
                                if entity.event == "Restart":
                                    control_in_level = True
                                    control_in_menu = False
                                    snake.rect.x = levels[level_num].starting_x
                                    snake.rect.y = levels[level_num].starting_y
                                    snake.set_length(levels[level_num].starting_length)
                                    snake.direction = (1, 0)
                                    for body_part in snake.snake_body:
                                        body_part.rect.x = snake.rect.x
                                        body_part.rect.y = snake.rect.y
                                        body_part.front_direction = snake.direction
                                        body_part.back_direction = snake.direction
                                    for entity_2 in levels[level_num].entity_list:
                                        entity_2.display = True
                                        if entity_2.type == "Enemy":
                                            entity_2.rect.x = entity_2.starting_position[0]
                                            entity_2.rect.y = entity_2.starting_position[1]
                                            entity_2.last_move = pygame.time.get_ticks()
                                            entity_2.move_stages = [0, 0]
                                    head_collision = pygame.sprite.spritecollide(snake, levels[level_num].entity_list, False)
                                if entity.event == "Exit":
                                    level_num = 0
                                    menu_num = 0
                                    snake.rect.x = levels[level_num].starting_x
                                    snake.rect.y = levels[level_num].starting_y
                                    snake.set_length(levels[level_num].starting_length)
                                    snake.direction = (1, 0)
                                    snake_health.rect.x = -40
                                    snake_health.rect.y = -40
                                    for body_part_health in snake_health.snake_body:
                                        body_part_health.rect.x = -40
                                        body_part_health.rect.y = -40



    """
    UPDATE section - manipulate everything on the screen
    """    

    # ALWAYS UPDATE THE SNAKES
    snake.update()
    snakes_health.update()

    # MORE LEVEL LOGIC
    if control_in_level:
        # ENTITIES UPDATES
        for entity in levels[level_num].entity_list:
                if entity.type == "Number":
                    if entity.linked_to == "Snake_Length":
                        entity.image = pygame.transform.scale(myfont.render(str(len(snake.snake_body.sprites()) + 1), True, (12, 16, 125)), (entity.entity_width, entity.entity_height))
                if entity.type == "Enemy":
                    if entity.display:
                        enemy_current_time = pygame.time.get_ticks()
                        if enemy_current_time - entity.last_move > entity.speed:
                            entity.last_move = enemy_current_time

                            entity.rect.x += (entity.move_pattern[entity.move_stages[0]][0][0] * entity.move_by)
                            entity.rect.y += (entity.move_pattern[entity.move_stages[0]][0][1] * entity.move_by)

                            entity.move_stages[1] += 1

                            if entity.move_stages[1] >= entity.move_pattern[entity.move_stages[0]][1]:
                                entity.move_stages[0] += 1
                                entity.move_stages[1] = 0
                            if entity.move_stages[0] >= len(entity.move_pattern):
                                entity.move_stages[0] = 0

        # LIVE COLLISION
        if len(head_collision) > 0:
            if head_collision[0].type == "Door":
                if head_collision[0].size_type == "Equal":
                    if (len(snake.snake_body.sprites()) + 1) == head_collision[0].length_needed:
                        control_in_level = False
                        control_in_menu = True
                        menu_num = 2
                if head_collision[0].size_type == "Lower":
                    if (len(snake.snake_body.sprites()) + 1) <= head_collision[0].length_needed:
                        control_in_level = False
                        control_in_menu = True
                        menu_num = 2
                if head_collision[0].size_type == "Higher":
                    if (len(snake.snake_body.sprites()) + 1) >= head_collision[0].length_needed:
                        control_in_level = False
                        control_in_menu = True
                        menu_num = 2
            if head_collision[0].type == "Food":
                if head_collision[0].display:
                    head_collision[0].display = False
                    snake.change_length(head_collision[0].change_amount)
            if head_collision[0].type == "Enemy":
                enemy_damage_current_time = pygame.time.get_ticks()
                if enemy_damage_current_time - snake.last_damage > snake.damage_time:
                    if head_collision[0].display:
                        if head_collision[0].die_on_contact:
                            head_collision[0].display = False
                        snake.last_damage = enemy_damage_current_time
                        if len(snake.snake_body.sprites()) > 0:
                            snake.change_length(head_collision[0].damage)
                        else:
                            control_in_level = False
                            control_in_menu = True
                            snake_health.rect.x = -40
                            snake_health.rect.y = -40
                            for entity_2 in levels[level_num].entity_list:
                                if entity_2.type == "Number":
                                    if entity_2.linked_to == "Snake_Length":
                                        entity_2.image = pygame.transform.scale(myfont.render("0", True, (12, 16, 125)), (entity_2.entity_width, entity_2.entity_height))
                            menu_num = 3
        for body_part_collision in snake_body_collisions:
            if len(body_part_collision) > 0:
                if body_part_collision[0].type == "Enemy":
                    enemy_damage_current_time = pygame.time.get_ticks()
                    if enemy_damage_current_time - snake.last_damage > snake.damage_time:
                        if body_part_collision[0].display:
                            if body_part_collision[0].die_on_contact:
                                body_part_collision[0].display = False
                            snake.last_damage = enemy_damage_current_time
                            snake.change_length(body_part_collision[0].damage)



    """
    DRAW section - make everything show up on screen
    """

    screen.fill((255, 0, 0))  # Fill the screen with one colour

    # ALWAYS DRAW THE SNAKE (SOMETIMES HIDDEN)
    snake.north_hitbox.draw(screen)
    snake.south_hitbox.draw(screen)
    snake.east_hitbox.draw(screen)
    snake.west_hitbox.draw(screen)
    snake.snake_body.draw(screen)
    snakes.draw(screen)

    # ALWAYS DRAW THE LEVEL (SOMETIMES BLANK)
    for entity in levels[level_num].entity_list:
        entity_draw = pygame.sprite.Group()
        entity_draw.add(entity)
        if entity.display:
            entity_draw.draw(screen)
    
    # SHOW SNAKE HEALTH BAR IN LEVELS 
    if control_in_level:
        snake_health.rect.x = 100
        snake_health.rect.y = 580
        snake_health.direction = (-1, 0)
        snake_health.set_length(len(snake.snake_body.sprites()) + 1)
        snake_health.last_pos = (snake_health.rect.x + 40, snake_health.rect.y)
        for body_part_health in snake_health.snake_body:
            body_part_health.rect.x = snake_health.last_pos[0]
            body_part_health.rect.y = snake_health.last_pos[1]
            body_part_health.front_direction = (-1, 0)
            body_part_health.back_direction = (-1, 0)
            snake_health.last_pos = (body_part_health.rect.x + 40, body_part_health.rect.y)
    
    # ALWAYS DRAW SNAKE HEALTH BAR (SOMETIMES HIDDEN)
    snake_health.snake_body.draw(screen)
    snakes_health.draw(screen)
    
    # MORE MENU LOGIC
    if control_in_menu:
        menus[menu_num].entity_list.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second