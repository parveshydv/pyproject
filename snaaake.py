import pygame

pygame.init()

SCREEN_WIDTH = 800
SCEEEN_HEIGHT = 600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCEEEN_HEIGHT))
snake = pygame.Rect((300,250,40,40))

run=True

while run:
       screen.fill((50,205,50))
       pygame.draw.rect(screen,(255,255,255),snake)

       key=pygame.key.get_pressed()
       if key[pygame.K_UP]==True:
          snake.move_ip(0,-1) 
       if key[pygame.K_DOWN]==True:
          snake.move_ip(0,1)
       if key[pygame.K_LEFT]==True:
          snake.move_ip(-1,0)
       if key[pygame.K_RIGHT]==True:
          snake.move_ip(1,0)      

       for event in pygame.event.get():
           if event.type==pygame.QUIT:
              run = False
       pygame.display.update(
)
pygame.quit()
