#Preguntas 1 y 2 
#Desafío 4:promedio de notas de estudiantes 

#Calculamos el promedio de notas de estudiantes (Creamos la lista de notas)
notas = [7, 8, 6, 5, 9, 10, 4, 3, 2, 1]

#Calculamos el promedio de notas sumando todas las notas y dividiendolas por la cantidad de las notas 
promedio = sum(notas) / len(notas)

#Imprimimos el resultado del promedio
print(f"El promedio de notas es: {promedio:.2f} ")

#Luego queremos saber cual es la nota mas alta y la nota mas baja mediante la siguente funcion:
def nota_mas_alta_baja(notas):
    nota_mas_alta = max(notas)
    nota_mas_baja = min(notas)
    return nota_mas_alta, nota_mas_baja
    
#Imprimimos el resultado de las notas mas altas y las notas mas bajas
nota_mas_alta, nota_mas_baja = nota_mas_alta_baja(notas)
print(f"La nota más alta es: {nota_mas_alta:.2f}")
print(f"La nota más baja es: {nota_mas_baja:.2f}")
