import pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, m√°s de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# VARIABLES GLOBALES
xEnemigo = ANCHO//2
yEnemigo = 0
DX = +10    # + derecha,  - izquierda
angulo = 0  # Movimiento senoidal

# Dibuja el menu (botones)
def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar, (300,275))


def dibujarCirculo(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 30)


def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0, 0))


def dibujarNave(ventana, imgNave, xNave, yNave, puntos):
    ventana.blit(imgNave, (xNave, yNave))
    ###########
    pygame.draw.rect(ventana, ROJO, (10, 50, puntos, 10))


def dibujarEnemigo(ventana, imgEnemigo):
    global xEnemigo, yEnemigo, DX, angulo
    ventana.blit(imgEnemigo, (xEnemigo, yEnemigo))
    # Actualizar coordenadas del enemigo
    xEnemigo += DX
    if xEnemigo + 128 >= ANCHO or xEnemigo <= 0:
        DX = -DX

    #Movimiento vertical
    dy = int(ALTO/2*math.sin(math.radians(angulo))) + ALTO/2
    yEnemigo = dy
    angulo += 10



def dibujarBala(ventana, spriteBala):
    if spriteBala.rect.left != -1:
        ventana.blit(spriteBala.image, spriteBala.rect)
        # Actualizar bala
        spriteBala.rect.top -= 20
        if spriteBala.rect.top <= -43:
            spriteBala.rect.left = -1   # NO se dibuja


def verificarColisionBalaEnemigo(spriteBala):   #  , spriteEnemigo
    global yEnemigo, xEnemigo, DX
    xBala = spriteBala.rect.left
    yBala = spriteBala.rect.top
    # xEnemigo = spriteEnemigo.rect.left
    if xBala>=xEnemigo and xBala<=xEnemigo+128:
        if yBala>=yEnemigo and yBala<=yEnemigo+63:
            # Colisi√≥n, desaparece bala y enemigo
            yEnemigo = -64
            spriteBala.rect.top = -44   # Fuera de la pantalla
            xEnemigo = -129
            DX = 0
            return True

    return False


def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render("Puntos: " + str(puntos), 1, ROJO)
    ventana.blit(texto, (20,50))


def generarEnemigos(listaEnemigos, imgEnemigo):
    for y in range(20, 150*3+1, 150):
        for x in range(133,600,133):
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = x
            spriteEnemigo.rect.top = y
            listaEnemigos.append(spriteEnemigo)


def dibujarListaEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:   # Visita cada sprite
        ventana.blit(enemigo.image, enemigo.rect)


def verificarColisionesListaEnemigos(listaBalas, listaEnemigos):
    for enemigo in listaEnemigos:
            for bala in listaBalas:
                if bala.rect.colliderect(enemigo) == True:  # Prueba colisi√≥n
                    listaEnemigos.remove(enemigo)
                    listaBalas.remove(bala)


def crearBala(imgBala, listaBalas, xNave, yNave):
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = xNave+64-16
    spriteBala.rect.top = yNave
    listaBalas.append(spriteBala)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.top -= 16
        if bala.rect.top < -32: #Sali√≥ de la pantalla
            listaBalas.remove(bala)


def dibujarListaBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujar√°
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecuci√≥n, iniciamos suponiendo que no

    #IMAGENES
    btnJugar = pygame.image.load("btnJugar.png")
    fondoJuego = pygame.image.load("fondoJuego.jpg")
    imgNave = pygame.image.load("nave.png")
    imgEnemigo = pygame.image.load("imgEnemigos.png")
    # Balas (sprites)
    imgBala = pygame.image.load("bala.png")
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = -1   # PARA que no se dibuje


    # COORDENADAS CIRCULO
    xMouse = -1
    yMouse = -1
    # COORDENADAS NAVE
    xNave = ANCHO//2        # izquierda
    yNave = ALTO - 64       # arriba

    # ESTADOS
    MENU = 1
    JUGANDO = 2
    estado = MENU   # Al inicio muestra el men√∫

    # AUDIO (SONIDO)
    pygame.mixer.init()
    # Sonido corto   Sound  --  wav
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    # Sonido largo   Music   -- mp3
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play()

    #TEXTO
    fuente = pygame.font.SysFont("Courier", 48)

    #Puntos
    puntos = 300      # NO ES GLOBAL

    # LISTA DE ENEMIGOS
    listaEnemigos = []
    generarEnemigos(listaEnemigos, imgEnemigo)

    # LISTA BALAS
    listaBalas = [] # Lista vac√≠a

    MOVIENDO = False
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite autom√°ticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el bot√≥n de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse>=300 and xMouse<=500 and yMouse>=275 and yMouse<=325:
                    xMouse = -1
                    # CAMBIA EL ESTADO
                    estado = JUGANDO    # PASA A JUGAR
            elif evento.type == pygame.KEYDOWN: # Tecla oprimida
                MOVIENDO = False
                if evento.key == pygame.K_RIGHT: # flecha derecha???
                    xNave += 100
                elif evento.key == pygame.K_LEFT:
                    xNave -= 100
                elif evento.key == pygame.K_SPACE:  # disparar????
                    if len(listaBalas) < 3:
                        crearBala(imgBala, listaBalas, xNave, yNave)
                    efectoDisparo.play()
                    spriteBala.rect.left = xNave+64-16  # Proyecto (getWidth...)
                    spriteBala.rect.top = yNave
            elif evento.type == pygame.KEYUP:   # SUELTAN la tecla
                MOVIENDO = False


        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aqu√≠ haces todos los trazos que requieras
        if estado == MENU:
            dibujarCirculo(ventana, xMouse, yMouse)
            dibujarMenu(ventana, btnJugar)
        elif estado == JUGANDO:
            # Verificar colisiones / Actualizar objetos
            resultado = verificarColisionBalaEnemigo(spriteBala)
            verificarColisionesListaEnemigos(listaBalas, listaEnemigos)
            if resultado == False:
                puntos -= 1
            elif resultado == True:
                puntos += 150

            moverBalas(listaBalas)
            dibujarFondo(ventana, fondoJuego)
            dibujarListaEnemigos(ventana, listaEnemigos)
            dibujarNave(ventana, imgNave, xNave, yNave, puntos)
            dibujarEnemigo(ventana, imgEnemigo)
            #dibujarBala(ventana, spriteBala)
            dibujarListaBalas(ventana, listaBalas)
            dibujarMarcador(ventana, fuente, puntos)

            if MOVIENDO == True:
                xNave += 5

        Enemigos = len(listaEnemigos)

        puntaje = puntos+1

        if puntos == -1:
            print("GameOver,", "Puntaje: ", puntaje)
            print(len(listaEnemigos))
            exit()
        elif Enemigos == 0:
            print("Ha terminado con todos los enemigos, el puntaje total es: ", puntos)
            exit()






        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta funci√≥n, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Despu√©s del ciclo principal
    pygame.quit()  # termina pygame


# Funci√≥n principal, aqu√≠ resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la funci√≥n principal
main()



