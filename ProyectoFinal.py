import random

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse!=-1:
        pygame.draw.circle(ventana,BLANCO,(xMouse,yMouse), 50)





def dibujarFondo(ventana, fondo1):
    ventana.blit(fondo1,(0,0))


def dibujarFondo2(ventana, fondoInicio):
    ventana.blit(fondoInicio,(0,0))


def dibujarPersonaje(ventana, spriteVanellope):
    ventana.blit(spriteVanellope.image, spriteVanellope.rect)


def dibujarDulce1(ventana, spriteDulce1):
    if spriteDulce1.rect.left!=-1:
        ventana.blit(spriteDulce1.image,spriteDulce1.rect)
        spriteDulce1.rect.top+=5


def dibujarDulce2(ventana, spriteDulce2):
    if spriteDulce2.rect.left!=-1:
        ventana.blit(spriteDulce2.image,spriteDulce2.rect)
        spriteDulce2.rect.top+=6


def dibujarTexto(ventana, marcador, fuenteTexto):
    texto =fuenteTexto.render(" " + str(marcador), 1, NEGRO)
    ventana.blit(texto , (698, 75))



def colisionDulce1(spriteDulce1,spriteVanellope):
    if spriteDulce1.rect.colliderect(spriteVanellope)==True:
        spriteDulce1.rect.left=-150
        return True
    else:
        return False


def dibujarBomba(ventana, spriteBomba):
    if spriteBomba.rect.left!=-1:
        ventana.blit(spriteBomba.image,spriteBomba.rect)
        spriteBomba.rect.top+=15
        return True
    else:
        return False


def colisionDulce2(spriteDulce2, spriteVanellope):
    if spriteDulce2.rect.colliderect(spriteVanellope)==True:
        spriteDulce2.rect.left=-170
        return True
    else:
        return False


def dibujardulce3(ventana, spriteDulce3):
    if spriteDulce3.rect.left!=-1:
        ventana.blit(spriteDulce3.image,spriteDulce3.rect)
        spriteDulce3.rect.top+=7


def colisionDulce3(spriteDulce3, spriteVanellope):
    if spriteDulce3.rect.colliderect(spriteVanellope)==True:
        spriteDulce3.rect.left=-180
        return True
    else:
        return False


def dibujarFondoFinal(ventana, fondoFinal):
    ventana.blit(fondoFinal,(0,0))


def dibujarTitulo(ventana, tituloGameOver):
    ventana.blit(tituloGameOver,(300,50))





def dibujarTexto2(ventana, marcador, fuenteTexto):
    texto=fuenteTexto.render(" "+ str(marcador),5,NEGRO)
    ventana.blit(texto,(415,292))


def dibujarTexto3(ventana, marcador, fuenteTexto):
    marcador=seleccionarPuntos("puntos.txt")
    texto=fuenteTexto.render(" " + str(marcador),10,NEGRO)
    ventana.blit(texto,(670,35))


def dibujarLista(ventana, lista):
    for dulce in lista:
        if dulce.rect.left!=-1:
            ventana.blit(dulce.image,dulce.rect)
            dulce.rect.top+=5



def dibujarListaAleatoria(lista):
    for dulce in lista:
        dulce.rect.left=random.randint(0,ANCHO)
        dulce.rect.top=0




def escribirPuntos(archivo,marcador):
    puntos=open(archivo,"a")
    puntos.write(str(marcador)+"\n")
    puntos.close()


def seleccionarPuntos(archivo):
    lista=[]
    entrada=open(archivo,"r")
    for linea in entrada:
        puntos=int(linea[0:-1])
        lista.append(puntos)
    maximo=max(lista)
    entrada.close()
    return maximo


def dibujarDulce4(ventana, spriteDulce4):
    if spriteDulce4.rect.left!=-1:
        ventana.blit(spriteDulce4.image,spriteDulce4.rect)
        spriteDulce4.rect.top+=5


def colisionDulce4(spriteDulce4, spriteVanellope):
    if spriteDulce4.rect.colliderect(spriteVanellope)==True:
        spriteDulce4.rect.left=-150
        return True
    else:
        return False


def dibujarDulce5(ventana, spriteDulce5):
    if spriteDulce5.rect.left!=-1:
        ventana.blit(spriteDulce5.image,spriteDulce5.rect)
        spriteDulce5.rect.top+=8


def colisionDulce5(spriteDulce5, spriteVanellope):
    if spriteDulce5.rect.colliderect(spriteVanellope)==True:
        spriteDulce5.rect.left=-150
        return True
    else:
        return False


