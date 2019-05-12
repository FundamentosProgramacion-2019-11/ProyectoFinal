#Ivana Olvera Mérida      A01746744
#PROYECTO FINAL: Integrar todos los conocimientos aprendidos
#durante el curso para crear un videojuego sencillo en Python.
#Videojuego: SNAKE

import pygame
import random

#Dimensiones de la pantalla
from pygame.sprite import Sprite

ANCHO = 800
ALTO = 600
#Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (239, 239, 4)
NEGRO = (0, 0, 0)


def checarColisiones(listaComida, listaSerpiente):
    estatus = False #El estado comienza como FALSE = 0
    for serpiente in listaSerpiente:
        borrarComida = False
        for k in range(len(listaComida) - 1, -1, -1):
            comida = listaComida[k]
            xb, yb, ab, alb = serpiente.rect
            xe, ye, ae, ale = comida.rect
            if (xe == xb and yb == ye and ab == ae and alb == ale):
                estatus = True
                borrarComida = True
        if borrarComida == True: #Si la serpiente choca con la comida, el estado de borrarComida se vuelve TRUE
            listaComida.pop() #Va a eliminar el dato que se tiene

    if estatus == True: #Si el estado pasa a ser TRUE (choque entre la serpiente y la comida), se regresará un punto. En caso de no ser así, se mantiene en 0
        return 1
    else:
        return 0

def dibujarSerpiente(ventana, listaSerpiente):
    for serpiente in listaSerpiente:
        ventana.blit(serpiente.image, serpiente.rect) #Dibuja la imagen de la serpiente junto con sus dimensiones

def dibujarComida(ventana, listaComida):
    for comida in listaComida:
        ventana.blit(comida.image, comida.rect) #Dibuja la imagen de la comida junto con sus dimensiones

def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 50) #Se dibuja un círculo blanco en caso de que no se haga clic en la zona establecida

def dibujarFondoMenu(ventana, fondoMenu): #Dibujar el fondo del menú principal
    ventana.blit(fondoMenu, (0, 0))

def dibujarBotonJugar(ventana, botonJugar): #Se muestra el botón de jugar en el menú
    ventana.blit(botonJugar, (125, 300))

def dibujarBotonPuntuaciones(ventana, botonPuntos): #Se muestra el botón de puntuaciones en el menú
    ventana.blit(botonPuntos, (125, 360))

def dibujarBotonInfo(ventana, botonInfo): #Se muestra el botón de información en el menú
    ventana.blit(botonInfo, (125, 420))

def dibujarFondo(ventana, fondo):
    ventana.blit(fondo, (0, 0))

def dibujarBotonMenu(ventana, botonMenu):
    ventana.blit(botonMenu, (625, 465))

def dibujarBotonMenuJugar(ventana, botonMenuJuego): #Se dibuja el botón de menú dentro del juego
    ventana.blit(botonMenuJuego, (675, 525))

def cuadricula(ventana): #Dibujar la cuadrícula que será el fondo del juego mientras ESTADO = JUGANDO
    xInicial= 0
    xFinal= 800
    y= 0
    x= 0
    yInicial= 0
    yFinal= 500
    i= 0
    k= 0
    for i in range(1,12,1):
        pygame.draw.line(ventana,BLANCO,(xInicial,y),(xFinal,y), 1)
        y = y + 50
        i = i + 1
    for k in range(1,17,1):
        pygame.draw.line(ventana,BLANCO,(x,yInicial),(x,yFinal), 1)
        x = x + 50
        k = k + 1

def dibujarMarcador(ventana, comidos, fuente):
    texto = fuente.render("Puntuación: " + str(comidos), 1, BLANCO)
    ventana.blit(texto, (60,545))

def registrarPuntos(puntos): #Se registrarán los puntajes de los jugadores
    salida = open("Puntuaciones.txt", "w", encoding="UTF-8")
    salida.write("%s, %d\n" % (puntos))


def crearComida(listaComida, imgComida):
    Comida = pygame.sprite.Sprite()
    Comida.image = imgComida
    Comida.rect = imgComida.get_rect()
    Comida.rect.left = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750)) #Rango de la cuadrícula en el que puede aparecer aleatoriamente la comida
    Comida.rect.top = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450)) #Rango de la cuadrícula en el que puede aparecer aleatoriamente la comida
    listaComida.append(Comida)



