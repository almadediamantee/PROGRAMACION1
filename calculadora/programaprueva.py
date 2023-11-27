import random
print("Este programa consiste en que el usuario eliga un numero del 1 al 50 e intente adivinarlo con pintas de muy bajo y muy alto")

numAleatorio= random.randint(1,50)

listaNumeros = []

while True:
    num1=int(input("Ingrese un numero del 1 al 50: "))
    listaNumeros.append(numAleatorio)
    print(listaNumeros)
    if num1 == numAleatorio:
        print("Has acertado el numero!!!")
        print(numAleatorio)
        break
    if num1 < numAleatorio:
        print(" El numero es DEMASIADO BAJO")
    if num1  > numAleatorio:
        print(" El numero es DEMASIADO ALTO")

