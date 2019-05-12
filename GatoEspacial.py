#Autor: Elizabeth citlalli Zapata Cortes, A01746002
#Descripción: La temática del juego esta basada  en una batalla intergaláctica entre gatos y robots.
#El personaje principal, el gato, tendrá que evitar tocar los asteroides y evitar los disparos laser de los robots
#moviéndose a lo largo y ancho de la pantalla,  también este podrá recolectar vidas al destruir un asteroide especial
#al igual que puntos al destruir robots y asteroides, el juego termina al dispara al enemigo más grande.

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

#GLOBALES PARA ENEMIGO
xEnemigo= 800
yEnemigo= random.randint(ALTO-400, ALTO-200)
DX= random.randint(1,3)
#Globales para PUNTOS EXTRA
xExtra = 950
yExtra= random.randint(ALTO-400, ALTO-200)

DXAsteroide= random.randint(1,8)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0, 0))


def dibujarMouse(ventana, xMouse, yMOUSE):

    if xMouse != -1:
        pygame.draw.circle(ventana, BLANCO, (xMouse,yMOUSE))


def dibujarMenu(ventana, btnPlay, btnInstruccion, btnScores):
    ventana.blit(btnPlay, (300, 200))  # medidas btn
    ventana.blit(btnInstruccion, (300 , 300))
    ventana.blit(btnScores, (300, 450))

#INSTRUCTIVO
def dibujarInstrucPt1(ventana, instructivoPrimero, btnNext):
    ventana.blit(instructivoPrimero, (100,100))
    ventana.blit(btnNext,(400,400))


def dibujarInstrucPt2(ventana, instructivoSegundo, btnNext):
    ventana.blit(instructivoSegundo, (100, 100))
    ventana.blit(btnNext, (500, 400))


def dibujarInstrucPt3(ventana, instructivoTercero, btnPlay):
    ventana.blit(instructivoTercero, (100, 100))
    ventana.blit(btnPlay, (500, 500))

#JUGANDO
def dibujarNave(ventana, nave, xNave, yNave):
    ventana.blit(nave, (xNave, yNave))


#BALA/PROYECTIL DEL GATO
def dibujarProyectil(ventana, spriteBala):
    if spriteBala.rect.left != -1:
        ventana.blit(spriteBala.image, spriteBala.rect)
        spriteBala.rect.top -= 20


def dibujarListaBalas(ventana, listaBalas):
    for bala in listaBalas: #visita cada elemento
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 15

#OLA DE ENEMIGOS
def dibujarOlaEnemigos(ventana, spriteEnemigo):
    global  DX
    ventana.blit(spriteEnemigo.image,(spriteEnemigo.rect.top,spriteEnemigo.rect.left))
    spriteEnemigo.rect.top -= 5
    #Mover a izq
    if spriteEnemigo.rect.top >= ANCHO+150:
        DX = - DX
    elif spriteEnemigo.rect.top <= -150:
        ventana.blit(spriteEnemigo.image,(spriteEnemigo.rect.top,spriteEnemigo.rect.left))
        spriteEnemigo.rect.top = 800  # x
        spriteEnemigo.rect.left = random.randint(ALTO - 400, ALTO - 200)  # y


def dibujarListaEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)


def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 15

#OLA ASTEROIDES VENTANA ALTA
def dibujarOlaAsteroidesP(ventana, spriteAsteroides, listaAsteroides):
    global DXAsteroide
    ventana.blit(spriteAsteroides.image, (spriteAsteroides.rect.top, spriteAsteroides.rect.left))
    spriteAsteroides.rect.top -= 5
    # MOVER A IZQ
    if spriteAsteroides.rect.top >= ANCHO + 100:
        DXAsteroide = - DXAsteroide
    elif spriteAsteroides.rect.top <= -100:
        ventana.blit(spriteAsteroides.image, (spriteAsteroides.rect.top, spriteAsteroides.rect.left))
        spriteAsteroides.rect.top = 850
        spriteAsteroides.rect.left = random.randint(ALTO - 400, ALTO - 200)


