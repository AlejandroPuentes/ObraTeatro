
class Estudiante:

    registrados = 0

    def __init__(self,nombre,apellido,identificacion,fnacimiento,codigo,correo):
        self.nombre = nombre
        self.apellido  = apellido
        self.identificacion = identificacion
        self.fnacimiento = fnacimiento
        self.codigo = codigo
        self.correo = correo
        Estudiante.registrados += 1