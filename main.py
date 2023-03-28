import math
import pygame
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

        self.velX = self.velY = 0
        if len(Planet.list_of_planet) > 0:
            sunMass = Planet.list_of_planet[0].mass
            self.velY = (Planet.G * sunMass / self.x) ** 0.5

        Planet.cuonter += 1
        Planet.list_of_planet.append(self)

    def count_gravity_force(self):
        sumForceX = sumForceY = 0
        for planet in Planet.list_of_planet:
            if planet == self:
                continue
            distance = ((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2) ** 0.5
            force = Planet.G * ((planet.mass * self.mass) / distance**2)

            angle = math.atan2(planet.y - self.y, planet.x - self.x)

            forceY = force * math.cos(angle)
            forceX = force * math.sin(angle)

            sumForceX += forceY * Planet.TIMESTEP
            sumForceY += forceX * Planet.TIMESTEP
        return sumForceX, sumForceY

    def apply_forces(self):
        forceX, forceY = self.count_gravity_force()

        self.velX += forceX / self.mass
        self.velY += forceY / self.mass

        self.x += self.velX * Planet.TIMESTEP
        self.y += self.velY * Planet.TIMESTEP

    def draw(self):
        x = (self.x - offsetX) * Planet.SCALE + SCREEN_WIDTH/2
        y = (self.y - offsetY) * Planet.SCALE + SCREEN_HEIGHT/2

        scaleRadius = self.radius * Planet.SCALE

        pygame.draw.circle(screen, self.color, (x, y), scaleRadius)
        pygame.draw.rect(screen, self.color, Rect(x, y-10, 1, 10))




    @staticmethod
    def draw_all_planets():
        for planet in Planet.list_of_planet:
            planet.draw()

    @staticmethod
    def update_all_planets():
        for planet in Planet.list_of_planet:
            planet.apply_forces()


def lerp(start, stop, interpolation):
    return start + (stop - start) * interpolation

# Odpalenie modułów pygame
pygame.init()

# Parametry Screena
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

offsetX = offsetY = 0


def main():
    global offsetX, offsetY
    targetScale = 200 / Planet.AU

    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 1392000, (255, 255, 0), 1.98892 * 10 ** 30)
    mercury = Planet(0.387 * Planet.AU, 0, 4879, (121, 133, 124), 3.30 * 10 ** 23)
    venus = Planet(0.723 * Planet.AU, 0, 12104, (193,143,23), 4.8685 * 10 ** 24)
    earth = Planet(Planet.AU, 0, 12756, (0, 0, 200), 29)
    mars = Planet(1.524 * Planet.AU, 0, 6805, (121, 133, 124), 1.98892 * 10 ** 23)
    jupiter = Planet(5.20 * Planet.AU, 0, 142984, (188, 39, 50), 1.90 * 10 ** 27)
    saturn = Planet(9.539 * Planet.AU, 0, 120536, (255, 255, 0), 5.69 * 10 ** 26)
    uranus = Planet(19.18 * Planet.AU, 0, 51118, (0, 0, 255), 8.68 * 10 ** 25)
    neptune = Planet(30.06 * Planet.AU, 0, 49528, (255, 255, 255), 1.02 * 10 ** 26)


    # Pętla gry
    running = True
    while running:

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            offsetY -= 10/Planet.SCALE
        if keys[K_s]:
            offsetY += 10/Planet.SCALE
        if keys[K_d]:
            offsetX += 10/Planet.SCALE
        if keys[K_a]:
            offsetX -= 10/Planet.SCALE


        # LOGIKA GRY (w przyszłości):
        Planet.SCALE = lerp(Planet.SCALE, targetScale, 0.13)
        Planet.update_all_planets()

        # RYSOWANIE GRAFIKI:

        # Wypełnienie okienka kolorem
        screen.fill((0, 0, 0))

        # Rysowanie kształtów w PyGame
        Planet.draw_all_planets()

        # Czekanie na kolejną klatkę
        clock.tick(60)

        left, middle, right = pygame.mouse.get_pressed()

        moveMouse = pygame.mouse.get_rel()
        if left:
            offsetX = offsetX - moveMouse[0] / Planet.SCALE
            offsetY = offsetY - moveMouse[1] / Planet.SCALE

        #Aktualizacja gry
        pygame.display.flip()



        # Te cztery linijki pozwalają nam normalnie zamknąć program
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                targetScale *= 1.02 ** (event.y * 2.5)
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

main()