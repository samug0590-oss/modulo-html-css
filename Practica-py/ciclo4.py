suma = 0
for i in range(5):
    nota = float(input(f"Ingrese la calificación {i+1}: "))
    suma = suma + nota
promedio = suma / 5
print("El promedio es:", promedio)
if promedio >= 6:
    print("Aprobado")
else:
    print("Reprobado")