import pygame
import random

puntos = 0
restantes = 0
restantes2 = 0

# Colores

BLANCO = (255, 255, 255)
VERDE = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
NARANJA = (238, 154, 0)
Turquesa = (0, 133, 104)

# Dimensiones de la pantalla

Ancho = 800
Alto = 600

# Estados de Juego
Menu = 1
Jugar = 2
Puntuaje = 3

# Estados de movimiento
Quieto = 1
Derecha = 2
Izquierda = 3
Findejuego = 4
Ganaste = 5


def dibujarPersonaje(ventana, spriteNave):
    ventana.blit(spriteNave.image, spriteNave.rect)


def dibujarEnemigo(ventana, listaEnemigos):
    for Enemigo in listaEnemigos:
        ventana.blit(Enemigo.image, Enemigo.rect)


def actualizarEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.bottom += 1

        if enemigo.rect.bottom <= 1000:
            pass
        else:
            break
        xe, ye, anchoe, altoe = enemigo.rect
        if ye + altoe <= 0:
            return True



def dibujarAmmo(ventana, listaAmmo):
    for Ammo in listaAmmo:
        ventana.blit(Ammo.image, Ammo.rect)

def actualizarAmmo(listaAmmo):
    for Ammo in listaAmmo:
        Ammo.rect.bottom -= 15

def verificarColisiones(listaAmmo, listaEnemigos):
    global restantes
    global restantes2
    global puntos
    SUN = False
    for k in range(len(listaAmmo) - 1, -1, -1):
        bala = listaAmmo[k]
        for e in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[e]
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, anchoe, altoe = enemigo.rect
            if xe <= xb <= xe + anchoe and ye >= yb >= ye - altoe:
                listaEnemigos.remove(enemigo)
                puntos += 10
                restantes -= 1
                restantes2 = 0
                SUN = True
                break
        if SUN:
            listaAmmo.remove(bala)
            return True


def Puntuacion():
    puntuaje = open("Puntuacion.txt", "r+")
    lista = []
    listas = puntuaje.readlines()
    for linea in listas:
        lista.append(int(linea.replace("\n", " ")))
    puntuaje.close()
    return lista


def losmejores():
    mejores = Puntuacion()
    mejores.append(puntos)
    mejores.sort(reverse=True)

    salida = open("Los_mejores_5.txt", "w")
    for puesto in range(0, 6):
        salida.write(str(mejores[puesto]) + "\n")
    salida.close()


