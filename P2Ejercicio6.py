cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant = cadena.count("@")+cadena.count("!")
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")

import string


cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant=cadena.count(string.punctuation)
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Clave válida")