def moverSerpiente(listaSerpiente, coordenadaX, coordenadaY, listaComida):
    cabeza = listaSerpiente[:][0] #Copia
    auxiliar = pygame.sprite.Sprite()
    auxiliar.rect = cabeza.image.get_rect()
    auxiliar.rect.left += cabeza.rect.left + coordenadaX
    auxiliar.rect.top += cabeza.rect.top + coordenadaY
    cuadroRojo = listaComida[0]
    if auxiliar.rect == cuadroRojo.rect:
        #Agregar un nuevo cuadro verde (nueva cabeza)
        nuevoVerde = pygame.sprite.Sprite()
        nuevoVerde.image = cabeza.image
        nuevoVerde.rect = cuadroRojo.rect
        listaSerpiente.insert(0, nuevoVerde)
        listaComida.remove(cuadroRojo)

    else: #No hay choque, movimiento normal
        cola = listaSerpiente[:][-1] #Último índice de los elementos
        cola.rect = auxiliar.rect
        listaSerpiente.pop() #Elimina la cola anterior
        listaSerpiente.insert(0, cola)

def actualizarSerpiente(listaSerpiente, imgSerpiente, colaC):
    Cola = pygame.sprite.Sprite()
    Cola.image = imgSerpiente
    Cola.rect = imgSerpiente.get_rect()
    Cola.rect.left = colaC.rect.left
    Cola.rect.top = colaC.rect.top
    listaSerpiente.insert(0,Cola)


def probarPerder(listaSerpiente):
    cabeza = listaSerpiente[0]
    if cabeza.rect.left < 0 or cabeza.rect.left > ANCHO:
        return True
    if cabeza.rect.top < 0 or cabeza.rect.top > 450:
        return True

def leerPuntuaciones(archivoTexto):
    entrada = open(archivoTexto, "r", encoding="UTF-8")
    lista = []
    for linea in entrada:
        if linea == '\n':
            pass
        else:
            lista.append(linea)
    entrada.close()
    return lista

def escribirPuntuaciones(archivoTexto, puntos):
    entrada = open(archivoTexto, "w", encoding="UTF-8")
    entrada.write(str(puntos))
    entrada.close()


def dibujar():

