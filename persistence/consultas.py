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

    def info_docente(self, cedula):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT E."nombre" || ' ' || E."apellido" docente, "correo" 
                   FROM "Empleado" E 
                   WHERE "cedula" = '{cedula}' ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar()
        return resultado

    def obra_activa(self, cedula):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT O."idObra", "titulo"
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
    
    def obtener_fechas_horas(self, idobra):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT O."idObra" id, "conseCalendario" cons, TO_CHAR("horaInicio", 'DD MM YYYY HH24 MI') inicio, TO_CHAR("horaFin", 'DD MM YYYY HH24 MI') fin
                   FROM "Calendario" C, "Obra" O 
                   WHERE O."idObra" = C."idObra" AND 
	                     O."idObra" = '{idobra}' 
                         ORDER BY inicio ''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return resultado

    def asistentes_obra(self, id_obra, conscal):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT E."CodEstudiante", E."nombre" || ' ' || E."apellido" estudiante 
                   FROM "Estudiante" E, "PersonajeEstudiante" PE, "Personaje" P, "Obra" O 
                   WHERE E."CodEstudiante" = PE."CodEstudiante" AND 
                         P."idObra" = PE."idObra" AND 
                         P."idPersonaje" = PE."idPersonaje" AND 
                         O."idObra" = P."idObra" AND 
                         O."idObra" = {id_obra} AND
                         E."CodEstudiante" NOT IN (SELECT "CodEstudiante" FROM "AsistenciaEstudiante" WHERE "conseCalendario" = {conscal}) ''')
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
        return resultado

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

    def actualizar_asistencia(self, casis, code, idobra, ccal):
        conexion = self.conexion.conectar()
        sql = (f'''INSERT INTO "AsistenciaEstudiante" VALUES({casis}, {code}, {idobra}, {ccal})''')
        cursor = conexion.cursor()
        cursor.execute(sql)
        cursor.execute('commit')
        self.conexion.desconectar()

    def consecutivo_asistencia(self):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT  count(A."consecAsis")
                   FROM "AsistenciaEstudiante" A''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return int(resultado[0][0])

    def pdfviatico(self,idObra):
        conexion = self.conexion.conectar()
        sql = (f'''SELECT E."nombre" || ' ' || E."apellido" estudiante, E."correo" correo, E."CodEstudiante",count("consecAsis") sesiones, SUM(TO_NUMBER(TO_CHAR("horaFin", 'HH24')) - TO_NUMBER(TO_CHAR("horaInicio", 'HH24'))) horas
                    FROM "Estudiante" E, "AsistenciaEstudiante" A, "Calendario" C, "TipoCalendario" T
                    WHERE E."CodEstudiante" = A."CodEstudiante" AND 
                        C."idObra" = A."idObra" AND 
                        C."conseCalendario" = A."conseCalendario" AND 
                        T."idTipoCalen" = C."idTipoCalen" AND 
                        A."idObra" = {int(idObra)}
                    GROUP BY E."nombre" || ' ' || E."apellido", E."correo", E."CodEstudiante"''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return resultado

    def estudianteObra(self, codi):
        conexion = self.conexion.conectar()
        sql = (f'''Select O."idObra" ,O."titulo" 
                    from  "PersonajeEstudiante" E, "Personaje" P, "Obra" O
                    where E."idPersonaje" = P."idPersonaje" and 
                        E."idObra" = P."idObra" and 
                        O."idObra" = P."idObra" AND
                        E."CodEstudiante"={codi} and
                        O."estado"= 0''')
        cursor = conexion.cursor()
        resultado = list(cursor.execute(sql))
        self.conexion.desconectar() 
        return resultado
        


        