def dibujarListaAsteroidesP(ventana, listaAsteroides):
    for asteroide in listaAsteroides:
        ventana.blit(asteroide.image, asteroide.rect)


def moverAsteroidesP(listaAsteroides):
    for asteroide in listaAsteroides:
        asteroide.rect.left -=15

#OLA ASTEROIDES VENTANA BAJA
def dibujarOlaAsteroidesS(ventana, spriteAsteroidesS, listaAsteroidesS):
    global DXAsteroide
    ventana.blit(spriteAsteroidesS.image, (spriteAsteroidesS.rect.top, spriteAsteroidesS.rect.left))
    spriteAsteroidesS.rect.top -= 5
    # MOVER A IZQ
    if spriteAsteroidesS.rect.top >= ANCHO + 100:
        DXAsteroide = - DXAsteroide
    elif spriteAsteroidesS.rect.top <= -100:
        ventana.blit(spriteAsteroidesS.image, (spriteAsteroidesS.rect.top, spriteAsteroidesS.rect.left))
        spriteAsteroidesS.rect.top = 800
        spriteAsteroidesS.rect.left= random.randint(ALTO-200, ALTO-100)


def dibujarListaAsteroidesS(ventana, listaAsteroidesS):
    for asteroide in listaAsteroidesS:
        ventana.blit(asteroide.image, asteroide.rect)


def moverAsteroidesS(listaAsteroidesS):
    for asteroide in listaAsteroidesS:
        asteroide.rect.left -=15

#ASTEROIDES DE PUNTOS EXTRA
def dibujarOlaPuntosExtra(ventana, spriteExtras):
    global DXAsteroide
    ventana.blit(spriteExtras.image, (spriteExtras.rect.top, spriteExtras.rect.left))
    spriteExtras.rect.top -= 5
    # MOVER A IZQ
    if spriteExtras.rect.top >= ANCHO + 100:
        DXAsteroide = - DXAsteroide
    elif spriteExtras.rect.top <= -1000:
        ventana.blit(spriteExtras.image, (spriteExtras.rect.top, spriteExtras.rect.left))
        spriteExtras.rect.top = 3000
        spriteExtras.rect.left = random.randint(ALTO - 400, ALTO - 200)


def dubijarListaPuntosExtra(ventana, listaPuntosExtra):
    for puntosExtra in listaPuntosExtra:
        ventana.blit(puntosExtra.image, puntosExtra.rect)


def moverPuntosExtra(listaPuntosExtra):
    for puntosExtra in listaPuntosExtra:
        puntosExtra.rect.left -=15

#ATAQUE ENEMIGO
def dibujarAtaque(ventana, spriteAtaque):
    if spriteAtaque.rect.left != -1:
        ventana.blit(spriteAtaque.image, spriteAtaque.rect)
        spriteAtaque.rect.left -= 20

#ENEMIGO FINAL PARA TERMINAR JUEGO
def dibujarEnemigoBoss(ventana, spriteBoss):
    global DX
    ventana.blit(spriteBoss.image, (spriteBoss.rect.top, spriteBoss.rect.left))
    spriteBoss.rect.top -= 5
    # Mover a izq
    if spriteBoss.rect.top >= ANCHO + 150:
        DX = - DX
    elif spriteBoss.rect.top <= -150:
        ventana.blit(spriteBoss.image, (spriteBoss.rect.top, spriteBoss.rect.left))
        spriteBoss.rect.top = 5000
        spriteBoss.rect.left = random.randint(ALTO - 400, ALTO - 300)


def dibujarListaEnemigoBoss(ventana, listaEnemigoBoss):
    for boss in listaEnemigoBoss:
        ventana.blit(boss.image,boss.rect)


def moverEnemigoBoss(listaEnemigoBoss):
    for boss in listaEnemigoBoss:
        boss.rect.left -= 15


def dibujarVidas(ventana, vidas, fuente):
    texto = fuente.render("Vidas: 0" + str(vidas), 1, BLANCO)
    ventana.blit(texto, (50, 110))


