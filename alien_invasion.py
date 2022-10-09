from email.mime import image
import imp
import sys
import pygame

from settings import Settings

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        # Initize the surface
        self.screen = pygame.display.set_mode(self.settings.screen_width, self.settings.screen_height)
        # self.screen = pygame.display.set_mode((1200, 700))
        # pygame.display.set_caption("Alien Invasion")
        
        # Set the Background Color
        # self.bg_color = (230, 230, 230)
                
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
            
            # Recolor the screen every circle
            self.screen.fill(self.settings.bg_color)
            
            pygame.display.flip()


if(__name__ == '__main__'):
    ai = AlienInvasion()
    ai.run_game()
