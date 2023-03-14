import math

import match as match
import pygame

from pygame.constants import *
from pygame.locals import *

class Planet:

    # Zmienne statyczne - nie są przypisane do obiektu, ale do całej klasy.


    cuonter =0
    list_of_planet = []
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

        Planet.cuonter += 1
        Planet.list_of_planet.append(self)

    def count_gravity_force(self):
        sumForceX = sumForceY = 0
        for planet in Planet.list_of_planet:
            if planet == self:
                continue
            distance = (((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2)) ** 0.5
            force = Planet.G * ((planet.mass * self.mass) / distance**2)

            angle = math.atan2(planet.y - self.y, planet.x - self.x)

            forceY = force * math.cos(angle)
            forceX = force * math.sin(angle)

            sumForceX += forceY
            sumForceY += forceX
        return sumForceX, sumForceY

    def draw(self):
        x = self.x * Planet.SCALE + SCREEN_WIDTH/2
        y = self.y * Planet.SCALE + SCREEN_HEIGHT/2
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

    @staticmethod
    def draw_all_planets(self):
        for planet in Planet.list_of_planet:
            planet.draw()

# Odpalenie modułów pygame
pygame.init()

# Parametry Screena
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, (255, 255, 0), 1.98892 * 10 ** 30)
    mercury = Planet(0.387 * Planet.AU, 0, 8, (121, 133, 124), 3.30 * 10 ** 23)
    venus = Planet(0.723 * Planet.AU, 0, 20, (193,143,23), 4.8685 * 10 ** 24)
    earth = Planet(1 * Planet.AU, 0, 16, (0, 0, 200), 29)
    mars = Planet(1.524 * Planet.AU, 0, 12, (121, 133, 124), 1.98892 * 10 ** 23)

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