def dibujarPuntaje(ventana, puntaje, fuente):
    texto = fuente.render("Puntaje: " + str(puntaje), 1, BLANCO)
    ventana.blit(texto, (500, 110))


def dibujarNivel(ventana, nivel, fuente):
    texto = fuente.render("Nivel: " + str(nivel), 1, BLANCO)
    ventana.blit(texto, (300, 110))


#PUNTAJE
def dibujarPuntajeFinal(ventana, puntaje, fuenteTotal, btnMenu):
    ventana.blit(btnMenu, (650, 0))
    textoJuegoTerminado = fuenteTotal.render("Game Over", 1, BLANCO)
    ventana.blit(textoJuegoTerminado, (200,200))
    texto = fuenteTotal.render("Score: " + str(puntaje), 1, BLANCO)
    ventana.blit(texto, (200, 300))

#COMPROBAR SI HUBO COLISIONES
def probarColision(listaEnemigos, listaBalas):
    for nuevaBala in listaBalas:
        for enemigo in listaEnemigos:
            if nuevaBala.rect.colliderect(enemigo) == True:
                listaEnemigos.remove(enemigo)
                listaBalas.remove(nuevaBala)
                break  # siguente bala


def generarColision(listaEnemigos, nave):
    for enemigo in listaEnemigos:
        if enemigo.rect.colliderect(nave.rect) == True:
            return True
    return False


def probarColisionPuntoExtra(listaBalas, listaPuntosExtra):
    for nuevaBala in listaBalas:
        for puntoExtra in listaPuntosExtra:
            if nuevaBala.rect.colliderect(puntoExtra) == True:
                listaPuntosExtra.remove(puntoExtra)
                listaBalas.remove(nuevaBala)
                break


def probarColisionAsteroide(listaBalas, listaAsteroides):
    for nuevaBala in listaBalas:
        for asteroide in listaAsteroides:
            if nuevaBala.rect.colliderect(asteroide) == True:
                listaAsteroides.remove(asteroide)
                listaBalas.remove(nuevaBala)
                break


def probarColisionAsteroideS(listaBalas, listaAsteroidesS):
    for nuevaBala in listaBalas:
        for asteroide in listaAsteroidesS:
            if nuevaBala.rect.colliderect(asteroide) == True:
                listaAsteroidesS.remove(asteroide)
                listaBalas.remove(nuevaBala)
                break


def probarColisionBoss(listaEnemigoBoss, listaBalas):
    for nuevaBala in listaBalas:
        for boss in listaEnemigoBoss:
            if nuevaBala.rect.colliderect(boss) == True:
                listaEnemigoBoss.remove(boss)
                listaBalas.remove(nuevaBala)
                break


def probarAtaque(spriteAtaque, xNave, yNave):
    xAtaque = spriteAtaque.rect.top
    yAtaque = spriteAtaque.rect.left

    if xAtaque == xNave and yAtaque == yNave:
        return True
    return False


def probarColisionBossConGato(listaEnemigoBoss, xNave, yNave):
    for enemigo in listaEnemigoBoss:
        xEnemigo = enemigo.rect.top
        yEnemigo = enemigo.rect.left
        if xEnemigo == xNave and yEnemigo == yNave:
            return True
    return False

#Salida adicional al menu
def dibujaBtnMenu(ventana, btnMenu):
    ventana.blit(btnMenu, (650, 0))


