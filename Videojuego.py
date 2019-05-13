# Autor: Mario Hernández Cárdenas
# Proyecto Final: Videojuego sobre carreras

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
ROJO = (208, 0, 0)
AZUL = (2, 79, 178)
NEGRO = (0, 0, 0)

# VARIABLES GLOBALES
sector = 0
velocidad = 1
posicion = 0  # Viendo hacia la derecha
posicionAdv = 0  # Viendo hacia la derecha
distanciaX = 0
distanciaY = 0
seleccion = "nada"
tiempoVuelta = 3200
cuentaRegresivaInicio = 180  # 3 segundos
cuentaRegresivaMeta = 180  # 3 segundos


# Dibujar el menu (botones)
def dibujarMenu(ventana, btnJugar, btnInstrucciones, btnSalir, fuente, fondoLetra):
    posicionImagenX = (ANCHO // 2) - (pygame.Surface.get_width(btnJugar) // 2)
    ventana.blit(btnJugar, (posicionImagenX, ALTO // 2 - pygame.Surface.get_height(btnJugar) // 2))
    ventana.blit(btnInstrucciones, (posicionImagenX, ALTO // 2 + 75 - pygame.Surface.get_height(btnInstrucciones) // 2))
    ventana.blit(btnSalir, (posicionImagenX, ALTO // 2 + 150 - pygame.Surface.get_height(btnSalir) // 2))
    texto = fuente.render("Bit Racing", 1, BLANCO)
    textoFondo = fondoLetra.render("Bit Racing", 1, NEGRO)
    posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2
    ventana.blit(textoFondo, (posicionTitulo + 3, 128))  # Fondo para el texto
    ventana.blit(texto, (posicionTitulo, 125))  # Texto


# Dibuja los botones para interactuar
def dibujarInstrucciones(ventana, btnRegresar):
    ventana.blit(btnRegresar, (550, 525))


# Dibuja los botones para interactuar
def dibujarMapa(ventana, btnContinuar, btnRegresar):
    ventana.blit(btnContinuar, (500, 515))
    ventana.blit(btnRegresar, (100, 515))


# Dibuja los autos para que sean seleccionados
def dibujarAutos(ventana, autoRojo, autoAzul, btnIniciarCarrera, fuente, fondoLetra, seleccion):
    autoRojoEleccion = pygame.transform.rotozoom(autoRojo, 90, 2)
    autoAzulEleccion = pygame.transform.rotozoom(autoAzul, 90, 2)
    ventana.blit(autoRojoEleccion, (133, 185))
    ventana.blit(autoAzulEleccion, (532, 185))
    texto = fuente.render("Selecciona un auto", 1, BLANCO)
    textoFondo = fondoLetra.render("Selecciona un auto", 1, NEGRO)
    posicionTituloX = pygame.Surface.get_width(texto)
    posicionTituloY = pygame.Surface.get_height(texto)
    ventana.blit(textoFondo, ((posicionTituloX + 3) // 3, posicionTituloY + 3))  # Fondo para el texto
    ventana.blit(texto, (posicionTituloX // 3, posicionTituloY))  # Texto
    if seleccion == "rojo" or seleccion == "azul":
        anchoBoton = pygame.Surface.get_width(btnIniciarCarrera)
        ventana.blit(btnIniciarCarrera, (ANCHO // 2 - anchoBoton // 2, 515))


# Dibuja la opción que hizo el usuario
def dibujarSeleccion(ventana, fuente, fondo, seleccion):
    if seleccion == "rojo":
        texto = fuente.render("Haz seleccionado", 1, ROJO)
        texto2 = fuente.render("el AUTO ROJO", 1, ROJO)
        textoFondo = fondo.render("Haz seleccionado", 1, AZUL)
        textoFondo2 = fondo.render("el AUTO ROJO", 1, AZUL)
        ventana.blit(textoFondo, (109, 471))  # Fondo para el texto
        ventana.blit(textoFondo2, (134, 491))
        ventana.blit(texto, (108, 470))  # Texto
        ventana.blit(texto2, (133, 490))

    elif seleccion == "azul":
        texto = fuente.render("Haz seleccionado", 1, AZUL)
        texto2 = fuente.render("el AUTO AZUL", 1, AZUL)
        textoFondo = fondo.render("Haz seleccionado", 1, ROJO)
        textoFondo2 = fondo.render("el AUTO AZUL", 1, ROJO)
        ventana.blit(textoFondo, (508, 471))  # Fondo para el texto
        ventana.blit(textoFondo2, (533, 491))
        ventana.blit(texto, (507, 470))  # Texto
        ventana.blit(texto2, (532, 490))


# Dibuja los fondos de cada pantalla
def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego, (0, 0))


# Dibuja el sector dependiente de la variable global
def dibujarSector(ventana, sector, listaSectores):
    if sector == 0 or sector == 39 or sector == 78 or sector == 117:
        ventana.blit(listaSectores[0], (0, 0))

    elif sector == 1 or sector == 3 or sector == 40 or sector == 42 or sector == 79 or sector == 81:
        ventana.blit(listaSectores[2], (0, 0))

    elif sector == 2 or sector == 41 or sector == 80:
        ventana.blit(listaSectores[1], (0, 0))

    elif sector == 4 or sector == 43 or sector == 82:
        ventana.blit(listaSectores[3], (0, 0))

    elif sector == 5 or sector == 7 or sector == 44 or sector == 46 or sector == 83 or sector == 85:
        ventana.blit(listaSectores[4], (0, 0))

    elif sector == 6 or sector == 8 or sector == 45 or sector == 47 or sector == 84 or sector == 86:
        ventana.blit(listaSectores[5], (0, 0))

    elif sector == 9 or sector == 48 or sector == 87:
        ventana.blit(listaSectores[6], (0, 0))

    elif sector == 10 or sector == 12 or sector == 49 or sector == 51 or sector == 88 or sector == 90:
        ventana.blit(listaSectores[8], (0, 0))

    elif sector == 11 or sector == 50 or sector == 89:
        ventana.blit(listaSectores[7], (0, 0))

    elif sector == 13 or sector == 52 or sector == 91:
        ventana.blit(listaSectores[9], (0, 0))

    elif sector == 14 or sector == 16 or sector == 53 or sector == 55 or sector == 92 or sector == 94:
        ventana.blit(listaSectores[10], (0, 0))

    elif sector == 15 or sector == 17 or sector == 54 or sector == 56 or sector == 93 or sector == 95:
        ventana.blit(listaSectores[11], (0, 0))

    elif sector == 18 or sector == 57 or sector == 96:
        ventana.blit(listaSectores[12], (0, 0))

    elif sector == 19 or sector == 21 or sector == 58 or sector == 60 or sector == 97 or sector == 99:
        ventana.blit(listaSectores[13], (0, 0))

    elif sector == 20 or sector == 22 or sector == 59 or sector == 61 or sector == 98 or sector == 100:
        ventana.blit(listaSectores[14], (0, 0))

    elif sector == 23 or sector == 62 or sector == 101:
        ventana.blit(listaSectores[15], (0, 0))

    elif sector == 24 or sector == 26 or sector == 63 or sector == 65 or sector == 102 or sector == 104:
        ventana.blit(listaSectores[16], (0, 0))

    elif sector == 25 or sector == 27 or sector == 64 or sector == 66 or sector == 103 or sector == 105:
        ventana.blit(listaSectores[17], (0, 0))

    elif sector == 28 or sector == 67 or sector == 106:
        ventana.blit(listaSectores[18], (0, 0))

    elif sector == 29 or sector == 31 or sector == 68 or sector == 70 or sector == 107 or sector == 109:
        ventana.blit(listaSectores[20], (0, 0))

    elif sector == 30 or sector == 32 or sector == 69 or sector == 71 or sector == 108 or sector == 110:
        ventana.blit(listaSectores[19], (0, 0))

    elif sector == 33 or sector == 72 or sector == 111:
        ventana.blit(listaSectores[21], (0, 0))

    elif sector == 34 or sector == 36 or sector == 73 or sector == 75 or sector == 112 or sector == 114:
        ventana.blit(listaSectores[22], (0, 0))

    elif sector == 35 or sector == 37 or sector == 74 or sector == 76 or sector == 113 or sector == 115:
        ventana.blit(listaSectores[23], (0, 0))

    elif sector == 38 or sector == 77 or sector == 116:
        ventana.blit(listaSectores[24], (0, 0))


# Dibuja el auto según la posición elegida por el usuario
def obtenerPosicion(autoElegido, posicion):
    if posicion == 0 or posicion == 8 or posicion == 16 or posicion == 24 or posicion == 32 or posicion == -8:
        return autoElegido
    elif posicion == 1 or posicion == 9 or posicion == 17 or posicion == 25 or posicion == 33 or posicion == -7:
        autoElegido1 = pygame.transform.rotate(autoElegido, -45)
        return autoElegido1
    elif posicion == 2 or posicion == 10 or posicion == 18 or posicion == 26 or posicion == 34 or posicion == -6:
        autoElegido2 = pygame.transform.rotate(autoElegido, -90)
        return autoElegido2
    elif posicion == 3 or posicion == 11 or posicion == 19 or posicion == 27 or posicion == 35 or posicion == -5:
        autoElegido3 = pygame.transform.rotate(autoElegido, -135)
        return autoElegido3
    elif posicion == 4 or posicion == 12 or posicion == 20 or posicion == 28 or posicion == 36 or posicion == -4:
        autoElegido4 = pygame.transform.rotate(autoElegido, -180)
        return autoElegido4
    elif posicion == 5 or posicion == 13 or posicion == 21 or posicion == 29 or posicion == 37 or posicion == -3:
        autoElegido5 = pygame.transform.rotate(autoElegido, -225)
        return autoElegido5
    elif posicion == 6 or posicion == 14 or posicion == 22 or posicion == 30 or posicion == 38 or posicion == -2:
        autoElegido6 = pygame.transform.rotate(autoElegido, -270)
        return autoElegido6
    elif posicion == 7 or posicion == 15 or posicion == 23 or posicion == 31 or posicion == 39 or posicion == -1:
        autoElegido7 = pygame.transform.rotate(autoElegido, -315)
        return autoElegido7


# Le da al programa el sprite del usuario según su elección del color del auto
def obtenerSpriteUsuario(seleccion, autoAzul, autoRojo, posicion):
    spriteUsuario = pygame.sprite.Sprite()
    if seleccion == "azul":
        posicionAutoAzul = obtenerPosicion(autoAzul, posicion)
        spriteUsuario.image = posicionAutoAzul
        spriteUsuario.rect = posicionAutoAzul.get_rect()

    elif seleccion == "rojo":
        posicionAutoRojo = obtenerPosicion(autoRojo, posicion)
        spriteUsuario.image = posicionAutoRojo
        spriteUsuario.rect = posicionAutoRojo.get_rect()

    return spriteUsuario


def obtenerSpriteAdversario(seleccion, autoAzul, autoRojo, posicionAdv):
    spriteAdversario = pygame.sprite.Sprite()
    if seleccion == "azul":
        posicionAutoRojo = obtenerPosicion(autoRojo, posicionAdv)
        spriteAdversario.image = posicionAutoRojo
        spriteAdversario.rect = posicionAutoRojo.get_rect()

    elif seleccion == "rojo":
        posicionAutoAzul = obtenerPosicion(autoAzul, posicionAdv)
        spriteAdversario.image = posicionAutoAzul
        spriteAdversario.rect = posicionAutoAzul.get_rect()

    return spriteAdversario


def dibujarVehiculo(ventana, spriteUsuario, velocidad, movimientoFrente, movimientoIzquierda, movimientoDerecha):
    global x, y
    velocidad1 = 5
    velocidad2 = 10
    velocidad3 = 20

    if posicion == 0 or posicion == 8 or posicion == 16 or posicion == 24 or posicion == 32 or posicion == -8:
        if velocidad == 1:
            if movimientoDerecha:
                y += velocidad1
            elif movimientoIzquierda:
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                y += velocidad1
            elif movimientoIzquierda:
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                y += velocidad1
            elif movimientoIzquierda:
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad3
    elif posicion == 1 or posicion == 9 or posicion == 17 or posicion == 25 or posicion == 33 or posicion == -7:
        if velocidad == 1:
            if movimientoDerecha:
                x -= velocidad1
                y += velocidad1
            elif movimientoIzquierda:
                x += velocidad1
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad1
                y += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                x -= velocidad1
                y += velocidad1
            elif movimientoIzquierda:
                x += velocidad1
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad2
                y += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                x -= velocidad1
                y += velocidad1
            elif movimientoIzquierda:
                x += velocidad1
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad3
                y += velocidad3
    elif posicion == 2 or posicion == 10 or posicion == 18 or posicion == 26 or posicion == 34 or posicion == -6:
        if velocidad == 1:
            if movimientoDerecha:
                x -= velocidad1
            elif movimientoIzquierda:
                x += velocidad1
            elif movimientoFrente:
                y += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                x -= velocidad1
            elif movimientoIzquierda:
                x += velocidad1
            elif movimientoFrente:
                y += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                x -= velocidad1
            elif movimientoIzquierda:
                x += velocidad1
            elif movimientoFrente:
                y += velocidad3
    elif posicion == 3 or posicion == 11 or posicion == 19 or posicion == 27 or posicion == 35 or posicion == -5:
        if velocidad == 1:
            if movimientoDerecha:
                x -= velocidad1
                y -= velocidad1
            elif movimientoIzquierda:
                x += velocidad1
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad1
                y += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                x -= velocidad1
                y -= velocidad1
            elif movimientoIzquierda:
                x += velocidad1
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad2
                y += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                x -= velocidad1
                y -= velocidad1
            elif movimientoIzquierda:
                x += velocidad1
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad3
                y += velocidad3
    elif posicion == 4 or posicion == 12 or posicion == 20 or posicion == 28 or posicion == 36 or posicion == -4:
        if velocidad == 1:
            if movimientoDerecha:
                y -= velocidad1
            elif movimientoIzquierda:
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                y -= velocidad1
            elif movimientoIzquierda:
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                y -= velocidad1
            elif movimientoIzquierda:
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad3
    elif posicion == 5 or posicion == 13 or posicion == 21 or posicion == 29 or posicion == 37 or posicion == -3:
        if velocidad == 1:
            if movimientoDerecha:
                x += velocidad1
                y -= velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad1
                y -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                x += velocidad1
                y -= velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad2
                y -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                x += velocidad1
                y -= velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
                y += velocidad1
            elif movimientoFrente:
                x -= velocidad3
                y -= velocidad3
    elif posicion == 6 or posicion == 14 or posicion == 22 or posicion == 30 or posicion == 38 or posicion == -2:
        if velocidad == 1:
            if movimientoDerecha:
                x += velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
            elif movimientoFrente:
                y -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                x += velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
            elif movimientoFrente:
                y -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                x += velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
            elif movimientoFrente:
                y -= velocidad3
    elif posicion == 7 or posicion == 15 or posicion == 23 or posicion == 31 or posicion == 39 or posicion == -1:
        if velocidad == 1:
            if movimientoDerecha:
                x += velocidad1
                y += velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad1
                y -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                x += velocidad1
                y += velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad2
                y -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                x += velocidad1
                y += velocidad1
            elif movimientoIzquierda:
                x -= velocidad1
                y -= velocidad1
            elif movimientoFrente:
                x += velocidad3
                y -= velocidad3

    spriteUsuario.rect.left = x
    spriteUsuario.rect.top = y
    ventana.blit(spriteUsuario.image, spriteUsuario.rect)


# Aqui se dibuja el sprite del adversario y le indica hacia donde moverse
def dibujarAdversario(ventana, spriteAdversario, posicionAdv, velocidad, movimientoFrente, movimientoIzquierda,
                      movimientoDerecha, distanciaX, distanciaY):
    global xAdv, yAdv, sector
    velocidad1 = 6
    velocidad2 = 16
    velocidad3 = 21

    if posicionAdv == 0 or posicionAdv == 8 or posicionAdv == 16 or posicionAdv == 24 or posicionAdv == 32 or posicionAdv == -8:
        if velocidad == 1:
            if movimientoDerecha:
                yAdv += velocidad1
            elif movimientoIzquierda:
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                yAdv += velocidad1
            elif movimientoIzquierda:
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                yAdv += velocidad1
            elif movimientoIzquierda:
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad3
    elif posicionAdv == 1 or posicionAdv == 9 or posicionAdv == 17 or posicionAdv == 25 or posicionAdv == 33 or posicionAdv == -7:
        if velocidad == 1:
            if movimientoDerecha:
                xAdv -= velocidad1
                yAdv += velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad1
                yAdv += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                xAdv -= velocidad1
                yAdv += velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad2
                yAdv += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                xAdv -= velocidad1
                yAdv += velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad3
                yAdv += velocidad3
    elif posicionAdv == 2 or posicionAdv == 10 or posicionAdv == 18 or posicionAdv == 26 or posicionAdv == 34 or posicionAdv == -6:
        if velocidad == 1:
            if movimientoDerecha:
                xAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
            elif movimientoFrente:
                yAdv += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                xAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
            elif movimientoFrente:
                yAdv += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                xAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
            elif movimientoFrente:
                yAdv += velocidad3
    elif posicionAdv == 3 or posicionAdv == 11 or posicionAdv == 19 or posicionAdv == 27 or posicionAdv == 35 or posicionAdv == -5:
        if velocidad == 1:
            if movimientoDerecha:
                xAdv -= velocidad1
                yAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad1
                yAdv += velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                xAdv -= velocidad1
                yAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad2
                yAdv += velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                xAdv -= velocidad1
                yAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv += velocidad1
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad3
                yAdv += velocidad3
    elif posicionAdv == 4 or posicionAdv == 12 or posicionAdv == 20 or posicionAdv == 28 or posicionAdv == 36 or posicionAdv == -4:
        if velocidad == 1:
            if movimientoDerecha:
                yAdv -= velocidad1
            elif movimientoIzquierda:
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                yAdv -= velocidad1
            elif movimientoIzquierda:
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                yAdv -= velocidad1
            elif movimientoIzquierda:
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad3
    elif posicionAdv == 5 or posicionAdv == 13 or posicionAdv == 21 or posicionAdv == 29 or posicionAdv == 37 or posicionAdv == -3:
        if velocidad == 1:
            if movimientoDerecha:
                xAdv += velocidad1
                yAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad1
                yAdv -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                xAdv += velocidad1
                yAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad2
                yAdv -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                xAdv += velocidad1
                yAdv -= velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
                yAdv += velocidad1
            elif movimientoFrente:
                xAdv -= velocidad3
                yAdv -= velocidad3
    elif posicionAdv == 6 or posicionAdv == 14 or posicionAdv == 22 or posicionAdv == 30 or posicionAdv == 38 or posicionAdv == -2:
        if velocidad == 1:
            if movimientoDerecha:
                xAdv += velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
            elif movimientoFrente:
                yAdv -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                xAdv += velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
            elif movimientoFrente:
                yAdv -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                xAdv += velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
            elif movimientoFrente:
                yAdv -= velocidad3
    elif posicionAdv == 7 or posicionAdv == 15 or posicionAdv == 23 or posicionAdv == 31 or posicionAdv == 39 or posicionAdv == -1:
        if velocidad == 1:
            if movimientoDerecha:
                xAdv += velocidad1
                yAdv += velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad1
                yAdv -= velocidad1
        elif velocidad == 2:
            if movimientoDerecha:
                xAdv += velocidad1
                yAdv += velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad2
                yAdv -= velocidad2
        elif velocidad == 3:
            if movimientoDerecha:
                xAdv += velocidad1
                yAdv += velocidad1
            elif movimientoIzquierda:
                xAdv -= velocidad1
                yAdv -= velocidad1
            elif movimientoFrente:
                xAdv += velocidad3
                yAdv -= velocidad3

    spriteAdversario.rect.left = xAdv - distanciaX
    spriteAdversario.rect.top = yAdv - distanciaY
    ventana.blit(spriteAdversario.image, spriteAdversario.rect)


def obtenerCoordenadasInicio(sector):
    global x, y
    if sector == 0:
        x = 200
        y = 175
        return x, y


def obtenerCoordenadasAdversario(sector):
    global xAdv, yAdv
    if sector == 0:
        xAdv = 145
        yAdv = 405
        return xAdv, yAdv


# Dibuja en la pantalla la velocidad elegida por el usuario
def dibujarVelocidad(ventana, fuente, fondo, velocidad):
    if velocidad == 1:
        texto = fuente.render("1er velocidad", 1, BLANCO)
        textoFondo = fondo.render("1er velocidad", 1, NEGRO)
        ventana.blit(textoFondo, (410, 557))  # Fondo para el texto
        ventana.blit(texto, (408, 555))  # Texto
    elif velocidad == 2:
        texto = fuente.render("2da velocidad", 1, BLANCO)
        textoFondo = fondo.render("2da velocidad", 1, NEGRO)
        ventana.blit(textoFondo, (410, 557))  # Fondo para el texto
        ventana.blit(texto, (408, 555))  # Texto
    elif velocidad == 3:
        texto = fuente.render("3ra velocidad", 1, BLANCO)
        textoFondo = fondo.render("3ra velocidad", 1, NEGRO)
        ventana.blit(textoFondo, (410, 557))  # Fondo para el texto
        ventana.blit(texto, (408, 555))  # Texto


# Le dice al usuario en que vuelta se encuentra
def dibujarVuelta(ventana, fuente, fondo, sector):
    if 0 <= sector <= 38:
        texto = fuente.render("Vuelta 1 de 3", 1, BLANCO)
        textoFondo = fondo.render("Vuelta 1 de 3", 1, NEGRO)
        ventana.blit(textoFondo, (410, 11))  # Fondo para el texto
        ventana.blit(texto, (408, 9))  # Texto
    elif 39 <= sector <= 77:
        texto = fuente.render("Vuelta 2 de 3", 1, BLANCO)
        textoFondo = fondo.render("Vuelta 2 de 3", 1, NEGRO)
        ventana.blit(textoFondo, (410, 11))  # Fondo para el texto
        ventana.blit(texto, (408, 9))  # Texto
    elif 78 <= sector <= 116:
        texto = fuente.render("Vuelta Final", 1, BLANCO)
        textoFondo = fondo.render("Vuelta Final", 1, NEGRO)
        ventana.blit(textoFondo, (410, 11))  # Fondo para el texto
        ventana.blit(texto, (408, 9))  # Texto


# Le dice al programa cuando cambiar de sector segun las coordenadas del usuario
def cambiarSector(spriteUsuario, spriteAdversario):
    global sector, x, y, xAdv, yAdv, distanciaX, distanciaY
    if sector == 0 or sector == 1 or sector == 2 or sector == 3 or sector == 39 or sector == 40 or sector == 41 or sector == 42 or sector == 78 or sector == 79 or sector == 80 or sector == 81:
        if x >= 730:
            sector += 1
            x = -70
            xAdv = -70
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 4 or sector == 43 or sector == 82:
        if x >= 688 and y >= 398:
            sector += 1
            x = 80
            y = -70
            xAdv = 0
            yAdv = 180
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 5 or sector == 6 or sector == 7 or sector == 8 or sector == 44 or sector == 45 or sector == 46 or sector == 47 or sector == 83 or sector == 84 or sector == 85 or sector == 86:
        if x >= 680 and y >= 550:
            sector += 1
            x = 80
            y = -70
            xAdv = 0
            yAdv = 180
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 9 or sector == 48 or sector == 87:
        if y >= 530:
            sector += 1
            x = 450
            y = -70
            xAdv = 225
            yAdv = -100
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 10 or sector == 11 or sector == 12 or sector == 49 or sector == 50 or sector == 51 or sector == 88 or sector == 89 or sector == 90:
        if y >= 530:
            sector += 1
            x = 450
            y = -70
            xAdv = 225
            yAdv = -100
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 13 or sector == 52 or sector == 91:
        if x <= 175 and y >= 540:
            sector += 1
            x = 690
            y = -70
            xAdv = 625
            yAdv = -300
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 14 or sector == 15 or sector == 16 or sector == 17 or sector == 53 or sector == 54 or sector == 55 or sector == 56 or sector == 92 or sector == 93 or sector == 94 or sector == 95:
        if x <= 185 and y >= 520:
            sector += 1
            x = 690
            y = -70
            xAdv = 625
            yAdv = -300
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 18 or sector == 57 or sector == 96:
        if x <= 70:
            sector += 1
            x = 730
            y = 355
            xAdv = 730
            yAdv = 125
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 19 or sector == 20 or sector == 21 or sector == 22 or sector == 58 or sector == 59 or sector == 60 or sector == 61 or sector == 97 or sector == 98 or sector == 99 or sector == 100:
        if x <= 70:
            sector += 1
            x = 800
            xAdv = 730
            yAdv = 125
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 23 or sector == 62 or sector == 101:
        if x <= 185 and y <= 80:
            sector += 1
            x = 585
            y = 530
            xAdv = 730
            yAdv = 365
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 24 or sector == 25 or sector == 26 or sector == 27 or sector == 63 or sector == 64 or sector == 65 or sector == 66 or sector == 102 or sector == 103 or sector == 104 or sector == 105:
        if x <= 185 and y <= 80:
            sector += 1
            x = 585
            y = 530
            xAdv = 730
            yAdv = 365
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 28 or sector == 67 or sector == 106:
        if y <= 70:
            sector += 1
            y = 530
            xAdv = 525
            yAdv = 530
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 29 or sector == 30 or sector == 31 or sector == 32 or sector == 68 or sector == 69 or sector == 70 or sector == 71 or sector == 107 or sector == 108 or sector == 109 or sector == 110:
        if y <= 70:
            sector += 1
            y = 530
            xAdv = 525
            yAdv = 570
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 33 or sector == 72 or sector == 111:
        if x >= 620 and y <= 70:
            sector += 1
            x = -90
            y = 600
            xAdv = 250
            yAdv = 570
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 34 or sector == 35 or sector == 36 or sector == 37 or sector == 73 or sector == 74 or sector == 75 or sector == 76 or sector == 112 or sector == 113 or sector == 114 or sector == 115:
        if x >= 620 and y <= 70:
            sector += 1
            x = -90
            y = 600
            xAdv = 250
            yAdv = 570
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 38 or sector == 77 or sector == 116:
        if x >= 730:
            sector += 1
            x = -70
            xAdv = -70
            yAdv = 405
            distanciaX, distanciaY = calcularDistancia(spriteUsuario, spriteAdversario)
    elif sector == 117:
        if x >= 430:
            sector += 1
            x = 801
            xAdv = 801


# Mueve al adversario de forma autónoma
def moverAdversario(ventana, spriteAdversario):
    global sector, xAdv, yAdv, posicionAdv
    # dibujarAdversario(ventana, spriteAdversario, posicionAdv, velocidad, movFrente, movIzq, movDer, distancia) Ejemplo
    if sector == 0 or sector == 1 or sector == 2 or sector == 3 or sector == 39 or sector == 40 or sector == 41 or sector == 42 or sector == 78 or sector == 79 or sector == 80 or sector == 81:
        posicionAdv = 0
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 4 or sector == 43 or sector == 82:
        if xAdv <= 400:
            posicionAdv = 0
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 1
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 5 or sector == 6 or sector == 7 or sector == 8 or sector == 44 or sector == 45 or sector == 46 or sector == 47 or sector == 83 or sector == 84 or sector == 85 or sector == 86:
        posicionAdv = 1
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 9 or sector == 48 or sector == 87:
        if xAdv <= 225:  # CAMBIAR
            posicionAdv = 1
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 2
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 10 or sector == 11 or sector == 12 or sector == 49 or sector == 50 or sector == 51 or sector == 88 or sector == 89 or sector == 90:
        posicionAdv = 2
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 13 or sector == 52 or sector == 91:
        if yAdv <= 70:
            posicionAdv = 2
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 3
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 14 or sector == 15 or sector == 16 or sector == 17 or sector == 53 or sector == 54 or sector == 55 or sector == 56 or sector == 92 or sector == 93 or sector == 94 or sector == 95:
        posicionAdv = 3
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 18 or sector == 57 or sector == 96:
        if yAdv <= 125:
            posicionAdv = 3
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 4
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 19 or sector == 20 or sector == 21 or sector == 22 or sector == 58 or sector == 59 or sector == 60 or sector == 61 or sector == 97 or sector == 98 or sector == 99 or sector == 100:
        posicionAdv = 4
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 23 or sector == 62 or sector == 101:
        if xAdv >= 375:
            posicionAdv = 4
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 5
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 24 or sector == 25 or sector == 26 or sector == 27 or sector == 63 or sector == 64 or sector == 65 or sector == 66 or sector == 102 or sector == 103 or sector == 104 or sector == 105:
        posicionAdv = 5
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 28 or sector == 67 or sector == 106:
        if xAdv >= 500:
            posicionAdv = 5
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 6
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 29 or sector == 30 or sector == 31 or sector == 32 or sector == 68 or sector == 69 or sector == 70 or sector == 71 or sector == 107 or sector == 108 or sector == 109 or sector == 110:
        posicionAdv = 6
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 33 or sector == 72 or sector == 111:
        if yAdv >= 350:
            posicionAdv = 6
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 7
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 34 or sector == 35 or sector == 36 or sector == 37 or sector == 73 or sector == 74 or sector == 75 or sector == 76 or sector == 112 or sector == 113 or sector == 114 or sector == 115:
        posicionAdv = 7
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 3, True, False, False, distanciaX, distanciaY)
    elif sector == 38 or sector == 77 or sector == 116:
        if yAdv >= 425:
            posicionAdv = 7
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
        else:
            posicionAdv = 0
            dibujarAdversario(ventana, spriteAdversario, posicionAdv, 2, True, False, False, distanciaX, distanciaY)
    elif sector == 117:
        posicionAdv = 0
        dibujarAdversario(ventana, spriteAdversario, posicionAdv, 1, True, False, False, distanciaX, distanciaY)


# Detecta la colisión entre el usuario y el adversario
def verificarColision(spriteUsuario, spriteAdversario):
    if pygame.sprite.collide_rect(spriteUsuario, spriteAdversario):
        return True

    else:
        return False


# Dibuja el menú de pausa y los botones de opciones
def dibujarPausa(ventana, btnContinuar, btnMenu, btnSalir, fondo, fuente):
    posicionImagenX = (ANCHO // 2) - (pygame.Surface.get_width(btnContinuar) // 2)
    ventana.blit(btnContinuar, (posicionImagenX, ALTO // 2 - pygame.Surface.get_height(btnContinuar) // 2))
    ventana.blit(btnMenu, (posicionImagenX, ALTO // 2 + 75 - pygame.Surface.get_height(btnMenu) // 2))
    ventana.blit(btnSalir, (posicionImagenX, ALTO // 2 + 150 - pygame.Surface.get_height(btnSalir) // 2))
    texto = fuente.render("PAUSA", 1, BLANCO)
    textoFondo = fondo.render("PAUSA", 1, NEGRO)
    posicionTitulo = pygame.Surface.get_width(texto) - 45
    ventana.blit(textoFondo, (posicionTitulo + 3, 123))  # Fondo para el texto
    ventana.blit(texto, (posicionTitulo, 120))  # Texto


# Obtiene la distancia en x entre usuario y adversario para saber donde dibujar al adversario en cada pantalla
def calcularDistancia(spriteUsuario, spriteAdversario):
    distanciaX = 0
    distanciaY = 0

    if sector == 0 or sector == 1 or sector == 2 or sector == 3 or sector == 39 or sector == 40 or sector == 41 or sector == 42 or sector == 78 or sector == 79 or sector == 80 or sector == 81:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 4 or sector == 43 or sector == 82:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 5 or sector == 6 or sector == 7 or sector == 8 or sector == 44 or sector == 45 or sector == 46 or sector == 47 or sector == 83 or sector == 84 or sector == 85 or sector == 86:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 9 or sector == 48 or sector == 87:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 10 or sector == 11 or sector == 12 or sector == 49 or sector == 50 or sector == 51 or sector == 88 or sector == 89 or sector == 90:
        distanciaY = spriteUsuario.rect.top - spriteAdversario.rect.top

    elif sector == 13 or sector == 52 or sector == 91:
        distanciaX = spriteAdversario.rect.left - spriteUsuario.rect.left

    elif sector == 14 or sector == 15 or sector == 16 or sector == 17 or sector == 53 or sector == 54 or sector == 55 or sector == 56 or sector == 92 or sector == 93 or sector == 94 or sector == 95:
        distanciaX = spriteAdversario.rect.left - spriteUsuario.rect.left

    elif sector == 18 or sector == 57 or sector == 96:
        distanciaX = spriteAdversario.rect.left - spriteUsuario.rect.left

    elif sector == 19 or sector == 20 or sector == 21 or sector == 22 or sector == 58 or sector == 59 or sector == 60 or sector == 61 or sector == 97 or sector == 98 or sector == 99 or sector == 100:
        distanciaX = spriteAdversario.rect.left - spriteUsuario.rect.left

    elif sector == 23 or sector == 62 or sector == 101:
        distanciaX = spriteAdversario.rect.left - spriteUsuario.rect.left

    elif sector == 24 or sector == 25 or sector == 26 or sector == 27 or sector == 63 or sector == 64 or sector == 65 or sector == 66 or sector == 102 or sector == 103 or sector == 104 or sector == 105:
        distanciaX = spriteAdversario.rect.left - spriteUsuario.rect.left

    elif sector == 28 or sector == 67 or sector == 106:
        distanciaY = spriteAdversario.rect.top - spriteUsuario.rect.top

    elif sector == 29 or sector == 30 or sector == 31 or sector == 32 or sector == 68 or sector == 69 or sector == 70 or sector == 71 or sector == 107 or sector == 108 or sector == 109 or sector == 110:
        distanciaY = spriteAdversario.rect.top - spriteUsuario.rect.top

    elif sector == 33 or sector == 72 or sector == 111:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 34 or sector == 35 or sector == 36 or sector == 37 or sector == 73 or sector == 74 or sector == 75 or sector == 76 or sector == 112 or sector == 113 or sector == 114 or sector == 115:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 38 or sector == 77 or sector == 116:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    elif sector == 117:
        distanciaX = spriteUsuario.rect.left - spriteAdversario.rect.left

    return distanciaX, distanciaY


# Dibuja el estado de colisión y los botones de opciones
def dibujarColision(ventana, btnContinuar, btnSalir, fondo, fuente):
    posicionImagenX = (ANCHO // 2) - (pygame.Surface.get_width(btnContinuar) // 2)
    ventana.blit(btnContinuar, (posicionImagenX, ALTO // 2 - pygame.Surface.get_height(btnContinuar) // 2))
    ventana.blit(btnSalir, (posicionImagenX, ALTO // 2 + 75 - pygame.Surface.get_height(btnSalir) // 2))
    texto = fuente.render("HAZ CHOCADO", 1, BLANCO)
    textoFondo = fondo.render("HAZ CHOCADO", 1, NEGRO)
    posicionTitulo = ANCHO - pygame.Surface.get_width(texto) - 75
    ventana.blit(textoFondo, (posicionTitulo + 3, 113))  # Fondo para el texto
    ventana.blit(texto, (posicionTitulo, 110))  # Texto


# Dibuja que el usuario ha terminado
def dibujarMeta(ventana, fondo, fuente):
    texto = fuente.render("META", 1, BLANCO)
    textoFondo = fondo.render("META", 1, NEGRO)
    posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2
    ventana.blit(textoFondo, (posicionTitulo + 3, 113))  # Fondo para el texto
    ventana.blit(texto, (posicionTitulo, 110))  # Texto


# Coloca al usuario en la posición inicial por si sale de la pantalla
def restaurarPosicion(sector):
    global posicion
    x = 0
    y = 0

    if sector == 0 or sector == 1 or sector == 2 or sector == 3 or sector == 39 or sector == 40 or sector == 41 or sector == 42 or sector == 78 or sector == 79 or sector == 80 or sector == 81:
        x = 200
        y = 175
        posicion = 0
    elif sector == 4 or sector == 43 or sector == 82:
        x = 80
        y = 175
        posicion = 0
    elif sector == 5 or sector == 6 or sector == 7 or sector == 8 or sector == 44 or sector == 45 or sector == 46 or sector == 47 or sector == 83 or sector == 84 or sector == 85 or sector == 86:
        x = 80
        y = -70
        posicion = 1
    elif sector == 9 or sector == 48 or sector == 87:
        x = 80
        y = -70
        posicion = 1
    elif sector == 10 or sector == 11 or sector == 12 or sector == 49 or sector == 50 or sector == 51 or sector == 88 or sector == 89 or sector == 90:
        x = 450
        y = -70
        posicion = 2
    elif sector == 13 or sector == 52 or sector == 91:
        x = 450
        y = -70
        posicion = 2
    elif sector == 14 or sector == 15 or sector == 16 or sector == 17 or sector == 53 or sector == 54 or sector == 55 or sector == 56 or sector == 92 or sector == 93 or sector == 94 or sector == 95:
        x = 690
        y = -70
        posicion = 3
    elif sector == 18 or sector == 57 or sector == 96:
        x = 730
        y = -70
        posicion = 3
    elif sector == 19 or sector == 20 or sector == 21 or sector == 22 or sector == 58 or sector == 59 or sector == 60 or sector == 61 or sector == 97 or sector == 98 or sector == 99 or sector == 100:
        x = 730
        y = 355
        posicion = 4
    elif sector == 23 or sector == 62 or sector == 101:
        x = 730
        y = 355
        posicion = 4
    elif sector == 24 or sector == 25 or sector == 26 or sector == 27 or sector == 63 or sector == 64 or sector == 65 or sector == 66 or sector == 102 or sector == 103 or sector == 104 or sector == 105:
        x = 585
        y = 530
        posicion = 5
    elif sector == 28 or sector == 67 or sector == 106:
        x = 585
        y = 530
        posicion = 5
    elif sector == 29 or sector == 30 or sector == 31 or sector == 32 or sector == 68 or sector == 69 or sector == 70 or sector == 71 or sector == 107 or sector == 108 or sector == 109 or sector == 110:
        x = 280
        y = 530
        posicion = 6
    elif sector == 33 or sector == 72 or sector == 111:
        x = 280
        y = 530
        posicion = 6
    elif sector == 34 or sector == 35 or sector == 36 or sector == 37 or sector == 73 or sector == 74 or sector == 75 or sector == 76 or sector == 112 or sector == 113 or sector == 114 or sector == 115:
        x = -90
        y = 600
        posicion = 7
    elif sector == 38 or sector == 77 or sector == 116:
        x = -90
        y = 600
        posicion = 7

    return x, y


# Dibuja una cuenta regresiva antes de pasar a JUGANDO
def dibujarCuentaRegresiva(ventana, numero, fondo, fuente):
    if numero == 3:
        texto = fuente.render("3", 1, BLANCO)
        textoFondo = fondo.render("3", 1, NEGRO)
        posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2 + 50
        ventana.blit(textoFondo, (posicionTitulo + 6, 116))  # Fondo para el texto
        ventana.blit(texto, (posicionTitulo, 110))  # Texto
    elif numero == 2:
        texto = fuente.render("2", 1, BLANCO)
        textoFondo = fondo.render("2", 1, NEGRO)
        posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2 + 50
        ventana.blit(textoFondo, (posicionTitulo + 6, 116))  # Fondo para el texto
        ventana.blit(texto, (posicionTitulo, 110))  # Texto
    elif numero == 1:
        texto = fuente.render("1", 1, BLANCO)
        textoFondo = fondo.render("1", 1, NEGRO)
        posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2 + 50
        ventana.blit(textoFondo, (posicionTitulo + 6, 116))  # Fondo para el texto
        ventana.blit(texto, (posicionTitulo, 110))  # Texto


def dibujarResultado(ventana, fondo, fuente, resultado):
    if resultado == "ganaste":
        texto = fuente.render("GANASTE", 1, BLANCO)
        textoFondo = fondo.render("GANASTE", 1, NEGRO)
        posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2
        ventana.blit(textoFondo, (posicionTitulo + 3, 313))  # Fondo para el texto
        ventana.blit(texto, (posicionTitulo, 310))  # Texto

    elif resultado == "perdiste":
        texto = fuente.render("PERDISTE", 1, BLANCO)
        textoFondo = fondo.render("PERDISTE", 1, NEGRO)
        posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2
        ventana.blit(textoFondo, (posicionTitulo + 3, 313))  # Fondo para el texto
        ventana.blit(texto, (posicionTitulo, 310))  # Texto


def interpetarTiempo(tiempoVuelta):
    if tiempoVuelta < 3600:
        segundos = tiempoVuelta // 60
        return "0", str(segundos)
    elif 3600 <= tiempoVuelta < 7200:
        tiempoVuelta = tiempoVuelta - 3600
        segundos = tiempoVuelta // 60
        return "1", str(segundos)
    elif 7200 <= tiempoVuelta <= 10800:
        tiempoVuelta = tiempoVuelta - 7200
        segundos = tiempoVuelta // 60
        return "2", str(segundos)
    else:
        minutos = tiempoVuelta / 3600
        segundos = (tiempoVuelta - 60 * minutos) // 60
        return str(minutos), str(segundos)


def dibujarTiempo(ventana, fondo, fuente, minutos, segundos):
    texto = fuente.render("Has hecho %s minutos con %s segundos" % (minutos, segundos), 1, BLANCO)
    textoFondo = fondo.render("Has hecho %s minutos con %s segundos" % (minutos, segundos), 1, NEGRO)
    posicionTitulo = ANCHO // 2 - pygame.Surface.get_width(texto) // 2
    ventana.blit(textoFondo, (posicionTitulo + 3, 128))  # Fondo para el texto
    ventana.blit(texto, (posicionTitulo, 125))  # Texto


def dibujarBotones(ventana, btnVolverAJugar, btnMenu, btnSalir):
    posicionImagenX = (ANCHO // 2) - (pygame.Surface.get_width(btnVolverAJugar) // 2)
    ventana.blit(btnVolverAJugar, (posicionImagenX, ALTO // 2 - pygame.Surface.get_height(btnVolverAJugar) // 2))
    ventana.blit(btnMenu, (posicionImagenX, ALTO // 2 + 75 - pygame.Surface.get_height(btnMenu) // 2))
    ventana.blit(btnSalir, (posicionImagenX, ALTO // 2 + 150 - pygame.Surface.get_height(btnSalir) // 2))


def dibujar():
    # Globales usadas en esta función
    global velocidad, sector, posicion, posicionAdv, seleccion, tiempoVuelta, cuentaRegresiva, cuentaRegresivaMeta, cuentaRegresivaInicio

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # IMAGENES
    # Botones
    btnJugar = pygame.image.load("btn_Jugar.png")
    btnInstrucciones = pygame.image.load("btn_Instrucciones.png")
    btnRegresar = pygame.image.load("btn_Regresar.png")
    btnContinuar = pygame.image.load("btn_Continuar.png")
    btnIniciarCarrera = pygame.image.load("btn_IniciarCarrera.png")
    btnMenu = pygame.image.load("btn_Menu.png")
    btnVolverAJugar = pygame.image.load("btn_VolverAJugar.png")
    btnSalir = pygame.image.load("btn_Salir.png")
    # Pista
    mapaPista = pygame.image.load("mapaPista.png")
    menuInstrucciones = pygame.image.load("Instrucciones.png")
    menuInstrucciones2 = pygame.image.load("Instrucciones2.png")
    pistaSalida = pygame.image.load("pistaSalida.png")
    pistaRectaDer1 = pygame.image.load("pistaRectaDer1.png")
    pistaRectaDer2 = pygame.image.load("pistaRectaDer2.png")
    pistaAnguloDerSup = pygame.image.load("pistaAnguloDerSup.png")
    pistaDiagonalDerSup1 = pygame.image.load("pistaDiagonalDerSup1.png")
    pistaDiagonalDerSup2 = pygame.image.load("pistaDiagonalDerSup2.png")
    pistaAnguloVertDerSup = pygame.image.load("pistaAnguloVertDerSup.png")
    pistaRectaVerDer1 = pygame.image.load("pistaRectaVerDer1.png")
    pistaRectaVerDer2 = pygame.image.load("pistaRectaVerDer2.png")
    pistaAnguloVertDerInf = pygame.image.load("pistaAnguloVertDerInf.png")
    pistaDiagonalDerInf1 = pygame.image.load("pistaDiagonalDerInf1.png")
    pistaDiagonalDerInf2 = pygame.image.load("pistaDiagonalDerInf2.png")
    pistaAnguloDerInf = pygame.image.load("pistaAnguloDerInf.png")
    pistaRectaIzq1 = pygame.image.load("pistaRectaIzq1.png")
    pistaRectaIzq2 = pygame.image.load("pistaRectaIzq2.png")
    pistaAnguloIzqInf = pygame.image.load("pistaAnguloIzqInf.png")
    pistaDiagonalIzqInf1 = pygame.image.load("pistaDiagonalIzqInf1.png")
    pistaDiagonalIzqInf2 = pygame.image.load("pistaDiagonalIzqInf2.png")
    pistaAnguloVertIzqInf = pygame.image.load("pistaAnguloVertIzqInf.png")
    pistaRectaVerIzq1 = pygame.image.load("pistaRectaVerIzq1.png")
    pistaRectaVerIzq2 = pygame.image.load("pistaRectaVerIzq2.png")
    pistaAnguloVertIzqSup = pygame.image.load("pistaAnguloVertIzqSup.png")
    pistaDiagonalIzqSup1 = pygame.image.load("pistaDiagonalIzqSup1.png")
    pistaDiagonalIzqSup2 = pygame.image.load("pistaDiagonalIzqSup2.png")
    pistaAnguloIzqSup = pygame.image.load("pistaAnguloIzqSup.png")
    # Lista sectores
    listaSectores = [pistaSalida, pistaRectaDer1, pistaRectaDer2, pistaAnguloDerSup, pistaDiagonalDerSup1,
                     pistaDiagonalDerSup2, pistaAnguloVertDerSup, pistaRectaVerDer1, pistaRectaVerDer2,
                     pistaAnguloVertDerInf, pistaDiagonalDerInf1, pistaDiagonalDerInf2, pistaAnguloDerInf,
                     pistaRectaIzq1, pistaRectaIzq2, pistaAnguloIzqInf, pistaDiagonalIzqInf1, pistaDiagonalIzqInf2,
                     pistaAnguloVertIzqInf, pistaRectaVerIzq1, pistaRectaVerIzq2, pistaAnguloVertIzqSup,
                     pistaDiagonalIzqSup1, pistaDiagonalIzqSup2, pistaAnguloIzqSup]
    # Autos
    autoRojo = pygame.image.load("autoRojo.png")
    autoAzul = pygame.image.load("autoAzul.png")

    # SPRITES
    # en funcion obtenerSpriteUsuario
    # en funcion obtenerSpriteAdversario

    # ESTADOS
    MENU = 1
    INSTRUCCIONES = 2
    INSTRUCCIONES2 = 3
    MAPA = 4
    SELECCIONAUTO = 5
    CUENTAREGRESIVA = 6
    JUGANDO = 7
    PAUSA = 8
    COLISION = 9
    META = 10
    RESULTADOS = 11
    estado = MENU  # Al inicio muestra el menú

    # AUDIO (SONIDO)
    pygame.mixer.init()
    # Sonido corto      Sound -- wav
    sonidoVelocidad2 = pygame.mixer.Sound("sonidoVelocidad2.wav")
    sonidoVelocidad3 = pygame.mixer.Sound("sonidoVelocidad3.wav")
    # Sonido largo      Music -- mp3
    pygame.mixer.music.load("musica_BornToBeWild_Steppenwolf.mp3")
    pygame.mixer.music.play(-1, 1.8)

    # TEXTO
    fuente8BitsGrande = pygame.font.Font("8-BIT WONDER.TTF", 60)
    fondo8BitsGrande = pygame.font.Font("8-BIT WONDER.TTF", 60)
    fuente8BitsTitulo = pygame.font.Font("8-BIT WONDER.TTF", 30)
    fondo8BitsTitulo = pygame.font.Font("8-BIT WONDER.TTF", 30)
    fuente8bitsResultados = pygame.font.Font("8-BIT WONDER.TTF", 21)
    fondo8bitsResultados = pygame.font.Font("8-BIT WONDER.TTF", 21)
    fuente8BitsChica = pygame.font.Font("8-BIT WONDER.TTF", 12)
    fondo8BitsChica = pygame.font.Font("8-BIT WONDER.TTF", 12)
    fuente8bitsConteo = pygame.font.Font("8-BIT WONDER.TTF", 300)
    fondo8bitsConteo = pygame.font.Font("8-BIT WONDER.TTF", 300)
    fuente8bitsMeta = pygame.font.Font("8-BIT WONDER.TTF", 150)
    fondo8bitsMeta = pygame.font.Font("8-BIT WONDER.TTF", 150)

    # Movimientos
    movimientoDerecha = False
    movimientoIzquierda = False
    movimientoFrente = False

    # Obtener coordenadas x, y de inicio
    obtenerCoordenadasInicio(sector)
    obtenerCoordenadasAdversario(sector)

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Tecleo de mouse
                xMouse, yMouse = pygame.mouse.get_pos()
                if estado == MENU:
                    if 300 <= xMouse <= 500 and 275 <= yMouse <= 325:
                        estado = MAPA
                    elif 300 <= xMouse <= 500 and 350 <= yMouse <= 400:
                        estado = INSTRUCCIONES
                    elif 300 <= xMouse <= 500 and 425 <= yMouse <= 475:
                        termina = True

                elif estado == INSTRUCCIONES:
                    if 550 < xMouse < 750 and 525 < yMouse < 575:
                        estado = INSTRUCCIONES2

                elif estado == INSTRUCCIONES2:
                    if 550 < xMouse < 750 and 525 < yMouse < 575:
                        estado = MENU

                elif estado == MAPA:
                    if 100 < xMouse < 300 and 515 < yMouse < 565:
                        estado = MENU

                    elif 500 < xMouse < 700 and 515 < yMouse < 565:
                        estado = SELECCIONAUTO

                elif estado == SELECCIONAUTO:
                    if 133 < xMouse < 273 and 185 < yMouse < 465:
                        seleccion = "rojo"  # CAMBIA SPRITE A ROJO
                    elif 532 < xMouse < 672 and 185 < yMouse < 465:
                        seleccion = "azul"  # CAMBIAR SPRITE A AZUL
                    if seleccion == "rojo" or seleccion == "azul":
                        if 300 < xMouse < 500 and 515 < yMouse < 565:
                            estado = CUENTAREGRESIVA

                elif estado == PAUSA:
                    if 300 <= xMouse <= 500 and 275 <= yMouse <= 325:
                        estado = JUGANDO
                    elif 300 <= xMouse <= 500 and 350 <= yMouse <= 400:
                        global x, y, xAdv, yAdv
                        estado = MENU
                        sector = 0
                        velocidad = 1
                        posicion = 0
                        posicionAdv = 0
                        x = 200
                        y = 175
                        xAdv = 145
                        yAdv = 405
                        seleccion = "nada"
                        cuentaRegresivaInicio = 180
                        movimientoDerecha = False
                        movimientoIzquierda = False
                        movimientoFrente = False
                    elif 300 <= xMouse <= 500 and 425 <= yMouse <= 475:
                        termina = True

                elif estado == COLISION:
                    if 300 <= xMouse <= 500 and 275 <= yMouse <= 325:
                        estado = MENU
                        sector = 0
                        velocidad = 1
                        posicion = 0
                        posicionAdv = 0
                        x = 200
                        y = 175
                        xAdv = 145
                        yAdv = 405
                        seleccion = "nada"
                        cuentaRegresivaInicio = 180
                        movimientoDerecha = False
                        movimientoIzquierda = False
                        movimientoFrente = False
                    elif 300 <= xMouse <= 500 and 350 <= yMouse <= 400:
                        termina = True

                elif estado == RESULTADOS:
                    if 300 <= xMouse <= 500 and 275 <= yMouse <= 325:
                        estado = SELECCIONAUTO
                    elif 300 <= xMouse <= 500 and 350 <= yMouse <= 400:
                        estado = MENU
                    elif 300 <= xMouse <= 500 and 425 <= yMouse <= 475:
                        termina = True

            elif evento.type == pygame.KEYDOWN:  # Tecla oprimida
                if estado == JUGANDO:
                    if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:  # Tecla flecha derecha
                        movimientoDerecha = True

                    elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:  # Tecla flecha izquierda
                        movimientoIzquierda = True

                    elif evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        movimientoFrente = True

                    elif evento.key == pygame.K_1:
                        velocidad = 1

                    elif evento.key == pygame.K_2:
                        velocidad = 2
                        sonidoVelocidad2.play()

                    elif evento.key == pygame.K_3:
                        velocidad = 3
                        sonidoVelocidad3.play()

                    elif evento.key == pygame.K_e:
                        posicion += 1  # Transformar sprite +45 grados

                    elif evento.key == pygame.K_q:
                        posicion -= 1  # Transformar sprite -45 grados

                    elif evento.key == pygame.K_ESCAPE or evento.key == pygame.K_p:
                        estado = PAUSA

                    elif evento.key == pygame.K_r:
                        x, y = restaurarPosicion(sector)

            elif evento.type == pygame.KEYUP:
                if estado == JUGANDO:
                    if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                        movimientoDerecha = False

                    elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                        movimientoIzquierda = False

                    elif evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        movimientoFrente = False

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == MENU:
            dibujarFondo(ventana, pistaSalida)
            dibujarMenu(ventana, btnJugar, btnInstrucciones, btnSalir, fuente8BitsGrande, fondo8BitsGrande)

        elif estado == INSTRUCCIONES:
            dibujarFondo(ventana, menuInstrucciones)
            dibujarInstrucciones(ventana, btnContinuar)

        elif estado == INSTRUCCIONES2:
            dibujarFondo(ventana, menuInstrucciones2)
            dibujarInstrucciones(ventana, btnMenu)

        elif estado == MAPA:
            dibujarFondo(ventana, mapaPista)
            dibujarMapa(ventana, btnContinuar, btnRegresar)

        elif estado == SELECCIONAUTO:
            dibujarFondo(ventana, pistaSalida)
            dibujarAutos(ventana, autoRojo, autoAzul, btnIniciarCarrera, fuente8BitsTitulo, fondo8BitsTitulo, seleccion)
            if seleccion == "nada":
                pass
            elif seleccion == "rojo":
                dibujarSeleccion(ventana, fuente8BitsChica, fondo8BitsChica, seleccion)
            elif seleccion == "azul":
                dibujarSeleccion(ventana, fuente8BitsChica, fondo8BitsChica, seleccion)

        elif estado == CUENTAREGRESIVA:
            cuentaRegresivaInicio -= 1
            dibujarSector(ventana, 0, listaSectores)
            spriteUsuario = obtenerSpriteUsuario(seleccion, autoAzul, autoRojo, posicion)
            spriteAdversario = obtenerSpriteAdversario(seleccion, autoAzul, autoRojo, posicionAdv)
            dibujarVehiculo(ventana, spriteUsuario, velocidad, movimientoFrente, movimientoIzquierda, movimientoDerecha)
            dibujarAdversario(ventana, spriteAdversario, 0, velocidad, False, False, False, 0, 0)
            if cuentaRegresivaInicio >= 120:
                dibujarCuentaRegresiva(ventana, 3, fondo8bitsConteo, fuente8bitsConteo)
            elif 120 >= cuentaRegresivaInicio >= 60:
                dibujarCuentaRegresiva(ventana, 2, fondo8bitsConteo, fuente8bitsConteo)
            elif 60 > cuentaRegresivaInicio >= 0:
                dibujarCuentaRegresiva(ventana, 1, fondo8bitsConteo, fuente8bitsConteo)
            else:
                estado = JUGANDO

        elif estado == JUGANDO:
            dibujarSector(ventana, sector, listaSectores)

            spriteUsuario = obtenerSpriteUsuario(seleccion, autoAzul, autoRojo, posicion)
            spriteAdversario = obtenerSpriteAdversario(seleccion, autoAzul, autoRojo, posicionAdv)

            dibujarVelocidad(ventana, fuente8BitsTitulo, fondo8BitsTitulo, velocidad)  # , sector while
            dibujarVuelta(ventana, fuente8BitsTitulo, fondo8BitsTitulo, sector)
            cambiarSector(spriteUsuario, spriteAdversario)

            dibujarVehiculo(ventana, spriteUsuario, velocidad, movimientoFrente, movimientoIzquierda, movimientoDerecha)
            moverAdversario(ventana, spriteAdversario)

            if verificarColision(spriteUsuario, spriteAdversario):
                estado = COLISION

            elif sector == 118:
                estado = META

        elif estado == PAUSA:
            dibujarSector(ventana, sector, listaSectores)
            dibujarVehiculo(ventana, spriteUsuario, 1, False, False, False)
            dibujarAdversario(ventana, spriteAdversario, 1, sector, False, False, False, 0, 0)
            dibujarPausa(ventana, btnContinuar, btnMenu, btnSalir, fondo8BitsGrande, fuente8BitsGrande)

        elif estado == COLISION:
            dibujarSector(ventana, sector, listaSectores)
            dibujarVehiculo(ventana, spriteUsuario, 1, False, False, False)
            dibujarAdversario(ventana, spriteAdversario, 1, sector, False, False, False, 0, 0)
            dibujarColision(ventana, btnContinuar, btnSalir, fondo8BitsGrande, fuente8BitsGrande)

        elif estado == META:
            if cuentaRegresivaMeta > 0:
                dibujarFondo(ventana, pistaSalida)
                dibujarVehiculo(ventana, spriteUsuario, 1, False, False, False)
                dibujarAdversario(ventana, spriteAdversario, 1, sector, False, False, False, 0, 0)
                cuentaRegresivaMeta -= 1
                dibujarMeta(ventana, fondo8bitsMeta, fuente8bitsMeta)
                if tiempoVuelta < 10800:
                    dibujarResultado(ventana, fondo8BitsGrande, fuente8BitsGrande, "ganaste")
                else:
                    dibujarResultado(ventana, fondo8BitsGrande, fuente8BitsGrande, "perdiste")
            else:
                estado = RESULTADOS

        elif estado == RESULTADOS:
            minutos, segundos = interpetarTiempo(tiempoVuelta)
            dibujarFondo(ventana, pistaSalida)
            dibujarVehiculo(ventana, spriteUsuario, 1, False, False, False)
            dibujarAdversario(ventana, spriteAdversario, 1, sector, False, False, False, 0, 0)
            dibujarTiempo(ventana, fondo8bitsResultados, fuente8bitsResultados, minutos, segundos)
            dibujarBotones(ventana, btnVolverAJugar, btnMenu, btnSalir)

        pygame.display.flip()
        reloj.tick(60)

    pygame.mixer.quit()
    pygame.quit()


def main():
    dibujar()


main()
