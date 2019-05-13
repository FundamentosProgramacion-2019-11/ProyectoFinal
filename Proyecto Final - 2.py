
#Cecilia Daniela Olivares Hernández, a01745727 Grupo 3. LAD
import random
import pygame

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# Temporalmente las coordenadas de la CANASTA(x,y)
xCanasta = 0
yCanasta = 690

# Temporalmente las coordenadas de la MANZANA(x,y)
xManzana = ANCHO // 2
yManzana = -75
DX = +5  # velocidadDERECHA (-1) IZQ
angulo = 0  # angulko en grados

#FUNCIONES
# Dibuja la pantalla del MENU PRINCIPAL
def dibujarMenu(ventana, botonJugar, botonInstrucciones, botonPuntuaciones):
    ventana.blit(botonJugar, (230, 230))
    ventana.blit(botonInstrucciones, (205, 320))
    ventana.blit(botonPuntuaciones, (205, 400))

# dibuja el MOUSE
def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 50)


# Dibuja la pantalla de las INSTRUCCIONES
def dibujarInstrucciones(ventana, fondoInstrucciones, botonMenu):
    ventana.blit(fondoInstrucciones, (0, 0))
    ventana.blit(botonMenu, (420, 660))


# Dibuja la pantalla de los PUNTAJE
def dibujarTablaPuntaje(ventana, fondoPuntaje, botonMenu):
    ventana.blit(fondoPuntaje, (0, 0))
    ventana.blit(botonMenu, (420, 660))

# Dibuja la pantalla de JUEGO
def dibujarJuego(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0, 0))

# Dibuja la CANASTA
def dibujarCanasta(ventana, canasta):
    ventana.blit(canasta, (xCanasta, yCanasta))

# Dibuja las MANZANAS
def dibujarManzanas(ventana, manzana):
    global xManzana, DX, yManzana, angulo
    ventana.blit(manzana, (xManzana, yManzana))
    xManzana += DX
    # CHOQUE DRCH
    if xManzana >= ANCHO - 70 or xManzana <= 0:  # ancho menos ancho manzanas
        DX = -DX

# Dibuja la CAIDA de MANZANAS
def dibujarCaida(ventana, spriteCaida):
    if spriteCaida.rect.left != -1:
        ventana.blit(spriteCaida.image, spriteCaida.rect)
        spriteCaida.rect.top += 10
        if spriteCaida.rect.top < -75:
            spriteCaida.rect.left = -1

# Regresa TRUE si HAY COLISIÓN, FALSE en otro caso
def probarColision(spriteCaida):
    global xCanasta
    xManzana = spriteCaida.rect.left
    yManzana = spriteCaida.rect.top
    if xManzana >= xCanasta and xManzana <= xCanasta + 100 and yManzana >= yCanasta and yManzana <= yCanasta:# medidas CANASTA
        return True
    if (xManzana <= xCanasta or xManzana >= xCanasta + 100)  and yManzana >= yCanasta and yManzana <= yCanasta:
        return False #no hay colision

#dibuja el PUNTAJE
def dibujarPuntaje(ventana, puntaje, fuente):
    texto = fuente.render("Puntaje: " + str(puntaje), 1, NEGRO)
    ventana.blit(texto, (30, 15))

#dibuja las VIDAS
def dibujarVidas(ventana, vidas, fuente):
    texto = fuente.render("Vidas: 0" + str(vidas), 1, NEGRO)
    ventana.blit(texto, (300, 15))

#dibuja el PUNTAJE FINAL
def dibujarPuntajeFinal(ventana, puntaje, fuenteTotal):
    texto = fuenteTotal.render("Score: " + str(puntaje), 1, NEGRO)
    ventana.blit(texto, (200, 400))

#Lista de ENEMIGOS
listaEnemigos = [] #Lista vacia

