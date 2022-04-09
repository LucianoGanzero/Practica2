tupla1=('a','e','i','o','u','l','r','s','t')
tupla2=('d','g')
tupla3=('b','c','m','p')
tupla4=('f','h','v','w','y')
tupla5='k'
tupla6=('j','x')
tupla7=('q','z')

supertupla =(tupla1,tupla2,tupla3,tupla4,tupla5,tupla6,tupla7)
tablaValores = {tupla1:1,tupla2:2,tupla3:3,tupla4:4,tupla5:5,tupla6:8,tupla7:10}

palabra = input("Ingrese una palabra ")

palabra=palabra.lower()
contador=0

for char in palabra:
    for elem in supertupla:
        if char in elem:
            estatupla = elem
    contador = contador + tablaValores[estatupla]

print(f'La palabra {palabra} vale {contador} puntos')