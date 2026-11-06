import mysql.connector

class CConexion:
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',password='johnc1to',
                                               host='127.0.0.1',
                                               database='importtrack',
                                               port='3306')
            print("Conexion Correcta")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos {}".format(error))
            return conexion
    ConexionBaseDeDatos()