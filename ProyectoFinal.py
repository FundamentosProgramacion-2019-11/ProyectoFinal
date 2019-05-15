# encoding: UTF-8
# Autor: Rosalía Serrano Herrera
# Moonight Fall: Juego sobre recolectar estrellas que caen del cielo
import random
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)

def dibujarFondo(ventana, spriteFondo):
    ventana.blit(spriteFondo.image, (0, 0))


def dibujarTitulo(ventana, fuenteTitulo):
    texto = fuenteTitulo.render("MOONLIGHT FALL", 1, BLANCO)
    ventana.blit(texto, (150, 150))


def dibujarMenu(ventana, spriteBtnJugar):
    ventana.blit(spriteBtnJugar.image, (150, 300))


def dibujarMarcador(ventana, spriteBtnMarcador):
    ventana.blit(spriteBtnMarcador.image, (450, 300))


def dibujarBtnMenu(ventana, spriteBtnMenu):
    ventana.blit(spriteBtnMenu.image, (500, 450))


def dibujarFondoOtro(ventana, spriteFondoOtro):
    ventana.blit(spriteFondoOtro.image, (0,0))


def dibujarFondoMoon(ventana, spriteFondoMoon):
    ventana.blit(spriteFondoMoon.image, (0,0))


def dibujarFrasco(ventana, spriteFrasco):
    ventana.blit(spriteFrasco.image, spriteFrasco.rect)


def dibujarListaEstrellas(ventana, listaEstrellas):
    for estrella in listaEstrellas:
        ventana.blit(estrella.image, estrella.rect)


def moverEstrellas(listaEstrellas):
    for estrella in listaEstrellas:
        estrella.rect.top += 10


def verificarColisionEstrellaFrasco(listaEstrellas, spriteFrasco, estrellaCae):
    for estrella in listaEstrellas:
        if estrella.rect.colliderect(spriteFrasco) == True:
            estrellaCae.play()
            listaEstrellas.remove(estrella)
            return True
    return False


def verificarMuerte(listaEstrellas, perder):
    for estrella in listaEstrellas:
        if estrella.rect.top >= 550:
            listaEstrellas.remove(estrella)
            perder.play()
            return True
    return False


def dibujarPuntaje(ventana, puntos, fuentePuntos):
    texto = fuentePuntos.render("Estrellas:" + str(puntos), 1, BLANCO)
    ventana.blit(texto, (320, 30))


def dibujarGameOver(ventana, fuenteTitulo):
    texto = fuenteTitulo.render("GAME OVER", 1, BLANCO)
    ventana.blit(texto, (80, 80))


def dibujarResultado(ventana, fuentePuntos, puntos):
    texto = fuentePuntos.render("Puntos:" + str(puntos), 1, BLANCO)
    ventana.blit(texto, (320, 300))


def dibujarVidas(ventana, vidas, fuentePuntos):
    texto = fuentePuntos.render("Vidas:" + str(vidas), 1, BLANCO)
    ventana.blit(texto, (600, 30))


def dibujarPalabra(ventana, fuenteTitulo):
    texto = fuenteTitulo.render("SCORE:", 1, BLANCO)
    ventana.blit(texto, (300, 100))


def escribirRecord(archivo, record):
    salida = open(archivo, "w")
    salida.write(str(record))
    salida.close()


def compararRecords(archivo, recordActual):
    for recordArchivo in archivo:
        if recordArchivo > recordActual:
            recordMayor = recordArchivo
            return recordMayor


def mandarRecord(archivo):
    entrada = open(archivo, "r")
    recordMayor = entrada.readline()
    entrada.close()
    return recordMayor

