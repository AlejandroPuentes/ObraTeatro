from data.estudiante import Estudiante 
from persistence.conexion import ConexionBD

class EstudianteDAO:

    def __init__(self):
        self.conexion = ConexionBD()

    def guardar(self, id, estudiante, carrera, tipoid):
        conexion = self.conexion.conectar()
        sql = (f'INSERT INTO \"Estudiante\" VALUES' +
                f'({id},' +
                f'{estudiante.identificacion},' +
                f'{carrera},' +
                f'{tipoid},' +
                f"'{estudiante.nombre}'," +
                f"'{estudiante.apellido}'," +
                f"to_date({estudiante.fnacimiento}, 'yyyy-mm-dd')," +             
                f'{estudiante.codigo},'+       
                f"'{estudiante.correo}')")
        cursor = conexion.cursor()
        cursor.execute(sql)
        cursor.execute('commit')
        self.conexion.desconectar()