def dibujar():
    #variables GLOBALES
        #Gato
    xNave = 0
    yNave = ALTO // 2


    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #IMAGENES
    fondoJuego = pygame.image.load("Fondo.jpg")
    nave = pygame.image.load("Nave_Gato.png")
    enemigo = pygame.image.load("Enemigo.png")  #Enemigos comunes
    enemyBoss = pygame.image.load("Enemigo_Boss.png")   #Lider Enemigo

        #BOTONES
    btnPlay = pygame.image.load("button_play.png")
    btnInstruccion = pygame.image.load("button_instructions.png")
    btnScores = pygame.image.load("button_scores.png")
    btnNext = pygame.image.load("button_next.png")
    btnMenu = pygame.image.load("button_menu.png")

        #LASERS Y ASTEROIDES
    asteroide = pygame.image.load("Asteroide.png")
    asteroidPuntosExtra = pygame.image.load("Asteroide_Puntos.png")
    balaEnemigo = pygame.image.load("Laser_Enemigo.png")
    balaGato = pygame.image.load("Laser_Gato.png")

        #INSTRUCTIVO
    instructivoPrimero = pygame.image.load("Instructivo.png")
    instructivoSegundo = pygame.image.load("Instructivo1.png")
    instructivoTercero = pygame.image.load("Instructivo2.png")

    #LISTA PROYECTILES
    listaBalas = []

    #LISTA ENEMIGOS
    listaEnemigos = []

    #LISTA ASTEROIDES
    listaAsteroides = []

    # LISTA ASTEROIDES2
    listaAsteroidesS = []

    #LISTA PUNTOS EXTRA
    listaPuntosExtra = []

    #LISTA ENEMIGO BOSS
    listaEnemigoBoss =[]

    #SPRITES: PUNTOS EXTRA
    spriteExtras = pygame.sprite.Sprite()
    spriteExtras.image = asteroidPuntosExtra
    spriteExtras.rect = asteroidPuntosExtra.get_rect()
    spriteExtras.rect.top = 3000
    spriteExtras.rect.left = random.randint(ALTO-400, ALTO-200)

    #SPRITES: ASTEROIDES
    spriteAsteroides = pygame.sprite.Sprite()
    spriteAsteroides.image = asteroide
    spriteAsteroides.rect = asteroide.get_rect()
    spriteAsteroides.rect.top = 850
    spriteAsteroides.rect.left= random.randint(ALTO-400, ALTO-200)

    #SPRITES: ASTEROIDES2
    spriteAsteroidesS = pygame.sprite.Sprite()
    spriteAsteroidesS.image = asteroide
    spriteAsteroidesS.rect = asteroide.get_rect()
    spriteAsteroidesS.rect.top = 800
    spriteAsteroidesS.rect.left= random.randint(ALTO-200, ALTO-100)

    #SPRITES: ENEMIGO
    spriteEnemigo = pygame.sprite.Sprite()
    spriteEnemigo.image = enemigo
    spriteEnemigo.rect = enemigo.get_rect()
    spriteEnemigo.rect.top = 1000 #x
    spriteEnemigo.rect.left = random.randint(ALTO-400, ALTO-300) #y

    #SPRITES: ATAQUE GATO
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = balaGato
    spriteBala.rect = balaGato.get_rect()  # Datos de la imagen
    spriteBala.rect.top = -1  # X
    spriteBala.rect.left = -1  # Y

    #SPRITES:   ATAQUE DE ENEMIGO
    spriteAtaque = pygame.sprite.Sprite
    spriteAtaque.image = balaEnemigo
    spriteAtaque.rect = balaEnemigo.get_rect()
    spriteAtaque.rect.left = -1
    spriteAtaque.rect.top = -1

    #SPRITES: ENEMIGOBOSS
    spriteBoss = pygame.sprite.Sprite()
    spriteBoss.image = enemyBoss
    spriteBoss.rect = enemyBoss.get_rect()
    spriteBoss.rect.top = 5000
    spriteBoss.rect.left = random.randint(ALTO-500, ALTO-300)

    # AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)

    # mouse
    xMouse = -1
    yMOUSE = -1


    # ESTADOS
    MENU = 1
    JUGANDO = 2
    INSTRUCCIONESpt1 = 3
    INSTRUCCIONESpt2 = 4
    INSTRUCCIONESpt3 = 5
    PUNTAJE = 6

    estado = MENU
    # pausa
    # gameover

    # Tiempos
    tiempoAtaque = 40  # cada cuanto el enemigo ataca

    # TEXTO
    fuente = pygame.font.SysFont("Arial", 30)
    puntaje = 0
    vidas = 3
    nivel = 1
    fuenteTotal = pygame.font.SysFont("Arial", 60)  # PuntajeFinal


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMOUSE = pygame.mouse.get_pos()
                print(xMouse,yMOUSE)
                if xMouse >= 300 and xMouse <= 500 and yMOUSE >= 200 and yMOUSE<=250:   #coordenadas btn
                    #oprimio el botton PLAY
                    xMouse=-1
                    estado= JUGANDO
                if xMouse >= 300 and xMouse <= 500 and yMOUSE >= 300 and yMOUSE <= 350:
                    # oprimio el boton INSTRUCCIONES
                    xMouse = -1
                    estado = INSTRUCCIONESpt1
                if xMouse >=400 and xMouse <= 500 and yMOUSE >= 400 and yMOUSE <= 450:
                    xMouse = -1
                    estado= INSTRUCCIONESpt2
                if xMouse >=500 and xMouse <= 700 and yMOUSE >= 400 and yMOUSE <= 450:
                    xMouse=-1
                    estado = INSTRUCCIONESpt3
                if xMouse >=500 and xMouse <= 700 and yMOUSE >= 500 and yMOUSE <= 550:
                    xMouse=-1
                    estado= JUGANDO
                if xMouse >= 300 and xMouse <= 500 and yMOUSE >= 450 and yMOUSE <= 500:
                    # oprimio el boton SCORES
                    xMouse = -1
                    estado = PUNTAJE
                if xMouse >= 700 and xMouse <= 800 and yMOUSE >=0 and yMOUSE <=45:
                    #oprimio el btn menu
                    xMouse = -1
                    estado = MENU

            elif evento.type == pygame.KEYDOWN:
                    # QUE TECLA SE OPRIMIO
                if evento.key == pygame.K_RIGHT:
                    xNave += 20
                elif evento.key == pygame.K_LEFT:
                     xNave -= 20
                elif evento.key == pygame.K_UP:
                    yNave -= 20
                elif evento.key == pygame.K_DOWN:
                    yNave += 20
                elif evento.key == pygame.K_SPACE:
                    nuevaBala =  pygame.sprite.Sprite()
                    nuevaBala.image = balaGato
                    nuevaBala.rect = balaGato.get_rect()
                    nuevaBala.rect.left = xNave+64-12
                    nuevaBala.rect.top = yNave
                    listaBalas.append(nuevaBala)

        # Borrar pantalla
        ventana.fill(BLANCO)

        dibujarFondo(ventana, fondoJuego)

        moverBalas(listaBalas)
        moverEnemigos(listaEnemigos)
        moverAsteroidesP(listaAsteroides)
        moverAsteroidesS(listaAsteroidesS)
        moverPuntosExtra(listaPuntosExtra)
        moverEnemigoBoss(listaEnemigoBoss)

        if estado == MENU:
            dibujarMouse(ventana,xMouse,yMOUSE)
            dibujarMenu(ventana,btnPlay,btnInstruccion,btnScores)
        elif estado == INSTRUCCIONESpt1:
            dibujarInstrucPt1(ventana,instructivoPrimero,btnNext)
            dibujaBtnMenu(ventana,btnMenu)
        elif estado == INSTRUCCIONESpt2:
            dibujarInstrucPt2(ventana,instructivoSegundo,btnNext)
            dibujaBtnMenu(ventana, btnMenu)
        elif estado == INSTRUCCIONESpt3:
            dibujarInstrucPt3(ventana,instructivoTercero,btnPlay)
            dibujaBtnMenu(ventana, btnMenu)
        elif estado == PUNTAJE:
            dibujarPuntajeFinal(ventana, puntaje, fuenteTotal, btnMenu)
        elif estado == JUGANDO:
            #dibujar salida al menu
            dibujaBtnMenu(ventana, btnMenu)

            # DIBUJAR
            dibujarNave(ventana, nave, xNave, yNave)
            dibujarProyectil(ventana, spriteBala)   #gato
            dibujarListaBalas(ventana, listaBalas)

                #DIBUJAR ENEMIGOS
            dibujarOlaEnemigos(ventana,spriteEnemigo)
            dibujarListaEnemigos(ventana,listaEnemigos)
            dibujarAtaque(ventana, spriteAtaque)
                #DIBUJAR Enemigo BOSS
            dibujarEnemigoBoss(ventana,spriteBoss)
            dibujarListaEnemigoBoss(ventana,listaEnemigoBoss)

                #DIBUJAR ASTEROIDES
            dibujarOlaAsteroidesP(ventana,spriteAsteroides,listaAsteroides)
            dibujarListaAsteroidesP(ventana,listaAsteroides)

            dibujarOlaAsteroidesS(ventana,spriteAsteroidesS,listaAsteroidesS)
            dibujarListaAsteroidesS(ventana,listaAsteroidesS)

                #DIBUJAR ASTEROIDES PUNTOS EXTRA
            dibujarOlaPuntosExtra(ventana,spriteExtras)
            dubijarListaPuntosExtra(ventana,listaPuntosExtra)

                #DIBUAJAR, NIVEL VIDAS Y PUNTAJE
            dibujarNivel(ventana,nivel,fuente)
            dibujarVidas(ventana, vidas, fuente)
            dibujarPuntaje(ventana, puntaje, fuente)

            #ACTUALIZACIONES
                #Ataque Enemigo hacia gato
            tiempoAtaque -= 1  # va restando al timepo inicial del ataque
            if tiempoAtaque == 0:
                spriteAtaque.rect.left = spriteEnemigo.rect.top  # aparece randomly [random.randint(0,ANCHO)]
                spriteAtaque.rect.top = spriteEnemigo.rect.left  # 0 aparece de lo alto de ventana
                tiempoAtaque = 40

                # colision BalaGato con Enemigo, destruir enemigo
            hayColisonBala = probarColision(listaEnemigos, listaBalas)  # regresa el true
            if hayColisonBala == True:
                puntaje += 100

                #colision BalaGato con Asteroide puntoExtra
            colisionPuntoExtra = probarColisionPuntoExtra(listaBalas, listaPuntosExtra)
            if colisionPuntoExtra == True:
                puntaje += 500

                #colision BalaGato con Asteroidearriba normal
            colisionAsteroideP = probarColisionAsteroide(listaBalas,listaAsteroides)
            if colisionAsteroideP == True:
                puntaje += 20

                #colision BalaGato con Asteroides abajo normal
            colisionAsteroideS = probarColisionAsteroideS(listaBalas,listaAsteroidesS)
            if colisionAsteroideS == True:
                puntaje += 500

                #colision BalaGato con enemigoBoss
            colisionEnemigoBoss = probarColisionBoss(listaEnemigoBoss, listaBalas)
            if colisionEnemigoBoss == True:
                puntaje += 10000

                #colision Ataque enemigo con Gato
            colisionAtaqueGato = probarAtaque(spriteAtaque, xNave, yNave)
            if colisionAtaqueGato == True:
                vidas -= 1
                puntaje += 0


                #colision enemigo boss con Gato
            colisionBossConGato = probarColisionBossConGato(listaEnemigoBoss, xNave,yNave)
            if colisionBossConGato == True:
                xNave = -100
                estado == PUNTAJE
                dibujarPuntajeFinal(ventana, puntaje, fuenteTotal, btnMenu)

                #colision enemigo con Gato, no es lo mismo que destruir enemigo
            hayColisonAtaque = generarColision(listaEnemigos,nave)
            if hayColisonAtaque == True:
                vidas -= 1
                puntaje -= 10

            #TERMINAR JUERO SI YA NO TIENE VIDAS
            if vidas <= 0:
                xNave = -100
                estado == PUNTAJE
                dibujarPuntajeFinal(ventana, puntaje, fuenteTotal, btnMenu)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()