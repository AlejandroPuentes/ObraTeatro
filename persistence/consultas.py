from data.estudiante import Estudiante 
from persistence.conexion import ConexionBD

class Consultas:

    def __init__(self):
        self.conexion = ConexionBD()

    def empleados_con_acceso(self):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT DISTINCT "cedula" , "correo" 
                   FROM "Empleado" E, "PersonalObra" P, "Rol" R, "LaborPersonalObra" L
                   WHERE E."codUnidad" = P."codUnidad" AND 
	                     E."icodEmpleado" = P."icodEmpleado" AND 
	                     R."rol" = P."rol" AND 
	                     P."codUnidad" = L."codUnidad" AND 
	                     P."icodEmpleado" = L."icodEmpleado" AND 
	                     P."idPersonalObra" = L."idPersonalObra" AND 
	                     R."rol" = 1 OR 
	                     L."codActividad" = '00018' ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar()

        return resultado

    def encabezado(self, cedula):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT "titulo", E."nombre" || ' ' || E."apellido" nombre 
                   FROM   "Empleado" E, "PersonalObra" P, "Obra" O
                   WHERE  E."codUnidad" = P."codUnidad" AND 
            	          E."icodEmpleado" = P."icodEmpleado" AND 
	                      P."idObra" = O."idObra" AND 
	                      E."cedula" = {cedula} AND 
	                      O."estado" = 1 ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar()
        return resultado
    
    def obtener_fechas_horas(self, titulo):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT O."idObra" id, "conseCalendario" cons, TO_CHAR("horaInicio", 'DD MM YYYY HH24 MI') inicio, TO_CHAR("horaFin", 'DD MM YYYY HH24 MI') fin
                   FROM "Calendario" C, "Obra" O 
                   WHERE O."idObra" = C."idObra" AND 
	                     O."titulo" = '{titulo}' 
                         ORDER BY inicio ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return resultado

    def asistentes_obra(self, id_obra):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT E."nombre" || ' ' || E."apellido" estudiante 
                   FROM "Estudiante" E, "PersonajeEstudiante" PE, "Personaje" P, "Obra" O 
                   WHERE E."CodEstudiante" = PE."CodEstudiante" AND 
	                     P."idObra" = PE."idObra" AND 
	                     P."idPersonaje" = PE."idPersonaje" AND 
	                     O."idObra" = P."idObra" AND 
	                     O."idObra" = {int(id_obra)} ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return resultado
    def obras_inactivas(self, cedula):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT O."idObra" id, "titulo" obra 
                   FROM   "Empleado" E, "PersonalObra" P, "Obra" O
                   WHERE  E."codUnidad" = P."codUnidad" AND 
	                      E."icodEmpleado" = P."icodEmpleado" AND 
	                      P."idObra" = O."idObra" AND 
	                      E."cedula" = '{cedula}' AND 
	                      O."estado" = 0 ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 

    def estudiantes_viaticos(self, id_obra):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT E."nombre" || ' ' || E."apellido" estudiante, "correo","descTipoCalen" tipo, TO_NUMBER(TO_CHAR("horaFin", 'HH24')) - TO_NUMBER(TO_CHAR("horaInicio", 'HH24')) horas
                   FROM "Estudiante" E, "AsistenciaEstudiante" A, "Calendario" C, "TipoCalendario" T
                   WHERE E."CodEstudiante" = A."CodEstudiante" AND 
                         C."idObra" = A."idObra" AND 
	                     C."conseCalendario" = A."conseCalendario" AND 
	                     T."idTipoCalen" = C."idTipoCalen" AND 
	                     A."idObra" = {id_obra} ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return resultado
        


        