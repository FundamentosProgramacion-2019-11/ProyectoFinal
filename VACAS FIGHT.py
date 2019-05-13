# encoding: UTF-8
# Autor: Sofia Trujillo Vargas
# Juego sobre una vaca peleando contra las almendras y cocos

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
NEGRO = (0,0,0)
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

xVaca = ANCHO//2
yVaca = ALTO//2

xAlmendra = ANCHO//2
yAlmendra = 0

xCoco = ANCHO//2
yCoco = 0

xCoco2 = ANCHO//2
yCoco2 = 0

xAlmendra2 = ANCHO//2
yAlmendra2 = 0

m = ""
marcador = 0
DX = +20
angulo = 0

Enemigosm = 0

def dibujarMenu(ventana,fondo,boton,bt1):
    ventana.blit(fondo,(0,0))
    ventana.blit(boton,(350,300))
    ventana.blit(bt1,(320,400))

def dibujarInsti(ventana,inst,bt2):
    ventana.blit(inst,(0,0))
    ventana.blit(bt2,(313,376))


def dibujarVaca(ventana,vacas):
    ventana.blit(vacas,(xVaca,yVaca))


def dibujarMouse(ventana,xMouse,yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana,BLANCO,(xMouse,yMouse),5)

def dibujarPantalla(ventana,pantalla):
    ventana.blit(pantalla,(0,0))

def dibujarGanaste(ventana,ganaste):
    ventana.blit(ganaste,(0,0))

def dibujarBala(ventana,spritebala):
    if spritebala.rect.left != -1:
        ventana.blit(spritebala.image,spritebala.rect)
        spritebala.rect.top -= 20
        if spritebala.rect.top < -40:
            spritebala.rect.left = -1

def moverBalas(listaBalas):
    for vaso in listaBalas:
        vaso.rect.top -= 20

def dibujarAlmendra(ventana,almendra):
    global xAlmendra, DX, yAlmendra,angulo
    ventana.blit(almendra,(xAlmendra,yAlmendra))
    xAlmendra += DX
    if xAlmendra == ANCHO-300 or xAlmendra <= 0:
        DX = -DX
    #Mover en y
    dy = int(20*math.sin(math.radians(angulo)))
    yAlmendra = dy
    angulo += 30

def dibujarAlmendra2(ventana,almendra):
    global xAlmendra2, DX, yAlmendra2,angulo
    ventana.blit(almendra,(xAlmendra2,246))
    xAlmendra2 += DX
    if xAlmendra2 == ANCHO-300 or xAlmendra2 <= 0:
        DX = -DX
    #Mover en y
    dy = int(20*math.sin(math.radians(angulo)))
    yAlmendra2 = dy
    angulo += 30


def dibujarCoco(ventana,coco):
    global xCoco, DX, yCoco,angulo
    ventana.blit(coco,(xCoco,146))
    xCoco += DX
    if xCoco == ANCHO-300 or xCoco <= 0:
        DX = -DX
    #Mover en y
    dy = int(20*math.sin(math.radians(angulo)))
    yCoco = dy
    angulo += 50

def dibujarCoco2(ventana,coco):
    global xCoco2, DX, yCoco2,angulo
    ventana.blit(coco,(xCoco2,346))
    xCoco2 += DX
    if xCoco2 == ANCHO-300 or xCoco2 <= 0:
        DX = -DX
    #Mover en y
    dy = int(20*math.sin(math.radians(angulo)))
    yCoco2 = dy
    angulo += 50


def dibujarMarcador(ventana,marcador,fuente):
    texto = fuente.render("Puntos: "+str(marcador),1,BLANCO)
    ventana.blit(texto,(10,500))

def dibujarTitulo(ventana,marcador,fuente):
    texto = fuente.render("VACA´S FIGHT" + str(m),1,BLANCO)
    ventana.blit(texto,(12,546))



def probarColision(spritebala):
    global xAlmendra, yAlmedra
    xBala = spritebala.rect.left
    yBala = spritebala.rect.top
    if xBala >= xAlmendra and xBala <= xAlmendra+128 and yBala >= yAlmendra and yBala <= yAlmendra+80:
        xAlmendra = -5000
        print("Hay Colision")
        return True




def probarColision2(spritebala):
    global xCoco, yCoco
    xBala = spritebala.rect.left
    yBala = spritebala.rect.top
    if xBala >= xCoco and xBala <= xCoco+128 and yBala >= yCoco and yBala <= yCoco+80:
        xCoco = -5000
        print("Hay colision")
        return True

