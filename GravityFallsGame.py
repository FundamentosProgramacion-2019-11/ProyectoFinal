#Autor: Mariana Teyssier Cervantes
#Probar elementos para proyecto final
import math
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
NEGRO = (0, 0, 0)


#TEMPORALMENTE las coordenadas de MABEL
xMabel = 0
yMabel = 300

xEnemigo = ANCHO//2
yEnemigo = 0
DX = +15      #derecha, (-1) izquierda

#FONDOS (Menú, Juego, Instrucciones, Fin)
xFondoMenu = 0
xFondoJuego = 0
xFondoInstrucciones = 0
xFondoFin = 0


# Estructura básica de un programa que usa pygame para dibujar

#Menu del juego
def dibujarFondoMenu(ventana, FondoMenu, btnJugar, btnInst):
    global xFondoMenu
    ventana.blit(FondoMenu, (xFondoMenu, 0))
    ventana.blit(btnJugar, (25, 400))
    ventana.blit(btnInst, (25, 450))


def dibujarFondoJuego(ventana, FondoJuego):
    global xFondoJuego
    ventana.blit(FondoJuego, (xFondoJuego, 0))

#Personaje principal - Mabel-
def dibujarMabel(ventana, Mabel):
    ventana.blit(Mabel, (xMabel, yMabel))

#Enemigo - Bill-
def dibujarEnemigo(ventana, spriteEnemigo):
    global xEnemigo, DX, yEnemigo
    ventana.blit(spriteEnemigo.image, spriteEnemigo.rect)
    spriteEnemigo.rect.top += DX
    if spriteEnemigo.rect.top >= ALTO-211 or spriteEnemigo.rect.top <= 0:
        DX = -DX

#Balas de Mabel -Nubes-
def dibujarBala(ventana, spriteBala):
    if spriteBala.rect.left != -1:
        ventana.blit(spriteBala.image, spriteBala.rect)
        spriteBala.rect.top -= 20
        if spriteBala.rect.top < -25:
            spriteBala.rect.left = -1

#Piñas para recolectar
def colisionFruta(listaFrutas, listaBalas):
    for Bala in listaBalas:
        for fruta in listaFrutas:
            if Bala.rect.colliderect(fruta) == True:
                listaFrutas.remove(fruta)
                listaBalas.remove(Bala)
                return True
    return False

#Función donde comprueba si las balas tocaron a la fruta.
def colisionEnemigo(listaBalas, spriteEnemigo):
    for Bala in listaBalas:
        if Bala.rect.colliderect(spriteEnemigo) == True:
            listaBalas.remove(Bala)
            return True
    return False

#Puntos que va ganando el usuario
def dibujarPuntos(ventana, puntos, fuente):
    texto1 = fuente.render("Puntos: " + str(puntos), 1, BLANCO)
    ventana.blit(texto1, (10,50))

#Número de vidas que tiene el usuario
def dibujarVida(ventana, vida, fuente):
    texto2 = fuente.render("Vida: " + str(vida), 1, BLANCO)
    ventana.blit(texto2, (10, 100))

#Número de tiros que tiene el usuario
def dibujarTiros(ventana, tiros, fuente):
    texto1 = fuente.render("Tiros: " + str(tiros), 1, BLANCO)
    ventana.blit(texto1, (10, 150))

#Filas y columnas de frutas
def generarFrutas(listaFrutas, fruta):
    for y in range(50, 550, 50):         #renglones
        for x in range(552, 750, 50):    #columnas
            #crear fruta en (x,y)
            spriteFruta = pygame.sprite.Sprite()
            spriteFruta.image = fruta
            spriteFruta.rect = fruta.get_rect()
            spriteFruta.rect.left = x
            spriteFruta.rect.top = y
            listaFrutas.append(spriteFruta)


def dibujarListaFrutas(ventana, listaFrutas):
    for fruta in listaFrutas:
        ventana.blit(fruta.image, fruta.rect)


def dibujarListaBalas(ventana, listaBalas):
    for Bala in listaBalas:
        ventana.blit(Bala.image, Bala.rect)


