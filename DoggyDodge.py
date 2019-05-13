# Autor: Sofía Daniela Méndez Sandoval, A01242259, Grupo 03
# Descripción: Projecto Final - Videojuego Doggy Dodge

import pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600


BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

# VARIABLES GLOBALES
xPerro = 336
yPerro = 400


def dibujarMenu(ventana, btnJugar, fuente):

    ventana.blit(btnJugar, (0, -7))

    mejorPuntaje = open("GuardarMejorPuntaje", "r", encoding="UTF-8")
    mejoresPuntos = mejorPuntaje.read()

    texto2 = fuente.render(("Mejor Puntaje: %s" % str(mejoresPuntos)), 1, NEGRO)
    ventana.blit(texto2, (530, 120))


def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0, 0))


def dibujarPerro(ventana, spritePerro):
    ventana.blit(spritePerro.image, spritePerro.rect)


def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render(str(puntos), 1, BLANCO)
    ventana.blit(texto, (125, 35))


def generarChocolates(listaChocolates, imgChocolate):
    global yChocolate
    xChocolate = random.randint(1, 714)
    yChocolate = -30
    spriteChocolate = pygame.sprite.Sprite()
    spriteChocolate.image = imgChocolate
    spriteChocolate.rect = imgChocolate.get_rect()
    spriteChocolate.rect.left = xChocolate
    spriteChocolate.rect.top = yChocolate
    listaChocolates.append(spriteChocolate)


def generarGatos(listaGatos, reinicia):
    global yGato
    xGato = random.randint(1, 715)
    yGato = -72
    spriteGato = pygame.sprite.Sprite()
    spriteGato.image = reinicia
    spriteGato.rect = reinicia.get_rect()
    spriteGato.rect.left = xGato
    spriteGato.rect.top = yGato
    listaGatos.append(spriteGato)


def generarHuesos(listaHuesos, suma):
    global yHueso
    xHueso = random.randint(1, 718)
    yHueso = -20
    spriteHueso = pygame.sprite.Sprite()
    spriteHueso.image = suma
    spriteHueso.rect = suma.get_rect()
    spriteHueso.rect.left = xHueso
    spriteHueso.rect.top = yHueso
    listaHuesos.append(spriteHueso)


def generarZapatos(listaZapatos, resta):
    global yZapato
    xZapato = random.randint(1, 709)
    yZapato = -46
    spriteZapato = pygame.sprite.Sprite()
    spriteZapato.image = resta
    spriteZapato.rect = resta.get_rect()
    spriteZapato.rect.left = xZapato
    spriteZapato.rect.top = yZapato
    listaZapatos.append(spriteZapato)


def generarPelotas(listaPelotas, gana):
    global yPelota
    xPelota = random.randint(1, 762)
    yPelota = -39
    spritePelota = pygame.sprite.Sprite()
    spritePelota.image = gana
    spritePelota.rect = gana.get_rect()
    spritePelota.rect.left = xPelota
    spritePelota.rect.top = yPelota
    listaPelotas.append(spritePelota)


def dibujarListaChocolates(ventana, listaChocolates):
    for chocolate in listaChocolates:
        ventana.blit(chocolate.image, chocolate.rect)


def dibujarListaGatos(ventana, listaGatos):
    for gato in listaGatos:
        ventana.blit(gato.image, gato.rect)


def dibujarListaHuesos(ventana, listaHuesos):
    for hueso in listaHuesos:
        ventana.blit(hueso.image, hueso.rect)


def dibujarListaZapato(ventana, listaZapatos):
    for zapato in listaZapatos:
        ventana.blit(zapato.image, zapato.rect)


def dibujarListaPelotas(ventana, listaPelotas):
    for pelota in listaPelotas:
        ventana.blit(pelota.image, pelota.rect)


def verificarColisionesListaEnemigos(spritePerro, listaObjetos):
    for objeto in listaObjetos:
        if spritePerro.rect.colliderect(objeto):
            listaObjetos.remove(objeto)
            return True

    return False


def obtenerSpritePerro(imgPerro):
    spritePerro = pygame.sprite.Sprite()
    spritePerro.image = imgPerro
    spritePerro.rect = imgPerro.get_rect()
    spritePerro.rect.left = xPerro
    spritePerro.rect.top = yPerro
    return spritePerro


def moverEnemigos(listaChocolates, listaGatos, listaHuesos, listaZapatos, listaPelotas):

    for spriteChocolate in listaChocolates:
        spriteChocolate.rect.top += 5
        if spriteChocolate.rect.top >= 600:
            listaChocolates.remove(spriteChocolate)

    for spriteGato in listaGatos:
        spriteGato.rect.top += 8
        if spriteGato.rect.top >= 600:
            listaGatos.remove(spriteGato)

    for spriteHueso in listaHuesos:
        spriteHueso.rect.top += 10
        if spriteHueso.rect.top >= 600:
            listaHuesos.remove(spriteHueso)

    for spriteZapato in listaZapatos:
        spriteZapato.rect.top += 15
        if spriteZapato.rect.top >= 600:
            listaZapatos.remove(spriteZapato)

    for spritePelota in listaPelotas:
        spritePelota.rect.top += 20
        if spritePelota.rect.top >= 600:
            listaPelotas.remove(spritePelota)


