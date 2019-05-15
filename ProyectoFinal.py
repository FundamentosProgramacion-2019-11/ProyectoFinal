#Autor: Marianela Contreras D.
# Videojuego Final. Explorador que sube a la colina

import math
import random
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO =800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
AMARILLO= (255,255,0)
NEGRO = (0,0,0)

#VARIABLES GLOBALES
xMonito = ANCHO //2 +150
yMonito = 30
DX= +6 # + derecha, - izquierda (como tiene + empieza moviendose a la derecha)
angulo =  0 #Movimiento senoidal
contadorVidas= 5 #empezamos con 5 vidas

# Estructura básica de un programa que usa pygame para dibujar

#dibuja el menú (botones)
def dibujarMenu(ventana, btnJugar):
    ventana.blit(btnJugar,(300,275))


#dibuja fondo del juego
def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego,(0,0))


#dibuja fondo de cuando se pierde el juego
def dibujarPerdiste(ventana,fondoGameOver):
    ventana.blit(fondoGameOver, (0, 0))


#dibuja fondo de cuando se gana el juego
def dibujarGanaste(ventana,fondoWinner,fuente):
    ventana.blit(fondoWinner, (0, 0))


#dibuja explorador1
def dibujarExplorador(ventana, imgExplorador, xExplorador, yExplorador):
    ventana.blit(imgExplorador,(xExplorador,yExplorador))


#dibuja explorador 2
def dibujarExplorador2(ventana, imgExplorador2,xExplorador2,yExplorador2):
    ventana.blit(imgExplorador2,(xExplorador2,yExplorador2))


#dibuja el dibujo de la Meta
def dibujarMeta(ventana,spriteMeta):
    ventana.blit(spriteMeta.image,spriteMeta.rect)


#dibuja al monito con sus coordenadas
def dibujarMonito(ventana,spriteMonito):
    global DX, angulo #avisar que xEnemigo es variable global y la vamos a modificar, igual con las demás
    ventana.blit(spriteMonito.image,spriteMonito.rect)
    #Actualizar coordenadas del enemigo
    spriteMonito.rect.left += DX #DELTA X (esta moviendo + 10)
    if spriteMonito.rect.left + 128 >= ANCHO -10 or spriteMonito.rect.left <= 20: #DEBEMOS SUMAR EL ANCHO DE LA IMAGEN PARA EVITAR QUE SE SALGA
        DX = -DX

    #Movimiento vertical   #en lugar de 100, se podría utilizar Alto/2 y así
    dy = int(100*math.sin(math.radians(angulo))) +130 #utiliza radianes, pasar angulo a radianes (el valor va a ser -20+20=0, ya no se sale de la parte superior)
    spriteMonito.rect.top = dy
    angulo += 0


#dibuja la manzana que lanza el explorador
def dibujarManzana(ventana, spriteManzana):
    if spriteManzana.rect.left != -1:
        ventana.blit(spriteManzana.image,spriteManzana.rect)
        #Actualizar manzana (subirla)
        spriteManzana.rect.top -=20   #esta es la y en sprite
        if spriteManzana.rect.top< -43:
            spriteManzana.rect.left = -1  #No se dibuja


#checamos colisiones de las manzanas con el monito
def verificarColisionesManzanaMonito(spriteMonito,spriteManzana, listaManzanas):
    for manzana in listaManzanas:
        if spriteMonito.rect.colliderect(manzana):
            global contadorVidas
            contadorVidas += 1
            listaManzanas.remove(manzana)


#checamos colisiones de las bananas con explorador
def verificarColisionesBananaExplorador(spriteBanana,spriteExplorador,listaBananas):
    for banana in listaBananas:
        if spriteExplorador.rect.colliderect(banana):
            global contadorVidas
            contadorVidas -= 1 #si choca le quitamos una vida
            listaBananas.remove(banana)


#checamos colisiones de las bombas con el explorador2
def verificarColisionesBombaExplorador2(spriteBomba,spriteExplorador2,listaBombas):
    for bomba in listaBombas:
        if spriteExplorador2.rect.colliderect(bomba):
            global contadorVidas
            contadorVidas -=2 #si chocan le quitamos 2 vidas
            listaBombas.remove(bomba)


