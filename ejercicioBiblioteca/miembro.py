class Miembro:
    def __init__(self, dni, nombre):
        self.__dni = dni
        self.__nombre = nombre
        self.__librosPrestados = []

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def agregarLibro(self, libro):
        self.__librosPrestados.append(libro)

    def quitarLibro(self, libro):
        self.__librosPrestados.remove(libro)

    def getLibros(self):
        return self.__librosPrestados

    def __str__(self):
        if self.__librosPrestados:
            titulos = ", ".join(
                f"'{l.getTitulo()}'" for l in self.__librosPrestados)
        else:
            titulos = "Ninguno"
        return f"[{self.__dni}] {self.__nombre} | Libros: {titulos}"
