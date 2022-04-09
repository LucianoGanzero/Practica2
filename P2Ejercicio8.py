from operator import truediv
import string

cadena = input("Ingrese una palabra o una frase ")

lista = []
es = True

for char in cadena:
    if char in string.ascii_letters:
         if char in lista:
            es=False
         else:
            lista.append(char)

print(('{} es un heterograma' if es else '{} no es un heterograma').format(cadena))