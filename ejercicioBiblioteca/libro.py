class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__prestado = False
        self.__miembro = None

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    def getPrestado(self):
        return self.__prestado

    def getMiembro(self):
        return self.__miembro

    def prestar(self, miembro):
        self.__prestado = True
        self.__miembro = miembro

    def devolver(self):
        self.__prestado = False
        self.__miembro = None

    def __str__(self):
        estado = f"Prestado a: {self.__miembro.getNombre()}" if self.__prestado else "Disponible"
        return f"[{self.__isbn}] '{self.__titulo}' — {self.__autor} | {estado}"