def dibujarRecord(ventana, fuentePuntos, recordMayor):
    texto = fuentePuntos.render("El puntaje mayor es: " + str(recordMayor), 1, BLANCO)
    ventana.blit(texto, (200, 300))


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # FONDOS
    # fondo
    imgFondo = pygame.image.load("fondo.jpg")
    spriteFondo = pygame.sprite.Sprite()
    spriteFondo.image = imgFondo
    spriteFondo.rect = imgFondo.get_rect()

    # fondo juego
    imgFondoMoon = pygame.image.load("moonlight.jpg")
    spriteFondoMoon = pygame.sprite.Sprite()
    spriteFondoMoon.image = imgFondoMoon
    spriteFondoMoon.rect = imgFondoMoon.get_rect()

    # fondo otro
    imgFondoOtro = pygame.image.load("lluvia.jpg")
    spriteFondoOtro = pygame.sprite.Sprite()
    spriteFondoOtro.image = imgFondoOtro
    spriteFondoOtro.rect = imgFondoOtro.get_rect()

    # BOTONES
    # botón jugar
    btnJugar = pygame.image.load("btn_jugar.png")
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = btnJugar
    spriteBtnJugar.rect = btnJugar.get_rect()

    # botón marcador
    btnMarcador = pygame.image.load("button_marcador.png")
    spriteBtnMarcador = pygame.sprite.Sprite()
    spriteBtnMarcador.image = btnMarcador
    spriteBtnMarcador.rect = btnMarcador.get_rect()

    # botón menú
    btnMenu = pygame.image.load("button_menu.png")
    spriteBtnMenu = pygame.sprite.Sprite()
    spriteBtnMenu.image = btnMenu
    spriteBtnMenu.rect = btnMenu.get_rect()

    # FUENTES
    # fiente título
    fuenteTitulo = pygame.font.SysFont("courier", 50, 2)

    # fuente puntos
    fuentePuntos = pygame.font.SysFont("courier", 30, 1)

    # SPRITES
    # frasco
    imgFrasco = pygame.image.load("jarro.png")
    spriteFrasco = pygame.sprite.Sprite()
    spriteFrasco.image = imgFrasco
    spriteFrasco.rect = imgFrasco.get_rect()
    spriteFrasco.rect.left = 350
    spriteFrasco.rect.top = 405

    # IMÁGENES
    # estrella
    imgEstrella = pygame.image.load("star.png")

    # LISTAS
    # lista estrellas
    listaEstrellas = []

    # PUNTOS
    puntos = 0

    # VIDAS
    vidas = 3

    # TIEMPO
    tiempo = 0

    # RECORD
    record = 0

    # SONIDOS
    pygame.mixer.init()
    # Sonido corto  Sound == wav
    estrellaCae = pygame.mixer.Sound("star.wav")
    perder = pygame.mixer.Sound("lose.wav")
    # Sonido largo  Music == mp3
    pygame.mixer.music.load("moonlight.mp3")
    pygame.mixer.music.play(-1)

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    MARCADOR = 3
    TERMINADO = 4
    estado = MENU   #Muestra el menú al inicio

    recordMayor = mandarRecord("Records.txt")
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 150 and xMouse <= 350 and yMouse >= 300 and yMouse <= 350:
                    # CAMBIAR EL ESTADO
                    estado = JUGANDO  # PASA A JUGAR
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    if xMouse >= 450 and xMouse <= 650 and yMouse >= 300 and yMouse <= 350:
                        # CAMBIAR EL ESTADO
                        estado = MARCADOR  # PASA AL MARCADOR
            elif evento.type == pygame.KEYDOWN:  # Tecla oprimida
                if evento.key == pygame.K_RIGHT:  # Flecha derecha
                    if spriteFrasco.rect.left <= 670:
                        spriteFrasco.rect.left += 40
                elif evento.key == pygame.K_LEFT:  # Flecha izquierda
                    if spriteFrasco.rect.left >= 2:
                        spriteFrasco.rect.left -= 40
        if estado == MENU:
            dibujarFondo(ventana, spriteFondo)
            dibujarTitulo(ventana, fuenteTitulo)
            dibujarMenu(ventana, spriteBtnJugar)
            dibujarMarcador(ventana, spriteBtnMarcador)
        elif estado == JUGANDO:
            moverEstrellas(listaEstrellas)
            tiempo += 1
            if tiempo == 30:
                nueva = pygame.sprite.Sprite()
                nueva.image = imgEstrella
                nueva.rect = imgEstrella.get_rect()
                nueva.rect.left = random.randint(0, 750)
                nueva.rect.top = -100
                listaEstrellas.append(nueva)
                tiempo = 0
            resultado = verificarColisionEstrellaFrasco(listaEstrellas, spriteFrasco, estrellaCae)
            if resultado == True:
                puntos += 1
            muerte = verificarMuerte(listaEstrellas, perder)
            if muerte == True:
                vidas -= 1
            if vidas == 0:
                estado = TERMINADO
            dibujarFondoMoon(ventana, spriteFondoMoon)
            dibujarFrasco(ventana, spriteFrasco)
            dibujarListaEstrellas(ventana, listaEstrellas)
            dibujarPuntaje(ventana, puntos, fuentePuntos)
            dibujarVidas(ventana, vidas, fuentePuntos)
        elif estado == MARCADOR:
            dibujarFondoOtro(ventana, spriteFondoOtro)
            dibujarPalabra(ventana, fuenteTitulo)
            dibujarRecord(ventana, fuentePuntos, recordMayor)
        elif estado == TERMINADO:
            dibujarFondoOtro(ventana, spriteFondoOtro)
            dibujarGameOver(ventana, fuenteTitulo)
            dibujarResultado(ventana, fuentePuntos, puntos)
            record = puntos
            recordActual = escribirRecord("Records.txt", record)
            compararRecords("Records.txt", recordActual)
            recordMayor = mandarRecord("Records.txt")
            dibujarBtnMenu(ventana, spriteBtnMenu)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 500 and xMouse <= 700 and yMouse >= 450 and yMouse <= 500:
                    # CAMBIAR EL ESTADO
                    estado = MENU  # PASA A MENÚ

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(20)

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()