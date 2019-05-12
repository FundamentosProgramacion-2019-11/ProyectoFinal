#Bruno Omar Jiménez Mancilla
import pygame   # Librería de pygame
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)   # nada de rojo, ni verde, solo azul
NEGRO =(0, 0, 0)
"""---------------------------------------------------------------------------------------------------------------------
VAR GLOBALES
Las variables que se usan a lo largo de distintas funciones van aquí, para poder modificarlas dentro de una funcion es 
necesario usar 'Global' """
xJugador = ANCHO//2
yJugador = ALTO//2
xEnemigo = 650
yEnemigo = 150
xEnemigo2 = 650
yEnemigo2 = 400
xEnemigo3 = 650
yEnemigo3 = 50
xEnemigo4 = 650
yEnemigo4 = 400
xEnemigo5 = 650
yEnemigo5 = 100
xHunter1 = 650
yHunter1 = 100
xHunter2 = 650
yHunter2 = 400
DY = 1
DX = 1
enemigosMuertos = 0
vidaJugador = 5
vidaNave1 = 20
vidaNave2 = 20



"""---------------------------------------------------------------------------------------------------------------------
FUNCIONES
Aquí se describen las funciones que usará el juego"""
def dibujarPersonaje(ventana,personaje ):
    ventana.blit(personaje,(xJugador,yJugador))