#checa que el explorador1 llegue a la meta
def verificarColisionMetaExplorador(spriteExplorador,spriteMeta):
    col = pygame.sprite.collide_rect(spriteExplorador, spriteMeta)
    if col == True:
        resultado = True
    else:
        resultado = False
    return resultado


#checa que el explorador2 llegue a la meta
def verificarColisionMetaExplorador2(spriteExplorador2,spriteMeta):
    col = pygame.sprite.collide_rect(spriteExplorador2, spriteMeta)
    if col == True:
        resultado = True
    else:
        resultado = False
    return resultado


#dibuja el marcador del tiempo
def dibujarMarcador(ventana, fuente, puntos):
    texto = fuente.render("Tiempo: " + str(puntos),1,AZUL)
    ventana.blit(texto,(20,50))


#dibuja el título en el menú
def dibujarTítulo(ventana,fuente,título):
    texto = fuente.render("CLIMB ",1, BLANCO)
    ventana.blit(texto,(300,50))


#dibuja el record en el menú
def dibujarRecord (ventana,fuente,record):
    entrada = open("JuegoFinal","r")
    contenido = entrada.read()
    listaRecord = contenido.split()
    texto = fuente.render("Mejor Explorador: " + listaRecord[0], 1, AMARILLO)
    ventana.blit(texto, (50, 100))
    texto = fuente.render ("Tiempo de: " + listaRecord[1], 1, AMARILLO)
    ventana.blit (texto,(50, 165))
    texto = fuente.render ("¿Puedes superarlo? ",1,BLANCO)
    ventana.blit (texto,(150,210))
    entrada.close()


#dibuja las vidas en los niveles
def dibujarVidas(ventana,fuente,vida):
    texto = fuente.render("Vidas:"+str(contadorVidas), 1, ROJO)
    ventana.blit(texto,(20,87))


#letrero de Nivel 1
def dibujarNivel(ventana,fuente,nivel):
    texto = fuente.render("NIVEL 1 ", 1, ROJO)
    ventana.blit(texto, (20, 13))


#letrero de Nivel2
def dibujarNivel2(ventana,fuente,nivel2):
    texto = fuente.render("NIVEL 2:",1,ROJO)
    ventana.blit (texto,(20,13))


#crea el sprite Explorador
def crearExplorador (imgExplorador,xExplorador,yExplorador):
    spriteExplorador = pygame.sprite.Sprite()
    spriteExplorador.image = imgExplorador
    spriteExplorador.rect = imgExplorador.get.rect()
    spriteExplorador.rect.top = yExplorador
    spriteExplorador.rect.left = xExplorador


#crea sprite Explorador 2
def crearExplorador2 (imgExplorador2,xExplorador2,yExplorador2):
    spriteExplorador2 = pygame.sprite.Sprite()
    spriteExplorador2.image = imgExplorador2
    spriteExplorador2.rect = imgExplorador2.get.rect()
    spriteExplorador2.rect.top = yExplorador2
    spriteExplorador2.rect.left = xExplorador2


#crea sprite del Monito
def crearMonito (imgMonito,xMonito,yMonito):
    spriteMonito = pygame.sprite.Sprite()
    spriteMonito.image = imgMonito
    spriteMonito.rect = imgMonito.get.rect()
    spriteMonito.rect.top = yMonito
    spriteMonito.rect.left = xMonito


#crea sprite de Manzana
def crearManzana(imgManzana, listaManzanas, xExplorador,yExplorador):
    spriteManzana = pygame.sprite.Sprite()
    spriteManzana.image = imgManzana
    spriteManzana.rect = imgManzana.get_rect()
    spriteManzana.rect.left = xExplorador+64-16
    spriteManzana.rect.top=yExplorador
    listaManzanas.append(spriteManzana)


