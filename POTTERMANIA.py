# encoding: UTF-8
# Autor: María Fernanda García Gastélum
# Juego de Harry Potter
import math

import pygame  # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)
AMARILLO = (240, 234, 66)

vidaUsuario = 14

# enemigo
DX = +10  # derecha, (-1)izquierda
vidaEnemigo = 100
angulo = 0
# FONDO
xFondo = 0
yFondo = 0



# Estructura básica de un programa que usa pygame para dibujar
def dibujarMenu(ventana, menu):
    ventana.blit(menu, (0, 0))  # calcular x, y, para centrar la imagen


def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 50)


def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0, 0))


def dibujarBackToMenu(ventana, backToMenu):
    ventana.blit(backToMenu, (0, 0))


def dibujarInstrucciones(ventana, instrucciones):
    ventana.blit(instrucciones, (0, 0))


def dibujarCasa(ventana, casa):
    ventana.blit(casa, (0, 0))


def dibujarCorazones(ventana, vida1, vida2, vida3, vida4, vida5, vida6, vida7, vida8, vida9, vida10,vida11, vida12, vida13, vida14):
    if vidaUsuario == 14:
        ventana.blit(vida14, (0,0))
    elif vidaUsuario == 13:
        ventana.blit(vida13, (0, 0))
    elif vidaUsuario == 12:
        ventana.blit(vida12, (0,0))
    elif vidaUsuario == 11:
        ventana.blit(vida11, (0,0))
    elif vidaUsuario == 10:
        ventana.blit(vida10, (0,0))
    elif vidaUsuario == 9:
        ventana.blit(vida9, (0,0))
    elif vidaUsuario == 8:
        ventana.blit(vida8, (0,0))
    elif vidaUsuario == 7:
        ventana.blit(vida7, (0,0))
    elif vidaUsuario == 6:
        ventana.blit(vida6, (0,0))
    elif vidaUsuario == 5:
        ventana.blit(vida5, (0,0))
    elif vidaUsuario == 4:
        ventana.blit(vida4, (0,0))
    elif vidaUsuario == 3:
        ventana.blit(vida3, (0,0))
    elif vidaUsuario == 2:
        ventana.blit(vida2, (0,0))
    elif vidaUsuario == 1:
        ventana.blit(vida1, (0,0))


def dibujarVidaEnemigo(ventana, vold10, vold20, vold30, vold40, vold50, vold60, vold70, vold80, vold90, vold100, vold0):
    if vidaEnemigo == 100:
        ventana.blit(vold100, (0,0))
    elif vidaEnemigo == 90:
        ventana.blit(vold90, (0,0))
    elif vidaEnemigo == 80:
        ventana.blit(vold80, (0,0))
    elif vidaEnemigo == 70:
        ventana.blit(vold70, (0,0))
    elif vidaEnemigo == 60:
        ventana.blit(vold60, (0,0))
    elif vidaEnemigo == 50:
        ventana.blit(vold50, (0,0))
    elif vidaEnemigo == 40:
        ventana.blit(vold40, (0,0))
    elif vidaEnemigo == 30:
        ventana.blit(vold30, (0,0))
    elif vidaEnemigo == 20:
        ventana.blit(vold20, (0,0))
    elif vidaEnemigo == 10:
        ventana.blit(vold10, (0,0))
    elif vidaEnemigo <= 0:
        ventana.blit(vold0, (0,0))


def dibujarBotonPausa(ventana, pause):
    ventana.blit(pause, (0, 0))


def dibujarVentanaPausa(ventana, pausedScreen):
    ventana.blit(pausedScreen, (0, 0))


def dibujarGanar(ventana, win):
    ventana.blit(win, (0, 0))


def dibujarPerder(ventana, lose):
    ventana.blit(lose, (0,0))


def dibujarBackToMenuInst(ventana, instBackToMenu):
    ventana.blit(instBackToMenu, (0, 0))


def dibujarNaveRavenclaw(ventana, usuarioRavenclaw):
    ventana.blit(usuarioRavenclaw.image, usuarioRavenclaw.rect)


