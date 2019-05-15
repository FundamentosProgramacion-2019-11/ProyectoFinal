# encoding: UTF-8


import pygame   # Librería de pygam
import Files
import menu
# Inicializa el motor de pygame


pygame.init()
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Radio Pelota
rPelota = 10
# Colores
NEGRO = (0, 0, 0)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
BLANCO= (255,255,255)
pygame.font.init()
letra = pygame.font.Font('game_over.ttf', 250)
# Crea una ventana de ANCHO x ALTO
ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
pygame.display.set_caption("PONG Rafael Romero Bello A01747730")
reloj = pygame.time.Clock()  # Para limitar los fps
puntaje=[]

def player1(posX1, posY1, xraq, yraq):
    pygame.draw.rect(ventana, BLANCO, [posX1, posY1, xraq, yraq])

def player2(posX2, posY2, xraq, yraq):
    pygame.draw.rect(ventana, BLANCO, [posX2,posY2,xraq,yraq])

def pelota(pelx, pely):
    pygame.draw.circle(ventana, BLANCO, [pelx, pely], rPelota)

def Score1(score1):
    texto = letra.render(str(score1), True, BLANCO)
    ventana.blit(texto, [ANCHO/4, 0])

def Score2(score2):
    texto = letra.render(str(score2), True, BLANCO)
    ventana.blit(texto, [(3*ANCHO/4), 0])

# Estructura básica de un programa que usa pygame para dibujar

def dibujar():
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    #puntuaciones
    score1=0
    score2=0
    # Posciones iniciales
    posX1 = 0
    posY1 = ALTO // 2
    posX2 = ANCHO - (15)
    posY2 = ALTO // 2


    # Tamaño Raquetas
    tamaRaquetaX = 15
    tamaRaquetaY = 65

    # Velocidaddes de Jugadores
    velJugador1 = 0
    velJugador2 = 0
    # Posicion pelotas
    pelx = ANCHO // 2
    pely = ALTO // 2

    # Velocidad Pelotas
    velocidadPX = 5
    velocidadPY = 5
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        Teclas = {'W': pygame.K_w, 'S': pygame.K_s, 'Ar': pygame.K_UP, 'Ab': pygame.K_DOWN,'Space':pygame.K_SPACE}
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

            #Deteccion Teclas Movimiento
            if evento.type == pygame.KEYDOWN:
                if evento.key == Teclas['W']:
                    velJugador1= -10
                if evento.key == Teclas['S']:
                    velJugador1= 10
                if evento.key == Teclas['Ar']:
                    velJugador2= -10
                if evento.key == Teclas['Ab']:
                    velJugador2= 10

            if evento.type == pygame.KEYUP:
                if evento.key == Teclas['W']:
                    velJugador1= 0
                if evento.key == Teclas['S']:
                    velJugador1= 0
                if evento.key == Teclas['Ar']:
                    velJugador2= 0
                if evento.key == Teclas['Ab']:
                    velJugador2= 0
                # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        pygame.draw.line(ventana, BLANCO, (ANCHO / 2, ALTO), (ANCHO / 2, 0), 5)
        # Dibujar jugadores

        player1(posX1, posY1, tamaRaquetaX, tamaRaquetaY)
        player2(posX2, posY2, tamaRaquetaX, tamaRaquetaY)
        pelota(pelx, pely)
        Score1(score1)
        Score2(score2)

        posY1 += velJugador1
        posY2 += velJugador2

        pelx += velocidadPX
        pely += velocidadPY


        #Rebotes
        if posY1 < 0:
            posY1 = 0
        if posY1 > ALTO-tamaRaquetaY:
            posY1 = ALTO-tamaRaquetaY

        if posY2 < rPelota:
            posY2 = rPelota

        if posY2 > ALTO-tamaRaquetaY:
            posY2 = ALTO-tamaRaquetaY


        #Colisiones
        if((pelx>= posX1 and pelx<= posX1+tamaRaquetaX)and (pely>=posY1 and pely<=(posY1+tamaRaquetaY-rPelota))):
            velocidadPX=-velocidadPX
            pygame.mixer.music.load('Assets/choque.wav')
            pygame.mixer.music.play()

        if ((pelx >= posX2 and pelx <= posX2 + tamaRaquetaX) and (pely >= posY2 and pely <= (posY2 + tamaRaquetaY-rPelota))):
            velocidadPX = -velocidadPX
            pygame.mixer.music.load('Assets/choque.wav')
            pygame.mixer.music.play()

        if (pely<=0 or pely >= ALTO):
            velocidadPY= -velocidadPY

        #Resetea la pelota al inicio
        if pelx<0:
            pelx = ANCHO // 2
            pely = ALTO // 2
            score1+=1
        if pelx>ANCHO:
            pelx = ANCHO // 2
            pely = ALTO // 2
            score2+=1

        if (score2>=5 or score1>=5):
            velocidadPX = 0
            velocidadPY = 0
            if (len(puntaje)<1):
                puntaje.append(0)
                Files.matchReport(score1,score2)
            texto = letra.render("GAME OVER", True, BLANCO)
            ventana.blit(texto, [ANCHO//2-600//2,300])
            instrucciones = letra.render("Pulse SPACE", True, BLANCO)
            ventana.blit(instrucciones, [50, 400])
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key==Teclas['Space']:

                        menu.main()

                        score1=0
                        score2=0
                        velocidadPX = 5
                        velocidadPY = 5


        pygame.display.flip() # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame
