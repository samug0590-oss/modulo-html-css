nombre = "Angelo"
print("Ingrese su edad")
edad = int(input())

print(f"Hola {nombre}, tienes {edad} años")

if edad >= 18:
    print(f"Puedes entrar {nombre}")

elif edad >= 13:
    print("Ncesitas permiso de un adulto para entrar al evento")
    print("Tienes permiso para entrar? 1=Si 2=No")
    per = int(input())

    if per == 1:
        print(f"Puedes entrar el evento {nombre}")

    elif per == 2:
        print(f"No puedes entrar al evento {nombre}")

    else:
        print("Respuesta no valida")

else:
    print(f"No puedes entrar al evento {nombre}")