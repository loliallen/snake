import pygame
import random
version = "Snake v1.2.0"
display_width, display_heigth = 600, 400

pygame.init()
win = pygame.display.set_mode((display_width, display_heigth))
pygame.display.set_caption(version)
clock = pygame.time.Clock()

class Apple(object):
    def __init__(self):
        self.x, self.y = round(random.random()*display_width)//10 * 10 + 5, round(random.random()*display_heigth)//10 * 10 + 5
    def draw(self, win):
        pygame.draw.circle(win,(126, 184, 122),(self.x,self.y),5)

class Snake(object):
    speed = 10

    def __init__(self,x,y,win):
        self.x, self.y = (x,y)
        self.win = win
        self.body = [[x,y],[x-self.speed, y],[x-2*self.speed,y]]

    def draw(self):
        for i in self.body:

            pygame.draw.rect(self.win,(255,255,255),(i[0],i[1],10,10))

    def move(self,direction):
        point = self.body[0]
        # print(direction)
        # print(self.body)
        if(direction == "left"):
            self.body.insert(0,[point[0]-self.speed,point[1]])
        if(direction == "right"):
            self.body.insert(0,[point[0]+self.speed,point[1]])
        if(direction == "down"):
            self.body.insert(0,[point[0],point[1]+self.speed])
        if(direction == "up"):
            self.body.insert(0,[point[0],point[1]-self.speed])

        self.body.pop()

    def eat(self, direction):
        point = self.body[0]
        # print(direction)
        # print(self.body)
        if(direction == "left"):
            self.body.insert(0,[point[0]-self.speed,point[1]])
        if(direction == "right"):
            self.body.insert(0,[point[0]+self.speed,point[1]])
        if(direction == "down"):
            self.body.insert(0,[point[0],point[1]+self.speed])
        if(direction == "up"):
            self.body.insert(0,[point[0],point[1]-self.speed])

# menu = Menu(win,width, heigth)
# in_Menu = True
inGame = True
#
# while in_Menu:
#     pygame.time.delay(100)
#
#
#     if False:
apple = Apple()
snake = Snake(50,50,win)
paused = False

state = "right"


while inGame:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    for i in snake.body:
        if(i[0] > display_width):
            i[0] = 0
        if(i[0] < 0):
            i[0] = display_width-10
        if(i[1] > display_heigth):
            i[1] = 0
        if(i[1] < 0):
            i[1] = display_heigth-10



    head = snake.body[0]
    for i in range(1,len(snake.body)):
        if head == snake.body[i]:
            inGame = False
            print("Stop eat")
            break
    print("<------------------->")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False

    if keys[pygame.K_LEFT] and not(state == "right"):
        state = "left"
    if keys[pygame.K_RIGHT] and not(state == "left"):
        state = "right"
    if keys[pygame.K_DOWN] and not(state == "up"):
        state = "down"
    if keys[pygame.K_UP] and not(state == "down"):
        state = "up"


    if keys[pygame.K_m]:
        snake.eat(state)

    snake.move(state)

    s_x, s_y = snake.body[0][0], snake.body[0][1]

    if (s_x >= apple.x - 5 and s_x < apple.x + 5):
        if(s_y < apple.y + 5 and s_y >= apple.y - 5):
            apple = Apple()
            snake.eat(state)

    if keys[pygame.K_ESCAPE]:
        inGame = False





    win.fill((0,0,0))

    # pygame.draw.circle(win,(255,255,255), (0, 0), 10)
    snake.draw()
    apple.draw(win)
    pygame.display.update()
    # menu.draw()
    # pygame.display.update()



pygame.quit()
