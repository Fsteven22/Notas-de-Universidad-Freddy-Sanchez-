from Conexion import *

class CClientes:

    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from Cliente;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))

    def ingresarClientes(direccion,correo,tipo):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into Cliente(Direccion,Correo,Tipo) values (%s,%s,%s);"
            valores = (direccion,correo,tipo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Ingresado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
    
    def modificarClientes(id,direccion,correo,tipo):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "update Cliente set Cliente.Direccion=%s, Cliente.Correo=%s, Cliente.Tipo=%s where ID_Cliente=%s;"
            valores = (direccion,correo,tipo,id)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))

    def eliminarClientes(id):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "delete from Cliente where Cliente.ID_Cliente=%s"
            valores = (id,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de eliminacion de datos {}".format(error))

   
    def seleccionarCliente(id):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "select * from Cliente where Cliente.ID_Cliente=%s"
            valores = (id,)
            cursor.execute(sql,valores)
            miResultado = cursor.fetchall()
            cone.commit()
            print(cursor.rowcount,"Mostrando al cliente seleccionado")
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de seleccion de cliente {}".format(error))
          