import snap7
import snap7.common
from snap7.util import *
import snap7


# Start the server
server = snap7.server.Server()
server.start_to('127.0.0.1', 2000)

# Add a database
conn = snap7.Connection()
conn.connect("127.0.0.1", 0, 0, 2000)
conn.add_area(snap7.types.Areas.DB, 1)

# Disconnect from the server
conn.disconnect()


# Iniciar el servidor
server.start()
print("Server created in the address 127.0.0.1 on port 2000")


def run_server():
    while True:
        pass


if __name__ == "__main__":
    # Create a process to run the server
    p = multiprocessing.Process(target=run_server)
    p.start()
