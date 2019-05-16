# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame
import Archivos

pygame.init()
pygame.font.init()
# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
font= pygame.font.Font('../Imagenes/Metal.ttf',100)

# Estructura básica de un programa que usa pygame para dibujar
def regis():
    # Inicializa el motor de pygame
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)
        fondo = pygame.image.load("../Imagenes/menu.png")
        fondoMenu = pygame.transform.scale(fondo, [ANCHO, ALTO])
        ventana.blit(fondoMenu, [0, 0])
        tituloM = font.render("Metal", True, ROJO)
        tituloT = font.render("Tec", True, AZUL)
        ventana.blit(tituloM, [ANCHO // 7, 0])
        ventana.blit(tituloT, [4 * ANCHO // 7, 0])
        data= Archivos.enviarRegistros()
        lastmatches= [data[len(data)-4],data[len(data)-3],data[len(data)-2],data[len(data)-1]]
        ventana.blit(font.render(str(lastmatches[0])+"seg",True,BLANCO),[ANCHO//2-100,100])
        ventana.blit(font.render(str(lastmatches[1])+"seg",True,BLANCO),[ANCHO//2-100,200])
        ventana.blit(font.render(str(lastmatches[2])+"seg",True,BLANCO),[ANCHO//2-100,300])
        ventana.blit(font.render(str(lastmatches[3])+"seg",True,BLANCO),[ANCHO//2-100,400])
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