#crea sprite de Banana
def crearBanana(imgBanana, listaBananas,spriteMonito):
    spriteBananas = pygame.sprite.Sprite()
    spriteBananas.image = imgBanana
    spriteBananas.rect = imgBanana.get_rect()
    spriteBananas.rect.left = spriteMonito.rect.left
    spriteBananas.rect.top = spriteMonito.rect.top
    listaBananas.append(spriteBananas)


#crea sprite de Bombas
def crearBombas(imgBomba, listaBombas,spriteMonito):
    spriteBomba = pygame.sprite.Sprite()
    spriteBomba.image = imgBomba
    spriteBomba.rect = imgBomba.get_rect()
    spriteBomba.rect.left = spriteMonito.rect.left
    spriteBomba.rect.top = spriteMonito.rect.top
    listaBombas.append(spriteBomba)


# función que hace que las bananas caigan
def moverBananas(listaBananas):
    for banana in listaBananas:
        banana.rect.top += 16   #velocidad de como caen, es + para que vaya hacia abajo


#función que hace que las bombas caigan
def moverBombas(listaBombas):
    for bomba in listaBombas:
        bomba.rect.top += 10


#función que mueve las manzanas hacia arriba
def moverManzanas(listaManzanas):
    for manzana in listaManzanas:
        manzana.rect.top -= 16


#dibujamos la lista de manzanas
def dibujarListaManzanas(ventana,listaManzanas):
    for manzana in listaManzanas:
        ventana.blit(manzana.image,manzana.rect) #para tener muchas manzanas en la misma pantalla


#dibujamos lista de bananas
def dibujarListaBananas(ventana,listaBananas):
    for banana in listaBananas:
        ventana.blit(banana.image,banana.rect) #para tener muchas bananas en la misma pantalla


#dibujamos lista de bombas
def dibujarListaBomas(ventana,listaBombas):
    for bomba in listaBombas:
        ventana.blit(bomba.image,bomba.rect) #para tener muchas bombas en la misma pantalla


