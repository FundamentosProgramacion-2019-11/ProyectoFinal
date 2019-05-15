# encoding: UTF-8
# Autor: César Guzmán Guadarrama
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla
import math
import random
import pygame  # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

angulo = 70
velocidadEnemigo = 5


# Estructura básica de un programa que usa pygame para dibujar
def dibujarFondoMenu(ventana, imgFondoMenu):
    ventana.blit(imgFondoMenu, (0, 0))


def dibujarMenu(ventana, btnJugar, imgExit):
    ventana.blit(btnJugar, (600, 500))
    ventana.blit(imgExit, (650, 25))


def dibujarFondo(ventana, fondo):
    ventana.blit(fondo, (0, 0))


def dibujarNave(ventana, spriteNave):
    ventana.blit(spriteNave.image, (spriteNave.rect.left, spriteNave.rect.top))


def dibujarProyectilEnemigo(ventana, spriteBalaEnemigo, spriteEnemigo):
    if spriteBalaEnemigo.rect.left != -1:
        spriteBalaEnemigo.rect.top = spriteEnemigo.rect.top
        spriteBalaEnemigo.rect.left = spriteEnemigo.rect.left
        ventana.blit(spriteBalaEnemigo.image, spriteBalaEnemigo.rect)



def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render("Puntos: " + str(puntos), 1, ROJO)
    ventana.blit(texto, (0, 0))


def generarEnemigos(listaEnemigos, imgEnemigo):
    for y in range(random.randint(50, 150), 300, 100):
        for x in range(random.randint(0, 100), 801, 200):
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = x
            spriteEnemigo.rect.top = y
            listaEnemigos.append(spriteEnemigo)


def generarEnemigos2(listaEnemigos2, imgEnemigo2):
    for y in range(random.randint(1, 100), 100, 100):
        for x in range(random.randint(0, 100), 600, 100):
            spriteEnemigo2 = pygame.sprite.Sprite()
            spriteEnemigo2.image = imgEnemigo2
            spriteEnemigo2.rect = imgEnemigo2.get_rect()
            spriteEnemigo2.rect.left = x
            spriteEnemigo2.rect.top = y
            listaEnemigos2.append(spriteEnemigo2)


def dibujarListaEnemigos(ventana, listaEnemigos):
    global velocidadEnemigo
    contador = 0
    for enemigo in listaEnemigos:
        anchoEnemigo = pygame.Surface.get_width(enemigo.image)
        ventana.blit(enemigo.image, enemigo.rect)
        enemigo.rect.left += velocidadEnemigo
        if enemigo.rect.left + velocidadEnemigo + anchoEnemigo >= ANCHO or enemigo.rect.left + velocidadEnemigo <= 1:  # Este ciclo if determina el rango en que se mueve el enemigo
            contador += 1

        else:
            enemigo.rect.left += velocidadEnemigo


    if contador >= 1:
        velocidadEnemigo = -velocidadEnemigo


def dibujarListaEnemigos2(ventana, listaEnemigos2):
    global velocidadEnemigo, angulo
    for enemigo2 in listaEnemigos2:
        anchoEnemigo = pygame.Surface.get_width(enemigo2.image)
        ventana.blit(enemigo2.image, enemigo2.rect)
        enemigo2.rect.left += velocidadEnemigo
        if enemigo2.rect.left + anchoEnemigo + velocidadEnemigo >= ANCHO or enemigo2.rect.left + velocidadEnemigo <= 1:
            velocidadEnemigo = -velocidadEnemigo

    for enemigo in listaEnemigos2:
        dy = int(100 * math.cos(math.radians(angulo))) + 100
        enemigo.rect.top = dy
        angulo += 1


def verificarColisionesListaEnemgos(listaProyectiles, listaEnemigos):
    for enemigo in listaEnemigos:
        for proyectil in listaProyectiles:
            if proyectil.rect.colliderect(enemigo) == True:  # PRUEBA COLISIÓN DIRECTAMENTE ¡¡¡¡¡USAR !!!!!
                listaEnemigos.remove(enemigo)
                listaProyectiles.remove(proyectil)
                return True


def verificarColisionesProyectilesEnemigos(listaProyectilesEnemigos, listaProyectiles):
    for proyectilEnemigo in listaProyectilesEnemigos:
        for proyectil in listaProyectiles:
            if proyectil.rect.colliderect(proyectilEnemigo) == True:
                listaProyectilesEnemigos.remove(proyectilEnemigo)
                listaProyectiles.remove(proyectil)
                return True


def crearProyectil(imgProyectil, listaProyectiles, spriteNave):
    anchoNave = pygame.Surface.get_width(spriteNave.image)
    altoNave = pygame.Surface.get_height(spriteNave.image)
    spriteProyectil = pygame.sprite.Sprite()
    spriteProyectil.image = imgProyectil  # PONE LA IMAGEN DEL PROYECTIL
    spriteProyectil.rect = imgProyectil.get_rect()  # COORDENADAS DE LA BALA
    spriteProyectil.rect.left = spriteNave.rect.left + anchoNave / 3.5
    spriteProyectil.rect.top = spriteNave.rect.top
    listaProyectiles.append(spriteProyectil)


def moverProyectiles(listaProyectiles):
    for proyectil in listaProyectiles:
        proyectil.rect.top -= 40  # Velocidad de las balas
        if proyectil.rect.top < -30:
            listaProyectiles.remove(proyectil)


def dibujarListaProyectiles(ventana, listaProyectiles):
    for proyectil in listaProyectiles:
        ventana.blit(proyectil.image, proyectil.rect)


def generarProyectilesEnemigo(listaProyectilesEnemigos, imgBalaEnemigo):
    for y in range(-500, 50, 600):  # renglones(coordenada y)
        for x in range(10, 750, 100):  # Columnas (x)
            # Crear enemigo en (x,y)
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgBalaEnemigo
            spriteEnemigo.rect = imgBalaEnemigo.get_rect()
            spriteEnemigo.rect.left = random.randint(0, 633)
            spriteEnemigo.rect.top = y
            listaProyectilesEnemigos.append(spriteEnemigo)  # Lista de sprites


def dibujarListaProyectilesEnemigo(ventana, listaProyectilesEnemigos):
    for proyectil in listaProyectilesEnemigos:
        ventana.blit(proyectil.image, proyectil.rect)



def moverProyectilesEnemigo(listaProyectilesEnemigos):
    for proyectil in listaProyectilesEnemigos:
        proyectil.rect.top += 10


def dibujarFondo2(ventana, fondoJuego2):
    ventana.blit(fondoJuego2, (0, 0))


def verificarColisionesListaEnemigos2(listaProyectiles, listaEnemigos2):
    for enemigo2 in listaEnemigos2:
        for proyectil in listaProyectiles:
            if proyectil.rect.colliderect(enemigo2) == True:  # PRUEBA COLISIÓN DIRECTAMENTE ¡¡¡¡¡USAR !!!!!
                listaEnemigos2.remove(enemigo2)
                listaProyectiles.remove(proyectil)
                return True


def verificarColisionesListaEnemigosNivel(listaProyectiles, listaEnemigosNivel):
    for enemigo in listaEnemigosNivel:
        for proyectil in listaProyectiles:
            if proyectil.rect.colliderect(enemigo) == True:
                listaEnemigosNivel.remove(enemigo)
                listaProyectiles.remove(proyectil)
                return True


def generarProyectilesEnemigo2(listaProyectilesEnemigos2, imgBalaEnemigo):
    for y in range(-500, 50, 600):  # renglones(coordenada y)
        for x in range(10, 750, 100):  # Columnas (x)
            # Crear enemigo en (x,y)
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgBalaEnemigo
            spriteEnemigo.rect = imgBalaEnemigo.get_rect()
            spriteEnemigo.rect.left = random.randint(0, 633)
            spriteEnemigo.rect.top = y
            listaProyectilesEnemigos2.append(spriteEnemigo)  # Lista de sprites


