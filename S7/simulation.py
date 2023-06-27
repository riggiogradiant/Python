import snap7
import snap7.common
from snap7.util import *
import snap7
print(snap7.__version__)
# from snap7 import snap7types

# from snap7.snap7types import *

# Crear un servidor
server = snap7.server.Server()

server.start_to('127.0.0.1', 2000)  # Puerto local para la conexión

# Iniciar el servidor
server.start()

print("Server creado en la dirección 127.0.0.1 en el puerto 2000")
#---------------------------------
# Crear una base de datos en el servidor
db_number = 1
db_size = 10  # Tamaño de la base de datos (en bytes)

# Escribir una lista vacía para crear la base de datos
server.create_area(snap7.types.Areas.DB, db_number, db_size)

print("Base de datos DB{} creada en el servidor".format(db_number))
#---------------------------------

# Crear un cliente
client = snap7.client.Client()
try:
    # Intentar conectar al servidor
    client.connect("127.0.0.1", 0, 0, 2000)  # Conectar al servidor [IP, Puerto, Slot]
    print("Cliente conectado al servidor")
    
#     # Crear una base de datos simulada
#     db_number = 1
#     db_size = 10
#     server.create_area(snap7.types.Areas.DB, db_number, db_size)
#     print("Base de datos DB{} creada en el servidor".format(db_number))
    
    
except Exception as e:
    # Manejar la excepción si ocurre algún error durante la conexión
    print("Error al conectar al servidor:", str(e))

#Desconectar el cliente
client.disconnect()

# Detener el servidor
server.stop()