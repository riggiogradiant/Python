# import snap7
# import snap7.common
# from snap7.util import *
# import snap7


# # Start the server
# server = snap7.server.Server()
# server.start_to('127.0.0.1', 2000)

# # Add a database
# conn = snap7.Connection()
# conn.connect("127.0.0.1", 0, 0, 2000)
# conn.add_area(snap7.types.Areas.DB, 1)

# # Disconnect from the server
# conn.disconnect()


# # Iniciar el servidor
# server.start()
# print("Server created in the address 127.0.0.1 on port 2000")


# def run_server():
#     while True:
#         pass


# if __name__ == "__main__":
#     # Create a process to run the server
#     p = multiprocessing.Process(target=run_server)
#     p.start()

import snap7
from snap7.util import *
import mysql.connector



# Connection parameters for the simulated server
server_ip = '0.0.0.0'  # Use 0.0.0.0 to listen on all available interfaces
server_port = 2000
server_rack = 0
server_slot = 2

# Create an instance of the server object
server = snap7.server.Server()

# Start the server
server.start_to(server_ip, server_port)

try:
    # Register a DB area to be accessed by the client
    db_number = 1
    db_size = 10  # Number of bytes in the DB area
    server.db_write(db_number, 0, bytearray(db_size))  # Initialize the DB with zero bytes

    while True:
        # Process incoming client requests
        server.process()
except KeyboardInterrupt:
    pass
finally:
    # Stop the server
    server.stop()
