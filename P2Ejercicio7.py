from collections import OrderedDict
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

fraseL=frase.split()

largo=len(fraseL)

for indice in range(largo):
    if (not fraseL[indice].islower()):
        fraseL[indice]=fraseL[indice].lower()

fraseL = list(OrderedDict.fromkeys(fraseL))

print(fraseL)