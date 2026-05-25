class Estudiante:
    _contador_id = 1

    def __init__(self, nombre, apellido, numero_matricula, carrera):
        self.id = Estudiante._contador_id
        Estudiante._contador_id += 1
        self.nombre = nombre
        self.apellido = apellido
        self.numero_matricula = numero_matricula
        self.carrera = carrera
        self.cursos_inscriptos = []

    def __str__(self):
        cursos = [c.nombre_curso for c in self.cursos_inscriptos]
        cursos_str = ", ".join(cursos) if cursos else "Ninguno"
        return (f"[ID: {self.id}] {self.nombre} {self.apellido} "
                f"Matrícula: {self.numero_matricula} "
                f"Carrera: {self.carrera} "
                f"Cursos: {cursos_str}")
