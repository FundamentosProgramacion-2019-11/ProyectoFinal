# Karimn Daniel Hernández Castorena
# Videojuego del mundo de Star Wars.


import math
import pygame

ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

xalaX = ANCHO // 2
yalaX = ALTO // 2 + 150

xcazaTie = ANCHO // 2
ycazaTie = 200
DX = + 10

naveTransporteX = ANCHO // 2
naveTransporteY = 520
nTx = + 2

xFondo = 0
angulo = 0


def dibujarBackground(ventana, background):
    global xFondo
    ventana.blit(background, (0, 0))


def dibujarMouse(ventana, xMouse, yMouse):
    if xMouse != 1:
        pygame.draw.circle(ventana, BLANCO, (xMouse, yMouse), 0)


def dibujarNombre(ventana, nombreJuego):
    ventana.blit(nombreJuego, (125, 45))


def dibujarMenu(ventana, btnJugar, mision, score1):
    ventana.blit(btnJugar, (300, 325))
    ventana.blit(mision, (300, 400))
    ventana.blit(score1, (300, 475))


def dibujarMision(ventana, bMenu, background, instruccion, btnJugar):
    ventana.blit(background, (0, 0))
    ventana.blit(bMenu, (550, 25))
    ventana.blit(btnJugar, (10, 25))
    ventana.blit(instruccion, (0, 0))


def dibujarPuntaje(ventana, score, puntuacion, btnMenu, f):
    ventana.blit(puntuacion, (0, 0))
    ventana.blit(btnMenu, (550, 25))
    text = f.render("SCORE: " + str(score), 3, AZUL)
    ventana.blit(text, (290, 200))

def dibujarAlaX(ventana, alaX):
    ventana.blit(alaX, (xalaX, yalaX))


def dibujarCazaTie(ventana, cazaTie):
    global xcazaTie, DX, ycazaTie, angulo
    ventana.blit(cazaTie, (xcazaTie, ycazaTie))
    xcazaTie += DX
    if xcazaTie >= ANCHO - 120 or xcazaTie <= 0:
        DX = -DX
    dy = int(100 * math.sin(math.radians(angulo))) + 70
    ycazaTie = dy
    angulo += 8


def dibujarNaveTransporte(ventana, naveTransporte):
    global naveTransporteX, naveTransporteY, nTx, angulo
    ventana.blit(naveTransporte, (naveTransporteX, naveTransporteY))
    naveTransporteX += nTx
    if naveTransporteX >= ANCHO - 70 or naveTransporteX <= 0:
        nTx = -nTx
    nTy = int(10 * math.sin(math.radians(angulo))) + 540
    naveTransporteY = nTy
    angulo += 2


def dibujarNombresPilotos(ventana, nombreCazaTie, nombreAlaX):
    ventana.blit(nombreAlaX, (670, 520))
    ventana.blit(nombreCazaTie, (30, 520))


def revisarAciertoDisparoRojo(redBlaster):
    global xcazaTie, ycazaTie
    xDisparo = redBlaster.rect.left
    yDisparo = redBlaster.rect.top
    if xcazaTie <= xDisparo <= xcazaTie + 128 and ycazaTie <= yDisparo <= ycazaTie + 73:
        return True
    return False


def revisarAciertoDisparoVerde(greenBlaster):
    global xalaX, yalaX
    xDisparoTie = greenBlaster.rect.left
    yDisparoTie = greenBlaster.rect.top
    if xalaX <= xDisparoTie <= xalaX + 90 and yalaX + 73 >= yDisparoTie >= yalaX:
        return True
    return False


def mostrarHpTieInicial(ventana, cuatroV):
    ventana.blit(cuatroV, (670, 40))


def mostrarHpXwingInicial(ventana, unaValaX):
    ventana.blit(unaValaX, (670, 40))


def dibujarDisparoBlasterRojo(ventana, redBlaster):
    if redBlaster.rect.left != 1:
        ventana.blit(redBlaster.image, redBlaster.rect)
        redBlaster.rect.top -= 40
        if redBlaster.rect.top < -82:
            redBlaster.rect.left = -1


