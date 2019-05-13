#Autor: Daniela Estrella Tovar
#Crear un código que mediante lo visto en clase, logré la ejecución de un videojuego.
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

# Temporalmente las coordenadas de la nave(x,y)
xNave = ANCHO // 2
yNave = ALTO // 2 + 60
# Enemigo
xEnemigo = ANCHO // 2
yEnemigo = 200
DX = +8  # derechas, (-1) izquierda

# Vaca
xVaca = ANCHO // 2
yVaca = 520
Vx = +3

# FONDO
xFondo = 0  # GLOBAL solo como ejemplo
# Movimiento Senoidal de la nave
angulo = 0  # grados


# Estructura básica de un programa que usa pygame para dibujar
# def dibujarFondoMenu(ventana, fondoJuego):
# ventana.blit(fondoJuego,(0,0))

def dibujarMenu(ventana, button_play, instr,puntos):

    ventana.blit(button_play, (300, 275))  # medidasbutton
    ventana.blit(instr,(300, 350))
    ventana.blit(puntos,(300,425))


def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 0)


def dibujarTitulo(ventana, titulo):
    ventana.blit(titulo, (125, 45))


def dibujarFondo(ventana, fondoJuego):
    global xFondo
    # ventana.blit(fondoJuego,(xFondo,0))para que se mueva
    # xFondo -=1
    ventana.blit(fondoJuego, (0, 0))
def dibujarInstrucciones(ventana, fondoJuego, bMenu,instruccion):
    ventana.blit(fondoJuego, (0,0))
    ventana.blit(bMenu,(590,10))
    ventana.blit(instruccion,(0,0))

def dibujarPuntaje(ventana, puntajeT,fondoJuego,puntosAlien, bMenu,fuente):
    ventana.blit(puntosAlien, (0, 0))
    ventana.blit(fondoJuego, (0,0))
    ventana.blit(bMenu,(590,10))
    texto= fuente.render("Puntaje: " + str(puntajeT),3, BLANCO)
    ventana.blit(texto,(170, 350))

def dibujarNave(ventana, nave):
    ventana.blit(nave, (xNave, yNave))


def dibujarVaca(ventana, vaca):
    global xVaca, Vx, yVaca
    ventana.blit(vaca, (xVaca, yVaca))
    xVaca += Vx
    # delimitarmov
    if xVaca >= ANCHO - 70 or xVaca <= 0:
        Vx = -Vx

def dibujarEnemigo(ventana, enemigo):
    global xEnemigo, DX, yEnemigo, angulo
    ventana.blit(enemigo, (xEnemigo, yEnemigo))
    xEnemigo += DX
    # probar choque der-izq
    if xEnemigo >= ANCHO - 128 or xEnemigo <= 0:  # el valor de 128 fue calculado de acuerdo a la img del profe, puede variar (128 x 78)
        DX = -DX
    # Mover en y
    dy = int(20 * math.sin(math.radians(angulo))) + 70
    yEnemigo = dy
    angulo += 8  # numero mas bajo, mas lento


def dibujarNombres(ventana, nombreAlien, nombreHumano):
    ventana.blit(nombreAlien, (30, 10))
    ventana.blit(nombreHumano, (670, 10))


def dibujarProyectil(ventana, spriteBala):
    if spriteBala.rect.left != -1:
        ventana.blit(spriteBala.image, spriteBala.rect)
        spriteBala.rect.top -= 20
        if spriteBala.rect.top < -32:  # se sale afuera de la pantalla
            spriteBala.rect.left = -1


# Regresa Tue si hay colisión, False en otro caso
def probarColision(spriteBala):
    global xEnemigo, yEnemigo
    xBala = spriteBala.rect.left
    yBala = spriteBala.rect.top

    if xBala >= xEnemigo and xBala <= xEnemigo + 128 and yBala >= yEnemigo and yBala <= yEnemigo + 73:
        return True

    return False


def probarChoque(listaEstrellas, spriteBala):
    imgBala= spriteBala.rect
    for estrella in listaEstrellas:
        if imgBala.colliderect(estrella) == True:
            listaEstrellas.remove(estrella)
            listaEstrellas.remove(imgBala)
            break


def probarAtaque(spriteAtaque):
    global xNave, yNave
    xBalaAlien = spriteAtaque.rect.left
    yBalaAlien = spriteAtaque.rect.top

    if xBalaAlien >= xNave and xBalaAlien <= xNave + 90 and yBalaAlien >=yNave and yBalaAlien<= yNave +73:
        return True

    return False

def probarColisionVaca(spriteAtaque):
    global xVaca, yVaca
    xBalaAlien = spriteAtaque.rect.left
    yBalaAlien = spriteAtaque.rect.top

    if xBalaAlien >= xVaca and xBalaAlien <= xVaca + 68 and yBalaAlien >= yVaca and yBalaAlien <= yVaca + 60:
        spriteAtaque.rect.left = -1

        return True

    return False

