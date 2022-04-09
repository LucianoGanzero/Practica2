
estructura=[
    '-***-',
    '-*-*-',
    '--*-*',
    '*--**',
]


def porLinea (linea):               ##crea la linea y la modifica de acuerdo a lo que hay en la misma linea
    milinea=["","","","",""]
    largo=len(milinea)
    linea= list(linea)
    for indice in range(largo):
        if (linea[indice]=='*'):
              milinea[indice]='*'
        else:
            if (indice==0):
                if linea[indice+1]=='*':
                  milinea[indice]='1'
                else:
                    milinea[indice]='0'
            elif (indice==(largo-1)):
                if linea[indice-1]=='*':
                    milinea[indice]='1'
                else:
                    milinea[indice]='0'
            else:
                if (linea[indice+1]=='*' and linea[indice-1]=='*'):
                    milinea[indice]='2'
                elif ((linea[indice+1]=='*' and linea[indice-1]!='*') or (linea[indice+1]!='*' and linea[indice-1]=='*')):
                    milinea[indice]='1'
                else:
                    milinea[indice]='0'
    return milinea

def lineaAbajo (miEstructura,indice): ##modifica una linea de acuerdo a lo que hay en la linea inferior/siguiente
    largo2=len(miEstructura[indice])
    for indice2 in range(largo2):
      if (miEstructura[indice][indice2]!='*'):
            if (indice2==0):
                if (miEstructura[indice+1][indice2]=='*' and miEstructura[indice+1][indice2+1]=='*'):
                    aux = int(miEstructura[indice][indice2])
                    aux = aux+2
                    miEstructura[indice][indice2]= str(aux)
                elif (miEstructura[indice+1][indice2]=='*' or miEstructura[indice+1][indice2+1]=='*'):
                    aux = int(miEstructura[indice][indice2])
                    aux = aux+1
                    miEstructura[indice][indice2]= str(aux)
            elif (indice2==(largo2-1)):
                    if (miEstructura[indice+1][indice2]=='*' and miEstructura[indice+1][indice2-1]=='*'):
                        aux = int(miEstructura[indice][indice2])
                        aux = aux+2
                        miEstructura[indice][indice2]= str(aux)
                    elif ((miEstructura[indice+1][indice2]=='*' and miEstructura[indice+1][indice2-1]!='*') or (miEstructura[indice+1][indice2]!='*' and miEstructura[indice+1][indice2-1]=='*')):
                        aux = int(miEstructura[indice][indice2])
                        aux = aux+1
                        miEstructura[indice][indice2]= str(aux)
            else:
                cant=0
                for i in range(indice2-1,indice2+2):
                    if (miEstructura[indice+1][i]=='*'):
                        cant=cant+1
                aux = int (miEstructura[indice][indice2])
                aux = aux+cant
                miEstructura[indice][indice2]= str(aux)
    return miEstructura

def lineaArriba (miEstructura,indice): ##modifica una linea de acuerdo a lo que hay en la linea superior/anterior
    largo2=len(miEstructura[indice])
    for indice2 in range(largo2):
        if (miEstructura[indice][indice2]!='*'):
            if (indice2==0):
                if (miEstructura[indice-1][indice2]=='*' and miEstructura[indice-1][indice2+1]=='*'):
                    aux = int(miEstructura[indice][indice2])
                    aux = aux+2
                    miEstructura[indice][indice2]= str(aux)
                elif (miEstructura[indice-1][indice2]=='*' or miEstructura[indice-1][indice2+1]=='*'):
                    aux = int(miEstructura[indice][indice2])
                    aux = aux+1
                    miEstructura[indice][indice2]= str(aux)
            elif (indice2==(largo2-1)):
                    if (miEstructura[indice-1][indice2]=='*' and miEstructura[indice-1][indice2-1]=='*'):
                        aux = int(miEstructura[indice][indice2])
                        aux = aux+2
                        miEstructura[indice][indice2]= str(aux)
                    elif ((miEstructura[indice-1][indice2]=='*' and miEstructura[indice-1][indice2-1]!='*') or (miEstructura[indice-1][indice2]!='*' or miEstructura[indice-1][indice2-1]=='*')):
                        aux = int (miEstructura[indice][indice2])
                        aux = aux+1
                        miEstructura[indice][indice2]= str(aux)
            else:
                cant=0
                for i in range((indice2-1),(indice2+2)):
                    if (miEstructura[indice-1][i]=='*'):
                        cant=cant + 1
                aux = int(miEstructura[indice][indice2])
                aux = aux+cant
                miEstructura[indice][indice2]= str(aux)
    return miEstructura
    
def cargarlineas (estructura): ##crea la estructura a partir de una lista de strings, la transforma en una lista de listas de caracteres y traduce los guiones en numeros por linea
    miEstructura=[[],[],[],[]]
    largo=len(estructura)
    for indice in range(largo):
        nuevalinea=porLinea(estructura[indice])
        miEstructura[indice]=nuevalinea
    return miEstructura

def armarEstructura(estructura): 
    miEstructura=cargarlineas(estructura)
    for indice in range(len(miEstructura)):
        if (indice == 0):
            miEstructura= lineaAbajo(miEstructura,indice)
        elif (indice==(len(miEstructura)-1)):
            miEstructura= lineaArriba(miEstructura,indice)
        else:
            miEstructura= lineaArriba(miEstructura,indice)
            miEstructura= lineaAbajo(miEstructura,indice)

    return miEstructura


nuevaEstructura=armarEstructura(estructura)

for i in range (len(estructura)):
    print(estructura[i])
for i in range (len(nuevaEstructura)):
    print(nuevaEstructura[i])

