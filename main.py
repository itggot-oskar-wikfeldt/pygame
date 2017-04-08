import pygame
import math
from src import spritesheet, input

pygame.init()

displayw = 800
displayh = 600
window = pygame.display.set_mode((displayw, displayh))

windowclock = pygame.time.Clock()

ss = spritesheet.spritesheet('res/spritesheet.png')
# Sprite is 16x16 pixels at location 0,0 in the file...

# Load two images into an array, their transparent bit is (255, 255, 255)
texwidth = 42
texheight = 32
taxi = []
taxi = ss.load_strip((6, 12, texwidth, texheight), 3, colorkey=(186, 254, 202))
pink = []
pink = ss.load_strip((6, 140, texwidth, texheight), 3, colorkey=(186, 254, 202))

background = pygame.Surface((displayw, displayh))
sky = pygame.Surface((displayw, displayh*0.2))
background.fill((0, 255, 100))
sky.fill((0, 230, 255))
road_width = 600

for i in range(len(pink)):
    pink[i] = pygame.transform.scale(pink[i], (84, 64))


# Main Class
class MainRun(object):
    def __init__(self):
        self.dw = displayw
        self.dh = displayh
        self.car = Car(50, 50, 0)
        self.camera = Camera(self.car)

        self.run()

    def run(self):
        running = True

        while running:
            window.fill((255, 255, 255))

            self.dir = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    input.invoke(event.key, event.type)

            self.update()
            self.render()

            pygame.display.update()
            windowclock.tick(60)

    def update(self):
        self.car.update()
        self.camera.update()
        self.update_road()


    def render(self):
        window.blit(background, (0, 0))
        window.blit(sky,(0,0))
        self.car.draw()


    def update_road(self):
        background.fill((0, 255, 100))
        for i in range(int(0.2 * displayh), displayh):
            scale = i / displayh
            width = (road_width * scale)
            x = math.sin((self.camera.z + i)*0.01) * 100 + displayw/2
            for j in range(int(x - width/2), int(x + width / 2)):
                background.set_at((j, i), (100, 100, 100))


class Car:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dir = 0

    def update(self):
        self.z+= 10
        if input.is_key_down(pygame.K_LEFT):
            self.dir = -1
        elif input.is_key_down(pygame.K_RIGHT):
            self.dir = 1
        else:
            self.dir = 0

    def draw(self):
        window.blit(pink[self.dir + 1], (displayw / 2 - texwidth, displayh / 2))


class Camera:
    def __init__(self, target):
        self.target = target
        self.x = target.x
        self.z = target.z

    def update(self):
        self.x = self.target.x
        self.z = self.target.z

if __name__ == "__main__":
    MainRun()
