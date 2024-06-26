import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, color_on, color_off, sound, x, y): # Add given properties as parameters
        pygame.sprite.Sprite.__init__(self)
        # Initialize properties here
        self.color_on = color_on
        self.color_off = color_off
        self.sound = sound
        self.x = x
        self.y = y
        self.image = pygame.Surface((230, 230))
        self.image.fill(self.color_off)
        self.rect = self.image.get_rect()
        # Assign x, y coordinates to the top left of the sprite
        self.rect.topleft = (self.x, self.y)

        
    '''
    Draws button sprite onto pygame window when called
    '''
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    '''
    Used to check if given button is clicked/selected by player
    '''
    def selected(self, mouse_pos):
    # Check if button was selected. Pass in mouse_pos.
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos)
    
    '''
    Illuminates button selected and plays corresponding sound.
    Sets button color back to default color after being illuminated.
    '''
    def update(self, screen):
        self.image.fill(self.color_on) # Illuminate button by filling color here
        screen.blit(self.image, (self.x, self.y)) # blit the image here so it is visible to the player
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play() # Play sound
        pygame.display.update()
        self.image.fill(self.color_off)
        screen.blit(self.image, (self.x, self.y))
        pygame.time.wait(500)
        pygame.display.update()