def dibujar():
    global restantes
    global restantes2
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje Principal
    imgNave = pygame.image.load("Endurance1.gif")
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = imgNave
    spriteNave.rect = imgNave.get_rect()
    spriteNave.rect.left = Ancho // 2 - spriteNave.rect.width // 2
    spriteNave.rect.bottom = Alto - spriteNave.rect.height + 40

    movimiento = Quieto

    # Enemigos

    listaEnemigos = []
    imgEnemigo = pygame.image.load("meteoritoP.gif")
    for k in range(10):
        spriteEnemy = pygame.sprite.Sprite()
        spriteEnemy.image = imgEnemigo
        spriteEnemy.rect = imgEnemigo.get_rect()
        spriteEnemy.rect.left = random.randrange(0, Ancho - spriteEnemy.rect.width - 1)
        spriteEnemy.rect.bottom = 0 - spriteEnemy.rect.height - 1
        listaEnemigos.append(spriteEnemy)

    restantes = len(listaEnemigos)

    # Munición
    imgAmmo = pygame.image.load("Sun.png")
    listaAmmo = []

    # Estado del juego
    estado = Menu

    #traducciones
    imgBtJugar = pygame.image.load("buttonPresstostar.gif")
    imgBtPuntuaje = pygame.image.load("buttoncredits.gif")
    imgBtPosicion = pygame.image.load("button_posicion.png")
    imgBtPuntos = pygame.image.load("button_puntos.png")
    imgFondo = pygame.image.load("gargantua.gif")
    yFondo = 0

    # Fuentes
    Fuente = pygame.font.SysFont("Jokerman", 30)

    # Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("MusicaFondo.wav")
    pygame.mixer.music.play()

    # Tiempo
    timer = 0

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    movimiento = Derecha
                if evento.key == pygame.K_LEFT:
                    movimiento = Izquierda
                if evento.key == pygame.K_SPACE:
                    efecto.play()
                    spriteAmmo = pygame.sprite.Sprite()
                    spriteAmmo.image = imgAmmo
                    spriteAmmo.rect = imgAmmo.get_rect()
                    spriteAmmo.rect.left = spriteNave.rect.left + 20
                    spriteAmmo.rect.bottom = spriteNave.rect.top
                    listaAmmo.append(spriteAmmo)

            if evento.type == pygame.KEYUP:
                movimiento = Quieto

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xm2, ym2 = pygame.mouse.get_pos()
                xm3, ym3 = pygame.mouse.get_pos()
                xb3 = 600
                yb3 = Alto // 2 - 40
                xb2 = Ancho // 2 - 80
                yb2 = Alto // 2 + 40
                xb = Ancho // 2 - 80
                yb = Alto // 2 - 40
                anchoB = 160
                altoB = 80
                anchoC = 200
                altoC = 160
                altoD = 80
                anchoD = 160

                if xb <= xm <= xb + anchoB and yb <= ym <= yb + altoB:
                    estado = Jugar
                if xb2 <= xm2 <= xb2 + anchoC and yb2 <= ym2 <= yb2 + altoC:
                    estado = Puntuaje
                if xb3 <= xm3 <= xb3 + anchoD and yb3 <= ym3 <= yb3 + altoD:
                    estado = Jugar

        # Pregunta en que estado está el juego

        if estado == Menu:
            ventana.fill(NEGRO)
            texto4 = Fuente.render("Gargantua's Battle", 0, BLANCO)
            ventana.blit(texto4, (Ancho // 2 - 80, Alto - 450))
            ventana.blit(imgBtJugar, (Ancho // 2 - 160, Alto // 2 - 40))
            ventana.blit(imgBtPuntuaje, (Ancho // 2 - 160, Alto // 2 + 40))

        elif estado == Puntuaje:
            ventana.fill(NEGRO)
            ventana.blit(imgBtPosicion, (0, 0))
            ventana.blit(imgBtPuntos, (200, 0))
            ventana.blit(imgBtJugar, (400, Alto // 2 - 40))

        elif estado == Jugar:

            # Actualizar objetos

            actualizarAmmo(listaAmmo)
            actualizarEnemigos(listaEnemigos)
            verificarColisiones(listaAmmo, listaEnemigos)

            # Movimiento

            if movimiento == Derecha and spriteNave.rect.left < 750:
                spriteNave.rect.left += 5
            elif movimiento == Izquierda and spriteNave.rect.left > 0:
                spriteNave.rect.left -= 5

            # Borrar pantalla

            ventana.fill(NEGRO)
            ventana.blit(imgFondo, (-100, yFondo))
            ventana.blit(imgFondo, (-100, yFondo - 1080))

            # Dibujar, aqui haces todos los trazos que haremos

            dibujarPersonaje(ventana, spriteNave)
            dibujarAmmo(ventana, listaAmmo)
            dibujarEnemigo(ventana, listaEnemigos)

            # Mostrar texto

            texto2 = Fuente.render("Puntuación: %.2f" % puntos, 0, BLANCO)
            ventana.blit(texto2, (Alto - 600, Ancho - 700))

            if restantes == 0:
                estado = Ganaste

            if restantes == 1:
                estado = Findejuego

        if estado == Ganaste:
            texto4 = Fuente.render("Ganaste", 0, BLANCO)
            ventana.blit(texto4, (Alto // 2, Ancho // 2))
        else:
            if estado == Findejuego:
                texto3 = Fuente.render("Game Over", 0, BLANCO)
                ventana.blit(texto3, (Ancho // 2, Alto // 2))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        timer += 1 / 30
        reloj.tick(120)  # 120 fps

        # Después del ciclo principal

    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