#Inicializa el motor de pygame
    pygame.init()
    #Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #IMAGENES
    botonJugar = pygame.image.load("button_jugar.png")
    botonPuntos = pygame.image.load("button_puntuaciones.png")
    botonInfo = pygame.image.load("button_informacion.png")
    botonMenu = pygame.image.load("button_menu.png")
    botonMenuJuego = pygame.image.load("button_menu.png")
    fondoMenu = pygame.image.load("FondoSnake.png")
    fondo = pygame.image.load("Fondo.png")

    #SPRITES
    imgSerpiente = pygame.image.load("cuboSerpiente.png")
    Serpiente = pygame.sprite.Sprite()
    Serpiente.image = imgSerpiente
    Serpiente.rect = imgSerpiente.get_rect()
    Serpiente.rect.left =  random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750))
    Serpiente.rect.top = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450))

    imgComida = pygame.image.load("cuboComida.png")
    Comida = pygame.sprite.Sprite()
    Comida.image = imgComida
    Comida.rect = imgComida.get_rect()
    Comida.rect.left = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750))
    Comida.rect.top = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450))

    #AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("MusicaJuego.mp3")
    pygame.mixer.music.play(-1)

    #TEXTO
    fuente = pygame.font.SysFont("Showcard Gothic", 25)

    #MOUSE
    xMouse = -1
    yMouse = -1

    #ESTADOS
    MENU = 1
    JUGANDO = 2
    PUNTUACION = 3
    INFORMACION = 4
    GANAR = 5
    PERDER = 6
    estado = MENU

    #LISTAS
    listaComida = [Comida]
    listaSerpiente = [Serpiente]

    puntos=0

    coorX = 50
    coorY = 0

    while not termina:  #Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #El usuario hizo click en el botón de salir
                termina = True      #Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                #Se oprimió el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if estado == MENU:
                    if xMouse>= 125 and xMouse<=325 and yMouse>=300 and yMouse<=350: #Muestra las coordenadas en las que se encuentra el botón
                        #Se oprimió el botón de jugar, CAMBIAR ESTADO
                        xMouse= -1
                        estado = JUGANDO
                        puntos = 0
                        Serpiente.rect.left = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750))
                        Serpiente.rect.top = random.choice((0, 50, 100, 150, 200, 250, 300, 350, 400, 450))
                        listaSerpiente = [Serpiente]
                        listaComida = []
                        crearComida(listaComida, imgComida)

                    if xMouse>= 125 and xMouse<=330 and yMouse>=360 and yMouse<=410:
                        #Se oprimió el botón de puntuaciones, CAMBIAR ESTADO
                        xMouse= -1
                        estado = PUNTUACION
                    if xMouse>= 125 and xMouse<=325 and yMouse>=420 and yMouse<=470:
                        #Se oprimió el botón de información, CAMBIAR ESTADO
                        xMouse= -1
                        estado = INFORMACION

            elif evento.type == pygame.KEYDOWN:
                if estado == JUGANDO: #Teclas que indican la dirección de la serpiente
                    if evento.key == pygame.K_UP:
                        coorX = 0
                        coorY = -50
                        #coordenadaY = (-50)
                        #coordenadaX = 0
                        #moverSerpiente(listaSerpiente,coordenadaX, coordenadaY, listaComida)
                    elif evento.key == pygame.K_DOWN:
                        coorX = 0
                        coorY = 50
                        #coordenadaY = 50
                        #coordenadaX = 0
                        #moverSerpiente(listaSerpiente, coordenadaX, coordenadaY, listaComida)
                    elif evento.key == pygame.K_LEFT:
                        coorX = -50
                        coorY = 0
                        #coordenadaY = 0
                        #coordenadaX = -50
                        #moverSerpiente(listaSerpiente, coordenadaX, coordenadaY, listaComida)
                    elif evento.key == pygame.K_RIGHT:
                        coorX = 50
                        coorY = 0
                        #coordenadaY = 0
                        #coordenadaX = 50
                        #moverSerpiente(listaSerpiente, coordenadaX, coordenadaY, listaComida)


        #Borrar pantalla
        ventana.fill(NEGRO)

        if estado == JUGANDO:
            if xMouse >= 675 and xMouse <= 775 and yMouse >= 525 and yMouse <= 575:
                # Se oprimió el botón de jugar, CAMBIAR ESTADO
                xMouse = -1
                estado = MENU

            moverSerpiente(listaSerpiente, coorX, coorY, listaComida)

            cuadricula(ventana)
            dibujarBotonMenuJugar(ventana, botonMenuJuego)
            dibujarSerpiente(ventana, listaSerpiente)
            dibujarComida(ventana, listaComida)
            dibujarMarcador(ventana, puntos, fuente)

            resultado = probarPerder(listaSerpiente)
            if resultado == True:
                archivoTexto = "Puntuaciones.txt"
                escribirPuntuaciones(archivoTexto, puntos)
                estado = PERDER

            if listaComida == []: #La lista queda vacía porque ya la serpiente ya se comió la comida
                colaC = listaSerpiente[len(listaSerpiente)-1]
                crearComida(listaComida, imgComida) #Se crea uno nuevo, ya sabe que se comió el anterior
                puntos += 1
                if puntos == 15:
                    estado = GANAR


        if estado == GANAR:
            dibujarBotonMenuJugar(ventana, botonMenuJuego)
            archivoTexto = "Puntuaciones.txt"
            escribirPuntuaciones(archivoTexto, puntos)
            if xMouse >= 675 and xMouse <= 775 and yMouse >= 525 and yMouse <= 575:
                # Se oprimió el botón de jugar, CAMBIAR ESTADO
                xMouse = -1
                estado = MENU

            #dibujar el texto
            textoGanar1 = fuente.render("¡GANASTE!", 1, AMARILLO)
            textoGanar2 = fuente.render("Lograste obtener 15 puntos", 1, AMARILLO)
            textoGanar3 = fuente.render("Presiona el botón MENÚ para volver a jugar", 1, AMARILLO)
            ventana.blit(textoGanar1, (60, 150))
            ventana.blit(textoGanar2, (60, 300))
            ventana.blit(textoGanar3, (60, 330))

        if estado == PERDER:
            dibujarBotonMenuJugar(ventana, botonMenuJuego)
            if xMouse >= 675 and xMouse <= 775 and yMouse >= 525 and yMouse <= 575:
                # Se oprimió el botón de jugar, CAMBIAR ESTADO
                xMouse = -1
                estado = MENU

            #dibujar el texto
            textoPerder1 = fuente.render("Has perdido", 1, AZUL)
            textoPerder2 = fuente.render("Presiona el botón MENÚ para volver a jugar", 1, AZUL)
            ventana.blit(textoPerder1, (60, 150))
            ventana.blit(textoPerder2, (60, 300))


        if estado == MENU:
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarFondoMenu(ventana, fondoMenu)
            dibujarBotonJugar(ventana, botonJugar)
            dibujarBotonPuntuaciones(ventana,botonPuntos)
            dibujarBotonInfo(ventana,botonInfo)

        elif estado == PUNTUACION:
            dibujarFondo(ventana, fondo)
            dibujarBotonMenu(ventana, botonMenu)
            puntuaciones = leerPuntuaciones("Puntuaciones.txt")
            registroPuntos = (puntuaciones[len(puntuaciones) - 1])
            print(puntuaciones)

            #dibujar el texto
            textoPuntuacion1 = fuente.render("PUNTUACIONES", 1, ROJO)
            textoPuntuacion2 = fuente.render("La última puntuación lograda fue: ", 1, ROJO)
            textoPuntuacion3 = fuente.render(registroPuntos, 1, ROJO)
            ventana.blit(textoPuntuacion1, (300,100))
            ventana.blit(textoPuntuacion2, (100, 200))
            ventana.blit(textoPuntuacion3, (100, 250))
            if xMouse >= 625 and xMouse <= 725 and yMouse >= 465 and yMouse <= 515:
                # Se oprimió el botón de información, CAMBIAR ESTADO
                xMouse = -1
                estado = MENU

        elif estado == INFORMACION:
            dibujarFondo(ventana, fondo)
            dibujarBotonMenu(ventana, botonMenu)

            #dibujar el texto
            textoInfo1 = fuente.render("Fundamentos de programación: Proyecto Final ",1,NEGRO)
            textoInfo2 = fuente.render("Ivana Olvera Mérida                                                A01746744", 1, NEGRO)
            textoInfo3 = fuente.render("Instrucciones del juego",1,NEGRO)
            textoInfo4 = fuente.render("El usuario se encarga de controlar una criatura", 1, NEGRO)
            textoInfo5 = fuente.render("larga y delgada, similar a una serpiente, que se",1,NEGRO)
            textoInfo6 = fuente.render("desplaza en un plano delimitado mientras recoge",1,NEGRO)
            textoInfo7 = fuente.render("alimentos; debe evitar golpear alguna parte de",1,NEGRO)
            textoInfo8 = fuente.render("las paredes que rodean el área sobre la cual se",1,NEGRO)
            textoInfo9 = fuente.render("desplaza.",1,NEGRO)
            ventana.blit(textoInfo1,(60,100))
            ventana.blit(textoInfo2,(60,150))
            ventana.blit(textoInfo3,(250,250))
            ventana.blit(textoInfo4,(60, 300))
            ventana.blit(textoInfo5,(60, 330))
            ventana.blit(textoInfo6,(60,360))
            ventana.blit(textoInfo7, (60, 390))
            ventana.blit(textoInfo8,(60, 420))
            ventana.blit(textoInfo9,(60,450))

            if xMouse >= 625 and xMouse <= 725 and yMouse >= 465 and yMouse <= 515:
                # Se oprimió el botón de información, CAMBIAR ESTADO
                xMouse = -1
                estado = MENU


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(3)  # 40 fps

    #Después del ciclo principal
    pygame.quit()  #Termina pygame


#Función principal, aquí resuelves el problema
def main():
    dibujar()   #Por ahora, solo dibuja

main()

