# Autor: Juan Carlos Flores García, A01376511. Grupo 4.

# Descripción: Videojuego ambientado en el espacio dónde el jugador maneja una nave y elimina enemigos disparando con la nave.


import pygame   # Librería de pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
AMARILLO = (255, 255, 0)    # solo amarillo
NEGRO = (0, 0, 0)

# Estados
MENU = 1
JUGANDO = 2
GANAR = 3
GAMEOVER = 4

# Estados de movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3
IZQUIERDA = 4
DERECHA = 5


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    # VISITAR a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 5


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 20


def dibujarMenu(ventana, imgBtnJugar, imgLogo):
    ventana.blit(imgBtnJugar, (ANCHO // 2 - 72.5, ALTO - 200))
    ventana.blit(imgLogo, (ANCHO // 2-280, ALTO // 4))


def verificarColision(listaEnemigos, listaBalas):
    for k in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        for e in range(len(listaEnemigos)-1, -1, -1):   # Recorrer con INDICES
            enemigo = listaEnemigos[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                # Le pegó
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                return True


def verificarColisionJugador(listaEnemigos, spritePersonaje):
    for enemigo in listaEnemigos:
        xp = spritePersonaje.rect.left
        yp = spritePersonaje.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xp >= xe and xp <= xe + ae and yp >= ye and yp <= ye + alte:
            listaEnemigos.remove(enemigo)
            return True


def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render("SCORE: " + str(puntos), 1, AMARILLO)
    ventana.blit(texto, (565, 15))


def dibujarMarcadorVida(ventana, fuente, vida):
    texto = fuente.render("HEALTH: " + str(vida), 1, AMARILLO)
    ventana.blit(texto, (35, 15))


def dibujarMensajeGanar(ventana, fuente, imgGanar):
    texto = fuente.render("YOU SCORED 5000!", 1, AMARILLO)
    ventana.blit(imgGanar, (ANCHO // 2 - 183, ALTO // 2 - 39))
    ventana.blit(texto, (ANCHO // 2 - 125, ALTO // 2 + 50))


def dibujarMensajePerder(ventana, fuente, imgPerder, vida):
    texto = fuente.render("YOU SCORED: " + str(vida), 1, ROJO)
    ventana.blit(imgPerder, (ANCHO // 2 - 242, ALTO // 2 - 39))
    ventana.blit(texto, (ANCHO // 2 - 125, ALTO // 2 + 50))


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Nave del jugador
    imgPersonaje = pygame.image.load("Enterprise.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO // 2 + spritePersonaje.rect.height // 2


    # Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("Klingon.png")
    for k in range(10):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo)

    # Proyectiles/balas
    listaBalas = []
    imgBala = pygame.image.load("Phaser-1.png")

    # Menu
    imgBtnJugar = pygame.image.load("button_start.png")
    imgLogo = pygame.image.load("Logo.png")

    # Pantalla de juego ganado
    imgGanar = pygame.image.load("YOU-WIN.png")

    # Pantalla de fin del juego
    imgPerder = pygame.image.load("GAME-OVER.png")

    # Puntos
    puntos = 0

    # Vida
    vida = 5000

    # Fondo
    imgFondo = pygame.image.load("Fondo.jpg")

    estado = MENU

    moviendo = QUIETO

    # Tiempo
    timer = 0  # Acumulador de tiempo

    # TEXTO
    fuente = pygame.font.SysFont("fixedsys", 35)

    # Audio
    pygame.mixer.init()
    pygame.mixer.music.load("STTOS.mp3")
    pygame.mixer.music.play(-1)
    efecto = pygame.mixer.Sound("shoot.wav")
    danoEnemigo = pygame.mixer.Sound("hitdamage.wav")
    danoPersonaje = pygame.mixer.Sound("damage.wav")


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    # spritePersonaje.rect.bottom -= 5
                    moviendo = ARRIBA

                elif evento.key == pygame.K_DOWN:
                    # spritePersonaje.rect.bottom += 5
                    moviendo = ABAJO

                elif evento.key == pygame.K_LEFT:
                    moviendo = IZQUIERDA

                elif evento.key == pygame.K_RIGHT:
                    moviendo = DERECHA

                elif evento.key == pygame.K_x:
                    # Crear una bala
                    efecto.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalas.append(spriteBala)
                    # ENEMIGO
                    spriteEnemigo = pygame.sprite.Sprite()
                    spriteEnemigo.image = imgEnemigo
                    spriteEnemigo.rect = imgEnemigo.get_rect()
                    spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
                    spriteEnemigo.rect.bottom = randint(0, ALTO)
                    listaEnemigos.append(spriteEnemigo)


            elif evento.type == pygame.KEYUP:
                moviendo = QUIETO

            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                # Preguntar si soltó el mouse dentro del botón
                xb = ANCHO//2-72.5
                yb = ALTO - 200
                if xm > xb and xm <= xb+145 and ym >= yb and ym <= yb+56:
                    pygame.mixer.music.stop()
                    estado = 2
                    pygame.mixer.init()
                    pygame.mixer.music.load("Beyond.mp3")
                    pygame.mixer.music.play(-1)




        # Borrar pantalla
        ventana.fill(NEGRO)


        if estado == JUGANDO:

            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 5
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 5
            elif moviendo == IZQUIERDA:
                spritePersonaje.rect.left -= 5
            elif moviendo == DERECHA:
                spritePersonaje.rect.right += 5

            # Tiempo
            if timer <= 2:
                timer = 0
                # Crear una bala
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                spriteBala.rect.bottom = spritePersonaje.rect.bottom
                listaBalas.append(spriteBala)
            # Actualizar enemigos
            moverEnemigos(listaEnemigos)
            moverBalas(listaBalas)
            resultado = verificarColision(listaEnemigos, listaBalas)
            if resultado == True:
                danoEnemigo.play()
                puntos += 250
            dano = verificarColisionJugador(listaEnemigos, spritePersonaje)
            if dano == True:
                danoPersonaje.play()
                vida -= 500
            # Dibujar, aquí haces todos los trazos que requieras
            # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
            # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
            ventana.blit(imgFondo, (0, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)
            dibujarMarcador(ventana, fuente, puntos)
            dibujarMarcadorVida(ventana, fuente, vida)
            if puntos == 5000:
                pygame.mixer.music.stop()
                estado = 3

            if vida == 0:
                pygame.mixer.music.stop()
                estado = 4

        elif estado == GANAR:
            dibujarMensajeGanar(ventana, fuente, imgGanar)


        elif estado == GAMEOVER:
            dibujarMensajePerder(ventana, fuente, imgPerder, puntos)


        elif estado == MENU:
            dibujarMenu(ventana, imgBtnJugar, imgLogo)

            # Texto en la pantalla
            # texto = fuente.render("Valor de xFondo %d" % xFondo, 1, BLANCO)
            # ventana.blit(texto, (ANCHO // 2 - 100, 50))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(60)  # 40 fps
        timer += 1/20
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamada a la función principal
main()

