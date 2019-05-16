# encoding: UTF-8

import pygame   # Librería de pygame
import Game2
import Archivos


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad

pasoMomia = 0
pasoJugador = 0
animacionBoss=0
ROJO = (255, 0, 0)
momia = []

pygame.font.init()
font= pygame.font.Font('../Imagenes/Metal.ttf',50)


TECLADO = {'R': pygame.K_d, 'L': pygame.K_a, 'S': pygame.K_p}


class Puntero(pygame.Rect):

    def __init__(self):
        pygame.Rect.__init__(self,0,0,2,2)

    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

def enemigo(ventana,x,y):
    # Lista enemigos
    global momia
    for i in range(1, 19):
        momia.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(
            "../Imagenes/Enemigos/" + str(i) + ".png"), [128, 128]), 1, 0))
    global pasoMomia
    ventana.blit(momia[pasoMomia], [x,y])
    if pasoMomia >= 17:
        pasoMomia = 0
    else:
        pasoMomia += 1

def enemigoD(ventana,x,y):
    global momia
    for i in range(1, 19):
        momia.append(pygame.transform.scale(pygame.image.load(
            "../Imagenes/Enemigos/" + str(i) + ".png"), [128, 128]))
    global pasoMomia
    ventana.blit(momia[pasoMomia], [x, y])

    if pasoMomia >= 17:
        pasoMomia = 0
    else:
        pasoMomia += 1


def boss(ventana,x,y):
    boss = []
    for k in range(15):
        boss.append(pygame.image.load("../Imagenes/BOSS/"+str(k)+".png"))
    global  animacionBoss
    ventana.blit(boss[animacionBoss],[x,y])
    if animacionBoss >= 14:
        animacionBoss = 0
    else:
        animacionBoss+=1

# Estructura básica de un programa que usa pygame para dibujar
def dibujarLevel1():
    # Inicializa el motor de pygame
    pygame.init()
    puntero=Puntero()
    cantidadMomias=10
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    velJugador = 0
    posX = 0
    jugador = []
    jugadorA = []
    jugadorL = []
    jugadorAA = []
    mov = False
    atack = False
    atackL = False
    atackA = False
    pygame.mixer.music.load('../Sonidos/BOSS.mp3')
    pygame.mixer.music.play()
    aux=1
    GAMEOVER =False
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        tiempo = pygame.time.get_ticks()/1000
        if (aux==tiempo):
            aux+=1
            print(tiempo)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            if evento.type == pygame.KEYDOWN:
                if evento.key== TECLADO['L']:
                    velJugador=-5
                    mov = True
                if evento.key == TECLADO['R']:
                    velJugador= 5
                    mov=True
            if evento.type == pygame.KEYUP:
                if evento.key== TECLADO['L']:
                    velJugador=0
                    mov = False
                if evento.key == TECLADO ['R']:
                    velJugador=0
                    mov=False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if GAMEOVER == True:
                    main.main()
                pygame.mixer.music.load('../Sonidos/disparo.mp3')
                pygame.mixer.music.play()
                x,y= pygame.mouse.get_pos()
                if y<300:
                    atackA = True
                if x>posX and y>400:
                    atack= True
                if x<posX and y>400:
                    atackL=True
                cantidadMomias-=1

            if evento.type == pygame.MOUSEBUTTONUP:
                atackA= False
                atack = False
                atackL = False

        contador= font.render("Tiempo : "+str(int(tiempo)),0,(120,70,0))



        fnivel= pygame.image.load('../Imagenes/fondo1.jpg')
        fondoNivel1 = pygame.transform.scale(fnivel,[ANCHO,ALTO])
        ventana.blit(fondoNivel1, [0, 0])
        ventana.blit(contador, (20, 20))
        #dibujaer enemigo
        gap=128
        for x in range(cantidadMomias):
            enemigo(ventana, (ANCHO - gap)-int(tiempo)*10, ALTO - 128)
            gap+=32
        if atack==False:
            for i in range(10):
                jugador.append(pygame.transform.scale(pygame.image.load(
                    "../Imagenes/Jugador/" + str(i) + ".png"), [150, 150]))
        if atack== True:
            for w in range(28):
                jugadorA.append(pygame.transform.scale(pygame.image.load(
                    "../Imagenes/Disparo/"+str(w)+".png"),[459,303]))
        if atackL == True:
            for z in range(28):
                jugadorL.append(pygame.transform.flip(
                    pygame.transform.scale(pygame.image.load("../Imagenes/Disparo/"+str(z)+".png"),[459,303]),1,0))
        if atackA == True:
            for y in range(24):
                jugadorAA.append(pygame.transform.scale(pygame.image.load(
                    "../Imagenes/Disparo_arriba/"+str(y)+".png"),[155,390]))

        global pasoJugador

        if velJugador>=0 and atack==False:
            ventana.blit(jugador[pasoJugador], [posX, ALTO-150])


        elif(velJugador<0):
            ventana.blit(pygame.transform.flip(jugador[pasoJugador],1,0),[posX,ALTO-150])

        if atack==True:
            ventana.blit(jugadorA[pasoJugador],[posX,ALTO-250])
            pasoJugador += 1

        if atackL== True:
            ventana.blit(jugadorL[pasoJugador],[posX-375,ALTO-250])
            pasoJugador+=1

        if atackA==True:
            ventana.blit(jugadorAA[pasoJugador],[posX,ALTO-390])
            pasoJugador+=1

        if pasoJugador >= 9 and atack== False:
            pasoJugador = 0

        elif pasoJugador>=27 and atack== True:
            pasoJugador = 0

        elif pasoJugador>=24 and atackL== True:
            pasoJugador = 0

        if mov == True:
            pasoJugador += 1

        posX+=velJugador
        if tiempo>50:
            ventana.fill(BLANCO)
            ventana.blit(font.render("GAME OVER", True, ROJO), [ANCHO // 2 - 100, 100])
            GAMEOVER = True
        if cantidadMomias==0:
            Archivos.guardarTiempo(tiempo)
            Game2.Level2()

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        puntero.update()

    # Después del ciclo principal
    pygame.quit()  # termina pygame,