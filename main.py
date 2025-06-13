import sounddevice as sd
import numpy as np
import pygame

pygame.init()
screen = pygame.display.set_mode((475,200))
pygame.display.set_caption("Sound Visualizer")
pygame.display.set_icon(pygame.image.load("logo.png"))
run = True
volume_norm = 0
val = [0]*100
def print_sound(indata, outdata, frames, time, status):
    global volume_norm,val
    data = indata
    volume_norm = np.linalg.norm(data)*100
    #val = indata
    """
    if len(val) == 0 and False:
        print(True)
        val = [indata[i*14] fr i in range(0,round(len(indata)/14))]"""

    for i in range(0,round(len(data)/14)):
        if val[i] >= 0:
            if val[i] < data[i*14][0]:
                val[i] = data[i*14][0]
            else:
                val[i] = val[i] * 90 / 100
        else:
            if val[i] > data[i*14][0]:
                val[i] = data[i*14][0]
            else:
                val[i] = val[i] * 90 / 100


a = sd.Stream(callback=print_sound)
a.start()
bg = pygame.image.load("line2.png")
mainScreen = pygame.Surface((500,500),pygame.SRCALPHA)
while run:
    screen.fill((0,0,0))
    mainScreen.fill((0,0,0))
    pygame.draw.line(mainScreen,(0,0,0,0),(0,screen.get_height()-45),(volume_norm*4,screen.get_height()-45),5)
    [pygame.draw.line(mainScreen,(0,0,0,0),(i * 6,screen.get_height()-50),(i * 6,round(screen.get_height()-50-val[i]*5000)),5) for i in range(0,round(len(val)))]
    #[pygame.draw.line(mainScreen,(0,0,0,0),(i * 50,250),(i * 50,round(250+val[i][0]*800)),5) for i in range(0,round(len(val)))]
    screen.blit(bg,(0,0))
    screen.blit(mainScreen,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            a.stop()
    pygame.display.update()
pygame.quit()


