# Autor: Andrea Romo Ortega
# Videojuego de gatitos

import pygame   # Librería de pygame
import math
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#temporalmente las coordenadas de la gotita
xgatita = ANCHO//2.5
ygatita = ALTO//1.4

xEnemigo = ANCHO//2
yEnemigo = 0

xMuerto = ANCHO//2
yMuerto = 0


Xnaranja = ANCHO//2
Ynajanja = ALTO //2

Xrosa = 0
Yrosa = ALTO//2

DX = +1 # va hacia la derecha, (-1) va la izquierda

#FONDO
xFondo = 0 # global

angulo=0 #grados

def dibujarMenu(ventana, btnPlay):
    global xFondo
    ventana.blit(btnPlay, (300, 275) )
    xFondo -= 1


def dibujarMouse(ventana, xmouse, ymouse):
    if xmouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xmouse, ymouse), 30)



def dibujarFondo(ventana, fondoJuego):
    global xFondo
    ventana.blit(fondoJuego, (0, 0))
    xFondo -= 1


def dibujarGatita(ventana, gatita):
    ventana.blit(gatita, (xgatita, ygatita))



def dibujarEnemigo(ventana,enemigo):
    global xEnemigo, DX, yEnemigo, angulo
    ventana.blit(enemigo, (xEnemigo, yEnemigo))
    xEnemigo += DX
    #probar choque der-izq
    if xEnemigo == ANCHO-239 or xEnemigo <=0:   #128 x 78
        DX= -DX
        # moverlo en y
        dy = int(200 * math.sin(math.radians(angulo))) + 200
        yEnemigo = dy
        angulo += 5



# Estructura básica de un programa que usa pygame para dibujar


def dibujarProyectil(ventana, spriteBala):
    if spriteBala.rect.left != -1 :
        ventana.blit(spriteBala.image, spriteBala.rect)
        spriteBala.rect.top -= 20
        if spriteBala.rect.top < 32:
            spriteBala.rect.left = -1



def ColisionEnemigo(listaBalas, listaEnemigos):

    for bala in listaBalas:
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo)== True:
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)








def dibujarMarcador(ventana, marcador, fuente, listaEnemigo):


    texto = fuente.render("Puntos: " + str(marcador),0, ROJO) #convierte texto a imagen
    ventana.blit(texto,(10,50))




def genararEnemigos(listaEnemigos, imgEnemigo):

    if xEnemigo == ANCHO - 239 or xEnemigo <= 0:  # 128 x 78
        DX = -DX
    for y in range(100, 200+1, 100): # donde empieza donde termina y va de 100 e 100  #renglones de enemigos que aparecerán en pantalla
        for x in range (133,670,133): # esta es la varieba x o sea columnas horizontales
            #crear enemigos en x,y con sprites
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image= imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = x
            spriteEnemigo.rect.top = y
            listaEnemigos.append (spriteEnemigo) #es la lista de sprite



def dibujarListaEnemigo(ventana, listaEnemigo):
    for enemigo in listaEnemigo:
        ventana.blit(enemigo.image, enemigo.rect)


def verificarColision(listaMuerto, spriteBala,listaBalas):
    for bala in listaBalas:
        for muerto in listaMuerto:
            if muerto.rect.colliderect(spriteBala)  == True:
                listaMuerto.remove(muerto)
                spriteBala.rect.left = -1



            break




def dibujarAtaque(ventana, spriteAtaque):
    if spriteAtaque.rect.left != -1:
        ventana.blit(spriteAtaque.img, spriteAtaque.rect, )
        spriteAtaque.rect.top += 2


def dibujarListaBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.top -= 20


def dibujarFondoMenu(ventana, fondoMenu):
    global xFondo
    ventana.blit(fondoMenu, (0, 0))
    xFondo-= 1


def dibujarFondoGanaste(ventana, fondoGanaste):
    global xFondo
    ventana.blit(fondoGanaste,(0, 0))
    xFondo -= 1


def dibujarFondoPerdiste(ventana, fondoPerdiste):
    global xFondo
    ventana.blit(fondoPerdiste,(0, 0))
    xFondo-= 1


def generarMuerto(listaMuerto, muerto):
    for y in range(200, 400+1, 100): # donde empieza donde termina y va de 100 e 100  #renglones de enemigos que aparecerán en pantalla
        for x in range (133): # esta es la varieba x o sea columnas horizontales
            #crear enemigos en x,y con sprites
            spriteMuerto = pygame.sprite.Sprite()
            spriteMuerto.image= muerto
            spriteMuerto.rect = muerto.get_rect()
            spriteMuerto.rect.left = x
            spriteMuerto.rect.top = y
            listaMuerto.append (spriteMuerto) #es la lista de sprite


def dibujarmuerto(ventana, muerto):
    global xMuerto, DX, yMuerto, DY
    ventana.blit(muerto, (xMuerto, yMuerto))
    xMuerto += DX
    # probar choque der-izq
    if xMuerto == ANCHO - 239 or xMuerto <= 0:  # 128 x 78
        DX = -DX






def contarPuntos(listaEnemigos, marcador):
    for enemigo in listaEnemigos:
        if ColisionEnemigo == True:
            marcador += 500


