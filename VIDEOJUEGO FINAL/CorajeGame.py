# Autor: Karla Ximena Rueda Ruiz
# Videojuego Coraje el perro cobarde.

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

# Global
xFondo = 0
vida=100

#Movimiento coraje
angulo=0  #grados

#FUNCIONES

def dibujarMenu(ventana, btnPlay,puntajes,instrucciones):
    ventana.blit(btnPlay, (280,420))    # Calcular x,y para centrar
    ventana.blit(puntajes, (400,420))
    ventana.blit(instrucciones, (300, 500))

def dibujarFondo(ventana,fondoJuego):
    global xFondo
    ventana.blit(fondoJuego,(xFondo,0))
    ventana.blit(fondoJuego,(xFondo+800,0))
    xFondo -= 1
    if xFondo==-800:
        xFondo=0

def dibujarCoraje(ventana,spriteCoraje):
    ventana.blit(spriteCoraje.image,spriteCoraje.rect)

def dibujarEnemigos(ventana,spriteEnemigos):
    ventana.blit(spriteEnemigos.image, spriteEnemigos.rect)

def dibujarSuelo(ventana,spriteSuelo):
    ventana.blit(spriteSuelo.image, spriteSuelo.rect)

def dibujarTubo(ventana,spriteTubo):
    ventana.blit(spriteTubo.image, spriteTubo.rect)

def dibujarBomba(ventana,listaBombas):
    for bomba in listaBombas:
        ventana.blit(bomba.image, bomba.rect)

def dibujarMedicina(ventana,listaMedicinas):
    for medicina in listaMedicinas:
        ventana.blit(medicina.image, medicina.rect)

def dibujarListaBombas(ventana, listaBombas):
    for bomba in listaBombas:
        ventana.blit(bomba.image,bomba.rect)

def dibujarVidas(ventana, fuente):
    texto=fuente.render("Puntos: "+str(vida), 1,NEGRO)
    ventana.blit(texto,(50,30))

def dibujarPuntos(ventana, fuente,record):
    texto=fuente.render("Último puntaje: "+record, 1,NEGRO)
    ventana.blit(texto,(365,400))

def dibujarFondoMenu(ventana, menu):
    ventana.blit(menu,(0,0))


def dibujarFondoInstrucciones(ventana, fondoInstrucciones):
    ventana.blit(fondoInstrucciones,(0, 0))


def dibujarFondoPuntajes(ventana, fondoPuntajes):
    ventana.blit(fondoPuntajes,(0,0))


def dibujarFondoFinal(ventana, gameover):
    ventana.blit(gameover, (0, 0))

def moverBombas(listaBombas):
    for bomba in listaBombas:
        bomba.rect.left -=4

def moverMedicinas(listaMedicinas):
    for medicina in listaMedicinas:
        medicina.rect.left -=3

def generarBombas(listaBombas,bomba):
    for y in range(300,300+1,100):#renglones(coordenada y va de arriba hacia abajo,
        for x in range(133+ANCHO,670+ANCHO,120): #columnas(x)
            #crear enemigo en (x,y)
            spriteBomba=pygame.sprite.Sprite()
            spriteBomba.image=bomba
            spriteBomba.rect=bomba.get_rect()
            spriteBomba.rect.left=x
            spriteBomba.rect.top=y
            listaBombas.append(spriteBomba)#lista de sprites que representan enemigos

def generarMedicinas(listaMedicinas,medicina):
    for y in range(300,300+1,100):#renglones(coordenada y va de arriba hacia abajo,
        for x in range(133,670,133): #columnas(x)
            #crear enemigo en (x,y)
            spriteMedicina=pygame.sprite.Sprite()
            spriteMedicina.image=medicina
            spriteMedicina.rect=medicina.get_rect()
            spriteMedicina.rect.left=x
            spriteMedicina.rect.top=y
            listaMedicinas.append(spriteMedicina)#lista de sprites que representan enemigos

def verificarColision(listaBombas, spriteCoraje):
    global vida
    for bomba in listaBombas:
        if bomba.rect.colliderect(spriteCoraje)==True:
            vida=vida-10
            listaBombas.remove(bomba)
            print(vida)

