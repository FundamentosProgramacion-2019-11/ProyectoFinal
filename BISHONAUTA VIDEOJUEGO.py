
import pygame   # Librería de pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

DX = +12
DX1 = +12
DX2 = +12



#FONDO
xFondo = 0

def dibujarMenu(ventana,menuJuego):
    ventana.blit(menuJuego,(0,0))



def dibujarFondo (ventana, fondoJuego):
    global xFondo
    ventana.blit(fondoJuego, (xFondo,0))
    #xFondo -= 0.3


def dibujarBisho (ventana, spriteBisho):
    ventana.blit(spriteBisho.image, spriteBisho.rect)


def dibujarAlien1 (ventana, spriteA1):
    global DX
    ventana.blit(spriteA1.image, spriteA1.rect)
    spriteA1.rect.left += DX
    if spriteA1.rect.left >= (ANCHO-315) or spriteA1.rect.left <= 300:
        DX = -DX

def dibujarAlien4(ventana,spriteA4):
    global DX1
    ventana.blit(spriteA4.image, spriteA4.rect)
    spriteA4.rect.left += DX1
    if spriteA4.rect.left >= (ANCHO-310) or spriteA4.rect.left <=300:
        DX1 = -DX1

def dibujarAlien3 (ventana, spriteA3):
    global DX2
    ventana.blit(spriteA3.image, spriteA3.rect)
    spriteA3.rect.left += DX2
    if spriteA3.rect.left >= (ANCHO-300) or spriteA3.rect.left <= 300:
        DX2 = -DX2


def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render ("Puntos: " + str(marcador),1 ,BLANCO)
    ventana.blit(texto,(50,50))

def dibujarLaser (ventana, spriteLaser):
    if spriteLaser.rect.left != -1:
        ventana.blit(spriteLaser.image, spriteLaser.rect)
        spriteLaser.rect.left += 20
        if spriteLaser.rect.left < -32:
            spriteLaser.rect.left = -1

def dibujarVidas (ventana, vidas, fuente):
    texto = fuente.render ("Vidas: " + str(vidas),1, BLANCO)
    ventana.blit(texto, (250, 50))

def generarMonedas (listaMonedas, moneda):
    for y in range (200,600, 150):
        for x in range(200, 800, 133):
            spriteMon = pygame.sprite.Sprite()
            spriteMon.image = moneda
            spriteMon.rect = moneda.get_rect()
            spriteMon.rect.left = x
            spriteMon.rect.top = y
            listaMonedas.append(spriteMon)

def dibujarListaMonedas (ventana, listaMonedas):
    for moneda in listaMonedas:
        ventana.blit(moneda.image, moneda.rect)

def verificarColisionMonedas(listaMonedas,spriteBisho):
    for moneda in listaMonedas:
        if moneda.rect.colliderect(spriteBisho) == True:
            listaMonedas.remove(moneda)


def probarColision(spriteLaser,spriteA1, spriteA4, spriteA3):
    if spriteLaser.rect.colliderect(spriteA1) == True:
        spriteA1.rect.top += 200
    elif spriteLaser.rect.colliderect(spriteA4) == True:
        spriteA4.rect.top -= 400
    elif spriteLaser.rect.colliderect(spriteA3) == True:
        spriteA3.rect.top -= 300