def dibujar():

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Imagenes
    fondo1=pygame.image.load("inicioFondo.png")
    vanellope=pygame.image.load("vanellope.png")
    fondoInicio=pygame.image.load("jugando.png")
    dulce1=pygame.image.load("dulce1.png")
    dulce2=pygame.image.load("dulce2.png")
    dulce3=pygame.image.load("dulce3.png")
    dulce4=pygame.image.load("dulce4.png")
    dulce5=pygame.image.load("dulce5.png")
    bomba=pygame.image.load("enemigo.png")
    fondoFinal=pygame.image.load("fondoGame.png")



    #SPRITES
    #Sprites del personaje
    spriteVanellope=pygame.sprite.Sprite()
    spriteVanellope.image=vanellope
    spriteVanellope.rect=vanellope.get_rect()
    spriteVanellope.rect.left=ANCHO//2
    spriteVanellope.rect.top=450


    #Sprites del dulce1
    spriteDulce1=pygame.sprite.Sprite()
    spriteDulce1.image=dulce1
    spriteDulce1.rect=dulce1.get_rect()
    spriteDulce1.rect.left=250
    spriteDulce1.rect.top=-1

    #Sprites del dulce 2
    spriteDulce2=pygame.sprite.Sprite()
    spriteDulce2.image=dulce2
    spriteDulce2.rect=dulce2.get_rect()
    spriteDulce2.rect.left=500
    spriteDulce2.rect.top=-1

    #Sprites del dulce 3
    spriteDulce3=pygame.sprite.Sprite()
    spriteDulce3.image=dulce3
    spriteDulce3.rect=dulce3.get_rect()
    spriteDulce3.rect.left=750
    spriteDulce3.rect.top=-1

    #Sprites dulce 4
    spriteDulce4=pygame.sprite.Sprite()
    spriteDulce4.image=dulce4
    spriteDulce4.rect=dulce4.get_rect()
    spriteDulce4.rect.left=100
    spriteDulce4.rect.top=-1

    #sprites dulce 5
    spriteDulce5=pygame.sprite.Sprite()
    spriteDulce5.image=dulce5
    spriteDulce5.rect=dulce5.get_rect()
    spriteDulce5.rect.left=50
    spriteDulce5.rect.top=-1
    #sprites bomba
    spriteBomba=pygame.sprite.Sprite()
    spriteBomba.image=bomba
    spriteBomba.rect=bomba.get_rect()
    spriteBomba.rect.left=-1
    spriteBomba.rect.top=-1

    #LISTA
    lista=[spriteDulce3,spriteDulce2,spriteDulce1,spriteDulce4,spriteDulce5]


    # Mouse
    xMouse = -1
    yMouse = -1

    # Estados
    MENU = 1
    JUGANDO = 2
    PERDIO=3
    estado = MENU

    #AUDIO
    pygame.mixer.init()
    ganoDulce=pygame.mixer.Sound("ganoPuntos.wav")
    perdio=pygame.mixer.Sound("perdio.wav")
    click=pygame.mixer.Sound("click.wav")




    # TEXTO
    fuenteTexto = pygame.font.SysFont("Comic Sans MS", 20)

    #MARCADOR
    marcador=0

    #TIEMPO
    tiempoDulce = 100

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type ==pygame.MOUSEBUTTONDOWN:
                #OPRIMIO EL MOUSE
                xMouse, yMouse =pygame.mouse.get_pos()
                print(xMouse,yMouse)
                if xMouse>=310 and xMouse<=460 and yMouse>=400 and yMouse<=490:
                    #Sabemos que se oprimío el botón de play, camabiar el ESTADO
                    click.play()
                    xMouse=-1
                    marcador=0
                    estado=JUGANDO
                if xMouse>=395 and xMouse<=450 and yMouse>=460 and yMouse<=567:
                    xMouse=-1
                    click.play()
                    estado=MENU
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    spriteVanellope.rect.left += 50
                elif evento.key == pygame.K_LEFT:
                    spriteVanellope.rect.left -= 50



        # Borrar pantalla
        ventana.fill(NEGRO)



        # Dibujar, aquí haces todos los trazos que requieras
        if estado==MENU:
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarFondo(ventana,fondo1)
            dibujarTexto3(ventana,marcador,fuenteTexto)

        elif estado==JUGANDO:
            tiempoDulce-=1
            dibujarFondo2(ventana,fondoInicio)
            dibujarPersonaje(ventana, spriteVanellope)
            dibujarDulce1(ventana, spriteDulce1)
            dibujarDulce2(ventana, spriteDulce2)
            dibujardulce3(ventana, spriteDulce3)
            dibujarDulce4(ventana,spriteDulce4)
            dibujarDulce5(ventana,spriteDulce5)
            dibujarLista(ventana,lista)
            dibujarBomba(ventana, spriteBomba)



            # DIBUJAR EL TEXTO
            dibujarTexto(ventana, marcador, fuenteTexto)
            if tiempoDulce==3:

                dibujarListaAleatoria(lista)
                spriteBomba.rect.left=random.randint(0,ANCHO)
                spriteBomba.rect.top=0
                tiempoDulce=100



            colision1=colisionDulce1(spriteDulce1,spriteVanellope)
            if colision1==True:
                ganoDulce.play()
                marcador+=5

            colision2=colisionDulce2(spriteDulce2,spriteVanellope)
            if colision2==True:
                ganoDulce.play()
                marcador+=5

            colision3=colisionDulce3(spriteDulce3,spriteVanellope)
            if colision3==True:
                ganoDulce.play()
                marcador+=5
            colision4=colisionDulce4(spriteDulce4,spriteVanellope)
            if colision4==True:
                ganoDulce.play()
                marcador+=5
            colision5=colisionDulce5(spriteDulce5,spriteVanellope)
            if colision5 ==True:
                ganoDulce.play()
                marcador+=5

            if spriteBomba.rect.colliderect(spriteVanellope) == True:
                spriteBomba.rect.top=-140


                estado = PERDIO
                perdio.play()
                escribirPuntos("puntos.txt", marcador)
                seleccionarPuntos("puntos.txt")
        elif estado==PERDIO:
            dibujarFondoFinal(ventana,fondoFinal)
            dibujarTexto2(ventana,marcador,fuenteTexto)















        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()