from pygame import *
from random import *
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption("Пинг-Понг")
background = transform.scale(image.load('galaxy.jpg'),(700,500))
lost = 0
score = 0
class GameSprite(sprite.Sprite):
    def __init__(self, picture, pos_1, pos_2, speed, width, height):
        super(). __init__()
        self.image = transform.scale(image.load(picture),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_1
        self.rect.y = pos_2
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket1 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((200,255,255))
        racket1.update_1()
        racket.update_r()
        racket1.reset()
        racket2.reset()



        display.update()
        clock.tick(FPS)     

