import math, random
import time, sys, os, random
import pygame
from pygame.locals import *

pygame.init()
#window size
#iniciar windows de jogo
comp_win = 1000
alt_win = 600


win = pygame.display.set_mode((comp_win, alt_win))
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.update()

###############################JOGADOR##################

xpos = int(comp_win / 2)
ypos = int(alt_win*0.67)
xpos1 = 200
ypos1 = 400
raioJog = 5

xposCursor = 0
yposCursor = 0

dx = 0
dy = 0

cx = 0
yx = 0

vx = 0
vy = 0

xposVetor = 0
yposVetor = 0

label = 0

inter = 0

distance = 0

ang = 0
angInter = 0

circle = pygame.draw.circle(win, (255,0,0), (xpos, ypos), raioJog)

v1 = 0

dt = 0.1

def getAceleration(x,y,x1,y1):

    d = math.sqrt(((x-x1)**2)+((y-y1)**2))

    return d

def getAngle(x,y,x1,y1):

    dy = y - y1

    dx = x - x1

    angulo = math.atan2(dy,dx)

    return angulo


###############################EXTRAS##################
#loadimagens

inImg = pygame.image.load(os.path.join("/Users/carlosguedes/Desktop/ESMAD/ESMAD---Licenciatura-TSIW---Carlos-Guedes/2-1/FAP/PROJETO/FAP PRO/IMG/inimigo.png")).convert_alpha()
bombImg = pygame.image.load(os.path.join("/Users/carlosguedes/Desktop/ESMAD/ESMAD---Licenciatura-TSIW---Carlos-Guedes/2-1/FAP/PROJETO/FAP PRO/IMG/cherries.png")).convert_alpha()
lifeImg = pygame.image.load(os.path.join("/Users/carlosguedes/Desktop/ESMAD/ESMAD---Licenciatura-TSIW---Carlos-Guedes/2-1/FAP/PROJETO/FAP PRO/IMG/heart.png")).convert_alpha()
playerImg=pygame.image.load(os.path.join("/Users/carlosguedes/Desktop/ESMAD/ESMAD---Licenciatura-TSIW---Carlos-Guedes/2-1/FAP/PROJETO/FAP PRO/IMG/player.png")).convert_alpha()
backGround=pygame.image.load(os.path.join("/Users/carlosguedes/Desktop/ESMAD/ESMAD---Licenciatura-TSIW---Carlos-Guedes/2-1/FAP/PROJETO/FAP PRO/IMG/backgroud.jpg")).convert()
scaled_bk=pygame.transform.scale(backGround,( comp_win,alt_win))
currentScale=2*15
scaled=pygame.transform.scale(playerImg,( currentScale,currentScale))

#linha
pygame.draw.line(win,(255,255,255),(0,(alt_win*0.7)),(comp_win,(alt_win*0.7)),2)

#Vidas
vidas=5

def drawLifes(vidas):
    x=comp_win*0.8
    for y in range(0,vidas):
        #pygame.draw.rect(win, (255,128,0), (x,alt_win*0.9,20,20))
        win.blit(lifeImg,(x,alt_win*0.9))
        x+=25

#score
score=0

def drawText(score):
 
    text=pygame.font.SysFont('Consolas', 32).render('Score: '+str(score), True, pygame.color.Color('White'))
    win.blit(text, (10, alt_win*0.9))


#Game Over
def drawGameOver():
    gameOver=pygame.font.SysFont('Consolas', 32).render('Game Over!!!', True, pygame.color.Color('White'))
    win.blit(gameOver, (comp_win*0.38, alt_win/2))


####################INIMIGOS####################

y=0
x=0
 #comp e alt dos objetos
raio=20
#velocidade
speed=1
#numero de inimigos
nInimigos=20

def drawInimigos(nInimigos):

    inimigos= [nInimigos]


    for x in range(-1, nInimigos-1):

        ini_x=random.randint(0,comp_win)
      
        ini_y=random.randint(0,alt_win*0.45)

        inimigos.append(pygame.Rect(ini_x, ini_y, raio, raio))

    return inimigos

inimigos_ecra=drawInimigos(nInimigos)

