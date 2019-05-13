#Autor: Luis Alberto Zepeda Hernández A01328616 Grupo 03
#Juego Breaking Bricks


import pygame
import sys
pygame.init()

#Dimensiones Ventana------------
ANCHO = 800
ALTO = 600

#Colores----------------
BLANCO =(255,255,255)
NEGRO =(0,0,0)
ROJO =(255,26,26)
AZUL =(26,219,255)
TURQUESA =(22,222,216)
AMARILLO =(254,238,28)
PURPURA =(166,30,248)
NARANJA =(248,156,30)
VERDE =(39,223,33)
CAFE =(104,85,7)
ROSA =(222,22,152)
LIMA =(190,255,26)
listaColores = [ROJO,AZUL,TURQUESA,AMARILLO,PURPURA,NARANJA,VERDE,CAFE,ROSA,LIMA]

#Imágenes-----------------
fondoMenu = pygame.image.load("tittle.png")
btnJugar = pygame.image.load("btnJugar.png")
btnPuntos = pygame.image.load("btnPuntos.png")
btnCreador = pygame.image.load("btnCreador.png")
fondoJugando = pygame.image.load("FONDO1.png")
btnMenu = pygame.image.load("PAUSE.png")
pelota = pygame.image.load("PELOTA.png")
win = pygame.image.load("WIN.png")
lose = pygame.image.load("LOSE.png")
#Audios----------------------
pygame.mixer.init()
selection = pygame.mixer.Sound("MenuSelect.wav")
ladrillo = pygame.mixer.Sound("BrickBreak.wav")
pygame.mixer.music.load("IntroMusic.mp3")
rebote = pygame.mixer.Sound("rebote.wav")
winSound = pygame.mixer.Sound("WIN.wav")
loseSound = pygame.mixer.Sound("LOSE.wav")
pygame.mixer.music.play(-1)



def dibujarMenu(ventana, fondoMenu):
    ventana.blit(fondoMenu,(100,50))
    ventana.blit(btnJugar,(335,250))
    ventana.blit(btnPuntos,(250,310))
    ventana.blit(btnCreador,(510,585))
def dibujarFondo(ventana, fondoJugando):
    ventana.blit(fondoJugando,(0,0))
def dibujarRegresaMenu(ventana, btnMenu):
    ventana.blit(btnMenu,(740,584))


def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render("Puntos: " + str(marcador), 1,BLANCO)
    ventana.blit(texto,(5,565))


def dibujarWin(ventana):
    ventana.blit(win,(328,309))
    winSound.play()


def dibujarLose(ventana):
    ventana.blit(lose,(317,309))
    loseSound.play()


def dibujar():

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    #MARCADOR
    fuente = pygame.font.SysFont("Arial", 30)  # Convierte los textos en imágenes

    marcador = 0

    #Valores Ladrillos
    target_width = 50
    target_height = 20
    target_size = (target_width, target_height)
    x_offs = 10
    y_offs = 10
    n_rows = 5
    target_color = (166,30,248)
    target_surf_list = []
    target_rect_list = []
    for col_ladrillos in range(int(ANCHO / (target_width + x_offs))):
        for fila_ladrillos in range(n_rows):
            target_surf = pygame.Surface(target_size)
            target_rect = target_surf.get_rect()
            x_location = x_offs + x_offs * col_ladrillos + target_width * col_ladrillos
            y_location = y_offs + y_offs * fila_ladrillos + target_height * fila_ladrillos
            target_rect.x = x_location
            target_rect.y = y_location
            target_surf.fill(target_color)
            target_surf_list.append(target_surf)
            target_rect_list.append(target_rect)

    # Valores Barra-------
    player_width = 100
    player_height = 20
    player_size = (player_width, player_height)
    player_surface = pygame.Surface(player_size)
    player_rect = player_surface.get_rect()
    rect_speed = 15
    player_rect.x = 300
    player_rect.y = ALTO - 50
    player_color = (255, 255, 255)
    player_surface.fill(player_color)

    #Valores Pelota---------
    ball = pygame.image.load("PELOTA.png")
    ball_rect = ball.get_rect()
    ball_rect.y = 400
    ball_speed = [6, 8]



    # ESTADOS DEL JUEGO----------------
    PAUSA = 1
    JUGANDO = 4
    estado = PAUSA

    while not termina:
        for evento in pygame.event.get(): #aqui se tienen todos los eventos como presión de teclas o mouse.
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >=335 and xMouse<=465 and yMouse>=250 and yMouse<=281:
                    # Oprimió el botón de play, CAMBIAR EL ESTADO
                    selection.play()
                    xMouse =-1
                    estado = JUGANDO

        ventana.fill(NEGRO)

        if estado == PAUSA:
            dibujarMenu(ventana,fondoMenu)


        elif estado == JUGANDO:

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()

                if xMouse >=740 and xMouse<=795 and yMouse>=584 and yMouse<=595:
                    # Oprimió el botón de play, CAMBIAR EL ESTADO
                    selection.play()
                    xMouse =-1
                    estado = PAUSA

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_rect = player_rect.move([-rect_speed, 0])
            if keys[pygame.K_RIGHT]:
                player_rect = player_rect.move([rect_speed, 0])

            ball_rect = ball_rect.move(ball_speed)
            if ball_rect.left < 0 or ball_rect.right > ANCHO:
                ball_speed[0] = -ball_speed[0]
                rebote.play()
            if ball_rect.top < 0:
                ball_speed[1] = -ball_speed[1]
                rebote.play()
            if ball_rect.bottom > ALTO:
                ball_speed[1] = -ball_speed[1]
                rebote.play()
                marcador -=100
            if player_rect.colliderect(ball_rect):
                ball_speed[1] = -ball_speed[1]
                rebote.play()

            for idx, x in enumerate(target_rect_list):
                if x.colliderect(ball_rect):
                    del target_rect_list[idx]
                    del target_surf_list[idx]
                    ladrillo.play()
                    marcador += 50
                    ball_speed[1] = -ball_speed[1]



            dibujarFondo(ventana, fondoJugando)
            dibujarRegresaMenu(ventana, btnMenu)
            ventana.blit(player_surface, player_rect)
            ventana.blit(ball, ball_rect)
            dibujarMarcador(ventana, marcador, fuente)
            for x in range(len(target_surf_list)):
                ventana.blit(target_surf_list[x], target_rect_list[x])
            dibujarMarcador(ventana, marcador, fuente)

            if marcador == 1500:
                dibujarWin(ventana)

            elif marcador < -200:
                dibujarLose(ventana)




        pygame.display.flip()
        reloj.tick(50)  # frames

    pygame.quit()


def main():
    dibujar()

main()