def dibujarListaProyectilesEnemigo2(ventana, listaProyectilesEnemigos2):
    for proyectil in listaProyectilesEnemigos2:
        ventana.blit(proyectil.image, proyectil.rect)



def moverProyectilesEnemigo2(listaProyectilesEnemigos2):
    for proyectil in listaProyectilesEnemigos2:
        proyectil.rect.top += 10


def generarProyectiles2Enemigo2(lista2ProyectilesEnemigos2, imgBalaEnemigo2):
    for y in range(0, 50, 600):  # renglones(coordenada y)
        for x in range(10, 750, 250):  # Columnas (x)
            # Crear enemigo en (x,y)
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgBalaEnemigo2
            spriteEnemigo.rect = imgBalaEnemigo2.get_rect()
            spriteEnemigo.rect.left = x
            spriteEnemigo.rect.top = y
            lista2ProyectilesEnemigos2.append(spriteEnemigo)  # Lista de sprites


def dibujarLista2ProyectilesEnemigo2(ventana, lista2ProyectilesEnemigos2):
    for proyectil in lista2ProyectilesEnemigos2:
        ventana.blit(proyectil.image, proyectil.rect)


def moverProyectiles2Enemigo2(lista2ProyectilesEnemigos2):
    for proyectil in lista2ProyectilesEnemigos2:
        proyectil.rect.top += 10


def verificarColisionNave(listaProyectilesEnemigos, spriteNave):
    for proyectil in listaProyectilesEnemigos:
        if proyectil.rect.colliderect(spriteNave.rect) == True:
            return True


def txt(archivo, e):
    archivo.write("Duraste aproximadamente: ")
    f = e / 40
    archivo.write(str(f))
    archivo.write(" segundos")

    archivo.close()


