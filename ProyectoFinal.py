# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame  # Librería de pygame
import random as r
import math as m

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)  # ningun color, solo negro

# Fondo
xFondo = 0  # Global

# Movimiento senoidal de la nave
angulo = 0  # grados

# Cantidad de marcianos
cantidadMarcianos = 10


# Estructura básica de un programa que usa pygame para dibujar

def dibujarPlay(ventana, btnPlay):
    ventana.blit(btnPlay, (100, 500))  # Calcular (x,y) para centrar boton


def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, ROJO, (xMouse, yMouse), 20)


def dibujarExit(ventana, btnExit):
    ventana.blit(btnExit, (500, 500))


def dibujarSettings(ventana, btnSettings):
    ventana.blit(btnSettings, (670, 30))


def dibujarSound(ventana, btnSound):
    ventana.blit(btnSound, (650, 50))


def dibujarImagen(ventana, imagen):
    ventana.blit(imagen, (0, 0))


def dibujarFondo(ventana, imagenFondoJuego):
    ventana.blit(imagenFondoJuego, (xFondo, 0))
    # xFondo -= 1      si se quiere hacer que el fondo se desplace a la izquierda


def dibujarNave(ventana, spriteNave):
    ventana.blit(spriteNave.image, (spriteNave.rect.left, spriteNave.rect.top))


def dibujarMarcador(ventana, fuente, marcador):
    texto = fuente.render("Puntos: " + str(marcador), 1, ROJO)
    ventana.blit(texto, (0, 0))


def generarEnemigos(listaEnemigos, EnemigoPersonaje):
    for y in range(-50000, 0, 100 ):  # renglones(coordenada y)
        for x in range(10, 700, 100):  # Columnas (x)
            # Crear enemigo en (x,y)
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = EnemigoPersonaje
            spriteEnemigo.rect = EnemigoPersonaje.get_rect()
            spriteEnemigo.rect.left = r.randint(10, 690)
            spriteEnemigo.rect.top = y
            listaEnemigos.append(spriteEnemigo)  # Lista de sprites


def dibujarListaEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverBalasEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.top += r.randint(0, 5)


def crearProyectil(imgbala, listaBalas, spriteNave):
    anchoNave = pygame.Surface.get_width(spriteNave.image)
    altoNave = pygame.Surface.get_height(spriteNave.image)
    spriteProyectil = pygame.sprite.Sprite()
    spriteProyectil.image = imgbala  # PONE LA IMAGEN DEL PROYECTIL
    spriteProyectil.rect = imgbala.get_rect()  # COORDENADAS DE LA BALA
    spriteProyectil.rect.left = spriteNave.rect.left + anchoNave / 3.5
    spriteProyectil.rect.top = spriteNave.rect.top
    listaBalas.append(spriteProyectil)


def moverBalas(listaBalas):
    for proyectil in listaBalas:
        proyectil.rect.top -= 80  # Velocidad de las balas
        if proyectil.rect.top < -30:
            listaBalas.remove(proyectil)


def dibujarListaProyectiles(ventana, listaBalas):
    for proyectil in listaBalas:
        ventana.blit(proyectil.image, proyectil.rect)


def verificarChoques(listaBalas, listaEnemigos):
    for enemigo in listaEnemigos:
        for proyectil in listaBalas:
            if proyectil.rect.colliderect(enemigo) == True:  # PRUEBA COLISIÓN DIRECTAMENTE ¡¡¡¡¡USAR !!!!!
                listaEnemigos.remove(enemigo)
                listaBalas.remove(proyectil)
                return True


def verificarChoquesNave(spriteNave, listaEnemigos):
    for enemigo in listaEnemigos:
        if enemigo.rect.colliderect(spriteNave.rect) == True:
            return True


def dibujarRegresar(ventana, imgRegresar):
    ventana.blit(imgRegresar, (50, 400))


def dibujarMarcadorFinal(ventana, fuente, marcador):
    texto = fuente.render("Tu puntuacion fue de: ", 1, AZUL)
    texto2 = fuente.render(str(marcador), 1, AZUL)
    ventana.blit(texto, (110, 50))
    ventana.blit(texto2, (325, 100))




def agregar(entrada, salida, marcador):
    for linea in entrada:
        datos = linea.split(".")
        record = datos[1]
        str2 = "La puntuacion mas alta es: "
        salida.write("%s %s \n" % (str2, record))
        num = datos[1]
        datosint = int(num)
        if datosint > marcador:
            resultado = datosint - marcador
            cadena = "Te faltaron"
            cadena2 = "puntos para superar el record"
            salida.write("%s, %2.f, %s" % (cadena, resultado, cadena2))
        elif datosint < marcador:
            resultado = marcador - datosint[1]
            cadena = "Superaste el record por"
            cadena2 = "puntos "
            salida.write("%s, %2.f, %s" % (cadena, resultado, cadena2))

        # %s = cadena
        # %.2f = 2 decimales


