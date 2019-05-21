# encoding: UTF-8
# Autor: Roberto Martínez Román
# Martha Margarita Dorantes Cordero
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla  (juego)

import pygame   # Librería de pygame
import time

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
CENTRO = (ANCHO//2, ALTO//2)

# Colores
BLANCO = (255, 255, 255)    # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = ( 0, 0, 0)

# COORDENADAS JUGADOR
xPlayer = ANCHO//2
yPlayer = ALTO//2

# COORDENADAS ENEMIGO
xEnemy = ANCHO //2
yEnemy = 10

# MAGNITUD DE MOVIMIENTO
DXP = 4
DXE = 2
DXB = 10

#EJE DE DISPARO
X = 0
Y = 1
ejeDisparo = Y

#Dibujar texto
def dibujaTexto(ventana, texto) :
    # Fill background
    instruc = pygame.Surface(ventana.get_size())
    instruc = instruc.convert()
    instruc.fill((0, 0, 0))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render(texto, 1, (250, 250, 250))
    textpos = text.get_rect()
    textpos.centery = instruc.get_rect().centery
    textpos.centerx = instruc.get_rect().centerx
    instruc.blit(text, textpos)
    # Blit everything to the screen
    ventana.blit(instruc, (0, 0))
    pygame.display.flip()
    

# Dibujar menu (botones)
def dibujarMenu(ventana, startButton) :
    ventana.blit(startButton, (ANCHO//2 - 150, ALTO//2 - 75))


# Dibujar menu (botones)
def dibujarFelicidades(ventana, felicidades) :
    ventana.blit(felicidades, (0, 0))


# Dibujar menu (botones)
def dibujarGameOver(ventana, terminado) :
    ventana.blit(terminado, (0, 0))


def crearSprite(spriteImage) :
    newSprite = pygame.sprite.Sprite()
    newSprite.image = spriteImage
    newSprite.rect = spriteImage.get_rect()
    #newSprite.rect.left = -1   # PARA que no se dibuje
    return newSprite


def posicionarJugador(playerSprite) :
    global xPlayer
    global yPlayer
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_UP] :
        yPlayer -= DXP
    if keyPressed[pygame.K_DOWN] :
        yPlayer += DXP
    if keyPressed[pygame.K_LEFT] :
        xPlayer -= DXP
    if keyPressed[pygame.K_RIGHT] :
        xPlayer += DXP
    playerSprite.rect.centerx = xPlayer
    playerSprite.rect.centery = yPlayer
    #ventana.blit(player, (xPlayer - 25, yPlayer - 25))


def posicionarEnemigo(enemySprite) :
    global xPlayer
    global yPlayer
    global xEnemy
    global yEnemy
    if xPlayer < xEnemy :
        xEnemy -= DXE
    if xPlayer > xEnemy :
        xEnemy += DXE
    if yPlayer < yEnemy :
        yEnemy -= DXE
    if yPlayer > yEnemy :
        yEnemy += DXE
    enemySprite.rect.centerx = xEnemy
    enemySprite.rect.centery = yEnemy
    #ventana.blit(enemy, (xEnemy - 25, yEnemy - 25))


def posicionarBala(balaSprite) :
    global xPlayer
    global yPlayer
    global xEnemy
    global yEnemy
    balaSprite.rect.centerx = xPlayer
    balaSprite.rect.centery = yPlayer
    balaSprite.tx = xEnemy
    balaSprite.ty = yEnemy
    if xPlayer < xEnemy :
        balaSprite.tx = xEnemy + ANCHO
    if xPlayer > xEnemy :
        balaSprite.tx = xEnemy - ANCHO
    if yPlayer < yEnemy :
        balaSprite.ty = yEnemy + ANCHO
    if yPlayer > yEnemy :
        balaSprite.ty = yEnemy - ANCHO


def actualizarBalas(balasGroup) :
    txReached = False
    tyReached = False
    for bala in balasGroup :
        if bala.rect.centerx > bala.tx :
            bala.rect.centerx -= DXB
        if bala.rect.centerx < bala.tx :
            bala.rect.centerx += DXB
        if bala.rect.centery > bala.ty :
            bala.rect.centery -= DXB
        if bala.rect.centery < bala.ty :
            bala.rect.centery += DXB
        if (bala.rect.centerx <= 0 or bala.rect.centerx >= ANCHO) or (bala.rect.centery <= 0 or bala.rect.centerx >= ALTO) :
            balasGroup.remove(bala)


def dibujar() :
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana donde dibujará
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #IMAGENES
    background = pygame.transform.scale(pygame.image.load("fondo.png"), (ANCHO,ALTO))
    startButton = pygame.transform.scale(pygame.image.load("button_jugar.png"), (300,150))
    felicidades = pygame.transform.scale(pygame.image.load("felicidades.gif"), (ANCHO,ALTO))
    terminado = pygame.transform.scale(pygame.image.load("terminado.jpg"), (ANCHO,ALTO))
    playerImage = pygame.transform.scale(pygame.image.load("player.png"), (50,50))
    enemyImage = pygame.transform.scale(pygame.image.load("enemy.png"), (50,50))
    balaImage = pygame.transform.scale(pygame.image.load("bala.png"), (30,30))
    
    #SPRITES
    playerSprite = crearSprite(playerImage)
    enemySprite = crearSprite(enemyImage)

    #GRUPOS DE SPRITES
    balasGroup = pygame.sprite.Group()
    enemiesGroup = pygame.sprite.Group()
    enemiesGroup.add(enemySprite)
    playersGroup = pygame.sprite.Group()
    playersGroup.add(playerSprite)

    #COORDENADAS MOUSE
    xMOUSE = 1
    yMOUSE = 1
    
    #ESTADOS
    MENU = 1
    JUGANDO = 2
    GANASTE = 3
    PERDISTE = 4
    estado = MENU

    dibujaTexto(ventana, "Bienvenidos al juego diablo no te lo lleves")
    time.sleep(2)
    dibujaTexto(ventana, "Desarrollado por Martha Margarita Dorantes Cordero")
    time.sleep(2)
    dibujaTexto(ventana, "Instrucciones")
    time.sleep(2)
    dibujaTexto(ventana, "Disparar = Barra espaciadora")
    time.sleep(2)
    dibujaTexto(ventana, "Mover = Teclas de navegación")
    time.sleep(2)
    while not termina :  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        ventana.blit(background, (0, 0))
        xMOUSE, yMOUSE = pygame.mouse.get_pos()

        if estado == MENU :
            dibujarMenu(ventana, startButton)
        elif estado == JUGANDO :
            posicionarJugador(playerSprite)
            posicionarEnemigo(enemySprite)
            actualizarBalas(balasGroup)
            enemiesGroup.draw(ventana)
            playersGroup.draw(ventana)
            balasGroup.draw(ventana)
            if pygame.sprite.spritecollide(enemySprite, balasGroup, True) :
                balasGroup.empty()
                estado = GANASTE
            if pygame.sprite.spritecollide(playerSprite, enemiesGroup, True) :
                balasGroup.empty()
                estado = PERDISTE
        elif estado == GANASTE :
            dibujarFelicidades(ventana, felicidades)
        elif estado == PERDISTE :
            dibujarGameOver(ventana, terminado)

        for evento in pygame.event.get() :
            if evento.type == pygame.QUIT :  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN and ANCHO//2 - 150 <= xMOUSE <= ANCHO//2 + 150 and ALTO//2 - 75 <= yMOUSE <= ALTO//2 + 75 :
                estado = JUGANDO  # PASA A JUGAR
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE :
                balaSprite = crearSprite(balaImage)
                balasGroup.add(balaSprite)
                posicionarBala(balaSprite, )

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()


# Llamas a la función principal
main()