def contarVidasAlien(ventana, dosVidas, unaVida, sVidas):
    vidaAlien = 3
    pruebaAlien = probarColision()
    if pruebaAlien == True:
        vidaAlien -= 1
        if vidaAlien == 2:
            ventana.blit(dosVidas, (45, 40))
        elif vidaAlien == 1:
            ventana.blit(unaVida, (45, 40))
        elif vidaAlien == 0:
            ventana.blit(sVidas, (45, 40))


def contarVidasHum(ventana, dosVidas, unaVida, sVidas):
    vidaHum = 3
    pruebaHum = ()
    if pruebaHum == True:
        vidaHum -= 1
        if vidaHum == 2:
            ventana.blit(dosVidas, (45, 40))
        elif vidaHum == 1:
            ventana.blit(unaVida, (45, 40))
        elif vidaHum == 0:
            ventana.blit(sVidas, (45, 40))


def dibujarAtaque(ventana, spriteAtaque):
    if spriteAtaque.rect.left != -1:
        ventana.blit(spriteAtaque.image, spriteAtaque.rect)
        spriteAtaque.rect.top += 5
        if spriteAtaque.rect.top < -32:  # se sale afuera de la pantalla
            spriteAtaque.rect.left = -1

def generarEstrellas(listaEstrellas, estrella):

    for y in range(130, 300 +1, 70):#renglones en y
        for x in range(120, 667+1, 100): #columnas
            spriteEstrella = pygame.sprite.Sprite()
            spriteEstrella.image= estrella
            spriteEstrella.rect= estrella.get_rect()
            spriteEstrella.rect.left= x
            spriteEstrella.rect.top = y
            listaEstrellas.append(spriteEstrella)

def dibujarListaEstrellas(ventana, listaEstrellas):
    for estrella in listaEstrellas:
        ventana.blit(estrella.image, estrella.rect)

def colisionarEstrellas(listaEstrellas,spriteBala):
    for estrella in listaEstrellas:
        if estrella.rect.colliderect(spriteBala)== True:
            listaEstrellas.remove(estrella)
            spriteBala.rect.left = -1
            return True
    return False


def marcarVidasAlien(ventana, tresVidas):
    ventana.blit(tresVidas, (45, 40))


def marcarVidasHum(ventana, tresVidas):
    ventana.blit(tresVidas, (670, 40))


def dibujarTriunfo(ventana, triunfo, bMenu):
    ventana.blit(triunfo, (0, 0))
    ventana.blit(bMenu, (590, 10))

def dibujarFracaso(ventana, fracaso, bMenu):
    ventana.blit(fracaso, (0,0))
    ventana.blit(bMenu, (590, 10))

"""def leerPuntos(archivo):
    listaP=[]
    entrada= open(archivo,"r", encoding="UTF-8")
    for linea in entrada:
        datos= linea

        puntuacion= datos[0]

        listaP.append(puntuacion)
    entrada.close()
    return listaP"""


