import pygame

pygame.init()

SCREEN_WIDTH = 1200 
SCEEEN_HEIGHT = 1200 
SNAKE_X_START=300
SNAKE_Y_START=250
SNAKE_HEIGHT=40
SNAKE_LENGTH=40
SCREEN_COLOR=(50,205,50)
SNAKE_COLOR="black"
SPEED=3

screen=pygame.display.set_mode((SCREEN_WIDTH,SCEEEN_HEIGHT))

pygame.display.set_caption("Snaaake dash")

snake = pygame.Rect((SNAKE_X_START,SNAKE_Y_START,SNAKE_HEIGHT,SNAKE_LENGTH))


run=True

while run:
       screen.fill(SCREEN_COLOR)

       pygame.draw.rect(screen,SNAKE_COLOR,snake)

       for event in pygame.event.get():
           if event.type==pygame.QUIT:
              run = False
      

       pygame.time.delay(SPEED)    
       if snake.x>=600:
         snake.update(0,snake.y,SNAKE_HEIGHT,SNAKE_LENGTH)
       elif snake.x<=0:
         snake.update(600,snake.y,SNAKE_HEIGHT,SNAKE_LENGTH)

       if snake.y>=600:
         snake.update(snake.x,0,SNAKE_HEIGHT,SNAKE_LENGTH)
       elif snake.y<=0:
         snake.update(snake.x,600,SNAKE_HEIGHT,SNAKE_LENGTH)

       key=pygame.key.get_pressed()
       if key[pygame.K_UP]==True:
          snake.move_ip(0,-1) 
       if key[pygame.K_DOWN]==True:
          snake.move_ip(0,1)
       if key[pygame.K_LEFT]==True:
          snake.move_ip(-1,0)
       if key[pygame.K_RIGHT]==True:
          snake.move_ip(1,0) 

      
       
       pygame.display.update()
pygame.quit()
