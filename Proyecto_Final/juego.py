#María Angélica Hernández Parada        A01169796
#Proyecto final

# coding=utf-8
import pygame   
import random
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

def dibujarMenu(ventana, btnPlay,x,y):
    ventana.blit(btnPlay,(x,y)) #medidas btn

def dibujarMouse(ventana, xMouse, yMOUSE):
    if xMouse != -1:
        pygame.draw.circle(ventana, ROJO, (xMouse,yMOUSE),10)
def dibujarFondo(ventana, fondoJuego):
    ventana.blit(fondoJuego,(0,0))
def dibujarText(ventana, text, fuente,x,y):
    texto = fuente.render(str(text), 1, BLANCO)   #antialiasing suaviza orilla, texto ya es imagen
    ventana.blit(texto, (x,y))    #dupla de cordenadas
def escribirLeaders(leaders):
    f=open("leaderboard.txt","w")
    for i in range(0,len(leaders)):
        f.write(str(leaders[i])+"\n")
    f.close()

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    #imagenes
    btnPlay = pygame.image.load("play.png")
    btnTrue = pygame.image.load("true.png")
    btnFalse = pygame.image.load("false.png")
    btnLeader = pygame.image.load("leader.png")
    logo = pygame.image.load("logo.png")
    btnBack=pygame.image.load("back.png")
    vida=pygame.image.load("vida.png")
    fondoJuego = pygame.image.load("fondo.jpg")
    #musica
    pygame.mixer.init()
    pygame.mixer.music.load("Mii.mp3")
    pygame.mixer.music.play(-1)
    #mouse
    xMouse= -1
    yMOUSE = -1
    #Estado
    state=0 #0 menu, 1 leader, 2 jugando
    #timer
    timeLeft=500
    #preguntas
    primer=""
    segun=""
    preguntas=[]
    f=open("questions.txt","r")
    linesf=f.readlines()
    for line in linesf:
        preguntas.append(line.split("|"))
       # print(line.split("|"))
    f.close()
    intPreg=random.randint(0,len(preguntas)-1)
    print(preguntas[intPreg][1])
    palbras=preguntas[intPreg][0].split(" ")
    for i in range(0,len(palbras)):
        if i < 7:
            primer+=str(palbras[i])+" "
        else:
            segun+=str(palbras[i])+" "
    print(primer+segun+"\n")
   
    #leadearboards
    leaders=[]
    f = open("leaderboard.txt", "r")
    for line in f:
        leaders.append(int(line))
        print(line)
    
      
    f.close()
    #fuente
    fuente = pygame.font.SysFont("Arial", 20) #tamaño de la leta
    fuenteTiempo = pygame.font.SysFont("Arial", 40) #tamaño de la leta tiempo
    fuentePreg = pygame.font.SysFont("Arial", 40) #tamaño de la leta tiempo
    #game related
    vidas=6
    score = 0    #de donde empieza
    #gameloop
    while not termina:  
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            xMouse, yMOUSE = pygame.mouse.get_pos()
            print(xMouse,yMOUSE)
            if state==0:
                if xMouse <= 200 and xMouse >=0 and yMOUSE <=600 and yMOUSE >=400:
                   pygame.time.delay(500) 
                   state=2
                   vidas=6
                   score=0
                if xMouse <= 800 and xMouse >=600 and yMOUSE <=600 and yMOUSE >=400:
                   state=1   
            elif state==1:#leader
                if xMouse <= 100 and xMouse >=0 and yMOUSE <=100 and yMOUSE >=0:
                    state=0
            elif state==2:
                if xMouse <= 100 and xMouse >=0 and yMOUSE <=600 and yMOUSE >=500:
                    print("false")
                    timeLeft=0
                    pygame.time.delay(100)
                    if preguntas[intPreg][1] == "False":
                        score+=int(preguntas[intPreg][2])
                        vidas+=1
                  
                if xMouse <= 800 and xMouse >=700 and yMOUSE <=600 and yMOUSE >=500:
                    print("true") 
                    timeLeft=0
                    pygame.time.delay(100)
                    if preguntas[intPreg][1] == "True":
                        score+=int(preguntas[intPreg][2])
                        vidas+=1
            elif state==3:
                if xMouse <= 500 and xMouse >=300 and yMOUSE <=600 and yMOUSE >=400:
                    state=0
                    
        # Borrar pantalla
        ventana.fill(BLANCO)
        if state==0:#menu
            dibujarFondo(ventana, fondoJuego)
            dibujarMenu(ventana,logo,100,100)
            dibujarMenu(ventana,btnPlay,0,400)
            dibujarMenu(ventana,btnLeader,600,400)
            dibujarMouse(ventana,xMouse,yMOUSE)
        elif state==1:#leader
            dibujarFondo(ventana, fondoJuego)
            dibujarMenu(ventana,btnBack,0,0)
            leaders.sort(reverse=True)
            dibujarText(ventana,"TOP 5:",fuentePreg,300,0)
            for i in range(0,5):
                dibujarText(ventana,leaders[i],fuentePreg,300,i*100+100)
        elif state==2:#jugando
            dibujarFondo(ventana, fondoJuego)
            dibujarMenu(ventana,btnFalse,0,500)
            dibujarMenu(ventana,btnTrue,700,500)
            timeLeft -=1
            if timeLeft <=0:
                vidas-=1
                primer=""
                segun=""
                timeLeft=500
                intPreg=random.randint(0,len(preguntas)-1)
                palbras=preguntas[intPreg][0].split(" ")
                print(preguntas[intPreg][1])
                for i in range(0,len(palbras)):
                    if i < 7:
                        primer+=str(palbras[i])+" "
                    else:
                        segun+=str(palbras[i])+" "
                print(primer+segun+"\n")
            #print(timeLeft)
            dibujarText(ventana,"Puntaje: "+str(score),fuente,0,0)
            dibujarText(ventana,timeLeft,fuenteTiempo,ANCHO/2-20,50)
            #dibujarText(ventana,str(preguntas[intPreg][0])[:32],fuentePreg,100,200)
            dibujarText(ventana,primer,fuentePreg,100,200)
            dibujarText(ventana,segun,fuentePreg,100,250)
            for i in range(0,vidas):
                dibujarMenu(ventana,vida,i*100+100,500)
            if vidas <= 0:
                
                leaders.append(score)
                escribirLeaders(leaders)
                state=3
        elif state==3:
            dibujarFondo(ventana, fondoJuego)
            dibujarText(ventana,"El juego se acabo",fuentePreg,250,100)
            dibujarText(ventana,"Puntaje Final: "+str(score),fuentePreg,250,200)
            dibujarMenu(ventana,btnPlay,300,400)
       
        

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(100)  # 100 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()