def dibujarDisparoBlasterVerde(ventana, greenBlaster):
    if greenBlaster.rect.left != -1:
        ventana.blit(greenBlaster.image, greenBlaster.rect)
        greenBlaster.rect.top += 20
        if greenBlaster.rect.top < -80:
            greenBlaster.rect.left = -1


def revisarDisparoTransporte(greenBlaster):
    global naveTransporteX, naveTransporteY
    yDisparoTie = greenBlaster.rect.top
    xDisparoTie = greenBlaster.rect.left
    if naveTransporteX <= xDisparoTie <= naveTransporteX + 80 and naveTransporteY <= yDisparoTie + 80:
        greenBlaster.rect.left = -1
        return True
    return False


def llamarImperio(ventana, empireWin, btnMenu):
    ventana.blit(empireWin, (0, 0))
    ventana.blit(btnMenu, (550, 25))


def llamarRebeldes(ventana, rebelWins, btnMenu):
    ventana.blit(rebelWins, (0, 0))
    ventana.blit(btnMenu, (550, 25))


def dibujarListA(ventana, listA):
    for asteroide1 in listA:
        ventana.blit(asteroide1.image, asteroide1.rect)


def dibujarAsteroides(listA, asteroide1):
    for y in range(100, 350 + 1, 100):
        for x in range(50, 700 + 1, 100):
            sAsteroide1 = pygame.sprite.Sprite()
            sAsteroide1.image = asteroide1
            sAsteroide1.rect = asteroide1.get_rect()
            listA.append(sAsteroide1)
            sAsteroide1.rect.left = x
            sAsteroide1.rect.top = y


def destruirAsteroide(listA, redBlaster):
    for asteroide1 in listA:
        if asteroide1.rect.colliderect(redBlaster):
            listA.remove(asteroide1)
            redBlaster.rect.left = -100
            return True
    return False




