#Desafío 62
#Crea una clase Musico que tenga un método instrumento
#Y crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. Instancia objetos de estas clases y demuestra el polimorfismo.

class Musico:
    def instrumento(self):
        return "Instrumento genérico"

class Guitarrista(Musico):
    def instrumento(self):
        return "Guitarra"

class Baterista(Musico):
    def instrumento(self):
        return "Batería"

# Crear instancias de las clases
musico = Musico()
guitarrista = Guitarrista()
baterista = Baterista()

# Demostrar el polimorfismo
print(musico.instrumento())
print(guitarrista.instrumento())
print(baterista.instrumento())


    