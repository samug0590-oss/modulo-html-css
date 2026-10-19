print("Menu de opciones")
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicación")
print("4 = Division")

opcion = int(input("Elija una operacion de las anteriores "))
numero1 = float(input("Ingrese el primer numero "))
numero2 = float(input("Ingrese el segundo numero "))

if opcion == 1:
    print(numero1 + numero2)

elif opcion == 2:
    print(numero1 - numero2)

elif opcion == 3:
    print(numero1 * numero2)

elif opcion == 4:
    print(numero1 / numero2)

else:
    print("Operacion no existente")