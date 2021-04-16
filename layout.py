import pygame

class Layout:
    def __init__(self, layout_type, starting_x, starting_y, starting_length, entity_list):
        self.layout_type = layout_type
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.starting_length = starting_length
        self.entity_list = pygame.sprite.Group()
        for entity in entity_list:
            self.entity_list.add(entity)