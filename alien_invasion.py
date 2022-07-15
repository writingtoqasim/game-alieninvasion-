
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import pygame
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1300, 700))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #  Make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    # Set the background color
    #bg_color = (230, 230, 230)
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Make an alien.
    alien = Alien(ai_settings, screen)
        # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)
        
        if stats.game_active:
            ship.update()
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)
run_game()  