# Paulina Guerrero Ruiz
# PROYECTO FINAL- KISSING GAME


import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600


posBoy = 625
posGirl = 200
frames = 12
time = 20
timer = time*frames
state = 2
menu = 1
estado = menu    #estados  #al inicio se muestra el menu

# EDibujar menu (botones)
def dibujarMenu(ventana, btnJugar1):
    ventana.blit(btnJugar1, (600, 275))

# Inicializa el motor de pygame
pygame.init()
font = pygame.font.SysFont(None, 80)
pygame.mixer.music.load("K-I-S-S-I-N-G/Friendly_Day.mp3")
pygame.mixer.music.play()
efecto = pygame.mixer.Sound("K-I-S-S-I-N-G/step.wav")

imagenes = {
"girlKiss": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niña2.png"),
"boyKiss": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niño2.png"),
"background": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_background.jpg"),
"teacher": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_maestro1.png"),
"girlLose": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niña3.png"),
"madTeacher": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_maestro4.png"),
"boyLose": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niño3.png"),
"sadTeacher": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_maestro2.png"),
"winKids": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niños.png"),
"menuBoy": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niño1.png"),
"menuGirl": pygame.image.load("K-I-S-S-I-N-G/FundamentosDeProgra_Ilustraciones1_niña1.png"),
"button": pygame.image.load("K-I-S-S-I-N-G/btnJugar1.png")

}
personajes = {
    "girlKiss": pygame.transform.scale(imagenes["girlKiss"], (200, int(200 * 1.17))),
    "boyKiss": pygame.transform.scale(imagenes["boyKiss"], (200, int(200 * 1.17))),
    "background": pygame.transform.scale(imagenes["background"], (800, 600)),
    "teacher": pygame.transform.scale(imagenes["teacher"], (200, 400)),
    "girLose": pygame.transform.scale(imagenes["girlLose"], (200, int(200 * 1.17))),
    "madTeacher": pygame.transform.scale(imagenes["madTeacher"], (200, 400)),
    "boyLose": pygame.transform.scale(imagenes["boyLose"], (200, int(200 * 1.17))),
    "sadTeacher": pygame.transform.scale(imagenes["sadTeacher"], (200, 400)),
    "winKids" : pygame.transform.scale(imagenes["winKids"], (200, int(200 * 1.17))),
    "menuBoy": pygame.transform.scale(imagenes["menuBoy"], (200, int(200 * 1.17))),
    "menuGirl": pygame.transform.scale(imagenes["menuGirl"], (200, int(200 * 1.17))),
    "button": pygame.transform.scale(imagenes["button"], (200, 50))
}

def openArchive(score):
    # abrir archivo
    archivo = open("K-I-S-S-I-N-G/highscore.txt", "r")

    # leer el contenido del archivo
    legend = archivo.read()

    highscore = int(legend)
    if highscore < score:
        highscore = score
        archivo.close()
        archivo = open("K-I-S-S-I-N-G/highscore.txt", "w")
        archivo.write(str(highscore))

    archivo.close()
    return highscore


def playing(ventana, reloj, termina):
    global posBoy, posGirl, timer, state
    # Procesa los eventos que recibe
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True  # Queremos terminar el ciclo
            return termina
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            efecto.play()
            posGirl += 35
            posBoy -= 35
            if posGirl > 420:
                state = 1
    if posGirl > 200:
        posGirl -= 15

    if posBoy < 625:
        posBoy += 15

    # Dibujar, aquí haces todos los trazos que requieras

    girl = personajes["girlKiss"]
    boy = personajes["boyKiss"]
    background = personajes["background"]
    teacher = personajes["teacher"]


    ventana.blit(background, (0, 0))
    ventana.blit(girl, (posGirl, 375))
    ventana.blit(boy, (posBoy, 375))
    ventana.blit(teacher, (0, 210))

    text = font.render("Tiempo: " + str(int(timer / frames)), True, (0, 0, 0)) #color rgb

    ventana.blit(text, (450, 50))
    timer -= 1
    if timer <0:
        state = -1

    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(frames)  # 40 fps
    return termina


def loose(ventana, reloj, termina):
    global posBoy, posGirl, timer, state
    # Procesa los eventos que recibe
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True  # Queremos terminar el ciclo
            return termina
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            state = 0
            timer = time*frames
    girl = personajes["girLose"]
    boy = personajes["boyLose"]
    background = personajes["background"]
    teacher = personajes["madTeacher"]

    ventana.blit(background, (0, 0))
    ventana.blit(girl, (posGirl, 375))
    ventana.blit(boy, (posBoy, 375))
    ventana.blit(teacher, (0, 210))

    text = font.render("Perdio Click para reiniciar", True, (0, 0, 0)) #color rgb

    ventana.blit(text, (20, 50))
    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(frames)


    return termina

def win(ventana, reloj, termina):
    global posBoy, posGirl, timer, state
    # Procesa los eventos que recibe
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True  # Queremos terminar el ciclo
            return termina
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            state = 0
            posGirl = 200
            posBoy = 675
            timer = time * frames
            return termina
    winner = personajes["winKids"]
    background = personajes["background"]
    teacher = personajes["madTeacher"]

    ventana.blit(background, (0, 0))
    ventana.blit(winner, (posGirl, 375))
    ventana.blit(teacher, (0, 210))

    text = font.render("Gano Click para reiniciar", True, (0, 0, 0)) #color rgb
    scoreText = font.render("Score: " +str(int(timer/frames)), True, (0,0,0))
    highscore = openArchive(int(timer/frames))
    highscoreText =font.render("HighScore: " +str(highscore), True, (0,0,0))

    ventana.blit(text, (20, 50))
    ventana.blit(scoreText, (20, 90))
    ventana.blit(highscoreText, (20, 130))
    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(frames)

    return termina

# Estructura básica de un programa que usa pygame para dibujar
def menu(ventana, reloj, termina):
    global posBoy, posGirl, timer, state
    # Procesa los eventos que recibe
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True  # Queremos terminar el ciclo
            return termina
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            xMouse, yMouse = pygame.mouse.get_pos()
            if xMouse >= 400 and xMouse <= 600 and yMouse >= 300 and yMouse <= 350:
                state = 0

    girl = personajes["menuGirl"]
    boy = personajes["menuBoy"]
    background = personajes["background"]
    teacher = personajes["teacher"]
    button= personajes["button"]

    ventana.blit(background, (0, 0))
    ventana.blit(girl, (posGirl, 375))
    ventana.blit(boy, (posBoy, 375))
    ventana.blit(teacher, (0, 210))
    ventana.blit(button, (400,  300))

    text = font.render("Kissing Game", True, (0, 0, 0))  # color rgb
    highscore = openArchive(-1)
    highscoreText = font.render("HighScore: " + str(highscore), True, (0, 0, 0))

    ventana.blit(text, (20, 50))
    ventana.blit(highscoreText, (20, 130))
    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(frames)

    return termina


def dibujar():
    global posBoy, posGirl, timer, state


    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
       if state == 0:
            termina = playing(ventana,reloj, termina)
       elif state == 1:
            termina = win(ventana,reloj, termina)
       elif state == -1:
            termina = loose(ventana,reloj, termina)
       elif state == 2:
            termina = menu(ventana, reloj, termina)
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()