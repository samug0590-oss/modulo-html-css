print("Ingrese el primer numero")
numero1 = int(input())
print("Ingrese el segundo numero")
numero2 = int(input())
print("Ingrese el tercer numero")
numero3 = int(input())

if numero1 > numero2 and numero3:
    print(f"{numero1} es el mayor de los tres numeros")

elif numero2 > numero1 and numero3:
    print(f"{numero2} es el mayor de los tres numeros")

else:
    print(f"{numero3} es el mayor de los tres numeros")