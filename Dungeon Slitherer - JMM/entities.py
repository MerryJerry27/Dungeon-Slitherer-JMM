import os
import pygame

import math

class Entity(pygame.sprite.Sprite):
    def __init__(self, type, x, y, image_width, image_height, entity_width, entity_height, display, extra_info):
        super().__init__()

        self.display = display

        self.type = type
        if self.type == "Panel":
            if extra_info[1] == "Normal":
                self.stored_image = "panel.png"
            else:
                self.stored_image = "panel_" + str.lower(extra_info[1]) + ".png"
            self.stored_rotation = 0
        if self.type == "Border":
            self.stored_image = "border.png"
            self.stored_rotation = 0
        if self.type == "Wall":
            self.stored_image = "wall_tile.png"
            self.stored_rotation = 0
        if self.type == "Button":
            self.event = extra_info[0]
            if self.event == "Pause" or self.event == "Next" or self.event == "Resume" or self.event == "Restart" or self.event == "Exit":
                self.stored_image = str.lower(self.event) + "_button.png"
                self.stored_rotation = 0
            if self.event == "Level":
                self.level = extra_info[1]
                self.stored_image = "level_" + str(self.level) + ".png"
                self.stored_rotation = 0
        if self.type == "Number":
            self.linked_to = extra_info
            self.stored_image = "door.png"
            self.stored_rotation = 0
        if self.type == "Door":
            self.length_needed = extra_info[0]
            self.size_type = extra_info[1]
            self.stored_image = "door_" + str(self.length_needed) + "_" + str.lower(self.size_type) + ".png"
            self.stored_rotation = 0
        if self.type == "Food":
            self.change_amount = extra_info
            self.stored_image = "food_" + str(self.change_amount) + ".png"
            self.stored_rotation = 0
        if self.type == "One_Way":
            self.enter_directions = extra_info[0]
            self.exit_directions = extra_info[1]
            if self.enter_directions == self.exit_directions:
                if self.enter_directions[0] == (1, 0):
                    self.stored_image = "one_way_straight_straight.png"
                    self.stored_rotation = 0
                if self.enter_directions[0] == (-1, 0):
                    self.stored_image = "one_way_straight_straight.png"
                    self.stored_rotation = 180
                if self.enter_directions[0] == (0, 1):
                    self.stored_image = "one_way_straight_straight.png"
                    self.stored_rotation = 270
                if self.enter_directions[0] == (0, -1):
                    self.stored_image = "one_way_straight_straight.png"
                    self.stored_rotation = 90
            elif self.enter_directions[1] == ("Single") and self.exit_directions[0] == self.enter_directions[0] and self.exit_directions[1] == (0, -1):
                self.stored_image = "one_way_straight_corner_right.png"
                self.stored_rotation = 180
        if self.type == "Enemy":
            self.damage = extra_info[0]
            self.die_on_contact = extra_info[1]
            self.move_by = extra_info[2]
            self.speed = extra_info[3]
            self.last_move = extra_info[4]
            self.move_stages = extra_info[5]
            self.starting_position = extra_info[6]
            self.move_pattern = extra_info[7]
            self.stored_image = "skeleton.png"
            self.stored_rotation = 0
            
        """
        Create an Entity sprite. These entities can be any size.
        
        Args:
            x: The x coordinate of the platform. Preferably a multiple of 40.
            y: The y coordinate of the platform. Preferably a multiple of 40.
            width: The width of the platform. Preferably a multiple of 40.
            height: The height of the platform. Preferably a multiple of 40.
        """
        self.image = self.create_image(os.path.join("Dungeon Slitherer", "assets", self.stored_image), self.stored_rotation, image_width, image_height, entity_width, entity_height)


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.entity_width = entity_width
        self.entity_height = entity_height
        
        '''
        EXTRA INFO REFERENCE
        
        "Panel": none

        "Button": (String event)
        type determines what the button does

        "Border" : none

        "Wall" : "none"

        "Door" : (int length_needed, String size_type)
        checks for <=, ==, or >= to length_needed

        "Food" : (int change_amount)
        determines how much to grow/shrink when touched

        "One_Way" : (list of coord-lists enter_directions), (list of coord-lists exit_directions))
        allows which direction you can enter and exit

        "Enemy" : (int damage, boolean contact_death, int move_by, int speed, int last_move, (list stages: int move_stage, int cycle_stage), (list move_cycle: movement-list direction, int distance)
        deals damage on contact, determined if contact_death, move_by pixels per speed seconds, travel move_cycle hold lines to follow, stages and last_move stores

        '''
        
    def create_image(self, image_location, rotation, image_width, image_height, entity_width, entity_height):
        """
        Create the image for this sprite by using one base image and tiling it horizontally. Note that vertical tiling HAS ALSO been implemented.
        Args:
            image_location: A string representing the file location for the image.
            width: The width of the output image in pixels
            height: The height of the output image in pixels
        Returns:
            A surface representing the output image.
        """
        tile_image = pygame.image.load(image_location).convert_alpha()
        tile_image = pygame.transform.scale(tile_image, (image_width, image_height))
        tile_image = pygame.transform.rotate(tile_image, rotation)

        # The self.image attribute expects a Surface, so we can manually create one and "blit" the tile image onto the surface (i.e. paint an image onto a surface).
        # We use list comprehension to quickly make the blits_data list of tuples (each tuple has the tile image, and the X and Y coordinates)
        # Don't know what list comprehension is? Go look it up on the Internet. That's what all professional software engineers do ;)

        # But now it can tile in both directions! 
        image = pygame.Surface((entity_width, entity_height))
        blits_data = []
        for i in range(math.ceil(entity_height / image_height)):
            for j in range(math.ceil(entity_width / image_width)):
                blits_data.append((tile_image, (image_width * j, image_height * i)))
        image.blits(blits_data)

        return image