def moverBalas(listaBalas):
    for Bala in listaBalas:
        Bala.rect.left += 20

#Ventana de instrucciones
def dibujarFondoInstrucciones(ventana, FondoInstrucciones, btnIrAJuego):
    global xFondoInstrucciones
    ventana.blit(FondoInstrucciones, (xFondoInstrucciones, 0))
    ventana.blit(btnIrAJuego, (25, 450))


def dibujarInstrucciones(ventana, fuente2, fuente3):
    TEXTO = fuente2.render("INSTRUCCIONES", 1, BLANCO)
    ventana.blit(TEXTO, (100, 50))
    texto3 = fuente3.render("*Debes de dispararle a las piñas y ganar PUNTOS.", 1, BLANCO )
    ventana.blit(texto3, (40, 100))
    texto4 = fuente3.render("*Pero cuidado con Bill, si le disparas pierdes 1 VIDA", 1, BLANCO)
    ventana.blit(texto4, (40, 150))
    texto5 = fuente3.render("*Presiona espacio para disparar", 1, BLANCO)
    ventana.blit(texto5, (40, 200))
    texto6 = fuente3.render("y muévete con las flechas.", 1, BLANCO)
    ventana.blit(texto6, (45, 230))
    texto7 = fuente2.render("DIVIÉRTETE", 1, BLANCO)
    ventana.blit(texto7, (50, 280))

#Ventana donde muestra el puntaje final del usuario y para regresar al Menú
def dibujarFondoFin(ventana, FondoFin, btnFinDelJuego, fuente2):
    global xFondoFin
    ventana.blit(FondoFin, (xFondoFin, 0))
    ventana.blit(btnFinDelJuego, (300, 400))

#Muestra puntaje final del usuario
def dibujarPuntaje(ventana, fuente4, Puntaje):
    texto = fuente4.render("Puntaje Final: " + str(Puntaje), 1, BLANCO)
    ventana.blit(texto, (200, 275))