def dibujarInformacion(ventana, imgInstrucciones):
    ventana.blit(imgInstrucciones, (400, 100))


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
    fondoJuego = pygame.image.load("fondoNivel1.png")
    fondoJuego2 = pygame.image.load("fondoNivel3.png")
    imgNave = pygame.image.load("Spaceship-PNG-File2.png")
    imgEnemigo = pygame.image.load("Enemigo.png")
    imgEnemigo2 = pygame.image.load("Enemigo2.png")
    imgProyectil = pygame.image.load("proyectil.png")
    imgBalaEnemigo = pygame.image.load("proyectilEnemigo.png")
    imgExit = pygame.image.load("exit.png")
    imgFondoMenu = pygame.image.load("fondoMenu.png")
    imgBalaEnemigo2 = pygame.image.load("proyectilEnemigo2.png")
    imgFondoPerder = pygame.image.load("perderFondo.png")
    imgPerder = pygame.image.load("lose.png")
    imgGanar = pygame.image.load("ganar.png")
    imgInstrucciones = pygame.image.load("informacion.png")
    imgMover = pygame.image.load("flechas.png")
    imgBack =pygame.image.load("back.png")

    # SPRITE NAVE
    anchoNave = pygame.Surface.get_width(imgNave)
    altoNave = pygame.Surface.get_height(imgNave)
    velocidadNave = 10
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = imgNave
    spriteNave.rect = imgNave.get_rect()
    spriteNave.rect.left = ANCHO // 2
    spriteNave.rect.top = ALTO - altoNave

    # SPRITE ENEMIGOS

    spriteEnemigo = pygame.sprite.Sprite()
    spriteEnemigo.image = imgEnemigo
    spriteEnemigo.rect = imgEnemigo.get_rect()
    spriteEnemigo.rect.left = ANCHO // 2
    spriteEnemigo.rect.top = 0

    # SPRITE ENEMIGOS 2
    spriteEnemigo2 = pygame.sprite.Sprite()
    spriteEnemigo2.image = imgEnemigo2
    spriteEnemigo2.rect = imgEnemigo2.get_rect()
    spriteEnemigo2.rect.left = ANCHO // 2
    spriteEnemigo2.rect.top = 0


    # SONIDOS
    # Sonido corto
    pygame.mixer.init()
    sonidoDisparo = pygame.mixer.Sound("Tone Shoot Iron Man-[AudioTrimmer.com].ogg")
    # Sonido Largo
    pygame.mixer.music.load("ringtones-the-avengers.mp3")
    pygame.mixer.music.play(-1)

    # TEXTO
    fuente = pygame.font.SysFont("arial", 20, bold=True)

    # puntos
    puntos = 50  # No es GLOBAL

    # LISTA ENEMIGOS1
    listaEnemigos = []
    generarEnemigos(listaEnemigos, spriteEnemigo.image)

    #LISTA ENEMIGOS1 NIVEL 2
    listaEnemigosNivel = []
    generarEnemigos(listaEnemigosNivel, spriteEnemigo.image)


    # LISTA ENEMIGOS2
    listaEnemigos2 = []
    generarEnemigos2(listaEnemigos2, spriteEnemigo2.image)

    # LISTA BALAS
    listaProyectiles = []  # LISTA VACÍA

    # LISTA BALAS ENEMIGOS
    listaProyectilesEnemigos = []
    listaProyectilesEnemigos2 = []
    lista2ProyectilesEnemigos2 = []

    # ESTADOS DE JUEGO
    MENU = 1
    JUGANDO = 2
    INSTRUCIONES = 5
    PERDER = 3
    GANAR = 4
    estado = MENU  # Al inicio muestra el menú.

    c = 0
    d = 0
    e = 0

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= 400 and xMouse <= ANCHO and yMouse >= 500 and yMouse <= ALTO:
                    xMouse = -1
                    # Cambio de Estado
                    estado = JUGANDO  # Pasa a jugar

                elif xMouse >= 600 and xMouse <= ANCHO and yMouse >= 0 and yMouse <= 100:
                    termina = True

                elif xMouse >=507 and xMouse <= 704 and yMouse >= 155 and yMouse <= 160:
                    estado = JUGANDO

                elif xMouse >= 507 and xMouse <= 704 and yMouse >= 177 and yMouse <= 200:
                    estado = MENU

                elif xMouse >= 400 and xMouse <= 500 and yMouse >= 100 and yMouse <= 200:
                    estado = INSTRUCIONES

                elif xMouse >= 0 and xMouse <= 200 and yMouse >= 410 and yMouse <= ALTO:
                    estado = MENU


        keys = pygame.key.get_pressed()
        if evento.type == pygame.KEYDOWN:  # TECLA OPRIMIDA

            if evento.key == pygame.K_SPACE:  # DISPARAR
                if len(listaProyectiles) < 1:
                    crearProyectil(imgProyectil, listaProyectiles, spriteNave)

                    sonidoDisparo.play()


            elif keys[pygame.K_RIGHT] and spriteNave.rect.left < ANCHO - anchoNave:
                spriteNave.rect.left += velocidadNave
            elif keys[pygame.K_LEFT] and spriteNave.rect.left >= 1:
                spriteNave.rect.left -= velocidadNave

        # Borrar pantalla.
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw.

        if estado == MENU:
            dibujarFondoMenu(ventana, imgFondoMenu)
            dibujarMenu(ventana, btnJugar, imgExit)
            dibujarInformacion(ventana, imgInstrucciones)




        elif estado == JUGANDO:

            # Verificar colisiones / Actualizar objetos
            resultado2 = verificarColisionesListaEnemgos(listaProyectiles, listaEnemigos)
            if resultado2 == True:
                puntos += 10

            choque = verificarColisionesProyectilesEnemigos(listaProyectilesEnemigos, listaProyectiles)
            if choque == True:
                puntos += 5
            perder = verificarColisionNave(listaProyectilesEnemigos, spriteNave)
            if perder == True:
                puntos -= 1
                if puntos <= 0:
                    estado = PERDER
            moverProyectiles(listaProyectiles)
            moverProyectilesEnemigo(listaProyectilesEnemigos)
            dibujarFondo(ventana, fondoJuego)
            dibujarListaEnemigos(ventana, listaEnemigos)
            dibujarNave(ventana, spriteNave)
            e += 1
            c += 1
            if c == 80:

                generarProyectilesEnemigo(listaProyectilesEnemigos, imgBalaEnemigo)

                if len(listaProyectilesEnemigos) < 10:
                    generarProyectilesEnemigo(listaProyectilesEnemigos, imgBalaEnemigo)

                c = 0

            dibujarListaProyectilesEnemigo(ventana, listaProyectilesEnemigos)
            dibujarListaProyectiles(ventana, listaProyectiles)

            dibujarMarcador(ventana, fuente, puntos)
            if puntos >= 100:  # PASAS AL NIVEL 2
                resultado3 = verificarColisionesListaEnemigos2(listaProyectiles, listaEnemigos2)
                resultado4 = verificarColisionesListaEnemigosNivel(listaProyectiles, listaEnemigosNivel)
                if resultado3 == True or resultado4 == True:
                    puntos += 10
                verificarColisionesProyectilesEnemigos(listaProyectilesEnemigos2, listaProyectiles)
                verificarColisionesProyectilesEnemigos(lista2ProyectilesEnemigos2, listaProyectiles)
                dibujarFondo2(ventana, fondoJuego2)
                dibujarNave(ventana, spriteNave)
                moverProyectiles(listaProyectiles)
                moverProyectilesEnemigo2(listaProyectilesEnemigos2)
                moverProyectiles2Enemigo2(lista2ProyectilesEnemigos2)
                dibujarListaProyectiles(ventana, listaProyectiles)
                dibujarListaEnemigos2(ventana, listaEnemigos2)
                dibujarLista2ProyectilesEnemigo2(ventana, lista2ProyectilesEnemigos2)
                dibujarMarcador(ventana, fuente, puntos)
                dibujarListaEnemigos(ventana, listaEnemigosNivel)
                d += 1
                e += 1
                if d == 40:

                    generarProyectilesEnemigo2(listaProyectilesEnemigos2, imgBalaEnemigo)
                    generarProyectiles2Enemigo2(lista2ProyectilesEnemigos2, imgBalaEnemigo2)

                    if len(listaProyectilesEnemigos) < 5:
                        generarProyectilesEnemigo2(listaProyectilesEnemigos2, imgBalaEnemigo)
                        generarProyectiles2Enemigo2(lista2ProyectilesEnemigos2, imgBalaEnemigo2)

                    d = 0

                dibujarListaProyectilesEnemigo2(ventana, listaProyectilesEnemigos2)
                dibujarListaProyectiles(ventana, listaProyectiles)
                if puntos >= 500:
                    estado = GANAR

        elif estado == PERDER:
            ventana.blit(imgFondoPerder, (0, 0))
            ventana.blit(imgPerder, (400, 0))
            archivo = open("Marcador.txt", "w", encoding="UTF-8")
            txt(archivo, e)

            archivo.close()

        elif estado == GANAR:
            ventana.blit(imgGanar, (0, 0))

        elif estado == INSTRUCIONES:
            ventana.blit(fondoJuego2, (0, 0))
            ventana.blit(imgMover, (0, 50))
            texto = fuente.render("MOVER", 1, VERDE_BANDERA)
            ventana.blit(texto, (40, 125))
            ventana.blit(imgEnemigo, (175, 50))
            texto2 = fuente.render("10 PUNTOS", 1, BLANCO)
            ventana.blit(texto2, (150, 125))
            ventana.blit(imgEnemigo2, (325, 50))
            texto3 = fuente.render("20 PUNTOS", 1, ROJO)
            ventana.blit(texto3, (300, 125))
            ventana.blit(imgBalaEnemigo, (450, 50))
            ventana.blit(imgBalaEnemigo2, (550, 10))
            texto4 = fuente.render("Proyectiles Enemigos", 1, AZUL)
            ventana.blit(texto4, (425, 125))
            ventana.blit(imgProyectil, (690, 50))
            texto5 = fuente.render("Proyectil", 1, ROJO)
            ventana.blit(texto5, (675, 125))
            ventana.blit(imgBack, (0, 410))



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja


# Llamas a la función principal
main()
