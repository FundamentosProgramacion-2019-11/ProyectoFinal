# encoding: UTF-8
# Autor: José Luis Macías
# ¡Acaba a los clones de la chica super poderosa tiempo record durante la cena! ¡Usa barra espaciadora, flechas y clic para jugar!

import math

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)

#Ship
xShip=(ANCHO//2)-64
yShip= (ALTO//2)+128
#Enemy
xEnemy= (ANCHO//2)-123
yEnemy=(0)
DX= +5
#fondo
xFondo=0

#Movimiento senoidal de la nave
angulo = 0

# Estructura básica de un programa que usa pygame para dibujar



def dibujarMenu(ventana, btnPlay):
    ventana.blit(btnPlay, (((ANCHO//2)-250),((ALTO//2))-23))

def dibujarFondo(ventana, gameBackground):
    global xFondo
    ventana.blit(gameBackground,(xFondo,0))
    xFondo-=0

def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse!= -1:
        pygame.draw.circle(ventana,AZUL,(xMouse,yMouse),55)


def dibujarShip(ventana, ship):
    ventana.blit(ship,(xShip,yShip))

def dibujarEnemy(ventana, enemy):
    global xEnemy, DX, yEnemy, angulo
    ventana.blit(enemy,(xEnemy,yEnemy))
    xEnemy += DX
    if (xEnemy >= ANCHO-256) or xEnemy <=0 :
        DX=-DX
    dy = int(20*math.sin(math.radians(angulo)))+20
    yEnemy = dy
    angulo += 10

def dibujarBullet(ventana, spriteBullet):
    if spriteBullet.rect.left != -1:
        ventana.blit(spriteBullet.image, spriteBullet.rect)
        spriteBullet.rect.top -= 20
        if spriteBullet.rect.top < -32:
            spriteBullet.rect.left=-1


def probarColision(listaBalas, listaEnemigos):
    #xdxd
    for bala in listaBalas:
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo)== True:
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                return True


def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render("Puntos: " + str(marcador), 1, ROJO)
    ventana.blit(texto, (ANCHO-350,10))


def dibujarTiempo(ventana,marcador1,fuente1):
    texto1 = fuente1.render("Tiempo: " + str(marcador1), 1, ROJO)
    ventana.blit(texto1, (ANCHO - 700, 10))

def dibujarAtaque(ventana, spriteAtaque):
    if spriteAtaque.rect.left != -1:
        ventana.blit(spriteAtaque.image, spriteAtaque.rect)
        spriteAtaque.rect.top += 20
        if spriteAtaque.rect.top < -32:
            spriteAtaque.rect.left=-1


def generarEnemigos(listaEnemigos, imgEnemigo):
    for y in range(50, 301, 100):
        for x in range(0, 670, 133):
            spriteEnemy = pygame.sprite.Sprite()
            spriteEnemy.image = imgEnemigo
            spriteEnemy.rect = imgEnemigo.get_rect()
            spriteEnemy.rect.left = x
            spriteEnemy.rect.top = y
            listaEnemigos.append(spriteEnemy) #conjunto de enemigos, cuando esta lista está vacia, lendpasas nombre de la lista y te dice cuantos objetos hay
    #en termina juego grabo el tiempo que utilice para eliminar a todos
    #meter boton en el meníu para consultar marcador
    #pantalla que diga gané o perdí

def dibujarListaEnemigos(ventana, listaEnemigos):
    for enemy in listaEnemigos:
        ventana.blit(enemy.image, enemy.rect)


def verificarColision(listaEnemigos, spriteBullet):
    for enemy in listaEnemigos:
        if enemy .rect.colliderect(spriteBullet) == True:
            listaEnemigos.remove(enemy)
            spriteBullet.rect.left=-5


def dibujarListaBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.top -= 20


def dibujar():
    global xShip, yShip
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    btnPlay = pygame.image.load("button (12).png")
    gameBackground=pygame.image.load("Mystery-Inc-Gang.jpg")
    ship=pygame.image.load("2.png")
    enemy=pygame.image.load("bombon.png")
    bullet=pygame.image.load("pizza1.png")

    #Lista de enemigos
    listaEnemigos = []
    generarEnemigos(listaEnemigos, enemy)
    listaBalas = []

    #Sprites
    spriteBullet= pygame.sprite.Sprite()
    spriteBullet.image=bullet
    spriteBullet.rect=bullet.get_rect()
    spriteBullet.rect.left= -1
    spriteBullet.rect.top= -1
    #Enemy Attack
    spriteAtaque = pygame.sprite.Sprite()
    spriteAtaque.image = bullet
    spriteAtaque.rect = bullet.get_rect()
    spriteAtaque.rect.left = -1
    spriteAtaque.rect.top = -1

    #Audio
    pygame.mixer.init()
    shoot = pygame.mixer.Sound("cartoon-throw.wav")
    pygame.mixer.music.load("scooby70.mp3")
    pygame.mixer.music.play(-1)

    xMouse = -1
    yMouse = -1

    #Estados
    MENU=1
    JUGANDO=2
    TERMINO=3
    estado=MENU

    # Texto
    fuente = pygame.font.SysFont("Century Gothic", 56)
    fuente1 = pygame.font.SysFont("Century Gothic", 56)
    marcador = 0

    #Tiempos
    tiempoAtaque = 58
    marcador1 = 200 #Tiempo inicial del cronometro en retroceso
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        marcador1 -= 1

        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if (xMouse > 150 and xMouse < 629) and (yMouse > 277 and yMouse < 341):
                    xMouse=-1
                    estado=JUGANDO
                if (xMouse > ANCHO//2 and xMouse < (ANCHO//2)+130 ) and (yMouse > ALTO//2 and yMouse < (ALTO//2)+50):
                    estado = MENU
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    xShip+=20
                elif evento.key == pygame.K_LEFT:
                    xShip-=20
                elif evento.key == pygame.K_UP:
                    yShip-=20
                elif evento.key == pygame.K_DOWN:
                    yShip+=20
                elif evento.key == pygame.K_SPACE:
                    nuevaBala=pygame.sprite.Sprite()
                    nuevaBala.image = bullet
                    nuevaBala.rect = bullet.get_rect()
                    nuevaBala.rect.left = xShip+62
                    nuevaBala.rect.top = yShip -5
                    listaBalas.append(nuevaBala)


                    if spriteBullet.rect.left == -1:
                        spriteBullet.rect.left = xShip + 62
                        spriteBullet.rect.top = yShip - 5
                        shoot.play()





        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado==MENU:
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, btnPlay)
        elif estado==JUGANDO:
            if marcador1 <= 0:
                estado=3
            tiempoAtaque -=   1
            if tiempoAtaque == 0:
                spriteAtaque.rect.left = xEnemy+128
                spriteAtaque.rect.top = yEnemy
                tiempoAtaque = 110
            hayColision = probarColision(listaBalas, listaEnemigos)
            if hayColision == True:
                marcador += 500





            verificarColision(listaEnemigos,spriteBullet)

            moverBalas(listaBalas)

            dibujarFondo(ventana, gameBackground)
            dibujarShip(ventana, ship)
            dibujarEnemy(ventana,enemy)
            dibujarListaEnemigos(ventana, listaEnemigos)
            dibujarBullet(ventana, spriteBullet)
            dibujarListaBalas(ventana, listaBalas)
            dibujarAtaque(ventana, spriteAtaque)
            
            dibujarMarcador(ventana, marcador, fuente)
            dibujarTiempo(ventana,marcador1,fuente1)

        elif estado == TERMINO:

            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, btnPlay)
            textofinish = fuente.render("Tu score fue de: " + str(marcador), 1, ROJO)
            ventana.blit(textofinish, (ANCHO-700, ALTO//5))
            marcador1 = 300









        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()