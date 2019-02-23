from typing import List

letras: List[str]="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
opcion=input("Ingrese 1 para cifrar y 2 para decifrar")
mensaje=input("Ingrese el mensaje")
clave=input("Ingrese la clave")
criptograma=""
auxClave=clave.__len__()
cont=0

for i in mensaje:
    if opcion=="1":
        criptograma+=letras[(letras.index(i)+(letras.index(clave[cont %auxClave])))%26]
        cont+=1
    elif opcion=="2":
        criptograma += letras[(letras.index(i)+26-(letras.index(clave[cont % auxClave]))) % 26]
        cont +=1

if opcion=="1":
    print("El mensaje ",mensaje, "cifrado con la clave ",clave, "es ",criptograma)
elif opcion=="2":
    print("El criptograma ",mensaje, "descifrado con la clave ",clave, "significa ",criptograma)