def dibujarNaranja(ventana, naranja):
    global Xnaranja, DX, Ynajanja, DY
    ventana.blit(naranja, (Xnaranja, Ynajanja))
    Xnaranja += DX
    # probar choque der-izq
    if Xnaranja == ANCHO - 239 or Xnaranja <= 0:  # 128 x 78
        DX = -DX


def dibujarRosa(ventana, rosa):
    global Xrosa, DX, Yrosa, DY
    ventana.blit(rosa, (Xrosa, Yrosa))
    Xrosa += DX
    # probar choque der-izq
    if Xrosa == ANCHO - 239 or Xrosa <= 0:  # 128 x 78
        DX = -DX


def premios(puntos, spriteBala, rosa, naranja):
    if spriteBala.rect.colliderect(naranja):
        puntos +=1000

    elif spriteBala.rect.colliderect(rosa):
        puntos+= 5000




def dibujar():
    global xgatita, ygatita #voyy a usar la variable global
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
#imagenes
    btnPlay=  pygame.image.load("btn_play.png")
    fondoMenu = pygame.image.load("fondo_menu_.png")
    fondoGanaste= pygame.image.load("fondo_ganaste.png")
    fondoPerdiste= pygame.image.load("fondo_perdiste.png")
    fondoJuego= pygame.image.load("fondo_nivel.png")
    gatita = pygame.image.load("gato_tamaño.png")
    muerto = pygame.image.load("estambre_morado_.png")
    naranja =pygame.image.load("estambre_naranja_.png")
    rosa=pygame.image.load("estambre_rosa_.png")
    enemigo = pygame.image.load("estambre_verde_.png")
    imgBala = pygame.image.load("estambre_azul_.png")

    #lista de enemigos
    listaEnemigos=[] #creamos una lista vacía
    genararEnemigos(listaEnemigos, enemigo)
    listaMuerto =[]
    generarMuerto(listaMuerto, muerto)

    #lista de proyectile
    listaBalas = [] #lista vacía

    #SPRITES
    spriteBala= pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect() #datos de la imagen.
    spriteBala.rect.left = -1 # x
    spriteBala.rect.top = -1 #y

    #AUDIO
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("miau.wav")
    pygame.mixer.music.load("Sm_Lost_In_Japan.mp3")
    pygame.mixer.music.play(-1)  #-1= infinito



    #mouse

    xmouse = -1
    ymouse = -1

    #estados
    MENU =1
    NIVEL1 = 2
    GANASTE = 3
    PERDISTE =4
    estado = MENU

    #texto
    fuente= pygame.font.SysFont("Arial", 56)

    marcador= 0
    puntos = 0



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xmouse,ymouse = pygame.mouse.get_pos()
                if xmouse>=301 and xmouse<= 446 and ymouse>=275 and ymouse<=447:
                    xmouse = -1
                    estado= NIVEL1
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    xgatita += 20
                elif evento.key == pygame.K_LEFT:
                    xgatita -= 20
                elif evento.key ==pygame.K_UP:
                    ygatita -= 20
                elif evento.key == pygame.K_DOWN:
                    ygatita += 20
                elif evento.key == pygame.K_SPACE:
                    nuevaBala = pygame.sprite.Sprite()
                    nuevaBala.image = imgBala
                    nuevaBala.rect = imgBala.get_rect()
                    nuevaBala.rect.left = xgatita+45-20
                    nuevaBala.rect.top = ygatita
                    listaBalas.append(nuevaBala)
                    efectoDisparo.play()
            elif evento.type == pygame.KEYUP:
                if evento.key== pygame.K_p:
                        estado = PERDISTE

                elif evento.key == pygame.K_m:
                        estado = MENU

                elif evento.key == pygame.K_g:
                        estado= GANASTE



                    #if spriteBala.rect.left == -1:
                    #spriteBala.rect.left = xgatita +45-20
                    #spriteBala.rect.top = ygatita



     # Borrar pantalla
        ventana.fill(BLANCO)

        if estado == MENU:
            dibujarMouse(ventana, xmouse, ymouse)
            dibujarMenu(ventana, btnPlay)
            dibujarFondoMenu(ventana, fondoMenu)

        elif estado== NIVEL1:
            # actualizar
            probarColision = ColisionEnemigo(listaBalas, listaEnemigos)
            while probarColision == True:  #es la condición
                marcador += 500





             #COLISIÓN CONTRA TODOS LOS ENEMIGOS

            contarPuntos(listaEnemigos, puntos)

            #premios(puntos,spriteBala, rosa, naranja)




            moverBalas(listaBalas)# lista para que avancen as balas

             #DIBUJAR
            dibujarFondo(ventana, fondoJuego)
            dibujarGatita(ventana, gatita)
            #dibujarEnemigo( ventana, enemigo)
            dibujarmuerto (ventana, muerto)
            dibujarListaEnemigo (ventana, listaEnemigos)
            dibujarProyectil( ventana, spriteBala)
            dibujarListaBalas(ventana, listaBalas)
            dibujarNaranja(ventana,naranja)
            dibujarRosa (ventana,rosa)
            dibujarMarcador(ventana, marcador, fuente, contarPuntos)
            #dibujarAtaque(ventana, spriteAtaque)






        elif estado == GANASTE:
            dibujarFondoGanaste(ventana, fondoGanaste)







        elif estado == PERDISTE:

            dibujarFondoPerdiste(ventana, fondoPerdiste)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()