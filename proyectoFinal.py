# encoding: UTF-8
# Autor: Luis Adrian Carmona Vilallobos
# Juego entre tanques

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO =800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)

# Estructura básica de un programa que usa pygame para dibujar
def dibujarCirculo(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 30)
def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego,(0,0))

def dibujarCampo(ventana,fondoCampo):
        ventana.blit(fondoCampo,(0,0))
def dibujarMenu(ventana, btnJugar1,btnComo,btnSalir):
    ventana.blit(btnJugar1, (300, 175))
    ventana.blit(btnComo, (300, 275))
    ventana.blit(btnSalir, (300, 375))

def dibujarTanques(ventana,imgTanque,xTanque,yTanque):
    ventana.blit(imgTanque, (xTanque, yTanque))


def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render("Puntos: "+str(puntos),1,VERDE_BANDERA)
    ventana.blit(texto,(345,50))


def dibujarBala(ventana,listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverbalas(listaBalas):
    for bala in listaBalas:

        bala.rect.right += 16
        #if bala.rect.top <-32: #s+alio de la pantalla
        #listaBalas.remove(bala)


def dibujarListaBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image,bala.rect)


def btnJugar(args):
    pass


def dibujarEnemy(ventana, Enemy, xEnemy, yEnemy):
    ventana.blit(Enemy, (xEnemy, yEnemy))



def verificarColision(listaBalas,listaEnemigos):
    for bala in listaBalas:
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo) == True: #prueba colosion
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                return True

def verificarColisionBalaEnemigo(spriteBala,spriteEnemy):  # , sprite enemigo

    xBala = spriteBala.rect.left
    yBala=spriteBala.rect.top
    xEnemigo = spriteEnemy.rect.left
    yEnemigo =spriteEnemy.rect.top
    if xBala >=xEnemigo and xBala<=xEnemigo+ 128:
        if yBala >= yEnemigo and yBala <= yEnemigo+63:
    #Colision, desaparece bala y enemigo
            #yEnemigo = -64
            spriteBala.rect.top = -44 # fuera de la pantalla
            #xEnemigo = -129

            return True
    return False



def verificarColision2(listaBalas,listaEnemigos):
    for bala in listaBalas:
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo) == True:
                listaEnemigos.remove(enemigo)
                return True
    return False


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    # Estados de movimiento
    QUIETO = 1
    DERECHA = 2
    IZQUIERDA = 3
    #SONIDO
    pygame.mixer.init()
    # sonido corto  Sound -- wav
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    
    #IMAGENES
    fondoJuego= pygame.image.load("fondojuego.jpg")
    btnJugar1 = pygame.image.load("btnJgar1.png")
    btnComo = pygame.image.load("btnJugar2.png")
    btnSalir = pygame.image.load("btnSalir.png")
    fondoCampo = pygame.image.load("batalla.png")
    #imgTanque = pygame.image.load("RED.png")
    #Tanque
    xTanque = 50
    yTanqye = 520
    width = 46
    height = 46
    vel = 5
    #Eenemy
    xEnemy = 750
    yEnemy = 505
    #PUNTOS
    puntos = 0
    run = True
    #Sprites
    #Sprites balas
    imgBala = pygame.image.load("balaCanon.png")


    #SpriteEnemigo2
    imgEnemigo2 = pygame.image.load("TGREEN.png")
    spriteEnemigo2 = pygame.sprite.Sprite()
    spriteEnemigo2.image = imgEnemigo2
    spriteEnemigo2.rect = imgEnemigo2.get_rect()
    spriteEnemigo2.rect.left = -1
    #SpriteTanque
    imgTanque = pygame.image.load("TBLUE.png")
    spriteTanque = pygame.sprite.Sprite()
    spriteTanque.image = imgTanque
    spriteTanque.rect = imgTanque.get_rect()
    spriteTanque.rect.left = -1

    #spriteTanqueEnemigo
    Enemy = pygame.image.load("TNARANJA.png")
    spriteEnemy = pygame.sprite.Sprite()
    spriteEnemy.image = Enemy
    spriteEnemy.rect = Enemy.get_rect()
    spriteEnemy.rect.left =-1
    # COORDENADAS CIRCULO
    xMouse = -1
    yMouse = -1


    #ESTADOS
    MENU = 1
    JUGANDO = 2
    ESTADO = MENU


    # LISTA BALAS
    listaBalas = []  # Lista vacia


    # LISTA DE ENEMIGOS
    listaEnemigos = [spriteEnemy,spriteEnemigo2]

    # TEXTO
    fuente = pygame.font.SysFont("arial", 40)
    # puntos
    puntos = 0  # NO ES GLOBAL


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse,yMouse = pygame.mouse.get_pos()
                if xMouse>=300 and xMouse<=500 and yMouse>= 175 and yMouse <=225:
                    xMouse =-1
                    #CAMBIA EL ESTADO
                    ESTADO = JUGANDO # PASA A JUGAR
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if len(listaBalas) < 2:
                        spriteBala = pygame.sprite.Sprite()
                        spriteBala.image = imgBala
                        spriteBala.rect = imgBala.get_rect()
                        spriteBala.rect.left = spriteTanque.rect.left + spriteTanque.rect.width / 2  # xTanque +- 16
                        spriteBala.rect.top = spriteTanque.rect.bottom
                        listaBalas.append(spriteBala)

                    efectoDisparo.play()
                    spriteBala.rect.left = xTanque + 64 - 16  # poscisiones, Proyecto(getWidth...)
                    spriteBala.rect.top = yTanqye


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and xTanque >vel:
            xTanque -= vel
        if keys[pygame.K_RIGHT] and xTanque <200 -width-vel:
            xTanque += vel
        if keys[pygame.K_UP] and yTanqye < vel:
            yTanqye -= vel
        if keys[pygame.K_DOWN] and yTanqye >600-height-vel:
            yTanqye += vel


            #No importa que tecla

        # Borrar pantalla
        #ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        if ESTADO == MENU:
            dibujarCirculo(ventana, xMouse, yMouse)
            dibujarFondo(ventana,fondoJuego)
            dibujarMenu(ventana,btnJugar1,btnComo,btnSalir)
        elif ESTADO == JUGANDO:
            resultado = verificarColision(listaBalas,listaEnemigos)
            #resultado = verificarColision(listaBalas,spriteEnemy,puntos)

            if resultado == True:
                puntos += 500

            moverbalas(listaBalas)
            dibujarCampo(ventana,fondoCampo)
            dibujarTanques(ventana,imgTanque,xTanque,yTanqye)
            moverbalas(listaBalas)
            dibujarListaBalas(ventana, listaBalas)
            dibujarEnemy(ventana,Enemy,xEnemy,yEnemy)
            verificarColision2(listaBalas,listaEnemigos)
            dibujarMarcador(ventana,fuente,puntos)
            #verificarColisionBalaEnemigo(spriteBala, spriteEnemy)
            #MOVER PERSONAJE




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()