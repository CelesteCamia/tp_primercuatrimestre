from libro import Libro
from miembro import Miembro


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__miembros = []

    def _buscarLibro(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn:
                return libro
        raise LookupError(f"No se encontró ningún libro con ISBN '{isbn}'.")

    def _buscarMiembro(self, dni):
        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                return miembro
        raise LookupError(f"No se encontró ningún miembro con DNI '{dni}'.")

    def agregarLibro(self, titulo, autor, isbn):
        try:
            for libro in self.__libros:
                if libro.getIsbn() == isbn:
                    raise ValueError(f"Ya existe un libro con ISBN '{isbn}'.")
            libro = Libro(titulo, autor, isbn)
            self.__libros.append(libro)
            print(f"Libro agregado: '{titulo}'.")
        except ValueError as e:
            print(f"{e}")

    def agregarMiembro(self, dni, nombre):
        try:
            for miembro in self.__miembros:
                if miembro.getDni() == dni:
                    raise ValueError(f"Ya existe un miembro con DNI '{dni}'.")
            miembro = Miembro(dni, nombre)
            self.__miembros.append(miembro)
            print(f"Miembro agregado: {nombre}.")
        except ValueError as e:
            print(f"{e}")

    def prestarLibro(self, isbn, dni):
        try:
            libro = self._buscarLibro(isbn)
            miembro = self._buscarMiembro(dni)
            if libro.getPrestado():
                raise PermissionError(
                    f"'{libro.getTitulo()}' ya está prestado a {libro.getMiembro().getNombre()}."
                )
            libro.prestar(miembro)
            miembro.agregarLibro(libro)
            print(f"'{libro.getTitulo()}' prestado a {miembro.getNombre()}.")
        except (LookupError, PermissionError) as e:
            print(f"{e}")

    def devolverLibro(self, isbn, dni):
        try:
            libro = self._buscarLibro(isbn)
            miembro = self._buscarMiembro(dni)
            if not libro.getPrestado():
                raise PermissionError(
                    f"'{libro.getTitulo()}' no está prestado actualmente.")
            if libro.getMiembro().getDni() != dni:
                raise PermissionError(
                    f"'{libro.getTitulo()}' no fue prestado a {miembro.getNombre()}."
                )
            miembro.quitarLibro(libro)
            libro.devolver()
            print(f"'{libro.getTitulo()}' devuelto por {miembro.getNombre()}.")
        except (LookupError, PermissionError) as e:
            print(f"{e}")

    def consultarEstadoLibros(self):
        print(" ESTADO DE LIBROS")
        if not self.__libros:
            print("  No hay libros registrados.")
        else:
            for libro in self.__libros:
                print(f"  {libro}")

    def consultarEstadoMiembros(self):
        print("  ESTADO DE MIEMBROS")
        if not self.__miembros:
            print("  No hay miembros registrados.")
        else:
            for miembro in self.__miembros:
                print(f"  {miembro}")


def mostrarMenu():
    print("\n 0: Salir")
    print(" 1: Agregar Libro")
    print(" 2: Agregar Miembro")
    print(" 3: Mostrar Libros")
    print(" 4: Mostrar Miembros")
    print(" 5: Prestar Libro")
    print(" 6: Devolver Libro")


biblioteca = Biblioteca()

mostrarMenu()

try:
    opcion = int(input("\nSeleccione una opción: "))
except ValueError:
    print("Opción inválida.")
    opcion = -1

while opcion != 0:

    if opcion == 1:
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        biblioteca.agregarLibro(titulo, autor, isbn)

    elif opcion == 2:
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        biblioteca.agregarMiembro(dni, nombre)

    elif opcion == 3:
        biblioteca.consultarEstadoLibros()

    elif opcion == 4:
        biblioteca.consultarEstadoMiembros()

    elif opcion == 5:
        dni = input("DNI del miembro: ")
        isbn = input("ISBN del libro: ")
        biblioteca.prestarLibro(isbn, dni)

    elif opcion == 6:
        isbn = input("ISBN del libro: ")
        dni = input("DNI del miembro: ")
        biblioteca.devolverLibro(isbn, dni)

    else:
        print("Opción no válida.")

    mostrarMenu()
    try:
        opcion = int(input("\n Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        opcion = -1

print("\n ¡Hasta luego!")