def dibujar():
    global xalaX, yalaX
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    background = pygame.image.load("fondo.jpg")
    nombreJuego = pygame.image.load("Name.png")
    btnJugar = pygame.image.load("btnJugar.png")
    mision = pygame.image.load("btnMision.png")
    score1 = pygame.image.load("btnPuntos.png")
    btnMenu = pygame.image.load("btnMenu.png")
    alaX = pygame.image.load("xwing.png")
    cazaTie = pygame.image.load("tie.png")
    naveTransporte = pygame.image.load("Transport.png")
    nombreAlaX = pygame.image.load("RebelPilot.png")
    nombreCazaTie = pygame.image.load("ImperialPilot.png")
    disparoRojo = pygame.image.load("redBlaster.png")
    disparoVerde = pygame.image.load("greenBlaster.png")
    cuatroV = pygame.image.load("Life4.png")
    tresV = pygame.image.load("Life3.png")
    dosV = pygame.image.load("Life2.png")
    unav = pygame.image.load("Life1.png")
    noV = pygame.image.load("NoLife.png")
    unaValaX = pygame.image.load("XWingLife.png")
    noValaX = pygame.image.load("XWingDeath.png")
    rebelWins = pygame.image.load("Rebeldes.jpg")
    empireWin = pygame.image.load("Imperio.png")
    asteroide1 = pygame.image.load("Asteroide.png")
    puntuacion = pygame.image.load("score.png")
    instruccion = pygame.image.load("Mission.png")

    redBlaster = pygame.sprite.Sprite()
    redBlaster.image = disparoRojo
    greenBlaster = pygame.sprite.Sprite()
    greenBlaster.image = disparoVerde

    redBlaster.rect = disparoRojo.get_rect()
    greenBlaster.rect = disparoVerde.get_rect()

    redBlaster.rect.top = - 1
    redBlaster.rect.left = -1
    greenBlaster.rect.top = -1
    greenBlaster.rect.left = -1

    f = pygame.font.SysFont("Times New Roman", 50)

    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    grito = pygame.mixer.Sound("grito.wav")
    pygame.mixer.music.load("MusicaFondo.mp3")
    tieSound = pygame.mixer.Sound("tieSound.wav")
    pygame.mixer.music.play(-1)

    xMouse = -1
    yMouse = -1

    disarmTie = 100

    MENU = 1
    MISION = 2
    IMPERIO = 3
    REBELDE = 4
    SCORE = 5
    PLAY = 6
    estate = MENU

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                print(xMouse, yMouse)
                if 300 <= xMouse <= 500 and 325 <= yMouse <= 376:
                    xMouse = -1
                    estate = PLAY
                    listA = []
                    dibujarAsteroides(listA, asteroide1)

                if 300 <= xMouse <= 500 and 400 <= yMouse <= 451:
                    xMouse = -1
                    estate = MISION

                if 300 <= xMouse <= 500 and 475 <= yMouse <= 524:
                    xMouse = -1
                    estate = SCORE
                if 540 <= xMouse <= 790 and 25 <= yMouse <= 91:
                    xMouse = -1
                    estate = MENU
                if 10 <= xMouse <= 210 and 25 <= yMouse <= 61:
                    xMouse = -1
                    estate = PLAY
                    listA = []
                    dibujarAsteroides(listA, asteroide1)

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    xalaX += 50
                elif evento.key == pygame.K_LEFT:
                    xalaX -= 50

                elif evento.key == pygame.K_SPACE:
                    if redBlaster.rect.left == -1:
                        redBlaster.rect.left = xalaX + 40
                        redBlaster.rect.top = yalaX - 73
                        efectoDisparo.play()

        ventana.blit(background, (0, 0))
        if estate == MENU:
            dibujarMouse(ventana, xMouse, yMouse)
            dibujarMenu(ventana, btnJugar, mision, score1)
            dibujarNombre(ventana, nombreJuego)
            hpTie = 4
            hpAlaX = 2
            score = 0

        elif estate == MISION:
            dibujarMision(ventana, btnMenu, background, instruccion, btnJugar)

        elif estate == IMPERIO:
            llamarImperio(ventana, empireWin, btnMenu)

        elif estate == REBELDE:
            llamarRebeldes(ventana, rebelWins, btnMenu)

        elif estate == SCORE:
            dibujarPuntaje(ventana, score, puntuacion, btnMenu, f)

        elif estate == PLAY:
            a = destruirAsteroide(listA, redBlaster)
            if a:
                a = 0
                score += 500
                score = a + score
                print(score)

            disarmTie -= 1
            if disarmTie == 0:
                greenBlaster.rect.top = ycazaTie
                greenBlaster.rect.left = xcazaTie
                disarmTie = 100
                tieSound.play()

            dibujarBackground(ventana, background)
            dibujarAlaX(ventana, alaX)
            dibujarDisparoBlasterRojo(ventana, redBlaster)
            dibujarNombresPilotos(ventana, nombreCazaTie, nombreAlaX)
            dibujarCazaTie(ventana, cazaTie)
            dibujarListA(ventana, listA)
            dibujarNaveTransporte(ventana, naveTransporte)
            dibujarDisparoBlasterVerde(ventana, greenBlaster)

            if destruirAsteroide(listA, redBlaster):
                grito.play()

            shieldDamage = revisarAciertoDisparoVerde(greenBlaster)
            if shieldDamage:
                hpAlaX -= 1
                greenBlaster.rect.top = 0
            if hpAlaX == 2:
                ventana.blit(unaValaX, (670, 550))
            if hpAlaX == 1:
                ventana.blit(noValaX, (670, 550))
            if hpAlaX == 0:
                estate = IMPERIO

            directHit = revisarAciertoDisparoRojo(redBlaster)
            if directHit:
                hpTie -= 1
                redBlaster.rect.top = 0
            if hpTie == 4:
                ventana.blit(cuatroV, (45, 550))
            if hpTie == 3:
                ventana.blit(tresV, (45, 550))
            elif hpTie == 2:
                ventana.blit(dosV, (45, 550))
            elif hpTie == 1:
                ventana.blit(unav, (45, 550))
            elif hpTie == 0:
                ventana.blit(noV, (45, 550))
                estate = REBELDE

        explosionTransporte = revisarDisparoTransporte(greenBlaster)
        if explosionTransporte:
            estate = IMPERIO
            dibujarMouse(ventana, xMouse, yMouse)

        pygame.display.flip()
        reloj.tick(40)


def main():
    dibujar()


main()
