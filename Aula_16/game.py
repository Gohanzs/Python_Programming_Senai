import pygame
import random
import sys

pygame.init()

Largura = 800
Altura = 400

tela = pygame.display.set_mode(Largura,Altura)
pygame.display.set_caption("Jogo de obstaculos")

#variaveis do jogo
# carregando das imagens
trex1 = pyame.image.load('assets/trex1.png')
trex2 = pygame.image.load('assets/trext2.png')
trex3 = pygame.image.load('assets/trext3.png')
ob1 = pygame.image.load('assets1/ob1.png')
ob2 = pygame.image.load('assets/ob2.png')
chao = pygame.image.load('assets/g1.png')


trex_x = 800
trex_y = 300

vel_y = 0
gravidade = 1
pulando = False
chao_x = 0
cact_x = 800
cact_y = 300

frame = 0

#texto na tela

pontuacao = 0
fonte = pygame.fonte.SysFont('arial', 30)
gameover = False


for event in pygame.event.get():
    if event.tipe == pygame.QUIT:
        pygame.quit()
        sys.exit
    if event.type == pyame.KEYDOWN:
        if event.type == pygame.K_SPACE and not pulando:
            vel_y = -12
            pulando = True
        if event.key.K_r and gameover:
            trex_x = 300
            cact_x = 800
            pontuacao = 0
            gameover = False
if not gameover:
    vel_y +=gravidade
    trex_x += vel_y
    if trex_y >= 300:
        trex_y = 300
        pulando = False
    chao -=5
    if chao_x <= -800:
        chao_x = 0
    cact_x -=5
    if cact_x < -50:
        cact_x = random.randint(800,100)
        pontuacao += 1
    frame +=1
    if frame > 20:
        frame = 0
    if frame < 10:
        trex2