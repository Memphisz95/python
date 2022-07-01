class Alumno:
    nombre = None
    nota = None

    def getNombre(self, nombre):
        self.nombre = nombre

    def getNota(self, nota):
        self.nota = nota

    def comprobarNota(self):
        if self.nota < 5 and self.nota >= 0:
            return 'Suspendido'
        elif self.nota > 5 and self.nota <= 10:
            return 'Aprobado'
        else:
            return 'Esta nota no existe'

a = Alumno()
a.getNombre('Adrian')
a.getNota(10)
print('Nombre del alumno:', a.nombre)
print('Nota de', a.nombre, ':', a.nota)
print(a.comprobarNota())