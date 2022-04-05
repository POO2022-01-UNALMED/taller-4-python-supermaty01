from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if (asignaturas is None): 
            asignaturas = []
        if (estudiantes is None): 
            estudiantes = []
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def __str__(self):
        if self._grupo == "grupo ordinado":
            return "Grupo de estudiantes: grupo predeterminado"
        else:
            return "Grupo de estudiantes: " + self.grupo
            
    
    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

