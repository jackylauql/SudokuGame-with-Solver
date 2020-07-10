import pygame

class Buttons:
    def __init__(self, position_x, position_y, width, height, text, function, color, highlightcolor, screen):
        self.surface = screen
        self.position = (position_x, position_y)
        self.width = width
        self.height = height
        self.text = text
        self.function = function
        self.color = color
        self.default_color = color
        self.highlight_color = highlightcolor
        self.highlighted = False
        self.screen = screen
        self.rect = pygame.draw.rect(self.screen, self.color,
                                     (self.position[0], self.position[1], self.width, self.height))
        self.font = pygame.font.SysFont('arial', 18, bold=True)
        self.cursor_within_button = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.width, self.height))
        text = self.font.render(self.text, False, (0, 0, 0))
        text_width, text_height = text.get_size()
        position_x = (self.width - text_width)//2
        position_y = (self.height - text_height)//2
        self.surface.blit(text, (self.position[0] + position_x, self.position[1] + position_y))

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.highlighted = True
        else:
            self.highlighted = False