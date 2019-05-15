# encoding: UTF-8
# Autor: César Guzmán Guadarrama
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla
import math

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#VARIABLES GLOBALES
xEnemigo = ANCHO // 2
yEnemigo = 0
DX = +5  #derecha  -  Izquierda
angulo = 0



# Estructura básica de un programa que usa pygame para dibujar
def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar, (300, 275))


def dibujarCirculo(ventana, x, y):
    if x != -1:
        pygame.draw.circle(ventana, BLANCO, (x, y), 30)


def dibujarFondo(ventana, fondo):
    ventana.blit(fondo, (0, 0))


def dibujarNave(ventana, imgNave, xNave, yNave):
    ventana.blit(imgNave, (xNave, yNave))


def dibujarEnemigo(ventana, imgEnemigo):
    global xEnemigo, DX, yEnemigo, angulo
    ventana.blit(imgEnemigo, (xEnemigo, yEnemigo))
    #ACTUALIZAR COORDENADAS DEL ENEMIGO
    xEnemigo += DX
    if xEnemigo + 65 >= ANCHO or xEnemigo <= 1:
        DX = -DX

    #Movimiento Vertical
    dy = int(100 * math.sin(math.radians(angulo))) + 100
    yEnemigo = dy
    angulo += 10


def dibujarProyectil(ventana, spriteProyectil):
    if spriteProyectil.rect.left != -1:
        ventana.blit(spriteProyectil.image, spriteProyectil.rect)
        #ACTUALIZAR BALA
        spriteProyectil.rect.top -= 40
        if spriteProyectil.rect.top <= -50:
            spriteProyectil.rect.left = -1 #NO SE DIBUJA


def verificarColisionBalaEnemigo(spriteProyectil):    #, spriteEnemigo
    global yEnemigo, xEnemigo, DX
    xProyectil = spriteProyectil.rect.left
    yProyectil = spriteProyectil.rect.top
    # xEnemgo = sprite.rect.left
    if xProyectil >= xEnemigo and xProyectil <= xEnemigo + 63:
        if yProyectil >= yEnemigo and yProyectil <= yEnemigo + 63:
            #Colision, desaparece bala y enemigo
            yEnemigo = -7000     #Esto es para sacarlo de la panalla
            spriteProyectil.rect.top = -10000
            xEnemigo = -3000
            DX = 0
            return True
    return False


def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render("Puntos: " + str(puntos), 1, ROJO)
    ventana.blit(texto, (0, 0))


def dibujar():
    # Inicializa el motor de pygame
    global evento
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Imagenes.
    btnJugar = pygame.image.load("rosh_boton_jugar.png")
    fondoJuego = pygame.image.load("thumb-1920-5514732.png")
    imgNave = pygame.image.load("Spaceship-PNG-File2.png")
    imgEnemigo = pygame.image.load("Enemigo.png")
    # PROYECTIL (sprites)
    imgProyectil = pygame.image.load("proyectil.png")
    #SONIDOS
    #Sonido corto
    pygame.mixer.init()
    sonidoDisparo = pygame.mixer.Sound("shoot.wav")
    #Sonido Largo
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)


    #TEXTO
    fuente = pygame.font.SysFont("arial", 60, bold=True)


    #puntos
    puntos = 0   #No es GLOBAL

    #Sprite proyectil
    spriteProyectil = pygame.sprite.Sprite()
    spriteProyectil.image = imgProyectil  # PONE LA IMAGEN DEL PROYECTIL
    spriteProyectil.rect = imgProyectil.get_rect()  # COORDENADAS DE LA BALA
    spriteProyectil.rect.left = -1 #PARA QUE NO SE DIBUJE


    # Coordenadas Circulo.
    xMouse = -1
    yMouse = -1

    # COORDENADAS NAVE
    xNave = ANCHO // 2  # IZQUIERDA
    yNave = ALTO - 128  # ARRIBA

    # ESTADOS DE JUEGO
    MENU = 1
    JUGANDO = 2
    estado = MENU  # Al inicio muestra el menú.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 300 and xMouse <= 500 and yMouse >= 275 and yMouse <=325:
                    print("DETECTO BOTON")
                    xMouse = -1
                    #Cambio de Estado
                    estado = JUGANDO    # Pasa a jugar

        keys = pygame.key.get_pressed()
        if evento.type == pygame.KEYDOWN:    #TECLA OPRIMIDA

            if evento.key == pygame.K_SPACE:   #DISPARAR
                sonidoDisparo.play()
                spriteProyectil.rect.left = xNave + 33  #pygsme.getwhith INVESTIGAR
                spriteProyectil.rect.top = yNave
            elif keys[pygame.K_RIGHT] and xNave < ANCHO-128:
                xNave += 10
            elif keys[pygame.K_LEFT] and xNave >= 1:
                xNave -= 10



        # Borrar pantalla.
        ventana.fill(NEGRO)



        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw.

        if estado == MENU:
            dibujarMenu(ventana, btnJugar)
            dibujarCirculo(ventana, xMouse, yMouse)

        elif estado == JUGANDO:
            # Verificar colisiones / Actualizar objetos
            resultado = verificarColisionBalaEnemigo(spriteProyectil)
            if resultado == True:
                puntos += 1
            dibujarFondo(ventana, fondoJuego)
            dibujarNave(ventana, imgNave, xNave, yNave)
            dibujarEnemigo(ventana, imgEnemigo)
            dibujarProyectil(ventana, spriteProyectil)
            dibujarMarcador(ventana, fuente, puntos)




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()