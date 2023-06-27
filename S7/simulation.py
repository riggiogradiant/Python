import snap7
import snap7.common
from snap7.util import *
import snap7

# Crear un servidor
server = snap7.server.Server()
server.start_to('127.0.0.1', 2000)

# Iniciar el servidor
server.start()
print("Server creado en la dirección 127.0.0.1 en el puerto 2000")


# Crear un cliente
client = snap7.client.Client()
try:
    # Intentar conectar al servidor
    client.connect("127.0.0.1", 0, 0, 2000)  #(IP, Puerto, Slot)
    print("Cliente conectado al servidor")
        
except Exception as e:
    print("Error al conectar al servidor:", str(e))

#Desconectar el cliente
client.disconnect()

# Detener el servidor
server.stop()

# import snap7
# from snap7 import common
# from snap7.server import Server


# class Server(snap7.server.Server):

#     def __init__(self):
#         super().__init__()

#         self._db_list = []

#     def create_db(self, db_number, db_size):
#         """Creates a database on the server.

#         Args:
#             db_number: The number of the database to create.
#             db_size: The size of the database in bytes.
#         """

#         if not 0 <= db_number <= 125:
#             raise ValueError("Database number must be between 0 and 125")

#         if db_size < 0:
#             raise ValueError("Database size must be non-negative")

#         self._db_list.append(snap7.server.DB(db_number, db_size))


# # Create a server
# server = Server()

# # Create a database in the server
# db_number = 1
# db_size = 10  # Database size (in bytes)

# # Write an empty list to create the database
# server.create_db(db_number, db_size)

# print("Database DB{} created in the server".format(db_number))

# # Start the server
# server.start()
# print("Server started")

# # Create a client
# client = snap7.client.Client()
# try:
#     # Try to connect to the server
#     client.connect("127.0.0.1", 0, 0, 2000)  # (IP, Port, Slot)
#     print("Client connected to the server")

#     # Get the value of the first byte in the database
#     value = client.read_area(snap7.types.Areas.DB, db_number, 0)
#     print("The value of the first byte in the database is:", value)

#     # Send the value 10 to the first byte in the database
#     client.write_area(snap7.types.Areas.DB, db_number, 0, 10)
#     print("The value of the first byte in the database has been changed to:", client.read_area(snap7.types.Areas.DB, db_number, 0))

# except Exception as e:
#     print("Error connecting to the server:", str(e))

# # Disconnect the client
# client.disconnect()

# # Stop the server
# server.stop()




