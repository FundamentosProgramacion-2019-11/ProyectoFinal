#Michel Antoine Dionne Gutierrez A01748632 Grupo:03
#Proyecto final de programacion
import math
import random

import pygame   # Librería de pygame

# Dimensiones de la pantalla

ANCHO = 800
ALTO = 600
# Colores

#FONDO
xFondo = 0
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#se declaran los archivos
archivo = "Score.txt"

# Enemigo
xEnemigo = ANCHO//2
yEnemigo = 20
DX = +6   #derecha, (-1) izquierda
#Fondo
planetas = 0
#Movimiento de la nave enemiga
angulo = 0    #grados

# Funcion para dibujar el boton de play
def dibujarMenu(ventana, btnPlay):
    ventana.blit(btnPlay, (300, 275))      #Calcular x, y para centrar la imagen

#funcion para dibujar en donde el usuario  pique con el mouse
def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 50)

#funcion para dibujar el boton de exit
def dibujarExit(ventana, btnExit):
    ventana.blit(btnExit, (300, 425))
#dibuja el fondo del menu principal
def dibujarFondo(ventana, fondoMenu):
    ventana.blit(fondoMenu, (0, 0))

#dibuja el personaje principal
def dibujarNave(ventana, spriteNave):
    ventana.blit(spriteNave.image, spriteNave.rect)

def dibujarFondoMenuMenu(ventana, fondoMenuMenu):
    #global xFondo
    ventana.blit(fondoMenuMenu, (0, 0))
    #xFondo -= 1

#dibuja el boton de la opcion de los controles
def dibujarControls(ventana, btnControl):
    ventana.blit(btnControl, (300, 350))

#dibuja el fondo del estado controls
def dibujarFondoControls(ventana, fondoMenuControls):
    ventana.blit( fondoMenuControls, (0,0))

#dibuja el boton de back en el estado controls
def dibujarBackUno(ventana, btnBackUno):
    ventana.blit(btnBackUno, (50,500))

#el proyectil del personaje o "rojo"
def dibujarProyectilSith(ventana, spriteLaserRojo):
    if spriteLaserRojo.rect.left != -1:
        ventana.blit(spriteLaserRojo.image, spriteLaserRojo.rect)
        spriteLaserRojo.rect.top -= 10
        if spriteLaserRojo.rect.top < -21:
            spriteLaserRojo.rect.left = -1

#prueba si el jugador le atina al enemigo
#Regresa True si hay colision, False en otro caso
def probarColision(listaLaserRojos, listaEnemigos):
    for laser in listaLaserRojos:
        for enemigo in listaEnemigos:
            if laser.rect.colliderect(enemigo) == True:
                listaEnemigos.remove(enemigo)
                listaLaserRojos.remove(laser)
                return True
                break  #siguiente bala

#dibuja los puntos que lleva en la partida el jugador
def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render("Score: "+ str(marcador), 1, ROJO)
    ventana.blit(texto, (10,550))

#dibuja el primer proyectil enemigo o "verde"
def dibujarProyectilJediUno(ventana, spriteLaserVerde):
    if spriteLaserVerde.rect.left != -1:
        ventana.blit(spriteLaserVerde.image, spriteLaserVerde.rect)
        spriteLaserVerde.rect.top += 3
        if spriteLaserVerde.rect.top >= 621:
            spriteLaserVerde.rect.left = -1
#dibuja el segundo proyectil enemigo o "verde"
def dibujarProyectilJediDos(ventana, spriteLaserVerdeDos):
    if spriteLaserVerdeDos.rect.left != -1:
        ventana.blit(spriteLaserVerdeDos.image, spriteLaserVerdeDos.rect)
        spriteLaserVerdeDos.rect.top += 7
        if spriteLaserVerdeDos.rect.top >= 621:
            spriteLaserVerdeDos.rect.left = -1

#dibuja la imagen del teclado para ver los controles
def dibujarTeclado(ventana, teclado):
    ventana.blit(teclado,(50,50))

#Dibuja y explica las teclas
def dibujarControles(ventana, fuenteControls):
    texto = fuenteControls.render("Arriba: Flecha hacia arriba",1,ROJO)
    texto1 = fuenteControls.render("Abajo: Flecha hacia abajo",1,ROJO)
    texto2 = fuenteControls.render("Izquierda: Flecha a la izquierda",1,ROJO)
    texto3 = fuenteControls.render("Derecha: Flecha a la derecha",1,ROJO)
    texto4 = fuenteControls.render("Disparo: Barra espaciadora",1,ROJO)
    ventana.blit(texto,(300,360))
    ventana.blit(texto1, (300, 400))
    ventana.blit(texto2, (300, 440))
    ventana.blit(texto3, (300, 480))
    ventana.blit(texto4, (300, 520))

