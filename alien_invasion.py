# Eugene Cook
# April 6, 2025
# Alien Invasion Game

"""
    alien_invasion.py

    This module contains the MAIN functions to run Alien Invasion game.

    Modules:
        - sys
        - pygame
        - settings
        - ship
        - arsenal
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion:
    """Class representing the MAIN functions to run Alien Invasion game

        Attributes:
        event: key presses and key releases

        Methods:
    """

    def __init__(self) -> None:
        """Initializes game
        """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((
            self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))

    def run_game(self) -> None:
        """Initializes game loop
        """
        # Game loop
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """Update then draw background and ship to screen
        """
        self.screen.blit(self.bg, (0,0))        
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        """Check for QUIT, KEYDOWN, and KEYUP events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Changed events to up and down instead of left and right            
    def _check_keyup_events(self, event) -> None:
        """Check for release of a key

        Args:
            event (_type_): Key release up or down
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event) -> None:
        """Check for key presses

        Args:
            event (_type_): Key presses UP, DOWN, SPACE, and Q (Quit)
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()        
        





if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
