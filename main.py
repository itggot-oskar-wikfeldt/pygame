#Load and initialize Modules here
import pygame
from src import spritesheet
pygame.init()

#Window Information
displayw = 800
displayh = 600
window = pygame.display.set_mode((displayw,displayh))

#Clock
windowclock = pygame.time.Clock()

#Load other things such as images and sound files here
#image = pygame.image.load("foo.png").convert #Use conver_alpha() for images with transparency

ss = spritesheet.spritesheet('res/spritesheet.png')
# Sprite is 16x16 pixels at location 0,0 in the file...
images = []
# Load two images into an array, their transparent bit is (255, 255, 255)
width = 42
height = 42
images = ss.images_at(((6, 6, width, height),(6+width, 6, width, height), (6+width*2, 6, width, height)), colorkey=(186, 254, 202))

#Main Class
class MainRun(object):
    def __init__(self,displayw,displayh):
        self.dw = displayw
        self.dh = displayh
        self.Main()

    def update(self):
        pass


    def render(self):
        window.blit(images[self.dir+1], images[self.dir+1].get_rect())


    def Main(self):
        self.dir = 0
        stopped = False

        while stopped == False:
            window.fill((255,255,255)) #Tuple for filling display... Current is white

            #Event Tasking
            #Add all your event tasking things here
            self.dir = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.dir = -1
                    elif event.key == pygame.K_RIGHT:
                        self.dir = 1
                    else:
                        self.dir = 0

            self.render()

            #Also things like score updates or drawing additional items
            #Remember things on top get done first so they will update in the order yours is set at

            #Remember to update your clock and display at the end
            pygame.display.update()
            windowclock.tick(60)

            #If you need to reset variables here
            #This includes things like score resets

            #After your main loop throw in extra things such as a main menu or a pause menu
            #Make sure you throw them in your main loop somewhere where they can be activated by the user

#All player classes and object classes should be made outside of the main class and called inside the class
#The end of your code should look something like this
if __name__ == "__main__":
    MainRun(800, 600)