def dibujar():

    global xPerro, yPerro
    teclaDer = False
    teclaIzq = False

    # Inicializa el motor de pygame
    pygame.init()

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    # IMAGENES
    btnJugar = pygame.image.load("DoggyPlay.png")
    fondoJuego = pygame.image.load("DoggyFondo.png")
    imgPerro = pygame.image.load("Doggy.png")
    imgChocolate = pygame.image.load("Chocolate.png")
    suma = pygame.image.load("Hueso.png")
    resta = pygame.image.load("Zapato.png")
    reinicia = pygame.image.load("Gato.png")
    gana = pygame.image.load("Pelota.png")
    pierdes = pygame.image.load("Perdiste.png")
    ganas = pygame.image.load("Ganaste.png")

    # ESTADOS
    global estado
    MENU = 1
    JUGANDO = 2
    PIERDES = 3
    GANAS = 4
    estado = MENU

    # AUDIO (SONIDO)
    pygame.mixer.init()

    # Sonido corto      Sound -- wav
    atrapaPelota = pygame.mixer.Sound("DogBark.wav")
    atrapaPelota.set_volume(1.5)


    # Sonido largo      Music -- mp3
    pygame.mixer.music.load("School_Bus_Shuffle.mp3")
    pygame.mixer.music.play()

    # TEXTO
    fuente = pygame.font.SysFont("Times New Roman", 40)
    fuenteGrande = pygame.font.SysFont("Times New Roman", 100)

    # Puntos (no es global)
    global puntos
    puntos = 0

    # LISTA DE OBJETOS
    listaChocolates = []
    listaGatos = []
    listaHuesos = []
    listaZapatos = []
    listaPelotas = []

    while not termina:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                termina = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if estado == MENU:
                    if 575 <= xMouse <= 750 and 165 <= yMouse <= 340:
                        estado = JUGANDO

                elif estado == GANAS:
                    if 515 <= xMouse <= 620 and 165 <= yMouse <= 330:
                        estado = JUGANDO

                elif estado == PIERDES:
                    if 135 <= xMouse <= 670 and 160 <= yMouse <= 460:
                        estado = JUGANDO

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclaDer = True

                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclaIzq = True

            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclaDer = False

                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclaIzq = False

        if teclaDer:
            xPerro += 10
        elif teclaIzq:
            xPerro -= 10

        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarMenu(ventana, btnJugar, fuente)

        elif estado == JUGANDO:
            spritePerro = obtenerSpritePerro(imgPerro)
            dibujarFondo(ventana, fondoJuego)

            if len(listaChocolates) <= 2:
                generarChocolates(listaChocolates, imgChocolate)
            if len(listaGatos) <= 1:
                generarGatos(listaGatos, reinicia)
            if len(listaHuesos) <= 5:
                generarHuesos(listaHuesos, suma)
            if len(listaZapatos) <= 4:
                generarZapatos(listaZapatos, resta)
            if len(listaPelotas) <= 0:
                generarPelotas(listaPelotas, gana)

            if verificarColisionesListaEnemigos(spritePerro, listaChocolates):
                estado = PIERDES

            elif verificarColisionesListaEnemigos(spritePerro, listaGatos):
                puntos = 0

            elif verificarColisionesListaEnemigos(spritePerro, listaHuesos):
                puntos += 10

            elif verificarColisionesListaEnemigos(spritePerro, listaZapatos):
                puntos -= 10

            elif verificarColisionesListaEnemigos(spritePerro, listaPelotas):
                estado = GANAS
                atrapaPelota.play()

            dibujarListaChocolates(ventana, listaChocolates)
            dibujarListaGatos(ventana, listaGatos)
            dibujarListaHuesos(ventana, listaHuesos)
            dibujarListaZapato(ventana, listaZapatos)
            dibujarListaPelotas(ventana, listaPelotas)

            dibujarPerro(ventana, spritePerro)

            dibujarMarcador(ventana, fuente, puntos)
            moverEnemigos(listaChocolates, listaGatos, listaHuesos, listaZapatos, listaPelotas)

        elif estado == PIERDES:
            texto = fuenteGrande.render(str(puntos), 1, BLANCO)
            ventana.blit(pierdes, (0, 0))
            ventana.blit(texto, (375, 125))

            mejorPuntaje = open("GuardarMejorPuntaje", "r", encoding="UTF-8")
            mejoresPuntos = mejorPuntaje.read()

            texto2 = fuente.render(str(mejoresPuntos), 1, BLANCO)
            ventana.blit(texto2, (375, 430))


        elif estado == GANAS:
            texto = fuenteGrande.render(str(puntos), 1, BLANCO)
            ventana.blit(ganas, (0, 0))
            ventana.blit(texto, (375, 125))

            mejorPuntaje = open("GuardarMejorPuntaje", "r", encoding="UTF-8")
            mejoresPuntos = mejorPuntaje.read()

            texto2 = fuente.render(str(mejoresPuntos), 1, BLANCO)
            ventana.blit(texto2, (375, 520))

            if int(mejoresPuntos) < puntos:
                mejor = open("GuardarMejorPuntaje", "w", encoding="UTF-8")
                mejor.write("%d" % puntos)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()


def main():
    dibujar()


main()