####################BOMBAS####################
def drawBombs(nInimigos):
    nBombas=int(nInimigos/5)
    bombas= [nBombas]


    for x in range(-1, nBombas-1):

        ini_x=random.randint(0,comp_win)
      
        ini_y=random.randint(0,alt_win*0.45)
 
        bombas.append(pygame.Rect(ini_x, ini_y, raio, raio))
      
    return bombas

bombas_ecra=drawBombs(nInimigos)

####################vidas####################
def drawHelp(nInimigos):
    nHelps=int(nInimigos/20)
    helps= [nHelps]


    for x in range(-1, nHelps-1):

        ini_x=random.randint(0,comp_win)
      
        ini_y=random.randint(0,alt_win*0.45)
 
        helps.append(pygame.Rect(ini_x, ini_y, raio, raio))
      
    return helps

helps_ecra=drawHelp(nInimigos)
    
##################RUN##############################


while True:
    for event in pygame.event.get():
        pass
    
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    key_pressed = pygame.key.get_pressed()


    if key_pressed[K_SPACE]: 
        pygame.quit()
        sys.exit()


    ###########################INIMIGOS###################################

    #limpar window
    win.blit(scaled_bk, (0, 0))
    ##desenhar score
    drawText(score)
    ###Desenha as vidas
    drawLifes(vidas)
    #desenhar inimigos
    if vidas<=0:
        drawGameOver()
    else:
        #desenhar inimigos
        for x in range(1, len(inimigos_ecra)):
        
            #quando chegarem ao limite do ecra passam para baixo
            if inimigos_ecra[x].left>=comp_win:inimigos_ecra[x].top+=40; inimigos_ecra[x].left=0
            #guardar coordenadas do inimigo
            coordX = inimigos_ecra[x].left
            coordY = inimigos_ecra[x].top
            coordX=coordX+speed
            #desenhar inimigo
            #pygame.draw.rect(win, (0,0,0), (coordX,coordY,raio,raio))
            win.blit(inImg,(coordX,coordY))
            inimigos_ecra[x].left=coordX
        
         #desenhar bombas
        for x in range(1, len(bombas_ecra)):
            #quando chegarem ao limite do ecra passam para baixo
            if bombas_ecra[x].left>=comp_win:bombas_ecra[x].top+=40; bombas_ecra[x].left=0
            #guardar coordenadas da bomba
            coordX = bombas_ecra[x].left
            coordY = bombas_ecra[x].top
            coordX=coordX+speed
            #desenhar bomba
            #pygame.draw.rect(win, (255,42,42), (coordX,coordY,raio,raio))
            win.blit(bombImg,(coordX,coordY))
            bombas_ecra[x].left=coordX

         #desenhar helps
        for x in range(1, len(helps_ecra)):
            #quando chegarem ao limite do ecra passam para baixo
            if helps_ecra[x].left>=comp_win:helps_ecra[x].top+=40; helps_ecra[x].left=0
            #guardar coordenadas da bomba
            coordX = helps_ecra[x].left
            coordY = helps_ecra[x].top
            coordX=coordX+speed
            #desenhar bomba
            #pygame.draw.rect(win, (0,255,0), (coordX,coordY,raio,raio))
            win.blit(helpImg,(coordX,coordY))
            helps_ecra[x].left=coordX

     

    ################################JOGADOR#######################################



        #print("tecla_premida : ", key_pressed)

        v1 = int(distance * dt)
        vx = v1
        vy = v1


        xposVetor, yposVetor = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN: distance = getAceleration(xpos,ypos,xposVetor,yposVetor); ang = getAngle(xpos,ypos,xposVetor,yposVetor);cx = int(vx * math.cos(ang));yx = int(vy * math.sin(ang));label = 1

        if label == 0:

           # circle = pygame.draw.circle(win, (0,0,0), (xpos, ypos), raioJog)
            new_rect=scaled.get_rect()
            win.blit(scaled,(xpos-new_rect.center[0],ypos-new_rect.center[1]))
            line = pygame.draw.line(win, (255,255,0), (xpos, ypos), (xposVetor, yposVetor), 4)


        if label == 1:

                if xpos + raioJog >= comp_win:
        
                    cx = -cx
            
                if ypos + (raioJog) >= alt_win - 5:

                    yx = -yx

                if ypos - raioJog <= 2:

                    yx = -yx

                if xpos - raioJog <= 0:
            
                    cx = -cx

                xpos += cx
                ypos += yx

                #circle = pygame.draw.circle(win, (0,0,0), (xpos, ypos), raioJog)
                #guardar coordenadas do jogador
                new_rect=scaled.get_rect()
                #desenhar jogador
                win.blit(scaled,(xpos-new_rect.center[0],ypos-new_rect.center[1]))

                

        

        ###############################EXTRAS##################
        #linha
        pygame.draw.line(win,(255,255,255),(0,(alt_win*0.8)),(comp_win,(alt_win*0.8)),2)

        #bola atravessa linha
        if ypos+ raio>=alt_win*0.8:label=0;xpos = int(comp_win / 2);ypos = int(alt_win*0.67)


        ###############################COLISOES#################
        for x in range(1,len(inimigos_ecra)):

            #guardar coordenadas doo inimigo
            coordIniX=inimigos_ecra[x].left
            coordIniY=inimigos_ecra[x].top
            
            if (xpos+raioJog >= (coordIniX ) and ypos + raioJog >= (coordIniY) and ypos - raioJog <= (coordIniY + raio) and xpos - raioJog <= (coordIniX+raio))and(label==1):
            
                del inimigos_ecra[x]
                raioJog+=1
                currentScale+=1
                scaled=pygame.transform.scale(playerImg,( currentScale,currentScale))
                new_rect=scaled.get_rect()
                win.blit(scaled,(xpos-new_rect.center[0],ypos-new_rect.center[1]))
                score+=1000
                if(score==70000):speed=speed+1
                if(score==140000):speed=speed+2
                #gerar posições random para mais um inimigo
                ini_x=random.randint(0,comp_win)
                ini_y=random.randint(0,alt_win*0.20)
                #adicionar ao array inimigos_ecra
                inimigos_ecra.append(pygame.Rect(ini_x, ini_y, raio, raio))
                break

            if  coordIniY+raio>=(alt_win*0.8): 
                vidas-=1
                del inimigos_ecra[x]
                #gerar posições random para mais um inimigo
                ini_x=random.randint(0,comp_win)
                ini_y=random.randint(0,alt_win*0.20)
                #adicionar ao array inimigos_ecra
                inimigos_ecra.append(pygame.Rect(ini_x, ini_y, raio, raio))
                break



        for x in range(1,len(bombas_ecra)):

            coordIniX=bombas_ecra[x].left
            coordIniY=bombas_ecra[x].top

            if (xpos+raioJog >= (coordIniX ) and ypos + raioJog >= (coordIniY) and ypos - raioJog <= (coordIniY + raio) and xpos - raioJog <= (coordIniX+raio))and(label==1):
            
                del bombas_ecra[x]
                raioJog=int(raioJog*2/3)
                score-=2000
                vidas-=1
                ini_x=random.randint(0,comp_win)
      
                ini_y=random.randint(0,alt_win*0.20)

                currentScale=int(currentScale/2)
                scaled=pygame.transform.scale(playerImg,( currentScale,currentScale))
                new_rect=scaled.get_rect()
                win.blit(scaled,(xpos-new_rect.center[0],ypos-new_rect.center[1]))

                #rects.append()
                bombas_ecra.append(pygame.Rect(ini_x, ini_y, raio, raio))
                break

        #helps
        for x in range(1,len(helps_ecra)):

            coordIniX=helps_ecra[x].left
            coordIniY=helps_ecra[x].top

            if (xpos+raioJog >= (coordIniX ) and ypos + raioJog >= (coordIniY) and ypos - raioJog <= (coordIniY + raio) and xpos - raioJog <= (coordIniX+raio))and(label==1):
            
                if(vidas<=4):
                    del helps_ecra[x]
                    vidas+=1
                    ini_x=random.randint(0,comp_win)
      
                    ini_y=random.randint(0,alt_win*0.20)

                    #rects.append()
                    helps_ecra.append(pygame.Rect(ini_x, ini_y, raio, raio))
                break

      
           


    #atualizar_pygame
    pygame.display.flip()
    #intervalo
    time.sleep(0.01)


   

input("para terminar prima <CR>")

pygame.quit()










