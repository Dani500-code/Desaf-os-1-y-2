#Realizamos la tarea 1 sobre el inventario de la veruleria dragonfruit

#Inventario inicial 1
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

#Que producto está en la posición 3 del inventario 2
tercer_producto = inventario[3]
print(tercer_producto)

#Actualizamos el inventario despues de la venta de bananas 3
inventario.pop(2) 
inventario.remove("bananas") 
print(f"{inventario}, 'Despues de hacer la venta de bananas'")

#Recibo un nuevo envío de productos y los agrego al inventario 4
inventario.extend(["frutillas", "apio", "papas"])
print(f"{inventario}, 'Despues de recibir el nuevo envio'")

#Verificamos si las papas están en el inventario mediante la siguiente función:5
def verificar_producto(inventario, producto):
    if producto in inventario:
        return f"{producto} está en el inventario."
    else:
        return f"{producto} no está en el inventario."
    
#Verificamos las papas en el inventario
producto_a_verificar = "papas"
print(f"Verificando si {producto_a_verificar} está en el inventario:")
print(verificar_producto(inventario=inventario, producto=producto_a_verificar))

#Ahora removemos un producto del inventario para agregar la nueva fruta "dragonfruit" 6
def remove_producto(inventario, producto):
 if producto in inventario:
   inventario.remove(producto)
   print(f"{producto} ha sido removido del inventario.")
   print(f"{inventario}, 'Así queda el inventario despues de sacar el {producto} del inventario'")
 else:
   print(f"{producto} no está en el inventario.")
   

#Agregamos la nueva fruta "dragonfruit" al inventario 
def agregar_producto(inventario, producto):
    if producto not in inventario:
       inventario.append(producto)
       print(f"{producto} ha sido agregado al inventario.")
    else:
     print(f"{producto} ya está en el inventario.")
     print(f"{inventario}, 'Se agrego la nueva fruta {producto} al inventario'")
    return inventario

#Funciones para remover y agregar los productos 
remove_producto(inventario, "brocoli")
agregar_producto(inventario, "dragonfruit")

#Sería mejor tener el inventario ordenado alfabeticamente y para eso usamos la siguiente función:
def ordenar_inventario(inventario):
    inventario.sort()
    print(f"{inventario}, 'Así queda el inventario ordenado alfabeticamente'")
    return inventario
#Función para ordenar el inventario
ordenar_inventario(inventario)

#Viene un nuevo empleado y le damos una copia del inventario, nos aseguramos de que si hace cambios no se vea afectada la lista original
def copiar_inventario(inventario):
   copiar_inventario = inventario.copy()
   print(f"{copiar_inventario}, 'Copia del inventario para el nuevo empleado'")
   return copiar_inventario
#Creamos la función para copiar el inventario
nuevo_empleado_inventario = copiar_inventario(inventario)

#Si el nuevo empleado quiere agregar un producto lo  hacemos mediante la siguiente función:
def agregar_agregar_prouducto_empleado(inventario_empleado, producto):
   if producto not in inventario_empleado:
      inventario_empleado.append(producto)
      print(f"{producto} ha sido agregado al inventario del empleado.")
   else:
      print(f"{producto} ya está en el inventario del empleado.")
      return inventario_empleado
   