def probarColision(listaMedicinas, spriteCoraje):
    global vida
    for medicina in listaMedicinas:
        if medicina.rect.colliderect(spriteCoraje)==True:
            vida=vida+5
            listaMedicinas.remove(medicina)
            print(vida)

def generarBomba(listaBombas, imgBomba):
    spriteBomba = pygame.sprite.Sprite()
    spriteBomba.image = imgBomba
    spriteBomba.rect = imgBomba.get_rect()  # datos  de la img
    spriteBomba.rect.left = ANCHO+random.randint(20, 40)  # x
    spriteBomba.rect.top = 380  # y
    listaBombas.append(spriteBomba)


def generarMedicina(listaMedicinas, medicina):
    spriteMedicina = pygame.sprite.Sprite()
    spriteMedicina.image = medicina
    spriteMedicina.rect = medicina.get_rect()
    spriteMedicina.rect.left = ANCHO+random.randint(40, 120)
    spriteMedicina.rect.top = 380
    listaMedicinas.append(spriteMedicina)

def escribirMarcador(archivo,ultimoTiempo):
    salida=open(archivo,"w",encoding="UTF-8")
    salida.write(str(ultimoTiempo))
    salida.close()


#ARCHIVOS

def leeUltimoTiempo(archivo):
    entrada=open(archivo,"r",encoding="UTF-8")
    record=entrada.readline()
    entrada.close()
    return record