def dibujar():
    global xMabel, yMabel
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #IMÁGENES
    FondoMenu = pygame.image.load("TituloGravityFalls.jpg")
    FondoJuego = pygame.image.load("FondoJuego.jpg")
    FondoInstrucciones = pygame.image.load("FondoInstrucciones.jpg")
    FondoFin = pygame.image.load("CabañaDelMisterio.jpg")
    Mabel= pygame.image.load("Mabel.png")
    Enemigo= pygame.image.load("Enemigo.png")
    btnJugar= pygame.image.load("btnJugar.jpg")
    btnInst= pygame.image.load("btnInst.jpg")
    btnIrAJuego = pygame.image.load("btnIrAJuego.jpg")
    fruta= pygame.image.load("Fruta.png")
    Bala= pygame.image.load("Bala.png")
    btnFinDelJuego= pygame.image.load("btnFinDelJuego.jpg")

    #LISTAs
    listaFrutas = []
    generarFrutas(listaFrutas, fruta)
    listaBalas = []

    #SPRITES
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = Bala
    spriteBala.rect = Bala.get_rect()
    spriteBala.rect.left = -1
    spriteBala.rect.top = -1

    spriteEnemigo = pygame.sprite.Sprite()
    spriteEnemigo.image = Enemigo
    spriteEnemigo.rect = Enemigo.get_rect()
    spriteEnemigo.rect.left = xEnemigo
    spriteEnemigo.rect.top = yEnemigo

    spriteMabel = pygame.sprite.Sprite()
    spriteMabel.image = Mabel
    spriteMabel.rect = Mabel.get_rect()
    spriteMabel.rect.left = -1
    spriteMabel.rect.top = -1

    #AUDIO
    pygame.mixer.init()
    disparo = pygame.mixer.Sound("Disparo.wav")
    pygame.mixer.music.load("MusicaFondo.mp3")
    pygame.mixer.music.play(-1)

    #MOUSE
    xMouse= -1
    yMouse= -1

    #ESTADOS
    MENU = 1
    JUGANDO = 2
    INSTRUCCIONES = 3
    FIN = 5
    estado = MENU

    #TEXTO
    fuente = pygame.font.SysFont("Arial", 30)
    fuente2 = pygame.font.SysFont("Arial", 45)
    fuente3 = pygame.font.SysFont("Arial", 40)
    fuente4 = pygame.font.SysFont("Arial", 60)

    #Contadores
    puntos = 0
    vida = 10
    tiros = 25

    #ARCHIVOS
    #archivo = "Puntaje.txt"


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:    #Oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                if estado == MENU and xMouse >=26 and xMouse<=130 and yMouse>=402 and yMouse<=442:    #esquinas de btnJugar
                    #Oprimió el botón de JUGAR, CAMBIAR el estado
                    xMouse = -1
                    puntos = 0
                    vida = 10
                    tiros = 25
                    estado = JUGANDO
                if estado == MENU and xMouse >=26 and xMouse<=200 and yMouse>=451 and yMouse<=497:   #esquinas btnInst
                    xMouse = -1
                    puntos = 0
                    vida = 10
                    tiros = 25
                    estado = INSTRUCCIONES

                if estado == INSTRUCCIONES and xMouse >= 26 and xMouse <= 186 and yMouse >= 452 and yMouse <= 502:  # esquinas de btnIrAJuego
                    xMouse = -1
                    puntos = 0
                    vida = 10
                    tiros = 25
                    estado = JUGANDO

                if estado == FIN and xMouse >= 301 and xMouse <= 499 and yMouse >= 402 and yMouse <= 450:  # esquinas de btnFinDelJuego
                    xMouse = -1
                    estado = MENU


            elif evento.type == pygame.KEYDOWN: #Oprimió una tecla
                #Verificar qué tecla se oprimió: Mabel
                if evento.key == pygame.K_RIGHT:
                    xMabel += 20
                elif evento.key == pygame.K_LEFT:
                    xMabel -= 20
                elif evento.key == pygame.K_UP:
                    yMabel -= 20
                elif evento.key == pygame.K_DOWN:
                    yMabel += 20
                elif evento.key == pygame.K_SPACE:
                    disparo.play()
                    nuevaBala = pygame.sprite.Sprite()
                    nuevaBala.image = Bala
                    nuevaBala.rect = Bala.get_rect()
                    nuevaBala.rect.left = xMabel + 108 - 87
                    nuevaBala.rect.top = yMabel
                    listaBalas.append(nuevaBala)

        # Crear el ARCHIVO del Puntaje
        Puntaje = puntos
        listaPuntaje = []
        listaPuntaje.append(str(Puntaje))
        ent = open("Puntaje.txt", "w", encoding="UTF-8")
        puntosFinales = listaPuntaje[0]
        ent.write((puntosFinales))
        ent.close()

        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarFondoMenu(ventana, FondoMenu, btnJugar, btnInst)

        elif estado == INSTRUCCIONES:
            dibujarFondoInstrucciones(ventana, FondoInstrucciones, btnIrAJuego)
            dibujarInstrucciones(ventana, fuente2, fuente3)

        elif estado == FIN:
            dibujarFondoFin(ventana, FondoFin, btnFinDelJuego, fuente2)
            dibujarPuntaje(ventana, fuente4, Puntaje)


        elif estado == JUGANDO:

            moverBalas(listaBalas)


            #DIBUJAR
            dibujarFondoJuego(ventana, FondoJuego)
            dibujarMabel(ventana, Mabel)
            dibujarEnemigo(ventana, spriteEnemigo)
            dibujarListaFrutas(ventana, listaFrutas)

            dibujarBala(ventana, spriteBala)
            dibujarListaBalas(ventana, listaBalas)

            #Dibujar texto
            dibujarPuntos(ventana, puntos, fuente)
            dibujarVida(ventana, vida, fuente)
            dibujarTiros(ventana, tiros, fuente)
            probarColision = colisionFruta(listaFrutas, listaBalas)

            if probarColision == True:
                puntos += 100
                tiros -= 1

            verificarColision = colisionEnemigo(listaBalas, spriteEnemigo)
            if verificarColision == True:
                tiros -= 1
                vida -= 1
            if vida == 0 or tiros == 0:
                estado = FIN
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()