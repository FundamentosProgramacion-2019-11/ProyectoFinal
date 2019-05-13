

import pygame   # Librería de pygame
from random import randint
import time
pygame.font.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)   # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#Estado
MENU = 1
JUGANDO = 2
PIERDE=4
GANA=3


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos2(ventana, listaEnemigos2):
    for enemigo2 in listaEnemigos2:
        ventana.blit(enemigo2.image, enemigo2.rect)

def moverEnemigos2(listaEnemigos2):
    for enemigos2 in listaEnemigos2:
        enemigos2.rect.left -= 1


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

def moverEnemigos(listaEnemigos):
    for enemigos in listaEnemigos:
        enemigos.rect.left -= 1


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 30



def dibujarMenu(ventana, btnPlay):
    ventana.blit(btnPlay,(300,225)) #medidas btn



def dibujarMarcador(ventana, marcador, fuente):
    texto = fuente.render("Puntos: "+ str(marcador), 1, ROJO)   #antialiasing suaviza orilla, texto ya es imagen
    ventana.blit(texto, (50,50))    #dupla de cordenadas



def verificarColision(listaEnemigos, listaBalas):
    for bala in listaBalas:
        for enemigo in listaEnemigos:   #Recorrer con INDICES
            #bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe = enemigo.rect.left
            ye = enemigo.rect.bottom
            ae = enemigo.rect.width
            alte = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                #Golpeo al enemigo
                listaEnemigos.remove(enemigo)
                break

def checharColisionNave(listaEnemigos2, spritePersonaje, estado):
    destruido = False
    for bala in listaEnemigos2:

        #bala vs enemigo
        xb = bala.rect.left
        yb = bala.rect.bottom
        xe = spritePersonaje.rect.left
        ye = spritePersonaje.rect.bottom
        ae = spritePersonaje.rect.width
        alte = spritePersonaje.rect.height
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            #Golpeo al enemigo
            destruido = True
            break
    return destruido

def dibujar():
    score = 0
    imgGANA = pygame.image.load("imgGANA.jpg")
    imgPIERDE = pygame.image.load("imgPIERDE.jpg")
    fuente = pygame.font.SysFont("monospace", 76)
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    imgPersonaje = pygame.image.load("nave.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO // 2 + spritePersonaje.rect.height // 2



    listaEnemigos2 = []
    imgEnemigo2 = pygame.image.load("enemigo2.png")


    listaEnemigos = []
    imgEnemigo = pygame.image.load("enemigo1.png")



    listaBalas = []
    imgBala = pygame.image.load("bala.png")
    estado = MENU

    #Menú
    imgBtnJugar = pygame.image.load("botonPlay.png")

    #Fondo
    imgFondo = pygame.image.load("fondo.png")

    # Tiempo
    timer = 0 # Acumulador de tiempo
    # Audio
    pygame.mixer.init()
    #pygame.mixer.music.load("shoot.wav")
    #pygame.mixer.music.play(-1)
    efecto = pygame.mixer.Sound("shoot.wav")

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    spritePersonaje.rect.bottom -= 10
                elif evento.key == pygame.K_DOWN:
                    spritePersonaje.rect.bottom += 10
                elif evento.key == pygame.K_z:
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalas.append(spriteBala)
                    print(len(listaBalas))
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos() #valores de dubla
                print(xm, ", ", ym)
                xb = ANCHO//2-128
                yb = ALTO//3
                if xm > xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                    estado = JUGANDO


        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == JUGANDO:



            #Tiempo
            if timer >= 1:
                timer = 0
                # Crear una bala
                efecto.play()
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                spriteBala.rect.bottom = spritePersonaje.rect.bottom
                listaBalas.append(spriteBala)
                # ENEMIGOS1
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
                spriteEnemigo.rect.bottom = randint(0, ALTO)
                listaEnemigos.append(spriteEnemigo)

                ## ENEMIGOS2
                spriteEnemigo2 = pygame.sprite.Sprite()
                spriteEnemigo2.image = imgEnemigo2
                spriteEnemigo2.rect = imgEnemigo2.get_rect()
                spriteEnemigo2.rect.left = randint(0, ANCHO) + ANCHO
                spriteEnemigo2.rect.bottom = randint(0, ALTO)
                listaEnemigos2.append(spriteEnemigo2)

            #Actualizar enemigos
            moverEnemigos(listaEnemigos)
            moverEnemigos2(listaEnemigos2)
            moverBalas(listaBalas)
            verificarColision(listaEnemigos, listaBalas)






            if(checharColisionNave(listaEnemigos2, spritePersonaje, estado) == True):
                estado=PIERDE
            # Dibujar, aquí haces todos los trazos que requieras
            # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
            # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
            ventana.blit(imgFondo, (0, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarEnemigos2(ventana, listaEnemigos2)
            dibujarBalas(ventana, listaBalas)
            tiempo = pygame.time.get_ticks()
            score = tiempo
            if tiempo>120000:
                estado=PIERDE

        elif estado == MENU:
            #Dinujar menú
            dibujarMenu(ventana, imgBtnJugar)

        elif estado == PIERDE:
            ventana.blit(imgPIERDE, (0, 0))

            texto = fuente.render("Score:"+str(score/1000), 4, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 4))


        elif estado == GANA:
            ventana.blit(imgGANA, (0, 0))
            texto = fuente.render("¡GANASTE!", 4, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 4))







        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(60)  # 40 fps
        timer += 1/60

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja

# Llamas a la función principal
main()