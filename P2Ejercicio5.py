
frase = input("Ingrese una frase")
palabra= input ("Ingrese una palabra")


if (not palabra.islower()):
    palabra=palabra.lower()
if (not frase.islower()):
    frase=frase.lower()

print(frase.count(palabra))