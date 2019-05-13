# Mariana Coria Rodríguez, A01374765
# Juego donde eres un alien y buscas vacas, cuidado con las vacas enfermas


# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame
from random import randint

# DIMENSIONES DE PANTALLA

ANCHO = 800
ALTO = 600

# COLORES
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# RECORD
archivoRecord = open("record.txt", "r")
archivoRecord = archivoRecord.readlines()
record = int(archivoRecord[len(archivoRecord) - 1])

# SONIDO
pygame.mixer.init()
cancionFondo = pygame.mixer.Sound("XFiles.wav")

# VACA
imgVaca = pygame.image.load("vaca.png")
Vacas = []

# Xfiles
imgXfiles = pygame.image.load("xfiles.png")
ListaXfiles = []

# NAVE
imgNave = pygame.image.load("naveEspacial.png")
Nave = pygame.sprite.Sprite()
Nave.image = imgNave
Nave.rect = imgNave.get_rect()
Nave.rect.bottom = ALTO - 10
Nave.rect.left = ANCHO / 2 - Nave.rect.width / 2

# Texto
pygame.font.init()
fuente = pygame.font.SysFont("Helvetica", 30, True, False)

# IMAGENES
btnJugar = pygame.image.load("btnJugar.png")
imgFondo = pygame.image.load("imgFondo.jpg")

# CONTADORES
PUNTOS = 0
VIDAS = 3


# DIBUJAR MENU (BOTONES)
def dibujarMenu(ventana):
    ventana.blit(btnJugar, (300, 275))


def dibujarFondo(ventana):
    ventana.blit(imgFondo, (0, 0))
    for vaca in Vacas:
        ventana.blit(vaca.image, vaca.rect)
    for xf in ListaXfiles:
        ventana.blit(xf[0].image, xf[0].rect)
    ventana.blit(Nave.image, Nave.rect)
    cuadroTexto = fuente.render("Puntos: %d" % PUNTOS, True, BLANCO)
    ventana.blit(cuadroTexto, (20, 20))
    cuadroVidas = fuente.render("Vidas: %d" % VIDAS, True, BLANCO)
    ventana.blit(cuadroVidas, (20, 50))


def dibujarFinal(ventana):
    cuadroRecord = fuente.render("Record: %d" % record, True, BLANCO)
    ventana.blit(cuadroRecord, (350, 200))
    cuadroPuntos = fuente.render("Puntos: %d" % PUNTOS, True, BLANCO)
    ventana.blit(cuadroPuntos, (350, 400))


# CREAR A LAS VACAS
def crearVaca():
    Vaca = pygame.sprite.Sprite()
    Vaca.image = imgVaca
    Vaca.rect = imgVaca.get_rect()
    Vaca.rect.top = randint(150, ALTO - 150)
    Vaca.rect.left = randint(150, ANCHO - 150)
    Vacas.append(Vaca)


# CREAR A LOS XFILES
def crearXfiles():
    Xf = pygame.sprite.Sprite()
    Xf.image = imgXfiles
    Xf.rect = imgXfiles.get_rect()
    Xf.rect.top = randint(150, ALTO - 150)
    Xf.rect.left = randint(150, ANCHO - 150)
    tiempoVida = 60
    ListaXfiles.append([Xf, tiempoVida])


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    FINAL = 3
    estado = MENU

    pygame.mixer.Sound.play(cancionFondo, 0)

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if estado == MENU:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    if xMouse >= 300 and xMouse <= 500 and yMouse >= 275 and yMouse <= 325:
                        # CAMBIA EL ESTADO
                        estado = JUGANDO  # PASA A JUGAR
                elif estado == JUGANDO:
                    global PUNTOS, VIDAS, record
                    for vaca in Vacas:
                        if pygame.sprite.collide_rect(vaca, Nave):
                            Vacas.remove(vaca)
                            PUNTOS += 5
                    for xf in ListaXfiles:

                        if pygame.sprite.collide_rect(xf[0], Nave):
                            ListaXfiles.remove(xf)
                            VIDAS -= 1
                            if VIDAS == 0:
                                estado = FINAL
                                if record < PUNTOS:
                                    record = PUNTOS
                                Vacas.clear()
                                ListaXfiles.clear()
                elif estado == FINAL:
                    PUNTOS = 0
                    VIDAS = 3
                    estado = MENU

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == MENU:
            dibujarMenu(ventana)
        elif estado == JUGANDO:
            if randint(0, 20) == 0:
                crearVaca()
            if randint(0, 100) == 0:
                crearXfiles()
            dibujarFondo(ventana)
            xMouse, yMouse = pygame.mouse.get_pos()
            Nave.rect.left = xMouse - Nave.rect.width / 2
            Nave.rect.top = yMouse - Nave.rect.height / 2
            for xf in ListaXfiles:
                xf[1] -= 1
                if xf[1] <= 0:
                    ListaXfiles.remove(xf)
        elif estado == FINAL:
            dibujarFinal(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame
    archivoRecord = open("record.txt", "w")
    archivoRecord.write(str(record))
    archivoRecord.close()


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# Llamas a la función principal
main()

