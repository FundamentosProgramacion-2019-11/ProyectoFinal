def guardarTiempo(x):
    archivo=open('tiempos.txt','a')
    archivo.write(str(x)+"\n")


def enviarRegistros():
    archivo=open('tiempos.txt','r')
    palabras=[]
    for linea in archivo:
        linea = linea[:-1]
        palabras.append(linea)
    return (palabras)