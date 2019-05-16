# encoding: UTF-8

# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame
import registros
import Game

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0,0,0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
#Fuentes
pygame.font.init()
font= pygame.font.Font('../Imagenes/Metal.ttf',200)



class Puntero(pygame.Rect):

    def __init__(self):
        pygame.Rect.__init__(self,0,0,2,2)

    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):

    def __init__(self,normal,efecto,x,y):

        self.imagen_normal=normal
        self.imagen_seleccion=efecto
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self, ventana, puntero):

        if puntero.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion

        else:
            self.imagen_actual=self.imagen_normal

        ventana.blit(self.imagen_actual,self.rect)

def musicaBoton(boton):
    if (boton=="Jugar"):
        pygame.mixer.music.load('../Sonidos/inicio.mp3')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('../Sonidos/botones.mp3')
        pygame.mixer.music.play()



# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()

    #sonido menu
    pygame.mixer.music.load('../Sonidos/menu.mp3')
    pygame.mixer.music.play(3)

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará




    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Puntero para botones
    puntero = Puntero()

    # Crear botones
    btnJugar = pygame.image.load('../Imagenes/Menu/jugar.png')
    btnJugar2 = pygame.image.load('../Imagenes/Menu/jugar2.png')
    botonJugar = Boton(btnJugar, btnJugar2, 300, 300)

    btnMarcadores = pygame.image.load('../Imagenes/Menu/marcadores.png')
    btnMarcadores2 = pygame.image.load('../Imagenes/Menu/marcadores2.png')
    botonMarcadores = Boton(btnMarcadores, btnMarcadores2, 300, 400)

    btnSalir = pygame.image.load('../Imagenes/Menu/salir.png')
    btnSalir2 = pygame.image.load('../Imagenes/Menu/salir2.png')
    botonSalir = Boton(btnSalir, btnSalir2, 300, 500)

    # Borrar pantalla
    ventana.fill(BLANCO)
    fondo = pygame.image.load("../Imagenes/menu.png")
    fondoMenu = pygame.transform.scale(fondo, [ANCHO, ALTO])
    ventana.blit(fondoMenu, [0, 0])
    tituloM = font.render("Metal", True, ROJO)
    tituloT = font.render("Tec", True, AZUL)
    ventana.blit(tituloM, [ANCHO // 7, 0])
    ventana.blit(tituloT, [4 * ANCHO // 7, 0])

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            if evento.type ==pygame.MOUSEBUTTONDOWN:
                if puntero.colliderect(botonJugar.rect):
                    musicaBoton("Jugar")
                    Game.dibujarLevel1()
                if puntero.colliderect(botonMarcadores.rect):
                    musicaBoton("Marcadores")
                    registros.regis()
                if puntero.colliderect(botonSalir.rect):
                    musicaBoton("Salir")
                    termina=True



        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

        puntero.update()

        botonJugar.update(ventana, puntero)
        botonMarcadores.update(ventana, puntero)
        botonSalir.update(ventana, puntero)

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()