def dibujar():
    global vida
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES
    btnPlay = pygame.image.load("btnPlay.png")
    fondoJuego = pygame.image.load("fondo.jpg")
    coraje = pygame.image.load("coraje.png")
    enemigo = pygame.image.load("enemigo.png")
    imgBomba = pygame.image.load("bomba.png")
    suelo=pygame.image.load("suelo.png")
    tubo = pygame.image.load("tubo.png")
    medicina=pygame.image.load("medicina.png")
    puntajes=pygame.image.load("button_puntajes.png")
    instrucciones = pygame.image.load("button_instrucciones.png")
    menu = pygame.image.load("menu.jpg")
    fondoInstrucciones = pygame.image.load("Fondo Instrucciones.jpg")
    fondoPuntajes = pygame.image.load("PuntajesRecord.jpg")
    gameover=pygame.image.load("gameover.jpg")

    # TEXTO
    fuente = pygame.font.SysFont("Arial", 50)

    #LISTA de ENEMIGOS

    listaEnemigos=[]#Lista vacía
    #generarEnemigos(listaEnemigos,enemigo)

    # LISTA DE PROYECTILES
    listaBombas=[]
    #generarBombas(listaBombas,imgBomba)

    listaMedicinas=[]
    #generarMedicinas(listaMedicinas,medicina)

    #SPRITES

    spriteCoraje=pygame.sprite.Sprite()
    spriteCoraje.image=coraje
    spriteCoraje.rect=coraje.get_rect()
    spriteCoraje.rect.left=20
    spriteCoraje.rect.top=250

    spriteEnemigos = pygame.sprite.Sprite()
    spriteEnemigos.image = enemigo
    spriteEnemigos.rect = enemigo.get_rect()
    spriteEnemigos.rect.left = 553
    spriteEnemigos.rect.top = 50

    spriteSuelo = pygame.sprite.Sprite()
    spriteSuelo.image = suelo
    spriteSuelo.rect = suelo.get_rect()
    spriteSuelo.rect.left = -20
    spriteSuelo.rect.top = 300

    spriteTubo = pygame.sprite.Sprite()
    spriteTubo.image = tubo
    spriteTubo.rect = tubo.get_rect()
    spriteTubo.rect.left = 600
    spriteTubo.rect.top = 250

    spriteMedicina = pygame.sprite.Sprite()
    spriteMedicina.image = medicina
    spriteMedicina.rect = medicina.get_rect()
    spriteMedicina.rect.left = 0
    spriteMedicina.rect.top = 0

    spriteBomba = pygame.sprite.Sprite()
    spriteBomba.image = imgBomba
    spriteBomba.rect = imgBomba.get_rect()    # datos  de la img
    spriteBomba.rect.left = -1   # x
    spriteBomba.rect.top = -1    # y

    #ATAQUE enemigo
    spriteAtaque=pygame.sprite.Sprite()
    spriteAtaque.image=imgBomba
    spriteAtaque.rect=imgBomba.get_rect()
    spriteAtaque.rect.left = -1
    spriteAtaque.rect.top = -1

    #AUDIO

    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1) # infinito

    # MOUSE
    xMouse = -1
    yMouse = -1

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    estado = MENU
    PERDIDO=3
    PUNTAJES=4
    INSTRUCCIONES=5

    #TIEMPOS
    tiempoAtaque=100

    #Tiempo para generar bombas
    tiempo=0

    #Tiempo para generar medicina
    tiempoMedicina=0

    #Ultimo Tiempo
    ultimoTiempo=0

    record=leeUltimoTiempo("Puntos.txt")
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if estado==INSTRUCCIONES:
                    estado=MENU
                    continue
                if estado == PUNTAJES:
                    estado = MENU
                    continue
                if estado == PERDIDO:
                    estado = MENU
                    continue
                # Oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if xMouse>=250 and xMouse<=350 and yMouse>=420 and yMouse<=455:
                    #  Oprimió el botón de play, CAMBIAR el ESTADO
                    xMouse = -1
                    estado = JUGANDO
                    vida=100

                if xMouse>=420 and xMouse<=580 and yMouse>=420 and yMouse<=452:
                    #  Oprimió el botón de play, CAMBIAR el ESTADO
                    xMouse = -1
                    estado = PUNTAJES

                if xMouse>=290 and xMouse<=534 and yMouse>=500 and yMouse<=539:
                    #  Oprimió el botón de play, CAMBIAR el ESTADO
                    xMouse = -1
                    estado = INSTRUCCIONES


            elif evento.type == pygame.KEYDOWN: # Oprimió una tecla
                    # Verificar qué tecla se oprimió
                if evento.key == pygame.K_RIGHT:
                    spriteCoraje.rect.left += 20
                elif evento.key == pygame.K_LEFT:
                    spriteCoraje.rect.left-= 20
                elif evento.key == pygame.K_UP:
                    spriteCoraje.rect.top -= 120
                elif evento.key == pygame.K_DOWN:
                    spriteCoraje.rect.top += 120
                elif evento.key == pygame.K_SPACE:
                    nuevaBomba=pygame.sprite.Sprite()
                    nuevaBomba.image=imgBomba
                    nuevaBomba.rect.imgBomba.get_rect()
                    nuevaBomba.rect.left=spriteCoraje+64-12
                    nuevaBomba.rect.top=spriteCoraje
                    listaBombas.append(nuevaBomba)



        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarFondoMenu(ventana,menu)
            dibujarMenu(ventana, btnPlay,puntajes,instrucciones)

        elif estado == JUGANDO:
            if tiempo>=120:
                generarBomba(listaBombas,imgBomba)
                tiempo=0


            if tiempoMedicina>=240:
               generarMedicina(listaMedicinas,medicina)
               tiempoMedicina=0

            if vida<=0:
                estado=PERDIDO
                escribirMarcador("Puntos.txt",ultimoTiempo)

            verificarColision(listaBombas,spriteCoraje)
            probarColision(listaMedicinas,spriteCoraje)
            dibujarFondo(ventana,fondoJuego)

            dibujarCoraje(ventana,spriteCoraje)
            dibujarEnemigos(ventana,spriteEnemigos)
            dibujarSuelo(ventana,spriteSuelo)
            dibujarTubo(ventana, spriteTubo)
            dibujarBomba(ventana,listaBombas)
            dibujarMedicina(ventana,listaMedicinas)
            moverBombas(listaBombas)
            moverMedicinas(listaMedicinas)
            dibujarVidas(ventana,fuente)

        elif estado==PUNTAJES:
            dibujarFondoPuntajes(ventana,fondoPuntajes)
            dibujarPuntos(ventana,fuente,record)


            
        elif estado==PERDIDO:
            dibujarFondoFinal(ventana,gameover)

        elif estado == INSTRUCCIONES:
            dibujarFondoInstrucciones(ventana, fondoInstrucciones)


        tiempo+=1
        tiempoMedicina+=1
        ultimoTiempo+=1
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja

#SUMAR GRADOS AL ANGULO
# Llamas a la función principal
main()