#LISTA DE ENEMIGOS
#dibuja la lista de los enemigos
def dibujarListaEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
#mueve los enemigos de la lista
def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.top += 15
#prueba la Colisión de los enemigos
def colisionarEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        global xCanasta
        xEnemigo = enemigo.rect.left
        yEnemigo = enemigo.rect.top
        if xEnemigo >= xCanasta and xEnemigo <= xCanasta + 100 and yEnemigo >= yCanasta and yEnemigo <= yCanasta:
            listaEnemigos.remove(enemigo)
            return True

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Hay que anunciar que hay variables globales
    global xCanasta, yCanasta  # Voy a usar la variable global
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES PARA VENTANA MENU
    fondoMenu = pygame.image.load("fondoMenu.jpg")
    botonJugar = pygame.image.load("bjugar.png")
    botonInstrucciones = pygame.image.load("binstrucciones.png")
    botonPuntuaciones = pygame.image.load("bpuntuaciones.png")

    # IMAGENES PARA VENTANA INSTRUCCIONES
    fondoInstrucciones = pygame.image.load("fondoInstrucciónes3.jpg")
    botonMenu = pygame.image.load("bmenu.png")

    # IMAGENES PARA VENTANA PUNTAJE
    fondoPuntaje = pygame.image.load("FondoPuntaje.jpg")

    # IMAGENES PARA VENTANA JUEGO
    fondoJuego = pygame.image.load("fondoJuego.jpg")
    canasta = pygame.image.load("canasta.png")
    imgManzana = pygame.image.load("manzana.png")
    manzana = pygame.image.load("manzana.png")
    imgEnemigo = pygame.image.load("enemigo.png")
    enemigo = pygame.image.load("enemigo.png")

    # SPRITES
    spriteManzana = pygame.sprite.Sprite()
    spriteManzana.image = imgManzana
    spriteManzana.rect = imgManzana.get_rect()  # Datos de la imagen
    spriteManzana.rect.top = -1  # X
    spriteManzana.rect.left = -1  # Y
    # Caida Manzanas
    spriteCaida = pygame.sprite.Sprite
    spriteCaida.image = imgManzana
    spriteCaida.rect = imgManzana.get_rect()
    spriteCaida.rect.left = -1
    spriteCaida.rect.top = -1


    # AUDIO
    pygame.mixer.init()
    efectoColision = pygame.mixer.Sound("sColisión.wav")
    pygame.mixer.music.load("musicaFondoM.mp3")
    pygame.mixer.music.play(-1)

    # MOUSE
    xMouse = -1
    yMouse = -1

    # Estados
    MENU = 1
    JUGANDO = 2
    INSTRUCCIONES = 3
    PUNTAJE = 4
    estado = MENU

    # TEXTO
    fuente = pygame.font.SysFont("Arial", 30)
    puntaje = 0
    vidas = 8
    fuenteTotal = pygame.font.SysFont("Arial", 60) #Texto de la puntuación final

    # TIEMPOS
    tiempoCaida = 23  # cada cuanto caen las manzanas

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Oprimio el mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if xMouse >= 230 and xMouse <= 360 and yMouse >= 230 and yMouse <= 300:
                    # Oprimió el botón de play
                    xMouse = -1
                    estado = JUGANDO
                if xMouse >= 200 and xMouse <= 385 and yMouse >= 320 and yMouse <= 375:
                    # Oprimió el botón de instrucciones
                    xMouse = -1
                    estado = INSTRUCCIONES
                if xMouse >= 205 and xMouse <= 415 and yMouse >= 400 and yMouse <= 455:
                    # Oprimió el botón de puntaje
                    xMouse = -1
                    estado = PUNTAJE
                if xMouse >= 420 and xMouse <= 520 and yMouse >= 660 and yMouse <= 715:
                    # Oprimió el botón de menu
                    xMouse = -1
                    estado = MENU
            elif evento.type == pygame.KEYDOWN:  # Oprimió la tecla
                # verificar que tecla se oprimió
                if evento.key == pygame.K_RIGHT:
                    xCanasta += 40
                elif evento.key == pygame.K_LEFT:
                    xCanasta -= 40



        # Borrar pantalla
        ventana.blit(fondoMenu, (0, 0))

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == MENU:
            yManzana = 0
            xCanasta = 0
            vidas = 8
            puntaje = 0
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, botonJugar, botonInstrucciones, botonPuntuaciones)
        elif estado == INSTRUCCIONES:
            dibujarInstrucciones(ventana, fondoInstrucciones, botonMenu)
        elif estado == PUNTAJE:
            dibujarTablaPuntaje(ventana, fondoPuntaje, botonMenu)
            dibujarPuntajeFinal(ventana, puntajeT, fuenteTotal)
        elif estado == JUGANDO:
            dibujarJuego(ventana, fondoJuego)
            dibujarCanasta(ventana, canasta)
            dibujarVidas(ventana, vidas, fuente)
            dibujarPuntaje(ventana, puntaje, fuente)
            # marcador +=  1 va aumentado por el segundo
            # reaparecer manzana if manzana==0:
            # manzana =0 regresa a posición inicial

            #Dibuja la LISTA de enemigos
            dibujarListaEnemigos(ventana, listaEnemigos)
            moverEnemigos(listaEnemigos)

            #Dibuja la caida de las manzanas originales
            dibujarCaida(ventana, spriteCaida)
            dibujarManzanas(ventana, manzana)

            #Sprites del ENEMIGO
            tiempoCaida -= 1  # va restando al timepo inicial del ataque
            if tiempoCaida == 0:
                #crea una nueva manzana
                nuevoEnemigo = pygame.sprite.Sprite()
                nuevoEnemigo.image = imgEnemigo
                nuevoEnemigo.rect = imgEnemigo.get_rect()
                nuevoEnemigo.rect.left = random.randint(0, 540)
                nuevoEnemigo.rect.top = 0
                listaEnemigos.append(nuevoEnemigo)

                #Las manzanas originales aparecen random
                spriteCaida.rect.left = xManzana  # aparece randomly [random.randint(0,ANCHO)]
                spriteCaida.rect.top = yManzana  # 0 aparece de lo alto de ventana
                tiempoCaida = 85 #Tiempo de duración de la caida de las manzanas

            #Prueba si hay colisión de las MANZANAS BUENAS
            hayColison = probarColision(spriteCaida)  # regresa el true
            if hayColison == True:
                efectoColision.play()
                tiempoCaida = 1
                puntaje += 10
            puntajeT = puntaje

            # Prueba si hay colisión de las MANZANAS MORDIDAS
            hayColisionEnemigo = colisionarEnemigos(listaEnemigos)
            if hayColisionEnemigo == True:
                efectoColision.play()
                if puntaje > 0:
                    puntaje -= 5

            #Si NO hay colisión, RESTA VIDAS
            if hayColison == False:
                vidas -= 1
            if vidas <= 0:
                xCanasta = -200
                estado == PUNTAJE

                #CREACIÓN DE ARCHIVO
                """listaP = []
                listaP.append(str(puntajeT))

                ent = open("Puntos.txt", "a", encoding="UTF-8")
                puntos = listaP[0]
                ent.write((puntos))
                ent.close()"""


                dibujarTablaPuntaje(ventana, fondoPuntaje, botonMenu)
                dibujarPuntajeFinal(ventana, puntajeT, fuenteTotal)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps


    # Después del ciclo principal
    pygame.quit()  # termina pygame



# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja



# Llamas a la función principal
main()