from data.estudiante import Estudiante 
from persistence.conexion import ConexionBD

class EstudianteDAO:

    def __init__(self):
        self.conexion = ConexionBD()

    def guardar(self, estudiante:Estudiante, carrera, tipoid):
        conexion = self.conexion.conectar()
        sql = (f'INSERT INTO \"Estudiante\" VALUES' +
                f'({estudiante.identificacion},' +
                f'{carrera},' +
                f'{tipoid},' +
                f"'{estudiante.nombre}'," +
                f"'{estudiante.apellido}'," +
                f'{estudiante.fnacimiento},' +             
                f'{estudiante.codigo},'+       
                f"'{estudiante.correo}')")
        print(sql)
        conexion.cursor().execute(sql)
        conexion.desconectar()
