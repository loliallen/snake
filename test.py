import pygame
pygame.init()
width, height = 600, 400
win = pygame.display.set_mode((width,height))
my_font = pygame.font.SysFont('Comic Sans MS',30)
button_width = 200
button_height = 50

def button(text):

    text_w, text_h = my_font.size(text)

    button_posX = (width - button_width)/2
    button_posY = (height - button_height)/2

    button = pygame.Rect(button_posX, button_posY, button_width, button_height)
    pygame.draw.rect(win,(0,0,0),button)
    textsurface = my_font.render(text,False,(255,255,255))
    win.blit(textsurface,(button_posX + button_width/2 - text_w/2,button_posY + button_height/2 - text_h/2))
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    win.fill((255,255,255))
    button("Press to play")
    pygame.time.delay(100)
    pygame.display.update()

pygame.quit()
