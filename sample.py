import os
import sys
import math
import pygame
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800 
SCEEEN_HEIGHT = 800
SNAKE_X_START=300
SNAKE_Y_START=250
FOOD_X_START = 200
FOOD_Y_START = 200
SNAKE_HEIGHT=40
SNAKE_LENGTH=40
SCREEN_COLOR="white"
SNAKE_COLOR="green"
FOOD_LENGTH=40
SPEED=3

screen=pygame.display.set_mode((SCREEN_WIDTH,SCEEEN_HEIGHT))
pygame.display.set_caption("Snaaake dash")
snake = pygame.Rect((SNAKE_X_START,SNAKE_Y_START,SNAKE_HEIGHT,SNAKE_LENGTH))
food = pygame.Rect((FOOD_X_START,FOOD_X_START,SNAKE_HEIGHT,SNAKE_LENGTH))

gameClock = pygame.time.Clock()

def delay(int):
    pygame.time.delay(SPEED)
    if snake.x>=800:
       snake.update(0,snake.y,SNAKE_HEIGHT,SNAKE_LENGTH)
    elif snake.x<=0:
       snake.update(800,snake.y,SNAKE_HEIGHT,SNAKE_LENGTH)

    if snake.y>=800:
       snake.update(snake.x,0,SNAKE_HEIGHT,SNAKE_LENGTH)
    elif snake.y<=0:
       snake.update(snake.x,800,SNAKE_HEIGHT,SNAKE_LENGTH)



def motion():
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]==True:
       snake.move_ip(0,-1)
    if key[pygame.K_DOWN]==True:
       snake.move_ip(0,1)
    if key[pygame.K_LEFT]==True:
       snake.move_ip(-1,0)
    if key[pygame.K_RIGHT]==True:
       snake.move_ip(1,0)

def size():
   if snake.x == food.x and snake.y == food.y:
      SNAKE_LENGTH = SNAKE_LENGTH + FOOD_LENGTH
      

run=True

while run:
       screen.fill(SCREEN_COLOR)
       pygame.draw.rect(screen,SNAKE_COLOR,snake)
       pygame.draw.rect(screen,SNAKE_COLOR,food)

       for event in pygame.event.get():
           if event.type==pygame.QUIT:
              run = False
      
       delay(SPEED)
       motion()
       size()
              
       pygame.display.update()
pygame.quit()