#Dibuja el puntaje mas alto de todos en el menu
def dibujarHighScore(ventana, highScore, marcadorHighScore):
    texto = highScore.render("High Score: "+ str(marcadorHighScore),1,ROJO)
    ventana.blit(texto, (480,50))

#Genera un set de enemigos
def generarEnemigos(listaEnemigos, enemigo):
    for y in range(30,231,100):#renglones (coordenada y)
        for x in range(133,670,133): #columnas (x)
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = enemigo
            spriteEnemigo.rect = enemigo.get_rect()
            spriteEnemigo.rect.left = x
            spriteEnemigo.rect.top = y
            listaEnemigos.append(spriteEnemigo) #lista de sprites

#dibuja el set de nemigos
def dibujarListaEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

#revisa si el proyectil rojo impacta una nave enemiga
def verificarColision(listaEnemigos, spriteLaserRojo):
    for enemigo in listaEnemigos:
        if enemigo.rect.colliderect(spriteLaserRojo) == True:
            listaEnemigos.remove(enemigo)
            spriteLaserRojo.rect.left = -1

#dibuja todos los proyectiles del jugador
def dibujarListaLaserRojos(ventana, listaLaserRojos):
    for laser in listaLaserRojos:
        ventana.blit(laser.image, laser.rect)

#mueve los proyectiles del jugador
def moverLaserSith(listaLaserRojos):
    for laser in listaLaserRojos:
        laser.rect.top -= 20

#dibuja el tercer proyectil enemigo o "verde"
def dibujarProyectilJediTres(ventana, spriteLaserVerdeTres):
    if spriteLaserVerdeTres.rect.left != -1:
        ventana.blit(spriteLaserVerdeTres.image, spriteLaserVerdeTres.rect)
        spriteLaserVerdeTres.rect.top += 11
        if spriteLaserVerdeTres.rect.top >= 621:
            spriteLaserVerdeTres.rect.left = -1

#en caso de ganar dibuja el fondo de victoria
def dibujarVictoria(ventana, fondoVictoria):
    ventana.blit(fondoVictoria,(0,0))

#en caso de perder dibuja el fondo de derrota
def dibujarPerdido(ventana, fondoPerdido):
    ventana.blit(fondoPerdido,(0,0))

#dibuja el boton para regresar al menu principal desde el estado de victoria o derrota
def dibujarBtnMenu(ventana, btnMenu):
    ventana.blit(btnMenu,(50,500))

#revisa si los proyectiles enemigos le pegan al personaje
def verificarColisionPerdida(spriteLaserVerde, spriteLaserVerdeDos, spriteLaserVerdeTres,spriteNave):
    if (spriteLaserVerde.rect.colliderect(spriteNave) == True) or (spriteLaserVerdeDos.rect.colliderect(spriteNave) == True) or (spriteLaserVerdeTres.rect.colliderect(spriteNave) == True):
        spriteNave.rect.left =-1
        spriteLaserVerde.rect.left=-1
        spriteLaserVerdeDos.remove()
        spriteLaserVerdeTres.remove()
        return True
    else:
        return False

#el otro boton para el regreso al menu
def dibujarBtnMenuDos(ventana, btnMenu):
    ventana.blit(btnMenu, (50, 500))

