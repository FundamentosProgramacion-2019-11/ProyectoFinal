
def matchReport(score1,score2):
    file=open('partidas.txt','a')
    file.write(str(score1)+","+str(score2) +"\n")

def readMatches():
    file=open('partidas.txt','r')
    l=[]
    for linea in file:
        linea= linea[:-1]
        l.append(linea)
    return (l)