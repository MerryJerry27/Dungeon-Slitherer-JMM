import os
import pygame

class SnakeHitbox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image_location = os.path.join("assets", "hitbox.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect()

        self.rect.x = x + 15
        self.rect.y = y + 15

    def update(self, x, y):
        self.rect.x = x + 15
        self.rect.y = y + 15

class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, x, y, front_direction, back_direction):
        super().__init__()
        image_location = os.path.join("assets", "snake_body_straight.png")
        image_location_two = os.path.join("assets", "snake_body_corner.png")
        image_location_three = os.path.join("assets", "snake_body_end.png")
        image_location_four = os.path.join("assets", "snake_body_straight_hurt.png")
        image_location_five = os.path.join("assets", "snake_body_corner_hurt.png")
        image_location_six = os.path.join("assets", "snake_body_end_hurt.png")
        self.original_straight = pygame.transform.scale(pygame.image.load(image_location).convert_alpha(), (40, 40))
        self.original_corner = pygame.transform.scale(pygame.image.load(image_location_two).convert_alpha(), (40, 40))
        self.original_end = pygame.transform.scale(pygame.image.load(image_location_three).convert_alpha(), (40, 40))
        self.original_straight_hurt = pygame.transform.scale(pygame.image.load(image_location_four).convert_alpha(), (40, 40))
        self.original_corner_hurt = pygame.transform.scale(pygame.image.load(image_location_five).convert_alpha(), (40, 40))
        self.original_end_hurt = pygame.transform.scale(pygame.image.load(image_location_six).convert_alpha(), (40, 40))
        
        self.east_facing = pygame.transform.rotate(self.original_straight, 0)
        self.west_facing = pygame.transform.rotate(self.original_straight, 180)
        self.south_facing = pygame.transform.rotate(self.original_straight, 270)
        self.north_facing = pygame.transform.rotate(self.original_straight, 90)

        self.south_east_facing = pygame.transform.rotate(self.original_corner, 0)
        self.south_west_facing = pygame.transform.rotate(self.original_corner, 270)
        self.north_east_facing = pygame.transform.rotate(self.original_corner, 180)
        self.north_west_facing = pygame.transform.rotate(self.original_corner, 90)

        self.east_end = pygame.transform.rotate(self.original_end, 0)
        self.west_end = pygame.transform.rotate(self.original_end, 180)
        self.south_end = pygame.transform.rotate(self.original_end, 270)
        self.north_end = pygame.transform.rotate(self.original_end, 90)

        self.east_facing_hurt = pygame.transform.rotate(self.original_straight_hurt, 0)
        self.west_facing_hurt = pygame.transform.rotate(self.original_straight_hurt, 180)
        self.south_facing_hurt = pygame.transform.rotate(self.original_straight_hurt, 270)
        self.north_facing_hurt = pygame.transform.rotate(self.original_straight_hurt, 90)

        self.south_east_facing_hurt = pygame.transform.rotate(self.original_corner_hurt, 0)
        self.south_west_facing_hurt = pygame.transform.rotate(self.original_corner_hurt, 270)
        self.north_east_facing_hurt = pygame.transform.rotate(self.original_corner_hurt, 180)
        self.north_west_facing_hurt = pygame.transform.rotate(self.original_corner_hurt, 90)

        self.east_end_hurt = pygame.transform.rotate(self.original_end_hurt, 0)
        self.west_end_hurt = pygame.transform.rotate(self.original_end_hurt, 180)
        self.south_end_hurt = pygame.transform.rotate(self.original_end_hurt, 270)
        self.north_end_hurt = pygame.transform.rotate(self.original_end_hurt, 90)

        self.image = self.east_facing
        
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.front_direction = front_direction
        self.back_direction = back_direction

    # LOGIC TO UPDATE SPRITE (USES DIRECTIONS TO DETECT)
    def update(self, new_image, last_damage, damage_time):
        if new_image == "east_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.east_facing_hurt
            else:
                self.image = self.east_facing
        if new_image == "west_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.west_facing_hurt
            else:
                self.image = self.west_facing
        if new_image == "south_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.south_facing_hurt
            else:
                self.image = self.south_facing
        if new_image == "north_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.north_facing_hurt
            else:
                self.image = self.north_facing
        if new_image == "south_east_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.south_east_facing_hurt
            else:
                self.image = self.south_east_facing
        if new_image == "south_west_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.south_west_facing_hurt
            else:
                self.image = self.south_west_facing
        if new_image == "north_east_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.north_east_facing_hurt
            else:
                self.image = self.north_east_facing
        if new_image == "north_west_facing":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.north_west_facing_hurt
            else:
                self.image = self.north_west_facing
        if new_image == "east_end":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.east_end_hurt
            else:
                self.image = self.east_end
        if new_image == "west_end":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.west_end_hurt
            else:
                self.image = self.west_end
        if new_image == "south_end":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.south_end_hurt
            else:
                self.image = self.south_end
        if new_image == "north_end":
            if pygame.time.get_ticks() - last_damage < damage_time:
                self.image = self.north_end_hurt
            else:
                self.image = self.north_end
        
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, update_every, damage_time, limit):
        super().__init__()
        image_location = os.path.join("assets", "snake_head.png")
        image_location_two = os.path.join("assets", "snake_head_hurt.png")
        self.original_image = pygame.transform.scale(pygame.image.load(image_location).convert_alpha(), (40, 40))
        self.original_image_hurt = pygame.transform.scale(pygame.image.load(image_location_two).convert_alpha(), (40, 40))
        self.east_facing = pygame.transform.rotate(self.original_image, 0)
        self.west_facing = pygame.transform.rotate(self.original_image, 180)
        self.south_facing = pygame.transform.rotate(self.original_image, 270)
        self.north_facing = pygame.transform.rotate(self.original_image, 90)
        self.east_facing_hurt = pygame.transform.rotate(self.original_image_hurt, 0)
        self.west_facing_hurt = pygame.transform.rotate(self.original_image_hurt, 180)
        self.south_facing_hurt = pygame.transform.rotate(self.original_image_hurt, 270)
        self.north_facing_hurt = pygame.transform.rotate(self.original_image_hurt, 90)
        self.image = self.east_facing

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # SNAKE BODY SETUP
        self.snake_body = pygame.sprite.Group()
        self.limit = limit - 1
        self.damage_time = damage_time
        self.last_damage = -999999

        # HITBOXES SETUP
        self.east_hitbox = pygame.sprite.Group()
        self.east_hitbox.add(SnakeHitbox(self.rect.x + 40, self.rect.y))
        
        self.west_hitbox = pygame.sprite.Group()
        self.west_hitbox.add(SnakeHitbox(self.rect.x - 40, self.rect.y))
        
        self.south_hitbox = pygame.sprite.Group()
        self.south_hitbox.add(SnakeHitbox(self.rect.x, self.rect.y + 40))

        self.north_hitbox = pygame.sprite.Group()
        self.north_hitbox.add(SnakeHitbox(self.rect.x, self.rect.y - 40))
        
        # MOVE SETUP
        self.last_moved = -999999
        self.last_in_tick = -999999
        self.update_every = update_every
        self.last_pos = (self.rect.x, self.rect.y)
        self.direction = (1, 0)
        '''

        (1, 0) : "EAST"
        (-1, 0) : "WEST"
        (0, 1) : "SOUTH"
        (0, -1) : "NORTH"

        '''

    def update(self, control_in_level):
        # LOGIC TO UPDATE SPRITE (USES DIRECTIONS TO DETECT)
        if control_in_level:
            if self.direction == (1, 0):
                if pygame.time.get_ticks() - self.last_damage < self.damage_time:
                    self.image = self.east_facing_hurt
                else:
                    self.image = self.east_facing
            if self.direction == (-1, 0):
                if pygame.time.get_ticks() - self.last_damage < self.damage_time:
                    self.image = self.west_facing_hurt
                else:
                    self.image = self.west_facing
            if self.direction == (0, 1):
                if pygame.time.get_ticks() - self.last_damage < self.damage_time:
                    self.image = self.south_facing_hurt
                else:
                    self.image = self.south_facing
            if self.direction == (0, -1):
                if pygame.time.get_ticks() - self.last_damage < self.damage_time:
                    self.image = self.north_facing_hurt
                else:
                    self.image = self.north_facing

            # UPDATE BODY PART SPRITES
            for body_part in self.snake_body:
                if body_part.back_direction == (1, 0) and body_part.front_direction == (1, 0):
                    if body_part == self.snake_body.sprites()[len(self.snake_body.sprites()) - 1]:
                        body_part.update("east_end", self.last_damage, self.damage_time)
                    else:
                        body_part.update("east_facing", self.last_damage, self.damage_time)
                if body_part.back_direction == (-1, 0) and body_part.front_direction == (-1, 0):
                    if body_part == self.snake_body.sprites()[len(self.snake_body.sprites()) - 1]:
                        body_part.update("west_end", self.last_damage, self.damage_time)
                    else:
                        body_part.update("west_facing", self.last_damage, self.damage_time)
                if body_part.back_direction == (0, 1) and body_part.front_direction == (0, 1):
                    if body_part == self.snake_body.sprites()[len(self.snake_body.sprites()) - 1]:
                        body_part.update("south_end", self.last_damage, self.damage_time)
                    else:
                        body_part.update("south_facing", self.last_damage, self.damage_time)
                if body_part.back_direction == (0, -1) and body_part.front_direction == (0, -1):
                    if body_part == self.snake_body.sprites()[len(self.snake_body.sprites()) - 1]:
                        body_part.update("north_end", self.last_damage, self.damage_time)
                    else:
                        body_part.update("north_facing", self.last_damage, self.damage_time)
                if (body_part.back_direction == (0, -1) and body_part.front_direction == (1, 0)) or (body_part.front_direction == (0, 1) and body_part.back_direction == (-1, 0)):
                    body_part.update("south_east_facing", self.last_damage, self.damage_time)
                if (body_part.back_direction == (0, -1) and body_part.front_direction == (-1, 0)) or (body_part.front_direction == (0, 1) and body_part.back_direction == (1, 0)):
                    body_part.update("south_west_facing", self.last_damage, self.damage_time)
                if (body_part.back_direction == (0, 1) and body_part.front_direction == (-1, 0)) or (body_part.front_direction == (0, -1) and body_part.back_direction == (1, 0)):
                    body_part.update("north_east_facing", self.last_damage, self.damage_time)
                if (body_part.back_direction == (0, 1) and body_part.front_direction == (1, 0)) or body_part.front_direction == (0, -1) and body_part.back_direction == (-1, 0):
                    body_part.update("north_west_facing", self.last_damage, self.damage_time)

        self.north_hitbox.update(self.rect.x, self.rect.y - 40)
        self.south_hitbox.update(self.rect.x, self.rect.y + 40)
        self.east_hitbox.update(self.rect.x + 40, self.rect.y)
        self.west_hitbox.update(self.rect.x - 40, self.rect.y)

    def move(self, head_colliding, body_colliding, entity_colliding, x, y):
        if len(head_colliding) > 0:
            if head_colliding[0].type == "One_Way": # MOVE OUT OF ONE-WAYS WHEN DIRECTION IS VALID
                if (x, y) in head_colliding[0].exit_directions:
                    pass
                else:
                    return
        if len(body_colliding) > 0:
            if body_colliding[0] == self.snake_body.sprites()[len(self.snake_body.sprites()) - 1]: # CAN MOVE THROUGH END OF BODY
                pass
            else:
                return
        if len(entity_colliding) > 0:
            if entity_colliding[0].type == "Wall" or entity_colliding[0].type == "Border": # STOP AT WALLS AND BORDERS
                return
            if entity_colliding[0].type == "One_Way": # MOVE INTO ONE WAYS WHEN DIRECTION IS VALID
                if (x, y) in entity_colliding[0].enter_directions:
                    pass
                else:
                    return

        move_time = pygame.time.get_ticks()
        if move_time - self.last_moved > self.update_every: # MOVE WHEN TIME HITS SPEED AMOUNT
            self.direction = (x / 1, y / 1)
            self.last_moved = move_time
            self.last_pos = (self.rect.x, self.rect.y)
            self.rect.x += x * 40
            self.rect.y += y * 40
            self.follow()

    def follow(self):
        body_part_index = 0
        for body_part in self.snake_body: # MOVES EACH BODY PART TO LAST LOCATION, FIRST FOLLOWING SNAKE HEAD THEN TO EACH BODY PART AFTER
            hold_pos = body_part.rect.x, body_part.rect.y
            body_part.rect.x = self.last_pos[0]
            body_part.rect.y = self.last_pos[1]
            self.last_pos = hold_pos

            # DIRECTION LINING UP
            if len(self.snake_body.sprites()) == 1: # ONLY ONE BODY PART, LINE UP TO HEAD
                body_part.front_direction = self.direction
                body_part.back_direction = self.direction
            elif self.snake_body.sprites()[0] == body_part and len(self.snake_body.sprites()) > 1: # START OF BODY, ALIGNS TO HEAD AND NEXT BODY PART
                if body_part.front_direction != body_part.back_direction: # CORNER CASE (LITERALLY)
                    body_part.back_direction = body_part.front_direction
                    body_part.front_direction = self.direction
                else:
                    body_part.front_direction = self.direction
                    body_part.back_direction = self.snake_body.sprites()[body_part_index + 1].front_direction
            elif self.snake_body.sprites()[len(self.snake_body.sprites()) - 1] == body_part and len(self.snake_body.sprites()) > 1: # END OF BODY, ALIGNS TO SECOND LAST BODY PART
                body_part.front_direction = self.snake_body.sprites()[body_part_index - 1].back_direction
                body_part.back_direction = self.snake_body.sprites()[body_part_index - 1].back_direction
            else: # EVERY OTHER BODY PART
                if body_part.front_direction != body_part.back_direction: # CORNER CASE (LITERALLY)
                    body_part.back_direction = body_part.front_direction
                    body_part.front_direction = self.snake_body.sprites()[body_part_index - 1].back_direction
                else:
                    body_part.front_direction = self.snake_body.sprites()[body_part_index - 1].back_direction
                    body_part.back_direction = self.snake_body.sprites()[body_part_index + 1].front_direction
            body_part_index += 1

    def change_length(self, amount):
        count = 0
        if amount > 0: # GROW
            if len(self.snake_body.sprites()) < self.limit and len(self.snake_body.sprites()) + amount <= self.limit: # CHECK IF CAN GROW
                while count < amount: # ADD ON AMOUNT YOU GROW
                    if len(self.snake_body.sprites()) == 0:
                        self.snake_body.add(SnakeBody(self.last_pos[0], self.last_pos[1], self.direction, self.direction))
                    else:
                        self.snake_body.add(SnakeBody(self.last_pos[0], self.last_pos[1], self.snake_body.sprites()[len(self.snake_body.sprites()) - 1].front_direction, self.snake_body.sprites()[len(self.snake_body.sprites()) - 1].back_direction))
                    if len(self.snake_body.sprites()) > 0: # UPDATE LAST POSITION FOR SNAKE BODY PROPERLY
                        self.last_pos = (self.snake_body.sprites()[len(self.snake_body.sprites()) - 1].rect.x, self.snake_body.sprites()[len(self.snake_body.sprites()) - 1].rect.y)
                    else:
                        self.last_pos = (self.rect.x - (self.direction[0] * 40), self.rect.y - (self.direction[1] * 40))
                    count += 1
            else:
                return
        elif amount < 0: # SHRINK
            if len(self.snake_body.sprites()) > 0 and len(self.snake_body.sprites()) + amount >= 0: # CHECK IF CAN SHRINK
                while count > amount: # REMOVE ON AMOUNT YOU SHRINK
                    self.snake_body.remove(self.snake_body.sprites()[len(self.snake_body.sprites()) - 1])
                    if len(self.snake_body.sprites()) > 0: # UPDATE LAST POSITION FOR SNAKE BODY PROPERLY
                        self.last_pos = (self.snake_body.sprites()[len(self.snake_body.sprites()) - 1].rect.x, self.snake_body.sprites()[len(self.snake_body.sprites()) - 1].rect.y)
                    else:
                        self.last_pos = (self.rect.x - (self.direction[0] * 40), self.rect.y - (self.direction[1] * 40))
                    count -= 1
            else:
                return
    
    def set_length(self, amount):
        if amount > 0 and amount <= self.limit + 1: # CHECK FOR VALID LENGTH
            if amount > len(self.snake_body.sprites()) + 1:
                while amount > len(self.snake_body.sprites()) + 1: # KEEP GROWING TILL DESIRED SIZE
                    self.change_length(1)
            if amount < len(self.snake_body.sprites()) + 1:
                while amount < len(self.snake_body.sprites()) + 1: # KEEP SHRINKING TILL DESIRED SIZE
                    self.change_length(-1)