def dibujarNaveSly(ventana, usuarioSly):
    ventana.blit(usuarioSly.image, usuarioSly.rect)


def dibujarNaveGryf(ventana, usuarioGryf):
    ventana.blit(usuarioGryf.image, usuarioGryf.rect)


def dibujarNaveHuf(ventana, usuarioHuf):
    ventana.blit(usuarioHuf.image, usuarioHuf.rect)


def dibujarEnemigo(ventana, voldemort, spriteLaserEnemigo, nave):
    global DX, angulo
    ventana.blit(voldemort.image, voldemort.rect)
    voldemort.rect.left += DX
    # probar choque contra pared
    if voldemort.rect.left >= ANCHO - 150 or voldemort.rect.left <= 0:
        DX = -DX
    #mover en y
    dy = int(20 * math.sin(math.radians(angulo))) + 100
    voldemort.rect.top = dy
    angulo += 6
    if voldemort.rect.left == nave.rect.left:
        spriteLaserEnemigo.rect.left = voldemort.rect.left + 50 - 6
        spriteLaserEnemigo.rect.top = nave.rect.top + 131
        if spriteLaserEnemigo> ALTO+50:
            spriteLaserEnemigo.rect.left = -1


def dibujarProyectilEnemigo(ventana, spriteLaserEnemigo):
    if spriteLaserEnemigo.rect.left != -1:
        ventana.blit(spriteLaserEnemigo.image, spriteLaserEnemigo.rect)
        spriteLaserEnemigo.rect.top += 10
        if spriteLaserEnemigo.rect.top > + 650:
            spriteLaserEnemigo.rect.left = -1


def colisionBoss(voldemort, listaLaser):
    global vidaEnemigo
    for laser in listaLaser:
        if voldemort.rect.colliderect(laser) == True:
            vidaEnemigo -= 10
            listaLaser.remove(laser)
            break


def naveColision(spriteLaserEnemigo, nave):
    global vidaUsuario
    if spriteLaserEnemigo.rect.colliderect(nave):
        vidaUsuario = vidaUsuario - 1
        spriteLaserEnemigo.rect.left = -1


def dibujarListaLaser(ventana, listaLaser):
    for laser in listaLaser:
        ventana.blit(laser.image, laser.rect)
        laser.rect.top -= 5
        if laser.rect.top < - 50:
            laser.remove()
            if laser.rect.top > + 650:
                laser.rect.left = -1


def dibujarTiempo(ventana, harryFontPuntaje, tiempoUsuario):
    text = harryFontPuntaje.render("Time: "+str(tiempoUsuario), True, AMARILLO)
    ventana.blit(text, (560, 555))


def dibujarListaTiempos(ventana, font, usuarioTiempo):
    text = font.render("Time in last game: "+ str(usuarioTiempo), True, NEGRO)
    ventana.blit(text, (300, 515))


