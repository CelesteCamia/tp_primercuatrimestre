from estudiante import Estudiante
from curso import Curso


class Facultad:
    def __init__(self, nombre="Facultad"):
        self.nombre = nombre
        self.lista_estudiantes = []
        self.lista_cursos = []

    def _buscar_estudiante(self, numero_matricula):
        for e in self.lista_estudiantes:
            if e.numero_matricula == numero_matricula:
                return e
        raise LookupError(
            f"No se encontró ningún estudiante con matrícula '{numero_matricula}'.")

    def _buscar_curso(self, codigo_curso):
        for c in self.lista_cursos:
            if c.codigo_curso == codigo_curso:
                return c
        raise LookupError(
            f"No se encontró ningún curso con código '{codigo_curso}'.")

    def agregar_estudiante(self, nombre, apellido, numero_matricula, carrera):
        try:
            for e in self.lista_estudiantes:
                if e.numero_matricula == numero_matricula:
                    raise ValueError(
                        f"Ya existe un estudiante con la matrícula '{numero_matricula}'.")
            estudiante = Estudiante(
                nombre, apellido, numero_matricula, carrera)
            self.lista_estudiantes.append(estudiante)
            print(
                f"Estudiante registrado: {estudiante.nombre} {estudiante.apellido} (ID: {estudiante.id})")
            return estudiante
        except ValueError as e:
            print(f"{e}")
            return None

    def agregar_curso(self, nombre_curso, codigo_curso, profesor, capacidad):
        try:
            for c in self.lista_cursos:
                if c.codigo_curso == codigo_curso:
                    raise ValueError(
                        f"Ya existe un curso con el código '{codigo_curso}'.")
            curso = Curso(nombre_curso, codigo_curso, profesor, capacidad)
            self.lista_cursos.append(curso)
            print(
                f"Curso registrado: {curso.nombre_curso} ({curso.codigo_curso})")
            return curso
        except ValueError as e:
            print(f"{e}")
            return None

    def inscribir_estudiante(self, numero_matricula, codigo_curso):
        try:
            estudiante = self._buscar_estudiante(numero_matricula)
            curso = self._buscar_curso(codigo_curso)
            if estudiante in curso.lista_estudiantes:
                raise PermissionError(
                    f"{estudiante.nombre} {estudiante.apellido} ya está inscripto en '{curso.nombre_curso}'.")
            if curso.cupos_disponibles == 0:
                raise PermissionError(
                    f"El curso '{curso.nombre_curso}' está lleno (capacidad máxima: {curso.capacidad}).")
            curso.lista_estudiantes.append(estudiante)
            estudiante.cursos_inscriptos.append(curso)
            print(
                f"{estudiante.nombre} {estudiante.apellido} inscripto en '{curso.nombre_curso}'.")
            return True
        except (LookupError, PermissionError) as e:
            print(f"{e}")
            return False

    def dar_baja_estudiante(self, numero_matricula, codigo_curso):
        try:
            estudiante = self._buscar_estudiante(numero_matricula)
            curso = self._buscar_curso(codigo_curso)
            if estudiante not in curso.lista_estudiantes:
                raise PermissionError(
                    f"{estudiante.nombre} {estudiante.apellido} no está inscripto en '{curso.nombre_curso}'.")
            curso.lista_estudiantes.remove(estudiante)
            estudiante.cursos_inscriptos.remove(curso)
            print(
                f"{estudiante.nombre} {estudiante.apellido} dado de baja de '{curso.nombre_curso}'.")
            return True
        except (LookupError, PermissionError) as e:
            print(f"{e}")
            return False

    def consultar_cursos(self):
        print(f"  ESTADO DE CURSOS — {self.nombre}")
        if not self.lista_cursos:
            print("  No hay cursos registrados.")
        else:
            for curso in self.lista_cursos:
                print(f"  {curso}")
                for est in curso.lista_estudiantes:
                    print(
                        f"  {est.nombre} {est.apellido} (Matrícula: {est.numero_matricula})")

    def consultar_estudiantes(self):
        print(f"  ESTADO DE ESTUDIANTES — {self.nombre}")
        if not self.lista_estudiantes:
            print("  No hay estudiantes registrados.")
        else:
            for estudiante in self.lista_estudiantes:
                print(f"  {estudiante}")


def mostrar_menu():
    print("\n 0: Salir")
    print(" 1: Agregar Estudiante")
    print(" 2: Agregar Curso")
    print(" 3: Inscribir Estudiante")
    print(" 4: Dar Baja Estudiante")
    print(" 5: Consultar Cursos")
    print(" 6: Consultar Estudiantes")


if __name__ == "__main__":

    facultad = Facultad("Facultad de Ingeniería")
    mostrar_menu()

    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        opcion = -1

    while opcion != 0:

        if opcion == 1:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            matricula = input("Número de matrícula: ")
            carrera = input("Carrera: ")
            facultad.agregar_estudiante(nombre, apellido, matricula, carrera)

        elif opcion == 2:
            nombre_curso = input("Nombre del curso: ")
            codigo = input("Código del curso: ")
            profesor = input("Profesor: ")
            try:
                capacidad = int(input("Capacidad máxima: "))
            except ValueError:
                print("La capacidad debe ser un número entero.")
                capacidad = None
            if capacidad is not None:
                facultad.agregar_curso(
                    nombre_curso, codigo, profesor, capacidad)

        elif opcion == 3:
            matricula = input("Número de matrícula del estudiante: ")
            codigo = input("Código del curso: ")
            facultad.inscribir_estudiante(matricula, codigo)

        elif opcion == 4:
            matricula = input("Número de matrícula del estudiante: ")
            codigo = input("Código del curso: ")
            facultad.dar_baja_estudiante(matricula, codigo)

        elif opcion == 5:
            facultad.consultar_cursos()

        elif opcion == 6:
            facultad.consultar_estudiantes()

        else:
            print("Opción no válida.")

        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            opcion = -1

    print("\n ¡Hasta luego!")
