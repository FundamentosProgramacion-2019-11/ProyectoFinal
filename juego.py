# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame, random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
FONDO = (82, 183, 189)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
x = 0


def instancia():
    if x == 0:
        menu()
    elif x == 1:
        juego()
    elif x == 3:
        puntaje()
    elif x == 4:
        fin()


def fin():
    global x, ganando, perdiendo, puntos, ganar
    if ganando > 0:
        fuente = pygame.font.Font(None, 150)
        texto4 = fuente.render("Correct", 1, BLANCO)
        ventana.blit(texto4, (100, 200))
        ganando -= 1
    elif perdiendo > 0:
        fuente = pygame.font.Font(None, 150)
        texto4 = fuente.render("YOU LOSE", 1, BLANCO)
        ventana.blit(texto4, (100, 200))
        fuente = pygame.font.Font(None, 50)
        texto4 = fuente.render("The Answere is: " + letras[0], 1, BLANCO)
        ventana.blit(texto4, (10, 500))
        perdiendo -= 1
    elif ganando == 0:
        x = 0
        puntos += 1
        ganar = True
        ganando = -1
    elif perdiendo == 0:
        x = 0
        perdiendo = -1


def menu():
    pygame.draw.polygon(ventana, BLANCO, ((355, 255), (355, 345), (445, 300)))
    fuente = pygame.font.Font(None, 70)


def juego():
    for i in range(0, len(palabra)):
        x = ANCHO / 2 - 10 - (30 * (len(palabra) - 1)) + (60 * i)
        pygame.draw.line(ventana, BLANCO,(x, 100), (x + 30, 100))
    for i in range(0, len(respuesta)):
        x = ANCHO / 2 - 10 - (30 * (len(palabra) - 1)) + (60 * i)
        fuente = pygame.font.Font(None, 50)
        texto = fuente.render(respuesta[i][0], 1, BLANCO)
        ventana.blit(texto, (x, 60))
    for i in range(0, len(errores)):
        x = 20 * i
        fuente = pygame.font.Font(None, 50)
        texto = fuente.render(errores[i], 1, BLANCO)
        ventana.blit(texto, (x + 10, ALTO - 50))
    if error >= 1:
        pygame.draw.circle(ventana, BLANCO, (400, 200), 50, 1)
    if error >= 2:
        pygame.draw.line(ventana, BLANCO, (400, 250), (400, 350))
    if error >= 3:
        pygame.draw.line(ventana, BLANCO, (350, 300), (400, 300))
    if error >= 4:
        pygame.draw.line(ventana, BLANCO, (400, 300), (450, 300))
    if error >= 5:
        pygame.draw.line(ventana, BLANCO, (400, 350), (350, 400))



def puntaje():
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render("Max Highscores", 1, BLANCO)
    ventana.blit(texto, (10, 60))
    for i in range(0, len(listpuntaje)):
        y = 100 + (50 * i)
        texto = fuente.render(listpuntaje[i], 1, BLANCO)
        ventana.blit(texto, (20, y))
    pygame.draw.rect(ventana, BLANCO, (630, 550, 160, 40), 1)
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render("Regresar", 1, BLANCO)
    ventana.blit(texto, (635, 555))


pygame.init()   # Inicializa pygame
ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
reloj = pygame.time.Clock() # Para limitar los fps
termina = False # Bandera para saber si termina la ejecución
letras = ""
palabra = []
respuesta = []
nuevaletra = False
letraagregada = ""
palabras = open("lista.txt")
puntajes = open("puntaje.txt")
numpalabras = -1
error = 0
correctas = 0
palabras.seek(0)
ganando = -1
perdiendo = -1
puntajemaximo = 0
ultimopuntaje = 0
puntos = 0
ganar = False
errores = []
listapuntaje = []
palabras.seek(0)
for linea in palabras:
    numpalabras += 1
puntajes.seek(0)
for linea in puntajes:
    cadena = linea.split()
    for i in range(0, len(cadena)):
        listapuntaje.append(cadena[i])
listpuntaje = sorted(listapuntaje, reverse=True)
puntajes.close()

while not termina:
    mousex, mousey = pygame.mouse.get_pos()
    boton_mouse = [0]
    # Procesa los eventos que recibe
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 1:
            boton_mouse[0] = 1

    if x == 0:
        if 350 <= mousex <= 450 and 250 <= mousey <= 350 and boton_mouse[0] == 1 or ganar:
            x = 1
            error = 0
            respuesta.clear()
            palabras.seek(0)
            alto = random.randint(0,numpalabras)
            contador = 0
            correctas = 0
            for linea in palabras:
                if contador == alto:
                    letras = linea.split()
                    break
                contador += 1
            for i in range(0, len(letras[0])):
                palabra.append(letras[0][i])
                respuesta.append(["?"])
            ganar = False
        if 290 <= mousex <= 340 and 275 <= mousey <= 325 and boton_mouse[0] == 1:
            x = 3

    if x == 1:
        if evento.type == pygame.KEYDOWN:
            name = pygame.key.name(evento.key)
            if len(name) == 1:
                agregar = True
                for i in range(0, len(letras)):
                    if name == letras[i]:
                        agregar = False
                if agregar:
                    letras.append(name)
                    nuevaletra = True
                    letraagregada = name

        if nuevaletra:
            for i in range(0, len(palabra)):
                if palabra[i] == letraagregada:
                    correctas += 1
                    nuevaletra = False
                    respuesta[i] = [letraagregada]
                    break
            if nuevaletra:
                error += 1
                errores.append(letraagregada)
                nuevaletra = False

        if len(palabra) == correctas:
            respuesta.clear()
            palabra.clear()
            errores.clear()
            x = 4
            ganando = 40

        if error == 6:
            respuesta.clear()
            errores.clear()
            palabra.clear()
            perdiendo = 40
            for i in range(0, len(listpuntaje)):
                if puntos >= int(listpuntaje[i]):
                    for x in range(i, len(listpuntaje)):
                        listpuntaje[i + 1] = listpuntaje[i]
                    listpuntaje[i] = str(puntos)
                    actualizar = open("puntaje.txt", "w")
                    actualizar.write(listpuntaje[0] + " " + listpuntaje[1] + " " + listpuntaje[2] + " " + listpuntaje[3] + " " + listpuntaje[4] + " " + listpuntaje[5] + " " + listpuntaje[6] + " " + listpuntaje[7] + " " + listpuntaje[8])
                    actualizar.close()
                    break
            x = 4

    if x == 3:
        if mousex >= 630 and mousex <= 790 and mousey >= 550 and mousey <= 590 and boton_mouse[0] == 1:
            x = 0

    # Borrar pantalla
    ventana.fill(FONDO)

    # Dibujar, aquí haces todos los trazos que requieras
    instancia()

    pygame.display.flip()   # Actualiza trazos
    reloj.tick(40)          # 40 fps

pygame.quit()   # termina pygame