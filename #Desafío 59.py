#Desafío 59
#Diseña una clase LibroDigital que herede de Libro y añada atributos como formato (e.g., PDF, EPUB) y tamaño_archivo.
#Además, implementa una subclase EBook que sobrescriba un método para mostrar información específica, como enlaces de descarga.

class Libro:
  def __init__(self, titulo, autor, año_publicacion):
      self.titulo = titulo
      self.autor = autor
      self.año_publicacion = año_publicacion
  
  def mostrar_informacion(self):
      return f"Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.año_publicacion}"


class LibroDigital(Libro):
  def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo):
      super().__init__(titulo, autor, año_publicacion)
      self.formato = formato
      self.tamaño_archivo = tamaño_archivo
  
  def mostrar_informacion(self):
      info_base = super().mostrar_informacion()
      return f"{info_base}\nFormato: {self.formato}\nTamaño del archivo: {self.tamaño_archivo}"


class EBook(LibroDigital):
  def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo, enlaces_descarga):
      super().__init__(titulo, autor, año_publicacion, formato, tamaño_archivo)
      self.enlaces_descarga = enlaces_descarga
  
  def mostrar_informacion(self):
      info_libro = super().mostrar_informacion()
      return f"{info_libro}\nEnlaces de descarga: {', '.join(self.enlaces_descarga)}"


# Ejemplo de uso
if __name__ == "__main__":
  libro_digital = LibroDigital(
      titulo="Cien años de soledad",
      autor="Gabriel García Márquez",
      año_publicacion=1967,
      formato="PDF",
      tamaño_archivo="2.5 MB"
  )
  
  ebook = EBook(
      titulo="El Principito",
      autor="Antoine de Saint-Exupéry",
      año_publicacion=1943,
      formato="EPUB",
      tamaño_archivo="1.2 MB",
      enlaces_descarga=["https://example.com/el-principito.epub", "https://example.com/el-principito.mobi"]
  )
  
  print("=== Información del Libro Digital ===")
  print(libro_digital.mostrar_informacion())
  
  print("\n=== Información del eBook ===")
  print(ebook.mostrar_informacion())
    