#función principal del programa y la que correrá
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    #IMAGENES
    btnJugar = pygame.image.load("button_jugar.png")
    fondoJuego= pygame.image.load("colina2.jpg")
    imgBanana= pygame.image.load("banana.png")
    imgExplorador = pygame.image.load ("explorador.png")
    imgExplorador2 = pygame.image.load("explorador.png")
    imgMonito = pygame.image.load ("monito.png")
    imgMeta = pygame.image.load ("banderaMeta.png")
    imgBomba = pygame.image.load ("bomba.png")
    fondoWinner = pygame.image.load("Winner.jpg")
    fondoGameOver = pygame.image.load ("GAME OVER.jpg")


    # sprites
    imgBanana = pygame.image.load("banana.png")
    imgManzana = pygame.image.load ("apple.png")
    spriteManzana = pygame.sprite.Sprite()
    spriteManzana.image = imgManzana #relación de la imagen con sprite
    spriteManzana.rect = imgManzana.get_rect() #obtiene las coordenadas de la imagen y lo asigna a rect
    spriteManzana.rect.left = -1 #indicador para que NO se dibuje

    spriteBanana = pygame.sprite.Sprite()
    spriteBanana.image = imgBanana  # relación de la imagen con sprite
    spriteBanana.rect = imgBanana.get_rect()  # obtiene las coordenadas de la imagen y lo asigna a rect
    spriteBanana.rect.left = -1  # indicador para que NO se dibuje

    spriteBomba = pygame.sprite.Sprite()
    spriteBomba.image = imgBomba  # relación de la imagen con sprite
    spriteBomba.rect = imgBomba.get_rect()  # obtiene las coordenadas de la imagen y lo asigna a rect
    spriteBomba.rect.left = -1  # indicador para que NO se dibuje

    spriteMonito = pygame.sprite.Sprite()
    spriteMonito.image = imgMonito
    spriteMonito.rect = imgMonito.get_rect()
    spriteMonito.rect.left = ANCHO//2
    spriteMonito.rect.top= 0


    spriteExplorador = pygame.sprite.Sprite()
    spriteExplorador.image = imgExplorador
    spriteExplorador.rect = imgExplorador.get_rect()
    spriteExplorador.rect.left = ANCHO/2 -170
    spriteExplorador.rect.top = ALTO - 90

    spriteExplorador2 = pygame.sprite.Sprite()
    spriteExplorador2.image = imgExplorador2
    spriteExplorador2.rect = imgExplorador2.get_rect()
    spriteExplorador2.rect.left = ANCHO / 2 - 170
    spriteExplorador2.rect.top = ALTO - 90

    spriteMeta = pygame.sprite.Sprite()
    spriteMeta.image = imgMeta
    spriteMeta.rect = imgMeta.get_rect()
    spriteMeta.rect.top = 180
    spriteMeta.rect.left = ANCHO//2



    #COORDENADAS MOUSE
    xMouse = -1
    yMouse = -1

    #COORDENADAS EXPLORADORES
    xExplorador= ANCHO/2 -170   #izquierda
    yExplorador= ALTO - 90   #arriba
    xExplorador2 = ANCHO / 2 - 170  # izquierda
    yExplorador2 = ALTO - 90

    #COORDENADAS META
    xMeta= ANCHO//2
    yMeta = 10


    #ESTADOS
    MENU = 0
    NIVEL1 = 1
    NIVEL2 = 2
    GANAR = 3
    PERDER = 4
    estado = MENU #Al inicio, muestra el menú


    #AUDIO (SONIDO)
    pygame.mixer.init()
    #SONIDO corto Sound --wav
    efectoDisparo = pygame.mixer.Sound ("disparo.wav")#carga un sonido
    #Sonido largo Music --mp3
    pygame.mixer.music.load("background.mp3") #solo carga el audio, es otro modulo porque es mp3, solo se puede cargar 1
    pygame.mixer.music.play()  #ponerle -1 es automaticamente se reproduce de nuevo


    #TEXTO
    fuente = pygame.font.SysFont("Arial",72)
    título = []
    record = []
    nivel = []
    vida = []
    nivel2 =[]


    #tiempo
    tiempo = 0 #NO ES GLOBAL


    #LISTAS
    listaManzanas = []  #lista vacía
    listaBananas = []
    listaBombas= []


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONDOWN:  #usuario oprime boton y juega
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >=300 and xMouse <= 500 and yMouse >=275 and yMouse<=325:
                    xMouse= -1
                    #CAMBIA EL ESTADO
                    estado = NIVEL1 #Pasa a jugar
            elif evento.type ==pygame.KEYDOWN and (estado == NIVEL1 or estado == NIVEL2):#Tecla oprimida
                if evento.key== pygame.K_RIGHT :
                    if estado == NIVEL1:
                        xExplorador += 10 #agregas pixeles a la coordenada de la nave
                        spriteExplorador.rect.left += 10
                    elif estado == NIVEL2:
                        xExplorador2 += 10  # agregas pixeles a la coordenada de la nave
                        spriteExplorador2.rect.left += 10
                elif evento.key == pygame.K_LEFT:
                    if estado == NIVEL1:
                        xExplorador -= 10
                        spriteExplorador.rect.left -= 10
                    elif estado == NIVEL2:
                        xExplorador2 -= 10
                        spriteExplorador2.rect.left -= 10
                elif evento.key == pygame.K_UP:
                    if estado == NIVEL1:
                        yExplorador -= 10
                        spriteExplorador.rect.top -= 10
                    elif estado == NIVEL2:
                        yExplorador2 -= 10
                        spriteExplorador2.rect.top -= 10
                elif evento.key == pygame. K_DOWN:
                    if estado == NIVEL1:
                        yExplorador += 10
                        spriteExplorador.rect.top += 10
                    elif estado == NIVEL2:
                        yExplorador2 += 10
                        spriteExplorador2.rect.top += 10
                if estado == NIVEL2 and evento.key == pygame.K_SPACE: #si el usuario quiere disparar
                    if len(listaManzanas)<10 :
                        crearManzana(imgManzana, listaManzanas, xExplorador2,yExplorador2)
                        efectoDisparo.play() #aquí ya se reproduce el sonido
                        spriteManzana.rect.left = xExplorador2+64-16 #Proyecto(getWidth...) o sea no podemos poner solo números, debemos poner getWidth
                        spriteManzana.rect.top = yExplorador2


        #Checando las vidas
        if contadorVidas <= 0:
            estado = PERDER #PERDER


        # Borrar pantalla
        ventana.fill(ROJO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == MENU:
            dibujarMenu(ventana,btnJugar)
            dibujarTítulo(ventana,fuente,título)
            dibujarRecord(ventana,fuente,record)
        elif estado == NIVEL1:
            verificarColisionMetaExplorador(spriteExplorador, spriteMeta)
            cb = random.randint(0,500)
            if cb<= 10:
                crearBanana(imgBanana, listaBananas, spriteMonito)
                spriteBanana.rect.left = xMonito + 64 - 16
                spriteBanana.rect.top = yMonito
                moverBananas(listaBananas)

            else:
                moverBananas(listaBananas)

            verificarColisionesBananaExplorador(spriteBanana, spriteExplorador, listaBananas)
            verificarColisionMetaExplorador(spriteExplorador, spriteMeta)

            tiempo +=1
            dibujarFondo(ventana,fondoJuego)
            dibujarExplorador(ventana,imgExplorador,xExplorador,yExplorador)
            dibujarMonito(ventana,spriteMonito)
            dibujarMarcador(ventana,fuente,tiempo)
            dibujarListaBananas(ventana,listaBananas)
            dibujarNivel(ventana,fuente,nivel)
            dibujarVidas(ventana, fuente, vida)
            dibujarMeta(ventana, spriteMeta)
            resultado = verificarColisionMetaExplorador(spriteExplorador, spriteMeta)

            if resultado == True and estado == NIVEL1:
                estado = NIVEL2
                pygame.sprite.Sprite.kill(spriteExplorador)

        elif estado == NIVEL2:
            cb = random.randint(0, 500)
            if cb%50 == 0:
                crearBombas(imgBomba,listaBombas,spriteMonito)
                spriteBomba.rect.left = xMonito + 64 - 16
                spriteBomba.rect.top = yMonito
                moverBombas(listaBombas)
            else:
                moverBombas(listaBombas)
            verificarColisionesManzanaMonito(spriteMonito, spriteManzana, listaManzanas)
            verificarColisionesBombaExplorador2(spriteBomba,spriteExplorador2,listaBombas)
            verificarColisionMetaExplorador2(spriteExplorador2, spriteMeta)


            tiempo += 1
            moverManzanas(listaManzanas)
            dibujarFondo(ventana, fondoJuego)
            dibujarExplorador2(ventana, imgExplorador2,xExplorador2,yExplorador2)  # puntos extra
            dibujarMonito(ventana, spriteMonito)
            dibujarMarcador(ventana, fuente, tiempo)
            dibujarListaManzanas(ventana, listaManzanas)
            dibujarListaBananas(ventana, listaBananas)
            dibujarNivel2(ventana, fuente, nivel2)
            dibujarVidas(ventana, fuente, vida)
            dibujarMeta(ventana, spriteMeta)
            dibujarListaBomas(ventana, listaBombas)
            resultado = verificarColisionMetaExplorador2(spriteExplorador2,spriteMeta)
            if resultado == True and estado == NIVEL2:
                estado = GANAR
                pygame.sprite.Sprite.kill(spriteExplorador2)


        elif estado == PERDER:
            dibujarPerdiste(ventana,fondoGameOver)

        elif estado == GANAR:
            dibujarGanaste(ventana,fondoWinner,fuente)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

        #ARCHIVOS (GUARDANDO RECORD DE TIEMPO)
    entrada = open("JuegoFinal", "r")
    cosa = entrada.read()
    lista = cosa.split()
    bestTime = int(lista[1])
    if tiempo < bestTime and estado == GANAR:
        print("Felicidades, nuevo campeón")
        print("Dame tu nombre para recordarlo")
        bestTime = tiempo
        name = input("Escriba su nombre: ")
        mejorTiempo = str(bestTime)
        entrada = open("JuegoFinal","w",encoding="UTF-8")
        entrada.write(name + " " + mejorTiempo)



    entrada.close()
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()