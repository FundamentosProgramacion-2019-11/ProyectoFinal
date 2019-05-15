# Yadira Fuentes Calderón
# Juego de video que toma lugar en una historia que estoy diseñando


import pygame

ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

xFondo = 0
angulo = 0

xindigoVillain = ANCHO // 2
yindigoVillain = 200
DX =+ 10

xandromedaHero = ANCHO // 2
yandromedaHero = ALTO // 2 + 160


def probarChoque(listaEnemy, andromeda_blast):
    andromedaBlast = andromeda_blast.rect
    for enemy in listaEnemy:
        if andromedaBlast.colliderect(enemy):
            listaEnemy.remove(enemy)
            listaEnemy.remove(andromedaBlast)
            break


def destruirEnemigo(listaEnemy, andromeda_blast):
    for enemy in listaEnemy:
        if enemy.rect.colliderect(andromeda_blast):
            listaEnemy.remove(enemy)
            andromeda_blast.rect.left = -100000
            return True
    return False


def dibujarEnemigos(listaEnemy, enemy):
    for y in range(100, 200 + 1, 100):
        for x in range(80, 600 + 1, 200):
            enemyA = pygame.sprite.Sprite()
            enemyA.image = enemy
            enemyA.rect = enemy.get_rect()
            listaEnemy.append(enemyA)
            enemyA.rect.left = x
            enemyA.rect.top = y


def dibujarReglas(ventana, bMenu, background, missionInstructions, bPlay):
    ventana.blit(background, (0, 0))
    ventana.blit(bMenu, (550, 25))
    ventana.blit(bPlay, (10, 25))
    ventana.blit(missionInstructions, (0, 0))


def dibujarPoints(ventana, redundant, scoreImage, bMenu, tipoLetra):
    ventana.blit(scoreImage, (0, 0))
    ventana.blit(bMenu, (550, 25))
    text = tipoLetra.render("SCORE: " + str(redundant), 3, BLANCO)
    ventana.blit(text, (310, 200))


def dibujarAndromeda(ventana, andromedaHero):
    ventana.blit(andromedaHero, (xandromedaHero, yandromedaHero))


def dibujarIndigo(ventana, indigoVillain):
    global xindigoVillain, DX, yindigoVillain
    ventana.blit(indigoVillain, (xindigoVillain, yindigoVillain))
    xindigoVillain += DX
    if xindigoVillain >= ANCHO - 120 or xindigoVillain <= 0:
        DX = -DX


def dibujarListEnemy(ventana, listaEnemy):
    for enemy in listaEnemy:
        ventana.blit(enemy.image, enemy.rect)


def dibujarNombreDePersonajes(ventana, nombreIndigo, nombreAndromeda):
    ventana.blit(nombreAndromeda, (670, 520))
    ventana.blit(nombreIndigo, (340, 10))


def revisarAndromedaDisparo(andromeda_blast):
    global xindigoVillain, yindigoVillain
    xDisparo = andromeda_blast.rect.left
    yDisparo = andromeda_blast.rect.top
    if xindigoVillain <= xDisparo <= xindigoVillain + 128 and yindigoVillain <= yDisparo <= yindigoVillain + 73:
        return True
    return False


def revisarAciertosIndigo(indigo_Blast):
    global xandromedaHero, yandromedaHero
    xDisparoInd = indigo_Blast.rect.left
    yDisparoInd = indigo_Blast.rect.top
    if xandromedaHero <= xDisparoInd <= xandromedaHero + 90 and yandromedaHero + 73 >= yDisparoInd >= xandromedaHero:
        return True
    return False


def dibujarDisparoAndromeda(ventana, andromeda_blast):
    if andromeda_blast.rect.left != 1:
        ventana.blit(andromeda_blast.image, andromeda_blast.rect)
        andromeda_blast.rect.top -= 20
        if andromeda_blast.rect.top < -32:
            andromeda_blast.rect.left = -1


def dibujarDisparoIndigo(ventana, indigo_Blast):
    if indigo_Blast.rect.left != -1:
        ventana.blit(indigo_Blast.image, indigo_Blast.rect)
        indigo_Blast.rect.top += 20
        if indigo_Blast.rect.top < -80:
            indigo_Blast.rect.left = -1


def sufrirDerrota(ventana, badEnding, bMenu):
    ventana.blit(badEnding, (0, 0))
    ventana.blit(bMenu, (550, 25))


def celebrarVictoria(ventana, goodEnding, bMenu):
    ventana.blit(goodEnding, (0, 0))
    ventana.blit(bMenu, (550, 25))


def dibujarMenu(ventana, bPlay, bMision, bScore):
    ventana.blit(bPlay, (300, 325))
    ventana.blit(bMision, (300, 400))
    ventana.blit(bScore, (300, 475))


def dibujarNombreVideojuego(ventana, starStart):
    ventana.blit(starStart, (100, 45))


def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != 1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 0)


def dibujarBackground(ventana, background):
    global xFondo
    ventana.blit(background, (0, 0))


