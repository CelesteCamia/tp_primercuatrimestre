print(
    " 0: Salir\n"
    " 1: Agregar Libro\n"
    " 2: Agregar Miembro\n"
    " 3: Mostrar Libros\n"
    " 4: Mostrar Miembros\n"
    " 5: Prestar Libro\n"
    " 6: Devolver Libro\n"
    " 7: Consulta Estado Libro\n"
    " 8: Consulta Libros de un Miembro"
)


class Libro:

    def __init__(self, titulo, autor, isbn):
        self.__titulo   = titulo
        self.__autor    = autor
        self.__isbn     = isbn
        self.__prestado = False

    def getTitulo(self):   return self.__titulo
    def getAutor(self):    return self.__autor
    def getIsbn(self):     return self.__isbn
    def getPrestado(self): return self.__prestado

    def setPrestado(self, estado: bool):
        self.__prestado = estado


class Miembro:

    def __init__(self, dni, nombre):
        self.__dni           = dni
        self.__nombre        = nombre
        self.__librosSacados = []

    def getNombre(self): return self.__nombre
    def getDni(self):    return self.__dni

    def agregarLibro(self, libro):
        self.__librosSacados.append(libro)

    def quitarLibro(self, isbn):
        self.__librosSacados = [
            l for l in self.__librosSacados if l.getIsbn() != isbn
        ]

    def getLibros(self):
        return self.__librosSacados

class Biblioteca:

    def __init__(self):
        self.__libros   = []
        self.__miembros = []

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def agregarMiembro(self, miembro):
        self.__miembros.append(miembro)

    def buscarLibro(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn:
                return libro
        return None

    def buscarMiembro(self, dni):
        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                return miembro
        return None

    def getLibros(self):
        if not self.__libros:
            print("No hay libros registrados.")
            return
        for libro in self.__libros:
            estado = "Prestado" if libro.getPrestado() else "Disponible"
            print(f"  Título: {libro.getTitulo()} | Autor: {libro.getAutor()} | ISBN: {libro.getIsbn()} | Estado: {estado}")

    def getMiembros(self):
        if not self.__miembros:
            print("No hay miembros registrados.")
            return
        for miembro in self.__miembros:
            libros = miembro.getLibros()
            lista  = ", ".join(l.getTitulo() for l in libros) if libros else "Ninguno"
            print(f"  Miembro: {miembro.getNombre()} | DNI: {miembro.getDni()} | Libros prestados: {lista}")

    def prestarLibro(self, isbn, dni):
        libro   = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is None:
            print("Error: libro no encontrado.")
            return
        if miembro is None:
            print("Error: miembro no encontrado.")
            return
        if libro.getPrestado():
            print(f"Error: el libro '{libro.getTitulo()}' ya está prestado.")
            return

        libro.setPrestado(True)
        miembro.agregarLibro(libro)
        print(f"Libro '{libro.getTitulo()}' prestado a {miembro.getNombre()}.")

    def devolverLibro(self, isbn, dni):
        libro   = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)

        if libro is None:
            print("Error: libro no encontrado.")
            return
        if miembro is None:
            print("Error: miembro no encontrado.")
            return
        if not libro.getPrestado():
            print(f"Error: el libro '{libro.getTitulo()}' no está prestado.")
            return

        libro.setPrestado(False)
        miembro.quitarLibro(isbn)
        print(f"Libro '{libro.getTitulo()}' devuelto por {miembro.getNombre()}.")

    def consultaEstadoLibro(self, isbn):
        libro = self.buscarLibro(isbn)
        if libro is None:
            print("No se encontró el libro.")
            return

        if libro.getPrestado():
            for miembro in self.__miembros:
                for lib in miembro.getLibros():
                    if lib.getIsbn() == isbn:
                        print(f"El libro '{libro.getTitulo()}' está prestado a {miembro.getNombre()} (DNI: {miembro.getDni()}).")
                        return
            print(f"El libro '{libro.getTitulo()}' está prestado (miembro no identificado).")
        else:
            print(f"El libro '{libro.getTitulo()}' está disponible.")

    def consultaLibrosMiembro(self, dni):
        miembro = self.buscarMiembro(dni)
        if miembro is None:
            print("No se encontró el miembro.")
            return

        libros = miembro.getLibros()
        if not libros:
            print(f"{miembro.getNombre()} no tiene libros prestados.")
            return

        print(f"Libros prestados a {miembro.getNombre()}:")
        for libro in libros:
            print(f"  Título: {libro.getTitulo()} | Autor: {libro.getAutor()} | ISBN: {libro.getIsbn()}")


def pedirOpcion():

    while True:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: ingrese un número entero válido.")


def pedirTexto(mensaje):

    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                raise ValueError("El campo no puede estar vacío.")
            return valor
        except ValueError as e:
            print(f"Error: {e}")


biblioteca = Biblioteca()
opcion = pedirOpcion()

while opcion != 0:

    if opcion == 1:
        titulo = pedirTexto("Ingrese el título del libro: ")
        autor  = pedirTexto("Ingrese el autor del libro: ")
        isbn   = pedirTexto("Ingrese el ISBN del libro: ")
        biblioteca.agregarLibro(Libro(titulo, autor, isbn))
        print("Libro agregado.")

    elif opcion == 2:
        dni    = pedirTexto("Ingrese el DNI del miembro: ")
        nombre = pedirTexto("Ingrese el nombre del miembro: ")
        biblioteca.agregarMiembro(Miembro(dni, nombre))
        print("Miembro agregado.")

    elif opcion == 3:
        biblioteca.getLibros()

    elif opcion == 4:
        biblioteca.getMiembros()

    elif opcion == 5:
        dni  = pedirTexto("Ingrese el DNI del miembro: ")
        isbn = pedirTexto("Ingrese el ISBN del libro: ")
        biblioteca.prestarLibro(isbn, dni)

    elif opcion == 6:
        isbn = pedirTexto("Ingrese el ISBN del libro: ")
        dni  = pedirTexto("Ingrese el DNI del miembro: ")
        biblioteca.devolverLibro(isbn, dni)

    elif opcion == 7:
        isbn = pedirTexto("Ingrese el ISBN del libro: ")
        biblioteca.consultaEstadoLibro(isbn)

    elif opcion == 8:
        dni = pedirTexto("Ingrese el DNI del miembro: ")
        biblioteca.consultaLibrosMiembro(dni)

    else:
        print("Opción inválida.")

    opcion = pedirOpcion()

print("Fin del programa")