def dibujar():
    #global xNave, yNave  #Voy a usar la variable global
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #IMAGENES
    btnPlay = pygame.image.load("button_play.png")
    btnExit = pygame.image.load("button_exit.png")
    btnControl = pygame.image.load("button_controls.png")
    fondoMenuMenu = pygame.image.load("fondo_menu.jpg")
    fondoMenuControls = pygame.image.load("fondo_controls.jpg")
    fondoMenuJugando = pygame.image.load("Fondo_planeta.jpg")
    nave = pygame.image.load("nave_tres.png")
    enemigo = pygame.image.load("nave_enemiga.png")
    btnBackUno = pygame.image.load("button_back_uno.png")
    laserRojo = pygame.image.load("proyectil_sith.png")
    laserVerde = pygame.image.load("laser_jedi.png")
    teclado = pygame.image.load("teclado.jpg")
    fondoVictoria = pygame.image.load("imagenVictoria.jpg")
    fondoPerdido = pygame.image.load("perdida.jpg")
    btnMenu = pygame.image.load("button_menu.png")
    btnMenuDos = pygame.image.load("button_menu.png")

    # LISTA de proyectiles
    listaLaserRojos = []


    #LISTA DE ENEMIGOS
    listaEnemigos = []  #Lista vacia
    generarEnemigos(listaEnemigos, enemigo)

    #Sprite
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = nave
    spriteNave.rect = nave.get_rect()
    spriteNave.rect.left = ANCHO//2
    spriteNave.rect.top = ALTO-spriteNave.rect.height

    spriteLaserRojo = pygame.sprite.Sprite()
    spriteLaserRojo.image = laserRojo
    spriteLaserRojo.rect = laserRojo.get_rect()     #datos de la imagen
    spriteLaserRojo.rect.left = -1   #x
    spriteLaserRojo.rect.top = -1    #y
    #el ataque enemigo
    spriteLaserVerde = pygame.sprite.Sprite()
    spriteLaserVerde.image = laserVerde
    spriteLaserVerde.rect = laserVerde.get_rect()  # datos de la imagen
    spriteLaserVerde.rect.left = -1  # x
    spriteLaserVerde.rect.top = -1  # y

    spriteLaserVerdeDos = pygame.sprite.Sprite()
    spriteLaserVerdeDos.image = laserVerde
    spriteLaserVerdeDos.rect = laserVerde.get_rect()
    spriteLaserVerdeDos.rect.left = -1
    spriteLaserVerdeDos.rect.top = -1

    spriteLaserVerdeTres = pygame.sprite.Sprite()
    spriteLaserVerdeTres.image = laserVerde
    spriteLaserVerdeTres.rect = laserVerde.get_rect()
    spriteLaserVerdeTres.rect.left = -1
    spriteLaserVerdeTres.rect.top = -1

    #AUDIO
    pygame.mixer.init()
    efectoDisparoSith = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("marchaImperial.mp3")
    pygame.mixer.music.play(-1)

    #MOUSE
    xMouse = -1
    yMouse = -1

    #ESTADOS
    MENU = 1
    JUGANDO = 2
    CONTROLS = 3
    estado = MENU
    VICTORIA = 4
    MUERTO = 5

    #TEXTO
    fuente = pygame.font.SysFont("Arial",25)
    fuenteControls = pygame.font.SysFont("Arial",40)
    highScore = pygame.font.SysFont("Arial",45)

    marcador = 0
    marcadorHighScore = 0

    #tiempos
    tiempoataqueUno = 190
    tiempoataqueDos = 320
    tiempoataqueTres = 600

    #Veces que aparecen los enemigos
    oleada = 0

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                #Oprimio el mouse
                xMouse , yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if estado==MENU and xMouse>= 300 and xMouse<=500 and yMouse>=275 and yMouse<=325:
                    #Oprimio el estado de play, CAMBIAR el ESTADO
                    xMouse = -1
                    estado = JUGANDO
                elif estado==MENU and xMouse>= 300 and xMouse<=500 and yMouse>=350 and yMouse<=400:
                    xMouse = -1
                    estado = CONTROLS
                elif estado==CONTROLS and xMouse>=50 and xMouse<=143 and yMouse>=500 and yMouse<=544:
                    xMouse = -1
                    estado =  MENU
                elif estado==MENU and xMouse>=300 and xMouse<=500 and yMouse>= 425 and yMouse<=475:
                    xMouse = -1
                    termina = True
                elif estado==VICTORIA and xMouse>=50 and xMouse<=153 and yMouse>=500 and yMouse<=540:
                    xMouse = -1
                    estado = MENU
                elif estado==MUERTO and xMouse>=50 and xMouse<=153 and yMouse>=500 and yMouse<=540:
                    xMouse = -1
                    estado = MENU
            elif evento.type == pygame.KEYDOWN:#Oprimio una tecla
                    #VERIFICA que tecla oprimio
                    if evento.key == pygame.K_RIGHT:
                        spriteNave.rect.left += 20
                    elif evento.key == pygame.K_LEFT:
                        spriteNave.rect.left -=20
                    elif evento.key == pygame.K_DOWN:
                        spriteNave.rect.top +=20
                    elif evento.key == pygame.K_UP:
                        spriteNave.rect.top -=20
                    elif evento.key == pygame.K_SPACE:
                        nuevoLaserRojo = pygame.sprite.Sprite()
                        nuevoLaserRojo.image = laserRojo
                        nuevoLaserRojo.rect = laserRojo.get_rect()
                        nuevoLaserRojo.rect.left = spriteNave.rect.left+63.5-6
                        nuevoLaserRojo.rect.top = spriteNave.rect.top
                        listaLaserRojos.append(nuevoLaserRojo)
                        efectoDisparoSith.play()

        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarFondoMenuMenu(ventana, fondoMenuMenu )
            dibujarMenu(ventana,btnPlay)
            dibujarControls(ventana,btnControl)# Va en orden, el primero sera el "menos" importante y el ultimo se superpondra sobre los demas
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarExit(ventana, btnExit)
            dibujarHighScore(ventana,highScore, marcadorHighScore)


        elif estado == JUGANDO:
            #ACTUALIZAR
            pygame.mixer.music.pause()

            tiempoataqueUno -= 1
            tiempoataqueDos -=1
            tiempoataqueTres -=1
            if tiempoataqueUno == 0:
                spriteLaserVerde.rect.left = random.randint(0, ANCHO)   #xEnemigo
                spriteLaserVerde.rect.top = 0 #yEnemigo
                tiempoataqueUno = 190
            elif tiempoataqueDos == 0:
                spriteLaserVerdeDos.rect.left = random.randint(0, ANCHO)  # xEnemigo
                spriteLaserVerdeDos.rect.top = 0  # yEnemigo
                tiempoataqueDos = 320
            elif tiempoataqueTres == 0:
                spriteLaserVerdeTres.rect.left = random.randint(0, ANCHO)  # xEnemigo
                spriteLaserVerdeTres.rect.top = 0  # yEnemigo
                tiempoataqueTres = 600

            if oleada>= 3:
                estado = VICTORIA
                pygame.mixer.music.play()
                spriteLaserVerde.rect.top = -1
                spriteLaserVerdeDos.rect.top = -1
                spriteLaserVerdeTres.rect.top =-1
                spriteNave.rect.left = -1
            elif len(listaEnemigos) == 0:
                generarEnemigos(listaEnemigos,enemigo)
                oleada += 1

            impacto = verificarColisionPerdida(spriteLaserVerde,spriteLaserVerdeDos,spriteLaserVerdeTres,spriteNave)
            if impacto == True:
                estado = MUERTO
                pygame.mixer.music.play()
                impacto = False
                marcador = 0
                spriteLaserVerde.rect.top = -1
                spriteLaserVerdeDos.rect.top = -1
                spriteLaserVerdeTres.rect.top = -1
                oleada = 0
                if len(listaEnemigos) != 15:
                    listaEnemigos.clear()
                    generarEnemigos(listaEnemigos,enemigo)


            hit = probarColision(listaLaserRojos, listaEnemigos)
            if hit == True:
                marcador += 100

            #Colision contra TODOS los enemigos
            verificarColision(listaEnemigos,spriteLaserRojo)
            verificarColisionPerdida(spriteLaserVerde,spriteLaserVerdeDos,spriteLaserVerdeTres,spriteNave)

            #Mover todas las balas
            moverLaserSith(listaLaserRojos)

            #DIBUJAR
            dibujarFondo(ventana,fondoMenuJugando)
            dibujarNave(ventana, spriteNave)
            dibujarListaEnemigos(ventana,listaEnemigos)
            dibujarProyectilSith(ventana, spriteLaserRojo)
            dibujarListaLaserRojos(ventana, listaLaserRojos)
            dibujarProyectilJediUno(ventana, spriteLaserVerde)
            dibujarProyectilJediDos(ventana,spriteLaserVerdeDos)
            dibujarProyectilJediTres(ventana,spriteLaserVerdeTres)
            #Dibuja el texto
            dibujarMarcador(ventana, marcador, fuente)
        elif estado == CONTROLS:
            dibujarFondoControls(ventana, fondoMenuControls)
            dibujarBackUno(ventana, btnBackUno)
            dibujarTeclado(ventana, teclado)
            dibujarControles(ventana, fuenteControls)

        elif estado == VICTORIA:
            dibujarVictoria(ventana, fondoVictoria)
            dibujarBtnMenu(ventana, btnMenu)

        elif estado == MUERTO:
            dibujarPerdido(ventana, fondoPerdido)
            dibujarBtnMenuDos(ventana, btnMenu)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def main():
    dibujar()


main()