def dibujar():
    global xandromedaHero, yandromedaHero, vidaIndigo, vidaAndromeda
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    tresVidasIndigo = pygame.image.load("Indigo_Life1.png")
    dosVidasIndigo = pygame.image.load("Indigo_Life2.png")
    unaVidaIndigo = pygame.image.load("Indigo_Life3.png")
    unaVidaAndromeda = pygame.image.load("andromeda_Life2.png")
    dosVidasAndromeda = pygame.image.load("andromeda_Life1.png")
    goodEnding = pygame.image.load("good_ending.png")
    badEnding = pygame.image.load("bad_ending.png")
    enemy = pygame.image.load("enemy.png")
    andromedaHero = pygame.image.load("andromeda_hero.png")
    indigoVillain = pygame.image.load("Indigo_villain.png")
    nombreAndromeda = pygame.image.load("andromeda_name.png")
    nombreIndigo = pygame.image.load("indigo_name.png")
    andromedaBlast = pygame.image.load("andromeda_blast.png")
    indigoBlast = pygame.image.load("indigo_blast.png")
    scoreImage = pygame.image.load("background 2.png")
    missionInstructions = pygame.image.load("instructions.png")
    background = pygame.image.load("background.png")
    starStart = pygame.image.load("starstart.png")
    bPlay = pygame.image.load("play_button.png")
    bMision = pygame.image.load("mission_button.png")
    bScore = pygame.image.load("score_button.png")
    bMenu = pygame.image.load("menu_button.png")

    tipoLetra = pygame.font.SysFont("arial", 65)

    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("MusicaFondo.mp3")
    pygame.mixer.music.play(-1)

    andromeda_blast = pygame.sprite.Sprite()
    andromeda_blast.image = andromedaBlast
    indigo_Blast = pygame.sprite.Sprite()
    indigo_Blast.image = indigoBlast

    andromeda_blast.rect = andromedaBlast.get_rect()
    indigo_Blast.rect = indigoBlast.get_rect()

    andromeda_blast.rect.top = - 1
    andromeda_blast.rect.left = -1
    indigo_Blast.rect.top = -1
    indigo_Blast.rect.left = -1

    xMouse = -1
    yMouse = -1

    indigoLoca = 200

    MENU = 1
    REGLAS = 2
    DEFEAT = 3
    VICTORY = 4
    POINTS = 5
    JUGAR = 6
    estado = MENU

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if 300 <= xMouse <= 500 and 325 <= yMouse <= 376:
                    xMouse = -1
                    estado = JUGAR
                    listaEnemy = []
                    dibujarEnemigos(listaEnemy, enemy)

                if 300 <= xMouse <= 500 and 400 <= yMouse <= 451:
                    xMouse = -1
                    estado = REGLAS

                if 300 <= xMouse <= 500 and 475 <= yMouse <= 524:
                    xMouse = -1
                    estado = POINTS
                if 540 <= xMouse <= 790 and 25 <= yMouse <= 91:
                    xMouse = -1
                    estado = MENU
                if 10 <= xMouse <= 210 and 25 <= yMouse <= 61:
                    xMouse = -1
                    estado = JUGAR
                    listaEnemy = []
                    dibujarEnemigos(listaEnemy, enemy)

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    xandromedaHero += 30
                elif evento.key == pygame.K_LEFT:
                    xandromedaHero -= 30

                elif evento.key == pygame.K_SPACE:
                    if andromeda_blast.rect.left == -1:
                        andromeda_blast.rect.left = xandromedaHero + 40
                        andromeda_blast.rect.top = yandromedaHero - 73
                        efectoDisparo.play()

        ventana.blit(background, (0, 0))
        if estado == MENU:
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, bPlay, bMision, bScore)
            dibujarNombreVideojuego(ventana, starStart)
            vidaIndigo = 3
            vidaAndromeda = 2
            puntos = 0

        elif estado == REGLAS:
            dibujarReglas(ventana, bMenu, background, missionInstructions, bPlay)

        elif estado == DEFEAT:
            sufrirDerrota(ventana, badEnding, bMenu)

        elif estado == VICTORY:
            celebrarVictoria(ventana, goodEnding, bMenu)

        elif estado == POINTS:
            dibujarPoints(ventana, redundant, scoreImage, bMenu, tipoLetra)


        elif estado == JUGAR:
            juas = destruirEnemigo(listaEnemy, andromeda_blast)
            if juas == True:
                redundant = 0
                puntos += 125
                redundant = redundant + puntos
                print(redundant)

            indigoLoca -= 1
            if indigoLoca == 0:
                indigo_Blast.rect.top = yindigoVillain
                indigo_Blast.rect.left = xindigoVillain
                indigoLoca = 50

            destruirEnemigo(listaEnemy, andromeda_blast)
            dibujarBackground(ventana, background)
            dibujarAndromeda(ventana, andromedaHero)
            dibujarDisparoAndromeda(ventana, andromeda_blast)
            dibujarNombreDePersonajes(ventana, nombreIndigo, nombreAndromeda)
            dibujarIndigo(ventana, indigoVillain)
            dibujarDisparoIndigo(ventana, indigo_Blast)
            destruirEnemigo(listaEnemy, andromeda_blast)
            dibujarListEnemy(ventana, listaEnemy)

            disparoRecibidoAndromeda = revisarAciertosIndigo(indigo_Blast)
            if disparoRecibidoAndromeda:
                vidaAndromeda -= 1
                indigo_Blast.rect.top = 0
            if vidaAndromeda == 2:
                ventana.blit(dosVidasAndromeda, (670, 550))
            elif vidaAndromeda == 1:
                ventana.blit(unaVidaAndromeda, (670, 550))
            elif vidaAndromeda == 0:
                estado = DEFEAT

            disparoDadoIndigo = revisarAndromedaDisparo(andromeda_blast)
            if disparoDadoIndigo:
                vidaIndigo -= 1
                andromeda_blast.rect.top = 0
            if vidaIndigo == 3:
                ventana.blit(tresVidasIndigo, (300, 40))
            elif vidaIndigo == 2:
                ventana.blit(dosVidasIndigo, (300, 40))
            elif vidaIndigo == 1:
                ventana.blit(unaVidaIndigo, (300, 40))
            elif vidaIndigo == 0:
                estado = VICTORY

        pygame.display.flip()
        reloj.tick(40)


def main():
    dibujar()


main()