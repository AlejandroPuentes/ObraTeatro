import cx_Oracle

class ConexionBD:

    def __init__(self, clave='clave01', usuario='usuario01'):
        self.clave = clave
        self.usuario = usuario
        self.conexion = None
        


    def conectar(self):
        
        self.conexion =  cx_Oracle.connect(user=self.usuario,  password=self.clave,
                               dsn="127.0.0.1")
        return self.conexion

    def desconectar(self):
        if self.conexion != None:
            self.conexion.close()