def dibujarMenu(ventana, buttonPlay,fondoMenu,buttonInstrucciones):
    ventana.blit(fondoMenu, (0, 0))
    ventana.blit(buttonPlay, (ANCHO//2 +150,ALTO//2 +200 ))
    ventana.blit(buttonInstrucciones, (ANCHO//2 +150,ALTO//2 +100))
def dibujarFondo(ventana, fondo):
    ventana.blit(fondo, (0,0))
def dibujarEnemigo(ventana, enemigoImg):
    global xEnemigo, yEnemigo, DY
    ventana.blit(enemigoImg,(xEnemigo,yEnemigo))
    yEnemigo += DY
    if yEnemigo >= ALTO-400 or yEnemigo <= 0:
        DY = -DY


def dibujarEnemigoH(ventana, enemigoImg, xEne, yEne):
    global xHunter1
    ventana.blit(enemigoImg, (xEne, yEne))
    xHunter1 -= DX
def dibujarEnemigoH2(ventana, enemigoImg, xEne, yEne):
    global xHunter2
    ventana.blit(enemigoImg, (xEne, yEne))
    xHunter2 -= DX
def dibujarBala(ventana, spriteBala):
    if spriteBala.rect.left != -1:
        ventana.blit(spriteBala.image, spriteBala.rect)
        spriteBala.rect.left += 20
        if spriteBala.rect.left > 800:
            spriteBala.rect.left = -1
def dibujarBalaEnemigo(ventana, spriteBala2):
    if spriteBala2.rect.left != 900:
        ventana.blit(spriteBala2.image, spriteBala2.rect)
        spriteBala2.rect.left -= 10
        if spriteBala2.rect.left < 0:
            spriteBala2.rect.left = 900
def probarColision(spriteBala,xEnemigo,yEnemigo):
    xBala = spriteBala.rect.left
    yBala = spriteBala.rect.top
    if xBala >= xEnemigo and xBala <= xEnemigo+120 and yBala <= yEnemigo+90 and yBala >= yEnemigo:
        print(True)
        return True
    else:
        return False
def probarColisionJugador(spriteBala2):
    yBala = spriteBala2.rect.top
    xBala = spriteBala2.rect.left
    if xBala >= xJugador and xBala <= xJugador+90 and yBala <= yJugador+100 and yBala >= yJugador:
        print("La bala impacto")
        return True
def dibujarEnemigo2(ventana, enemigoImg):
    ventana.blit(enemigoImg,(xEnemigo2,yEnemigo2))
def dibujarEnemigox(ventana, enemigoImg,xEne,yEne):
    ventana.blit(enemigoImg,(xEne,yEne))


def dibujarEnemigo3(ventana, enemigoImg):
    ventana.blit(enemigoImg,(xEnemigo4,yEnemigo4))
def dibujarBalaEnemigo2(ventana, spriteBala3):
    if spriteBala3.rect.left != 900:
        ventana.blit(spriteBala3.image, spriteBala3.rect)
        spriteBala3.rect.left -= 10
        if spriteBala3.rect.left < 0:
            spriteBala3.rect.left = 900
def dibujarDerrotaOaVictoria(ventana, fondo, buttonMenu):
    ventana.blit(fondo,(0,0))
    ventana.blit(buttonMenu,(50,500))
def dibujarDerrotaOVictoria(ventana, fondo):
    ventana.blit(fondo,(0,0))
def dibujarSuministros(ventana, supplies):
    ventana.blit(supplies,(600,300))
def dibujarNave(ventana,naveImg,x,y):
    ventana.blit(naveImg,(x,y))
def dibujarVida(ventana, vida, x,y):
    ventana.blit(vida, (x,y))
def probarColisionNave(spriteBala,x):
    xBala = spriteBala.rect.left
    if xBala <= x and xBala >= 0:
        print("La bala le dio a la nave")
        return True
def dibujarBalaEnemigox(ventana ,spriteBala):
    if spriteBala.rect.left != 900:
        ventana.blit(spriteBala.image, spriteBala.rect)
        spriteBala.rect.left -= 10
        if spriteBala.rect.left < 0:
            spriteBala.rect.left = 900


""""-----------------------------------------------------------------------------------------------------------------"""
# Estructura básica de un programa que usa pygame para dibujar






def dibujar():
    """En este espacio se nombrá a las variables globales que serán modificadas en algúm momento"""
    global xJugador, yJugador, xEnemigo4,yEnemigo4, vidaJugador, vidaNave1, vidaNave2, xEnemigo5,yEnemigo5, xHunter1,yHunter1,xHunter2,yHunter2
    gruntsMuertos = 2
    vidaHunter1 = 5
    vidaHunter2 = 5
    victoria = 0
    victoria2 = 0

    """--------------------------------------------------------------------------------------------------------------"""
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    """-----------------------------------------------------------------------------------------------------------------
    IMAGENES
    Aqui se incluyen todas las imágenes que se usarán para el proyecto (fondo,personajes,botones, etc
    Para incluir una imagen se escribe asi -> nombreimagen = pygame.image.load(#Imagen.jpg#)"""
    personajeImg = pygame.image.load("personajeEditado.png")
    buttonPlay = pygame.image.load("button_play200x55.jpg")
    buttonMenu = pygame.image.load("button_menu200x55.jpg")
    fondo = pygame.image.load("playa.png")
    enemigoImg = pygame.image.load("grunteditado.png")
    fondoMenu = pygame.image.load("fondoMenu800x600.jpg")
    balaImg = pygame.image.load("bala20x15.png")
    balaEne = pygame.image.load("bala20x15enemigo.png")
    fondoDerrota = pygame.image.load("perdiste800x600.jpg")
    fondoVictoria = pygame.image.load("fondoVictoria800x600.jpg")
    fondoEscena2 = pygame.image.load("escenario 2.jpg")
    supplies = pygame.image.load("supplies.png")
    escenario3 = pygame.image.load("escenario3.png")
    escenario4 = pygame.image.load("escenario4.png")
    personajeArmadura = pygame.image.load("personajeConArmadura.png")
    naveImg = pygame.image.load("nave.png")
    vida1 = pygame.image.load("vida1.png")
    vida2 = pygame.image.load("vida2.png")
    vida3 = pygame.image.load("vida3.png")
    vida4 = pygame.image.load("vida4.png")
    vida5 = pygame.image.load("vida5.png")
    hunter = pygame.image.load("hunter.png")
    buttonInstrucciones = pygame.image.load("button_instrucciones.png")
    instrucciones = pygame.image.load("instrucciones.png")

    vidaNave100 = pygame.image.load("vidaNave100.png")
    vidaNave90 = pygame.image.load("vidaNave90.png")
    vidaNave80 = pygame.image.load("vidaNave80.png")
    vidaNave70 = pygame.image.load("vidaNave70.png")
    vidaNave60 = pygame.image.load("vidaNave60.png")
    vidaNave50 = pygame.image.load("vidaNave50.png")
    vidaNave40 = pygame.image.load("vidaNave40.png")
    vidaNave30 = pygame.image.load("vidaNave30.png")
    vidaNave20 = pygame.image.load("vidaNave20.png")
    vidaNave10 = pygame.image.load("vidaNave10.png")


    """--------------------------------------------------------------------------------------------------------------"""
    """-----------------------------------------------------------------------------------------------------------------
    ESTADOS 
    Se usan para cargar los diferentes escenarios del juego. (Menu, Pausa, Ajustes, etc.)                    """
    xMouse = -1
    yMouse = -1
    estado = 1
    """-----------------------------------------------------------------------------------------------------------------
    Sprites"""
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = balaImg
    spriteBala.rect = balaImg.get_rect()
    spriteBala.rect.left = -1
    spriteBala.rect.top = -1

    spriteBala2 = pygame.sprite.Sprite()
    spriteBala2.image = balaEne
    spriteBala2.rect = balaEne.get_rect()
    spriteBala2.rect.left = -1
    spriteBala2.rect.top = -1

    spriteBala3 = pygame.sprite.Sprite()
    spriteBala3.image = balaEne
    spriteBala3.rect = balaEne.get_rect()
    spriteBala3.rect.left = -1
    spriteBala3.rect.top = -1

    spriteBala4 = pygame.sprite.Sprite()
    spriteBala4.image = balaEne
    spriteBala4.rect = balaEne.get_rect()
    spriteBala4.rect.left = -1
    spriteBala4.rect.top = -1

    spriteBala5 = pygame.sprite.Sprite()
    spriteBala5.image = balaEne
    spriteBala5.rect = balaEne.get_rect()
    spriteBala5.rect.left = -1
    spriteBala5.rect.top = -1

    spriteBala6 = pygame.sprite.Sprite()
    spriteBala6.image = balaEne
    spriteBala6.rect = balaEne.get_rect()
    spriteBala6.rect.left = -1
    spriteBala6.rect.top = -1

    """-----------------------------------------------------------------------------------------------------------------
    Sonidos"""
    pygame.mixer.init()
    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    efectoDisparoEnemigo = pygame.mixer.Sound("chargefire.wav")
    efectoMuerteEnemigo = pygame.mixer.Sound("dth5.wav")
    musicaFondo = pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)  # Cuando acabe vuelve a iniciar

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        """-------------------------------------------------------------------------------------------------------------
        Los eventos que van aquí son en caso de que el jugador apriete x botón. Ej. El jugador aprieta space y el 
        personaje salta"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse,yMouse = pygame.mouse.get_pos()
                if xMouse >= 550 and xMouse <=750 and yMouse>= 500 and yMouse<= 555:
                    xMouse = -1
                    yMouse = -1
                    #Cambiar el estado a menu
                    estado = 10
                elif xMouse >= 50 and xMouse <= 250 and yMouse >= 500 and yMouse<= 555:
                    xMouse = -1
                    yMouse = -1
                    #Cambiar el estado a menu
                    estado = 1
                elif xMouse >= 550 and xMouse <= 750 and yMouse >= 400 and yMouse<=454:
                    estado = 8
                    """Aquí van los movimientos del jugador"""
            elif evento.type == pygame.KEYDOWN:
                """Verificar que tecla se pulso"""
                if (evento.key == pygame.K_s) or (evento.key == pygame.K_DOWN):
                    yJugador += 17
                    print(yJugador)
                elif (evento.key == pygame.K_w) or (evento.key == pygame.K_UP):
                    yJugador -= 17
                    print(yJugador)
                elif (evento.key == pygame.K_d) or (evento.key == pygame.K_RIGHT):
                    xJugador += 17
                    print(xJugador)
                elif (evento.key == pygame.K_a) or (evento.key == pygame.K_LEFT):
                    xJugador -= 17
                    print(xJugador)
                elif (evento.key == pygame.K_SPACE):
                    if (spriteBala.rect.left == -1) or (spriteBala4.rect.left == -1):
                        spriteBala.rect.left = xJugador +100
                        spriteBala.rect.top = yJugador + 50
                        efectoDisparo.play()
                        spriteBala4.rect.left = xJugador +150
                        spriteBala4.rect.top = yJugador +30


                elif (evento.key == pygame.K_KP_ENTER):
                    print("Ultimo nivel")
                    estado = 6








        """----------------------------------------------------------------------------------------------------------"""
        # Borrar pantalla
        ventana.fill(NEGRO)
        """-------------------------------------------------------------------------------------------------------------
        Aqui se nombra a todas las funciones que llamará el juego"""

        """----------------------------------------------------------------------------------------------------------"""
        """-------------------------------------------------------------------------------------------------------------
        ESTRUCTURA IF
        Aqui se usa la variable 'estado' para cargar la pantalla de carga, la pantalla de pausa o la pantalla de juego"""
        if estado == 1:
            dibujarMenu(ventana, buttonPlay, fondoMenu,buttonInstrucciones)
        elif estado == 10:
            global enemigosMuertos
            global xEnemigo, yEnemigo, xEnemigo2, yEnemigo2
            if spriteBala2.rect.left == 900:
                if (yEnemigo == yJugador) or (yEnemigo+20 == yJugador+20):
                    spriteBala2.rect.left = xEnemigo -20
                    spriteBala2.rect.top = yEnemigo +30
                    efectoDisparoEnemigo.play()
            if spriteBala3.rect.left == 900:
                spriteBala3.rect.left = xEnemigo2 -20
                spriteBala3.rect.top = yEnemigo2 +30

            dibujarFondo(ventana, fondo)
            dibujarPersonaje(ventana, personajeImg)
            dibujarEnemigo(ventana,enemigoImg )
            dibujarBala(ventana, spriteBala)
            if probarColision(spriteBala,xEnemigo,yEnemigo) == True:
                efectoMuerteEnemigo.play()
                xEnemigo = -100
                yEnemigo = -100
                enemigosMuertos += 1
            if probarColision(spriteBala,xEnemigo2,yEnemigo2) == True:
                efectoMuerteEnemigo.play()
                xEnemigo2 = -100
                yEnemigo2 = -100
                enemigosMuertos += 1
            dibujarBalaEnemigo(ventana, spriteBala2)
            dibujarEnemigo2(ventana, enemigoImg)
            dibujarBalaEnemigo2(ventana, spriteBala3)
            x = probarColisionJugador(spriteBala2)
            y = probarColisionJugador(spriteBala3)
            if (x == True) or (y == True):
                estado = 3
            elif enemigosMuertos == 2:
                estado = 4
                print("Siguiente pantalla")

        elif estado == 3:
            dibujarDerrotaOVictoria(ventana, fondoDerrota)
            xJugador = ANCHO // 2
            yJugador = ALTO // 2
        elif estado == 4:
            """Escena 2"""
            dibujarFondo(ventana, fondoEscena2)
            dibujarPersonaje(ventana, personajeImg)
            dibujarSuministros(ventana, supplies)
            if xJugador >= 520 and xJugador <= 670 and yJugador >= 210 and yJugador <= 360:
                estado = 5
        elif estado == 5:
            dibujarFondo(ventana,escenario3)
        elif estado == 6:
            dibujarFondo(ventana, escenario4)
            dibujarPersonaje(ventana,personajeArmadura)
            dibujarNave(ventana,naveImg,-150,50)
            dibujarNave(ventana, naveImg, -150, 350)
            dibujarBala(ventana,spriteBala4)
            dibujarEnemigo3(ventana, enemigoImg)
            dibujarBalaEnemigo2(ventana, spriteBala5)
            if vidaJugador >= 5:
                dibujarVida(ventana, vida5,20,20)
            elif vidaJugador == 4:
                dibujarVida(ventana, vida4,20,20)
            elif vidaJugador == 3:
                dibujarVida(ventana, vida3,20,20)
            elif vidaJugador == 2:
                dibujarVida(ventana, vida2,20,20)
            elif vidaJugador == 1:
                dibujarVida(ventana, vida1,20,20)

            if vidaNave1 == 20 or vidaNave1 == 19:
                dibujarVida(ventana,vidaNave100,10,60 )
            elif vidaNave1 == 18 or vidaNave1 == 17:
                dibujarVida(ventana,vidaNave90,10,60 )
            elif vidaNave1 == 16 or vidaNave1 == 15:
                dibujarVida(ventana,vidaNave80,10,60 )
            elif vidaNave1 == 14 or vidaNave1 == 13:
                dibujarVida(ventana,vidaNave70,10,60 )
            elif vidaNave1 == 12 or vidaNave1 == 11:
                dibujarVida(ventana,vidaNave60,10,60 )
            elif vidaNave1 == 10 or vidaNave1 == 9:
                dibujarVida(ventana,vidaNave50,10,60 )
            elif vidaNave1 == 8 or vidaNave1 == 7:
                dibujarVida(ventana,vidaNave40,10,60 )
            elif vidaNave1 == 6 or vidaNave1 == 5:
                dibujarVida(ventana,vidaNave30,10,60 )
            elif vidaNave1 == 4 or vidaNave1 == 3:
                dibujarVida(ventana,vidaNave20,10,60 )
            elif vidaNave1 == 2 or vidaNave1 == 1:
                dibujarVida(ventana,vidaNave10,10,60 )

            if vidaNave2 == 20 or vidaNave2 == 19:
                dibujarVida(ventana,vidaNave100,10,350 )
            elif vidaNave2 == 18 or vidaNave2 == 17:
                dibujarVida(ventana,vidaNave90,10,350 )
            elif vidaNave2 == 16 or vidaNave2 == 15:
                dibujarVida(ventana,vidaNave80,10,350 )
            elif vidaNave2 == 14 or vidaNave2 == 13:
                dibujarVida(ventana,vidaNave70,10,350 )
            elif vidaNave2 == 12 or vidaNave2 == 11:
                dibujarVida(ventana,vidaNave60,10,350 )
            elif vidaNave2 == 10 or vidaNave2 == 9:
                dibujarVida(ventana,vidaNave50,10,350 )
            elif vidaNave2 == 8 or vidaNave2 == 7:
                dibujarVida(ventana,vidaNave40,10,350 )
            elif vidaNave2== 6 or vidaNave2 == 5:
                dibujarVida(ventana,vidaNave30,10,350 )
            elif vidaNave2 == 4 or vidaNave2 == 3:
                dibujarVida(ventana,vidaNave20,10,350 )
            elif vidaNave2 == 2 or vidaNave2 == 1:
                dibujarVida(ventana,vidaNave10,10,350 )



            if spriteBala5.rect.left == 900:
                spriteBala5.rect.left = xEnemigo4 -20
                spriteBala5.rect.top = yEnemigo4 +50

            dibujarEnemigox(ventana, enemigoImg, xEnemigo5, yEnemigo5)
            dibujarBalaEnemigox(ventana, spriteBala6)
            if spriteBala6.rect.left == 900:
                spriteBala6.rect.left = xEnemigo5 -20
                spriteBala6.rect.top = yEnemigo5 +50

            if probarColision(spriteBala4,xEnemigo4,yEnemigo4) == True:
                efectoMuerteEnemigo.play()
                xEnemigo4 = -100
                yEnemigo4 = -100
                gruntsMuertos -=1
                spriteBala4.rect.left = 900

            if probarColision(spriteBala4,650,100) == True:
                efectoMuerteEnemigo.play()
                xEnemigo5 = -100
                yEnemigo5 = -100
                gruntsMuertos -=1
                spriteBala4.rect.left = 900

                """---------------------------------------------------------------------------------------------------------------------
                parte2"""
            if gruntsMuertos == 0:
                dibujarEnemigoH(ventana, hunter, xHunter1, yHunter1)
                dibujarEnemigoH2(ventana, hunter, xHunter2, yHunter2)
            if probarColision(spriteBala4, xHunter1, yHunter1) == True:
                spriteBala4.rect.left = 900
                vidaHunter1 -= 1
                print("La vida restante es",vidaHunter1)
            if probarColision(spriteBala4, xHunter2, yHunter2) == True:
                spriteBala4.rect.left = 900
                vidaHunter2 -= 1
                print("La vida restante es",vidaHunter2)
            if xHunter1 <= 145 and xHunter1 > 0:
                vidaNave1 -= 10
            if xHunter2 <= 145 and xHunter2 > 0:
                vidaNave2 -= 10
            if vidaHunter1 == 0:
                xHunter1 = -100
                yHunter1 = -100
                victoria = 1
                print("El hunter murio")
            if vidaHunter2 == 0:
                xHunter2 = -100
                yHunter2 = -100
                victoria2 = 1
                print("print el hunter murio")

            if probarColisionJugador(spriteBala5) == True:
                spriteBala5.rect.left = -20
                vidaJugador -= 1
                print(vidaJugador)
            if probarColisionJugador(spriteBala6) == True:
                spriteBala6.rect.left = -20
                vidaJugador -= 1
                print(vidaJugador)
            if probarColisionNave(spriteBala5,145)== True:
                vidaNave2 -= 1
                spriteBala5.rect.left = -20
            if probarColisionNave(spriteBala6,145)==True:
                vidaNave1 -= 1
                print(vidaNave1)
                spriteBala6.rect.left = -20

            if (vidaJugador <= 0) or (vidaNave1 <= 0) or (vidaNave2 <= 0):
                estado = 3
            if victoria == 1 and victoria2 == 1 :
                estado = 7
        elif estado == 7:
            dibujarDerrotaOVictoria(ventana, fondoVictoria)
            xJugador = ANCHO // 2
            yJugador = ALTO // 2
        elif estado == 8:
            dibujarDerrotaOaVictoria(ventana, instrucciones, buttonMenu)
            xJugador = ANCHO // 2
            yJugador = ALTO // 2

        """----------------------------------------------------------------------------------------------------------"""
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()