def dibujar():
    global vidaEnemigo, hayColisionBoss, vidaUsuario
    # Voy a usar la variable global

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    # IMAGENES
    menu = pygame.image.load("Menú.png")
    instrucciones = pygame.image.load("Inst.png")
    fondoJuego = pygame.image.load("Hog.png")
    ravenclaw = pygame.image.load("Rav.png")
    gryffindor = pygame.image.load("Gryff.png")
    hufflepuff = pygame.image.load("Huff.png")
    slytherin = pygame.image.load("Sly.png")
    enemigoImagen = pygame.image.load("Voldi.png")
    laser = pygame.image.load("Harry.png")
    laserEnemigo = pygame.image.load("Avada.png")
    backToMenu = pygame.image.load("Back to menu.png")
    casa = pygame.image.load("Choose your house.png")
    pause = pygame.image.load("Pause.png")
    pausedScreen = pygame.image.load("paused.png")
    win = pygame.image.load("win.png")
    lose = pygame.image.load("lose.png")
    instBackToMenu = pygame.image.load("InstBackToMenu.png")
    #VIDAS DEL USUARIO
    vida14 = pygame.image.load("7H.png")
    vida13 = pygame.image.load("6.5H.png")
    vida12 = pygame.image.load("6H.png")
    vida11= pygame.image.load("5.5H.png")
    vida10 = pygame.image.load("5H.png")
    vida9 = pygame.image.load("4.5H.png")
    vida8 = pygame.image.load("4H.png")
    vida7 = pygame.image.load("3.5H.png")
    vida6 = pygame.image.load("3H.png")
    vida5 = pygame.image.load("2.5H.png")
    vida4 = pygame.image.load("2H.png")
    vida3 = pygame.image.load("1.5H.png")
    vida2 = pygame.image.load("1H.png")
    vida1 = pygame.image.load("0.5H.png")
    #VIDAS ENEMIGO
    vold100 = pygame.image.load("100Vold.png")
    vold90 = pygame.image.load("90Vold.png")
    vold80 = pygame.image.load("80Vold.png")
    vold70 = pygame.image.load("70Vold.png")
    vold60 = pygame.image.load("60Vold.png")
    vold50 = pygame.image.load("50Vold.png")
    vold40 = pygame.image.load("40Vold.png")
    vold30 = pygame.image.load("30Vold.png")
    vold20 = pygame.image.load("20Vold.png")
    vold10 = pygame.image.load("10Vold.png")
    vold0 = pygame.image.load("0Vold.png")

    #LISTA DE PROYECTILES
    listaLaser =[]
    #LISTA DE PUNTAJE
    listaTiempos = []

    # SPRITES
    #Laser del enemigoImagen
    spriteLaserEnemigo = pygame.sprite.Sprite()
    spriteLaserEnemigo.image = laserEnemigo
    spriteLaserEnemigo.rect = laserEnemigo.get_rect()
    spriteLaserEnemigo.rect.left = -1  # x
    spriteLaserEnemigo.rect.top = -1  # y

    #Sprite enemigo BOSS
    voldemort = pygame.sprite.Sprite()
    voldemort.image = enemigoImagen
    voldemort.rect = enemigoImagen.get_rect()
    voldemort.rect.left = 350
    voldemort.rect.top = 50

    # Sprite del usuario
    #RAVENCLAW
    usuarioRavenclaw = pygame.sprite.Sprite()
    usuarioRavenclaw.image = ravenclaw
    usuarioRavenclaw.rect = ravenclaw.get_rect()
    usuarioRavenclaw.rect.left = (ANCHO // 2) - 35
    usuarioRavenclaw.rect.top = (ALTO // 2) + 43.5
    #GRYFFINDOR
    usuarioGryf = pygame.sprite.Sprite()
    usuarioGryf.image = gryffindor
    usuarioGryf.rect = gryffindor.get_rect()
    usuarioGryf.rect.left = (ANCHO // 2) - 35
    usuarioGryf.rect.top = (ALTO // 2) + 43.5
    #SLYTHERIN
    usuarioSly = pygame.sprite.Sprite()
    usuarioSly.image = slytherin
    usuarioSly.rect = slytherin.get_rect()
    usuarioSly.rect.left = (ANCHO // 2) - 35
    usuarioSly.rect.top = (ALTO // 2) + 43.5
    #HUFFLEPUFF
    usuarioHuf = pygame.sprite.Sprite()
    usuarioHuf.image = hufflepuff
    usuarioHuf.rect = hufflepuff.get_rect()
    usuarioHuf.rect.left = (ANCHO // 2) - 35
    usuarioHuf.rect.top = (ALTO // 2) + 43.5


    # MOUSE
    xMouse = -1
    yMouse = -1


    # ESTADOS
    MENU = 1
    JUGANDO = 2
    INSTRUCCIONES = 3
    CASA = 4
    PAUSA = 5
    GANAR = 6
    PERDER = 7

    estado = MENU

    # AUDIO
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    fondo = pygame.mixer.music.load("FondoJuego.mp3")
    pygame.mixer.music.play(-1)  # infinito

    # FONTS
    harryFontPuntaje = pygame.font.SysFont("HARRYP_.TTF", 35)
    harryFontBestScore = pygame.font.SysFont("HARRYP_.TTF", 30)

    #TIEMPOS
    tiempoAtaque = 35
    tiempoUsuario = 0

    # MOVIMIENTOS
    movimientoDerecha = False
    movimientoIzquierda = False

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # oprimio el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
            elif estado == MENU:
                if xMouse >= 355 and xMouse <= 445 and yMouse >= 365 and yMouse <= 400:
                    # Oprimió el botón de Play, CAMBIAR el ESTADO
                    xMouse = -1
                    estado = CASA
                elif xMouse >= 270 and xMouse <= 530 and yMouse >= 445 and yMouse <= 470:
                    xMouse = -1
                    estado = INSTRUCCIONES
            elif estado == INSTRUCCIONES:
                if xMouse >= 22 and xMouse <= 150 and yMouse >= 22 and yMouse <= 45:
                    xMouse = -1
                    estado = MENU
            elif estado == CASA:
                if 55 <= xMouse <= 135 and 260 <= yMouse <= 405:
                    xMouse = -1
                    nave = usuarioRavenclaw
                    estado = JUGANDO
                    vidaUsuario = 14
                    vidaEnemigo = 100
                    voldemort.rect.left = 350
                    voldemort.rect.top = 50
                    nave.rect.left = (ANCHO // 2) - 35
                    nave.rect.top = (ALTO // 2) + 43.5
                    spriteLaserEnemigo.rect.left = -1
                    tiempoUsuario = 0
                elif 250 <= xMouse <= 350 and 260 <= yMouse <= 405:
                    xMouse = -1
                    estado = JUGANDO
                    nave = usuarioSly
                    vidaUsuario = 14
                    vidaEnemigo = 100
                    voldemort.rect.left = 350
                    voldemort.rect.top = 50
                    nave.rect.left = (ANCHO // 2) - 35
                    nave.rect.top = (ALTO // 2) + 43.5
                    spriteLaserEnemigo.rect.left = -1
                    tiempoUsuario = 0
                elif 445 <= xMouse <= 550 and 260 <= yMouse <= 405:
                    xMouse = -1
                    estado = JUGANDO
                    nave = usuarioGryf
                    vidaUsuario = 14
                    vidaEnemigo = 100
                    voldemort.rect.left = 350
                    voldemort.rect.top = 50
                    nave.rect.left = (ANCHO // 2) - 35
                    nave.rect.top = (ALTO // 2) + 43.5
                    spriteLaserEnemigo.rect.left = -1
                    tiempoUsuario = 0
                elif 655 <= xMouse <= 750 and 260 <= yMouse <= 405:
                    xMouse = -1
                    estado = JUGANDO
                    nave = usuarioHuf
                    vidaUsuario = 14
                    vidaEnemigo = 100
                    voldemort.rect.left = 350
                    voldemort.rect.top = 50
                    nave.rect.left = (ANCHO // 2) - 35
                    nave.rect.top = (ALTO // 2) + 43.5
                    spriteLaserEnemigo.rect.left = -1
                    tiempoUsuario = 0
            elif estado == JUGANDO:
                if evento.type == pygame.KEYDOWN:  # oprimió una tecla
                    # verificar que tecla se oprimió
                    if evento.key == pygame.K_RIGHT:
                        movimientoDerecha = True
                    elif evento.key == pygame.K_LEFT:
                        movimientoIzquierda = True
                    elif evento.key == pygame.K_SPACE:
                        nuevoLaser = pygame.sprite.Sprite()
                        nuevoLaser.image = laser
                        nuevoLaser.rect = laser.get_rect()
                        nuevoLaser.rect.left = nave.rect.left + 35-6
                        nuevoLaser.rect.top = nave.rect.top - 50
                        listaLaser.append(nuevoLaser)
                        efectoDisparo.play()
                    elif evento.key == pygame.K_ESCAPE:
                        estado = PAUSA
                elif evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_RIGHT:
                        movimientoDerecha = False
                    elif evento.key == pygame.K_LEFT:
                        movimientoIzquierda = False
                if xMouse >= 22 and xMouse <= 150 and yMouse >= 22 and yMouse <= 45:
                    xMouse = -1
                    estado = MENU
                if xMouse >= 705 and xMouse <= 755 and yMouse >= 18 and yMouse <= 41:
                    xMouse = -1
                    estado = PAUSA
                if vidaEnemigo == 0:
                    estado = GANAR
                if vidaUsuario == 0:
                    estado = PERDER
            elif estado == GANAR:
                listaTiempos.append(tiempoUsuario)
                if 22 <= xMouse <= 150 and 22 <= yMouse <= 45:
                    xMouse = -1
                    estado = MENU
            elif estado == PERDER:
                listaTiempos.append(tiempoUsuario)
                if 64 <= xMouse <= 276 and 425 <= yMouse <= 472:
                    estado = CASA
                if 510 <= xMouse <= 725 and 425 <= yMouse <= 472:
                    estado = MENU
            elif estado == PAUSA:
                if xMouse >= 480 and xMouse <= 705 and yMouse >= 425 and yMouse <= 470:
                    xMouse = -1
                    estado = MENU
                if xMouse >= 105 and xMouse <= 290 and yMouse >= 425 and yMouse <= 475:
                    xMouse = -1
                    estado = JUGANDO
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        estado = JUGANDO

        if movimientoDerecha:
            if nave.rect.left <= 800-85:
                nave.rect.left += 10
        elif movimientoIzquierda:
            if nave.rect.left >=15:
                nave.rect.left -= 10



        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, menu)
            dibujarListaTiempos(ventana, harryFontBestScore, tiempoUsuario)
        elif estado == INSTRUCCIONES:
            dibujarInstrucciones(ventana, instrucciones)
            dibujarBackToMenuInst(ventana, instBackToMenu)
        elif estado == JUGANDO:
            # ACTUALIZAR
            hayColisionBoss = colisionBoss(voldemort, listaLaser)
            tiempoAtaque -= 1
            tiempoUsuario += 1
            if tiempoAtaque == 0:
                spriteLaserEnemigo.rect.left = voldemort.rect.left + 50 - 6
                spriteLaserEnemigo.rect.top = voldemort.rect.top + 131
                tiempoAtaque = 35

            naveColision(spriteLaserEnemigo, nave)
            # DIBUJAR
            dibujarFondo(ventana, fondoJuego)
            if nave == usuarioRavenclaw:
                dibujarNaveRavenclaw(ventana, usuarioRavenclaw)
            elif nave == usuarioSly:
                dibujarNaveSly(ventana, usuarioSly)
            elif nave == usuarioGryf:
                dibujarNaveGryf(ventana, usuarioGryf)
            elif nave == usuarioHuf:
                dibujarNaveHuf(ventana, usuarioHuf)
            dibujarEnemigo(ventana, voldemort, spriteLaserEnemigo, nave)
            dibujarCorazones(ventana, vida1, vida2, vida3, vida4, vida5, vida6, vida7, vida8, vida9, vida10,vida11, vida12, vida13, vida14)
            dibujarVidaEnemigo(ventana, vold10, vold20, vold30, vold40, vold50, vold60, vold70, vold80, vold90, vold100, vold0)
            dibujarBotonPausa(ventana, pause)
            dibujarBackToMenu(ventana, backToMenu)
            dibujarProyectilEnemigo(ventana, spriteLaserEnemigo)
            dibujarListaLaser(ventana, listaLaser)
            dibujarTiempo(ventana, harryFontPuntaje, tiempoUsuario)

        elif estado == CASA:
            dibujarCasa(ventana, casa)

        elif estado == PAUSA:
            dibujarVentanaPausa(ventana, pausedScreen)

        elif estado == GANAR:
            dibujarGanar(ventana, win)
            dibujarBackToMenu(ventana, backToMenu)

        elif estado == PERDER:
            dibujarPerder(ventana, lose)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# Llamas a la función principal
main()