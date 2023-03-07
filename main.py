import pygame

from pygame.constants import *
from pygame.locals import *

class Planet:

    # Zmienne statyczne - nie są przypisane do obiektu, ale do całej klasy.
    AU = 149.6e9
    G = 6.67428e-11
    SCALE = 250 / AU # 1 AU = 100 pikseli
    TIMESTEP = 3600 * 24 # 1 doba ziemska

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.isSun = False

    def draw(self):
        x = self.x * Planet.SCALE + SCREEN_WIDTH/2
        y = self.y * Planet.SCALE + SCREEN_HEIGHT/2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

# Odpalenie modułów pygame
pygame.init()

# Parametry Screena
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 20, (255, 255, 0), 19891000000000000000000000000000)
    mercury = Planet(5790917, 0, 20, (121, 133, 124), 3302000000000000000000000)
    venus = Planet(108208926, 0, 20, (193,143,23), 48685000000000000000000000)
    earth = Planet(Planet.AU, 0, 10, (0, 0, 200), 29)
    mars = Planet(227936637, 0, 20, (121, 133, 124), 64190000000000000000000000)

    # Pętla gry
    running = True
    while running:
        # LOGIKA GRY (w przyszłości):


        # RYSOWANIE GRAFIKI:

        # Wypełnienie okienka kolorem
        screen.fill((0, 0, 0))

        # Rysowanie kształtów w PyGame
        sun.draw()
        mercury.draw()
        venus.draw()
        earth.draw()
        mars.draw()

        # Czekanie na kolejną klatkę
        clock.tick(60)

        #Aktualizacja gry
        pygame.display.flip()

        # Te cztery linijki pozwalają nam normalnie zamknąć program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

main()