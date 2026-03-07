import pygame


pygame.init()
tamanho  =  300,150
screen = pygame.display.set_mode(tamanho)

px = 150
py = 75

run = True
while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         screen.fill('LightSkyBlue')
         
         pygame.draw.rect(screen,'black',(125,50,50,50) ) 
         pygame.draw.line(screen, 'red', (0,0), (300,150), width= 5)
         pygame.draw.ellipse(screen, (64, 255, 0),  (50,50, 100, 60))
         pygame.draw.circle(screen, (255, 0, 191), (px,py), 7,2)

         pygame.display.update()
         
pygame.quit()               
         
         
    


  



