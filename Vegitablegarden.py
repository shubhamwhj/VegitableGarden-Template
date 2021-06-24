
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
tomatoes=[]
mushrooms=[]
carrots=[]
brinjals=[]
pumpkins=[]

for i in range(1,6):
    tomatoes.append(pygame.Rect(i*60,50,40,40))

        
while True:    
    screen.fill((30,80,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             
    for tomato in tomatoes:        
        pygame.draw.rect(screen,(223,50,20),tomato)
    
    
    pygame.display.update()
    clock.tick(30)