def probarColision3(spritebala):
    global xAlmendra2, yAlmendra2
    xBala = spritebala.rect.left
    yBala = spritebala.rect.top
    if xBala >= xAlmendra2 and xBala <= xAlmendra2+128 and yBala >= yAlmendra2 and yBala <= yAlmendra2+80:
        xAlmendra2 = -5000
        print("Hay colision")
        return True

def dibujarLeche(ventana,spriteleche):
    if spriteleche.rect.left != -1:
        ventana.blit(spriteleche.image,spriteleche.rect)
        spriteleche.rect.top += 10
        if spriteleche.rect.top < -75:
            spriteleche.rect.left = -1

def dibujarGanaste(ventana,ganaste):
    ventana.blit(ganaste,(0,0))

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    global yVaca
    global xVaca
    global marcador
    global Enemigosm
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #TIEMPO
    tiempoAtaque = 200

    #MOUSE
    xMouse = -1
    yMouse = -1

    #ESTADOS
    MENU = 1
    JUGANDO = 3
    HISTI = 2
    estado = MENU
    PERDI = 4

    #IMAGENES
    boton = pygame.image.load("btt.png")
    vacas = pygame.image.load("vacas.png")
    fondo = pygame.image.load("fondo.png")
    bala = pygame.image.load("vaso.png")
    pantalla = pygame.image.load("de.png")
    almendra = pygame.image.load("almendra.png")
    coco = pygame.image.load("coco.png")
    inst = pygame.image.load("instrucciones.png")
    bt1 = pygame.image.load("bt1.png")
    bt2 = pygame.image.load("bt2.png")
    ganaste = pygame.image.load("ganar.png")

    #Musica
    pygame.mixer.init()
    pygame.mixer.music.load("robot rock.mp3")
    pygame.mixer.music.play(-1)

    #SPRITES
    spritebala = pygame.sprite.Sprite()
    spritebala.image = bala
    spritebala.rect = bala.get_rect()
    spritebala.rect.left = -1
    spritebala.rect.top = -1



    #TEXTO
    fuente = pygame.font.SysFont("Fixedsys Normal", 30)

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse,yMouse = pygame.mouse.get_pos()
                print(xMouse,yMouse)
                if xMouse>=300 and xMouse<=500 and yMouse>=275 and yMouse<=325:
                    xMouse=-1
                    yMouse=-1
                    estado = JUGANDO
                if xMouse>=324 and xMouse>=486 and yMouse>=400 and yMouse<=404:
                    estado = HISTI
                    if xMouse>=319 and 427<=xMouse and yMouse>=382 and 479<=yMouse:
                        estado = JUGANDO
            elif evento.type == pygame.KEYDOWN:  # Oprimio una tecla
                # Verificar que tecla se oprimio
                if evento.key == pygame.K_UP:
                    yVaca -= 20
                if evento.key == pygame.K_RIGHT:
                    xVaca += 20
                elif evento.key == pygame.K_LEFT:
                    xVaca -= 20
                elif evento.key == pygame.K_DOWN:
                    yVaca += 20
                elif evento.key == pygame.K_SPACE:
                    if spritebala.rect.left == -1:
                        spritebala.rect.left = xVaca
                        spritebala.rect.top = yVaca



        if estado == MENU:
            dibujarMenu(ventana,fondo,boton,bt1)
            dibujarMouse(ventana,xMouse,yMouse)

        elif estado == HISTI:
            dibujarInsti(ventana, inst, bt2)
            dibujarMouse(ventana, xMouse, yMouse)
            if xMouse>=319 and 427<=xMouse and yMouse>=382 and 479<=yMouse:
                estado = JUGANDO


        elif estado == JUGANDO:


            dibujarPantalla(ventana,pantalla)
            dibujarVaca(ventana,vacas)
            dibujarBala(ventana,spritebala)
            dibujarMarcador(ventana,marcador,fuente)
            dibujarTitulo(ventana,marcador,fuente)
            dibujarAlmendra(ventana,almendra)
            dibujarAlmendra2(ventana,almendra)
            dibujarCoco(ventana,coco)
            if probarColision(spritebala) == True:
                xAlmendra = -100
                yAlmedra = -100
                marcador += 50
                Enemigosm +=1
            if probarColision2(spritebala) == True:
                xCoco = -100
                yCoco = -100
                marcador += 50
                Enemigosm += 1
            if probarColision3(spritebala) == True:
                xAlmendra2 = -100
                yAlmendra2 = -100
                Enemigosm += 1
                marcador += 50
            if Enemigosm == 3:
                dibujarGanaste(ventana,ganaste)
                print(marcador)





        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja



# Llamas a la función principal
main()