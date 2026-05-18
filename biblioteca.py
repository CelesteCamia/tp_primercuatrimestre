#cambio para pushear
print(" 0: Salir \n 1: Agregar Libro \n 2: Agregar Miembro  \n 3: Mostrar Libros \n 4: Mostrar Miembros \n 5: Prestar Libros \n 6: Devolver Libros \n 7: Consulta Estado Libros \n 8: Consulta Libros Miembros")


class Biblioteca:
    def __init__(self, libros, miembros):
        self.__libros = []
        self.__miembros = []

    def agregarMiembro(self, miembro):
        self.__miembros.append(miembro)

    def agregarLibros(self, libro):
        self.__libros.append(libro)
      

    def getMiembros(self):
        for miembro in self.__miembros:
            print (f"Miembro: {miembro.getNombre()}, DNI: {miembro.getDni()}")

    def getLibros(self):
        for libro in self.__libros:
             print(f"Titulo: {libro.getTitulo()}, Autor: {libro.getAutor()}")

    def buscarLibro(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn:
                return libro
    def buscarMiembro(self, dni):
        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                return miembro
    
    def prestarLibro(self, isbn, dni):
      libro = self.buscarLibro(isbn)
      miembro = self.buscarMiembro(dni)

      if libro is not None and miembro is not None:
        if not libro.getPrestado():
          libro.setPrestado()
          miembro.agregarLibro(libro.getIsbn())

        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                miembro.agregarLibro(libro)
    
    def devolverLibro(self, isbn, dni):
        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is not None and miembro is not None:
            if libro.getPrestado():
                libro.setPrestado()
    
    def consultaEstadoLibros(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn :
                if libro.getPrestado():
                    print(f"El libro {libro.getTitulo()} esta prestado")
                else:
                    print(f"El libro {libro.getTitulo()} esta disponible")
            else:
                print(f"No se encontro libro")

    def consultaLibrosMiembros(self, dni):
        miembro = self.buscarMiembro(dni)
        if miembro is not None:
          for li1bro in miembro.getLibros():
            for lib in self.__libros:
              if libro == lib.getIsbn():    
                print(f"Titulo: {lib.getTitulo()}, Autor: {lib.getAutor()}")

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__prestado = False
        

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getIsbn(self):
        return self.__isbn
    
    def getPrestado(self):
        return self.__prestado

    def setPrestado(self):
         self.__prestado = True if self.__prestado == False else False

class Miembro:
    def __init__(self, dni, nombre):
        self.__dni = dni
        self.__nombre = nombre
        self.__libroSacado = []

    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def agregarLibro(self, libro):
        self.__libroSacado.append(libro)
    
    def getLibros(self):
        return self.__libroSacado

biblioteca = Biblioteca([], [])

opcion = int(input("Seleccione una opcion: "))

while (opcion != 0):

  if(opcion == 1):
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el isbn del libro: ")
    libro = Libro( titulo, autor, isbn)
    biblioteca.agregarLibros(libro)
    print ("Libro agregado")  
    opcion = int(input("Seleccione una opcion: "))

  elif(opcion == 2):
    dni = input("Ingrese el dni del miembro: ")
    nombre = input("Ingrese el nombre del miembro: ")
    miembro = Miembro(dni, nombre)
    biblioteca.agregarMiembro(miembro)
    print ("Miembro agregado") 
    opcion = int(input("Seleccione una opcion: "))

  elif(opcion  == 3):
    biblioteca.getLibros()
    opcion = int(input("Seleccione una opcion: "))

  elif(opcion == 4):
    biblioteca.getMiembros()
    opcion = int(input("Seleccione una opcion: "))
  
  elif(opcion == 5):
    dni = input("Ingrese el dni del miembro: ")
    isbn = input("Ingrese el isbn del libro: ")
    biblioteca.prestarLibro(isbn, dni)
    print ("Libro prestado")
    opcion = int(input("Seleccione una opcion: "))
  
  elif(opcion == 6):
    isbn = input("Ingrese el isbn del libro: ")
    dni = input("Ingrese el dni del miembro: ")
    biblioteca.devolverLibro(isbn, dni)
    print ("Libro devuelto")
    opcion = int(input("Seleccione una opcion: "))
  
  elif(opcion == 7):
    isbn = input("Ingrese el isbn del libro: ")
    biblioteca.consultaEstadoLibros(isbn)
    opcion = int(input("Seleccione una opcion: "))
  
  elif(opcion == 8):
    dni = input("Ingrese el dni del miembro: ")
    biblioteca.consultaLibrosMiembros(dni)
    opcion = int(input("Seleccione una opcion: "))