def dibujarGameOver (ventana,gameOver):
    ventana.blit(gameOver, (0,0))


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #IMAGENES
    fondoJuego = pygame.image.load ("FONDO BISHONAUTA.jpg")
    bishonauta = pygame.image.load ("BISHONAUTA.png")
    menuJuego = pygame.image.load("MENU BISHONAUTA.jpg")
    alien1 = pygame.image.load ("ALIEN1.png")
    alien2 = pygame.image.load("ALIEN2.png")
    alien3 = pygame.image.load("ALIEN3.png")
    alien4 = pygame.image.load("ALIEN4.png")
    laser = pygame.image.load ("LASER1.png")
    moneda = pygame.image.load ("MONEDA1.png")
    gameOver = pygame.image.load ("GAME OVER.jpg")

    #LISTA MONEDAS
    listaMonedas = []
    generarMonedas(listaMonedas, moneda)



    #SPRITES
    spriteBisho = pygame.sprite.Sprite()
    spriteBisho.image = bishonauta
    spriteBisho.rect = bishonauta.get_rect() #datos de la imagen
    spriteBisho.rect.left = -2
    spriteBisho.rect.top = 350

    spriteLaser = pygame.sprite.Sprite()
    spriteLaser.image = laser
    spriteLaser.rect = laser.get_rect()
    spriteLaser.rect.left = -1
    spriteLaser.rect.top = -1

    spriteA1 = pygame.sprite.Sprite()
    spriteA1.image = alien1
    spriteA1.rect = alien1.get_rect()
    spriteA1.rect.left = ANCHO//2
    spriteA1.rect.top = 400

    spriteA2 = pygame.sprite.Sprite()
    spriteA2.image = alien2
    spriteA2.rect = alien2.get_rect()

    spriteA3 = pygame.sprite.Sprite()
    spriteA3.image = alien3
    spriteA3.rect = alien1.get_rect()
    spriteA3.rect.left = 490
    spriteA3.rect.top = 80

    spriteA4 = pygame.sprite.Sprite()
    spriteA4.image = alien4
    spriteA4.rect = alien1.get_rect()
    spriteA4.rect.left = 300
    spriteA4.rect.top = 250





    #ESTADOS
    MENU = 1
    JUGANDO = 2
    GAMEOVER = 3
    estado = MENU

    #TEXTO
    fuente = pygame.font.SysFont("Ultra",45)
    marcador = 0
    vidas = 3
    monedas = 0

    #TIEMPOS
    tiempoataque = 120

    #AUDIO
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    gameOv = pygame.mixer.Sound("GAME OVER.wav")
    pygame.mixer.music.load("MUSICA BISHONAUTA1.mp3")
    pygame.mixer.music.play(-1)




    #EVENTOS
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse,yMouse)
                if xMouse >= 193 and xMouse <= 620 and yMouse >=250 and yMouse <= 344: #SE OPRIMIÓ BOTÓN DE JUGAR
                    xMouse = -1
                    estado = JUGANDO



            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    spriteBisho.rect.left += 12
                elif evento.key == pygame.K_LEFT:
                    spriteBisho.rect.left -= 12
                elif evento.key == pygame.K_UP:
                    spriteBisho.rect.top -=12
                elif evento.key == pygame.K_DOWN:
                    spriteBisho.rect.top +=12
                elif evento.key == pygame.K_SPACE:

                    if spriteLaser.rect.left == -1:
                       spriteLaser.rect.left = spriteBisho.rect.left+64-12
                       spriteLaser.rect.top = spriteBisho.rect.top + 50
                       efectoDisparo.play()

                if estado == GAMEOVER:
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        xMouse, yMouse = pygame.mouse.get_pos()
                        if xMouse >= 235 and xMouse <= 485 and yMouse >= 172 and yMouse <= 485: #SE OPRIMO EN BOTÓN HOME
                            xmouse = -1
                            estado = MENU




        # Borrar pantalla
        ventana.fill(BLANCO)

        if estado == MENU:
            dibujarMenu(ventana, menuJuego)
        elif estado == JUGANDO:

            #DIBUJAR
            dibujarFondo(ventana,fondoJuego)
            dibujarBisho(ventana, spriteBisho)
            dibujarAlien1(ventana, spriteA1)
            dibujarAlien4(ventana, spriteA4)
            dibujarAlien3(ventana, spriteA3)
            dibujarMarcador(ventana, marcador, fuente)
            dibujarLaser(ventana, spriteLaser)
            dibujarVidas(ventana, vidas, fuente)
            dibujarListaMonedas(ventana, listaMonedas)



            #ACTUALIZAR
            tiempoataque -= 1
            if tiempoataque == 0:
                spriteA4.rect.left = random.randint(0, ANCHO-100)
                spriteA4.rect.top = random.randint (0, ALTO-133)
                tiempoataque = 120

            colisionMoneda = verificarColisionMonedas(listaMonedas, spriteBisho)
            if colisionMoneda == True:
                monedas += 1
            hayColision = probarColision(spriteLaser, spriteA1, spriteA3, spriteA4)
            if hayColision == True:
                marcador += 500
            if spriteBisho.rect.colliderect(spriteA4) == True:
                vidas -= 1
                spriteA4.rect.top -= 400
                if vidas == 0:
                    estado = GAMEOVER
                    gameOv.play()

        elif estado == GAMEOVER:
            dibujarGameOver(ventana, gameOver)





        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()