def dibujar():
    global xNave, yNave  # Voy a usarla variable global
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES
    btnPlay = pygame.image.load("button_play.png.jpeg")
    btnExit = pygame.image.load("button_exit.png.jpeg")
    imagen = pygame.image.load("fondo2.png")
    imagenFondoJuego = pygame.image.load("espacioestrellas.jpg")
    navePersonaje = pygame.image.load("personaje.png")
    EnemigoPersonaje = pygame.image.load("ufo_Juego.png")
    imgbala = pygame.image.load("bala.png")
    imgHighScore = pygame.image.load("highScore.png")
    imgRegresar = pygame.image.load("atras.png")
    imgGameOver = pygame.image.load("gameover.png")
    fondo = pygame.image.load("FONDO-NEGRO.png")

    # Lista de enemigos
    listaEnemigos = []  # Lista vacia
    generarEnemigos(listaEnemigos, EnemigoPersonaje)

    # Lista Proyectiles
    listaBalas = []

    # SPRITE NAVE
    anchoPersonaje = pygame.Surface.get_width(navePersonaje)
    altoPersonaje = pygame.Surface.get_height(navePersonaje)
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = navePersonaje
    spriteNave.rect = navePersonaje.get_rect()
    spriteNave.rect.left = ANCHO // 2 + 70
    spriteNave.rect.top = ALTO - altoPersonaje

    # SPRITE
    spriteMisil = pygame.sprite.Sprite()
    spriteMisil.image = imgbala
    spriteMisil.rect = imgbala.get_rect()  # Datos de la imagen
    spriteMisil.rect.left = -1  # Coordenada X
    spriteMisil.rect.top = -1  # Coordenada Y

    # AUDIO
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)  # se repite de manera infinita

    # Mouse
    xMouse = -1
    yMouse = -1

    # PUNTUACION
    marcador = 0

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    PAUSADO = 3
    GAMEOVER = 4
    MENUSTTNGS = 5
    HIGHSCORE = 6
    estado = MENU

    # TEXTO
    # TEXTO
    fuente = pygame.font.SysFont("arial", 60)
    marcador = 0

    # TIEMPOS
    tiempoAtaque = 200

    x = 0

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Oprmió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 100 and xMouse <= 300 and yMouse >= 500 and yMouse <= 650:  # Boton de Play
                    # Oprimio el boton de play, CAMBIAR el ESTADO
                    xMouse = -1
                    estado = JUGANDO
                elif xMouse >= 500 and xMouse <= 700 and yMouse >= 500 and yMouse <= 650:  # Boton de Exit
                    termina = True
                elif xMouse >= 50 and xMouse <= 150 and yMouse >= 400 and yMouse <= 500:
                    xMouse = -1
                    estado = MENU
            elif evento.type == pygame.KEYDOWN:  # Oprimio una tecla
                # Verificar que tecla se orpimio
                tecla = pygame.key.get_pressed()
                if evento.key == pygame.K_SPACE:  # DISPARAR
                    if len(listaBalas) < 1:
                        crearProyectil(imgbala, listaBalas, spriteNave)

                elif tecla[pygame.K_RIGHT] and spriteNave.rect.left < ANCHO - 128:

                    spriteNave.rect.left += 50

                elif tecla[pygame.K_LEFT] and spriteNave.rect.left >= 1:

                    spriteNave.rect.left -= 50

                elif tecla[pygame.K_DOWN] and spriteNave.rect.top < ALTO - 128:

                    spriteNave.rect.top += 50
                elif tecla[pygame.K_UP] and spriteNave.rect.top >= 0:
                    spriteNave.rect.top -= 50
        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == MENU:
            dibujarImagen(ventana, imagen)
            dibujarPlay(ventana, btnPlay)  # Dependiendo del orden es lo primero que se dibujara
            dibujarExit(ventana, btnExit)
            dibujarMouse(ventana, xMouse, yMouse)
            # Se pueden dibujar cosas atras de otras

        elif estado == JUGANDO:
            choque = verificarChoques(listaBalas, listaEnemigos)
            if choque == True:
                marcador += 500

            perder = verificarChoquesNave(spriteNave, listaEnemigos)
            if perder == True:
                print("Tu marcador fue de: ", marcador)
                estado = GAMEOVER

            moverBalas(listaBalas)

            dibujarFondo(ventana, imagenFondoJuego)

            moverBalasEnemigos(listaEnemigos)
            dibujarNave(ventana, spriteNave)


            x += 1
            if x >= 40: 
                dibujarListaEnemigos(ventana, listaEnemigos)

            dibujarListaProyectiles(ventana, listaBalas)
            dibujarMarcador(ventana, fuente, marcador)



        elif estado == GAMEOVER:
            ventana.blit(fondo, (0, 0))
            ventana.blit(imgGameOver, (100, 5))
            dibujarExit(ventana, btnExit)
            dibujarRegresar(ventana, imgRegresar)
            dibujarMarcadorFinal(ventana, fuente, marcador)
            entrada = open("resultados.txt", "r", encoding="UTF-8")
            salida = open("Puntuaciones.txt", "w", encoding="UTF-8")
            agregar(entrada, salida, marcador)

            entrada.close()
            salida.close()

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# Llamas a la función principal
main()