def dibujar():
    # Hay que anunciar que hay variables globales
    global xNave, yNave
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES
    button_play = pygame.image.load("button_play.png")
    instr = pygame.image.load("btn instrucciones.png")
    puntos = pygame.image.load("btn Puntaje.png")
    titulo = pygame.image.load("TITULO.png")
    fondoJuego = pygame.image.load("fondo.jpg")
    nave = pygame.image.load("nave.png")
    enemigo = pygame.image.load("alien.png")
    imgBala = pygame.image.load("proyectil.png")
    vaca = pygame.image.load("vaca.png")
    nombreAlien = pygame.image.load("nombrealien.png")
    nombreHumano = pygame.image.load("nombreHumano.png")
    tresVidas = pygame.image.load("tresVidas.png")
    dosVidas = pygame.image.load("dosVidas.png")
    unaVida = pygame.image.load("unaVida.png")
    sVidas = pygame.image.load("sinVidas.png")
    balaAlien = pygame.image.load("prAlien.png")
    triunfo = pygame.image.load("ganador.jpg")
    fracaso= pygame.image.load("perdedor.jpg")
    bMenu= pygame.image.load("btnMenu.jpg")
    estrella= pygame.image.load("estrella.png")
    puntosAlien = pygame.image.load("alienpuntaje.png")
    instruccion= pygame.image.load("alieninstruccion.png")



    # Sprites
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()

    spriteBala.rect.top = -1  # x
    spriteBala.rect.left = -1  # y

    # ATAQUE enemigo
    spriteAtaque = pygame.sprite.Sprite()
    spriteAtaque.image = balaAlien
    spriteAtaque.rect = balaAlien.get_rect()
    spriteAtaque.rect.left = -1
    spriteAtaque.rect.top = -1

    # AUDIO
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")  # sonidos pequeños
    pygame.mixer.music.load("musicaFondo.wav")
    pygame.mixer.music.play(-1)  # infinito

    # MOUSE
    xMouse = -1
    yMouse = -1

    # Estados
    MENU = 1
    JUGANDO = 2
    GANADO = 3
    PERDIDO = 4
    INSTRUC = 5
    PUNTOS = 6
    estado = MENU

    #Achivos
   # archivo= ("archivo.txt")


    #Texto
    fuente= pygame.font.SysFont("Arial", 80)

    # Tiempos
    tiempoAtaque = 50  # tiempo de ataque del enemigo

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # SE QUE SE OPRIMIO EL MOUSE CON LA ORDEN ANTERIOR
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 275 and yMouse <= 325:
                    # Oprimió el botón de play
                    xMouse = -1
                    estado = JUGANDO
                    # lista
                    listaEstrellas = []
                    generarEstrellas(listaEstrellas, estrella)
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 350 and yMouse <= 401:
                    xMouse= -1
                    estado = INSTRUC
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 425 and yMouse <= 476:
                    xMouse= -1
                    estado = PUNTOS
                if xMouse >= 590 and xMouse <= 790 and yMouse >= 10 and yMouse <= 61:
                    xMouse =-1
                    estado = MENU



            elif evento.type == pygame.KEYDOWN:  # Oprimió la tecla
                # verificar que tecla se oprimió
                if evento.key == pygame.K_RIGHT:
                    xNave += 20
                elif evento.key == pygame.K_LEFT:
                    xNave -= 20

                elif evento.key == pygame.K_SPACE:
                    if spriteBala.rect.left == -1:
                        spriteBala.rect.left = xNave + 40
                        spriteBala.rect.top = yNave - 73
                        efectoDisparo.play()

        # Borrar pantalla
        ventana.blit(fondoJuego, (0, 0))

        if estado == MENU:

            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, button_play, instr, puntos)
            dibujarTitulo(ventana, titulo)
            vidasAlien = 3
            vidasHum = 3
            puntaje = 0

        elif estado == GANADO:
            dibujarTriunfo(ventana, triunfo, bMenu)

        elif estado == PERDIDO:
            dibujarFracaso(ventana, fracaso, bMenu)
        elif estado ==INSTRUC:
            dibujarInstrucciones(ventana, fondoJuego, bMenu, instruccion)
        elif estado == PUNTOS:


            dibujarPuntaje(ventana, puntajeT,puntosAlien, fondoJuego, bMenu,fuente)


        elif estado == JUGANDO:
            # ACTUALIZAR
            tiempoAtaque -= 1
            if tiempoAtaque == 0:
                spriteAtaque.rect.left = xEnemigo  # *random.randint(0.ANCHO)
                spriteAtaque.rect.top = yEnemigo
                tiempoAtaque = 90

            hayChoque= colisionarEstrellas(listaEstrellas, spriteBala)
            if hayChoque== True:
                puntajeT = 0
                puntaje += 100
                puntajeT = puntajeT+ puntaje
                print(puntajeT)


            # DIBUJAR
            dibujarFondo(ventana, fondoJuego)
            dibujarNave(ventana, nave)
            dibujarEnemigo(ventana, enemigo)
            dibujarListaEstrellas(ventana,listaEstrellas)
            dibujarVaca(ventana, vaca)
            dibujarProyectil(ventana, spriteBala)
            dibujarAtaque(ventana, spriteAtaque)

            dibujarNombres(ventana, nombreAlien, nombreHumano)

            # MarcarVidas
            marcarVidasAlien(ventana, tresVidas)
            marcarVidasHum(ventana, tresVidas)


            hayColision = probarColision(spriteBala)
            if hayColision == True:

                vidasAlien -= 1
                puntaje += 100
                spriteBala.rect.top = 0

                print("colision a enemigo", vidasAlien)

            if vidasAlien == 2:
                ventana.blit(dosVidas, (45, 40))
            elif vidasAlien == 1:
                ventana.blit(unaVida, (45, 40))
            elif vidasAlien == 0:
                ventana.blit(sVidas, (45, 40))
                estado = GANADO


            hayAtaque = probarAtaque(spriteAtaque)
            if hayAtaque == True:

                vidasHum -= 1
                puntaje -= 100
                spriteAtaque.rect.top = 0

                print("colision")
            if vidasHum == 2:
                ventana.blit(dosVidas, (670, 40))
            elif vidasHum == 1:
                ventana.blit(unaVida, (670, 40))
            elif vidasHum == 0:
                ventana.blit(sVidas, (670, 40))
                estado = PERDIDO
                dibujarFracaso(ventana, fracaso, bMenu)

            hayRapto = probarColisionVaca(spriteAtaque)
            if hayRapto == True:
                estado = PERDIDO
                dibujarFracaso(ventana, fracaso, bMenu)

            dibujarMouse(ventana, xMouse, yMouse)

            #Colisiones

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    """ ent = open("archivo.txt", "w", encoding="UTF-8")

 puntos = listaP[0]
    ent.write((puntos))
    ent.close()
    # Después del ciclo principal
    pygame.quit()  # termina pygame"""




# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja
   # print(listaP)


# Llamas a la función principal
main()
