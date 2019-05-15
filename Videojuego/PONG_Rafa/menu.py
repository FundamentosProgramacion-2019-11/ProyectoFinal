# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame
# Dimensiones de la pantalla



ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO =(0,0,0)
import Game
import matches

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Buton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarM():
    # Inicializa el motor de pygame
    pygame.init()

    pygame.mixer.music.load('Assets/menu.mp3')
    pygame.mixer.music.play(5)
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps

    jugar=pygame.image.load('Assets/jugar.png')
    jugarP = pygame.image.load('Assets/jugarP.png')
    recientes = pygame.image.load('Assets/recientes.png')
    recientesP = pygame.image.load('Assets/recientesP.png')
    salir = pygame.image.load('Assets/salir.png')
    salirP = pygame.image.load('Assets/salirP.png')

    botonJugar=Buton(jugar,jugarP,340,250)
    botonRecientes=Buton(recientes,recientesP,320,350)
    botonSalir=Buton(salir,salirP,340,450)


    cursor1=Cursor()


    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    Pong=pygame.image.load('Assets/BANNER.jpeg')
    ventana.fill(NEGRO)
    ventana.blit(Pong, [ANCHO // 2 - 655 // 2, 0])
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            if evento.type ==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botonJugar.rect):
                    pygame.mixer.music.load('Assets/choque.wav')
                    pygame.mixer.music.play()
                    Game.dibujar()
                if cursor1.colliderect(botonRecientes.rect):
                    matches.match()
                if cursor1.colliderect(botonSalir.rect):
                    pygame.mixer.music.load('Assets/choque.wav')
                    pygame.mixer.music.play()
                    termina=True
                #x,y=evento.pos
                #x,y=pygame.mouse.get_pos()
                #if play.get_rect().collidepoint(x, y):
                #    Game.dibujar()

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps


        cursor1.update()

        botonJugar.update(ventana,cursor1)
        botonRecientes.update(ventana, cursor1)
        botonSalir.update(ventana, cursor1)

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujarM()   # Por ahora, solo dibuja


# Llamas a la función principal
main()