num = int(input ("Ingrese un numero: "))

if ((num % 2) == 1 ):
    print ("El numero es impar")
else:
    print ("El numero es par")


if ((num % 2) == 0):
    print ("Es multiplo de 2")
if ((num % 3) == 0):
    print ("Es multiplo de 3")
if ((num % 5) == 0):
    print ("Es multiplo de 5")


letra = input ("Ingrese una letra: ")
if (letra >= "a" and letra <= "z"):
    print ("La letra ingresada es minuscula.")
elif (letra >= "A" and letra <= "Z"):
    print ("La letra ingresada es mayuscula.")
elif (letra == "\"" or letra == "\'" ):
    print ("Es una comilla.")
else:
    print ("No sabria decirte que es.")


cadena_1 = input ("Ingresa la primera cadena txt: ")
cadena_2 = input ("Ingrese la segunda cadena txt: ")
if (len(cadena_1) > len (cadena_2)):
    print (cadena_1)
else:
    print (cadena_2)


cadena_a = input ("Ingrese una cadena: ")
cantidad_a = 0
for car in cadena_a:
    if (car == "a" or car == "A"):
        cantidad_a = cantidad_a + 1
print ("La cadena ingresada tiene ", cantidad_a, "letras a.")