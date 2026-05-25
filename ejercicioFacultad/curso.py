class Curso:
    def __init__(self, nombre_curso, codigo_curso, profesor, capacidad):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.profesor = profesor
        self.capacidad = capacidad
        self.lista_estudiantes = []

    @property
    def cupos_disponibles(self):
        return self.capacidad - len(self.lista_estudiantes)

    def __str__(self):
        return (f"[{self.codigo_curso}] {self.nombre_curso} "
                f"Profesor: {self.profesor} "
                f"Inscriptos: {len(self.lista_estudiantes)}/{self.capacidad} "
                f"Cupos disponibles: {self.cupos_disponibles}")
