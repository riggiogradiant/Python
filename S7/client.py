import snap7
import snap7.common
from snap7.util import *
import snap7


# Crea un cliente para conectarse al servidor
client = snap7.client.Client()
try:
    # Intentar conectar al servidor
    client.connect("127.0.0.1", 0, 0, 2000)  #(IP, Rack, Slot, Puerto)
    client.connect()
    print("Cliente conectado al servidor")

    msg = "Hello, server!"

    # Enviar un mensaje al servidor
    client.write_area(snap7.types.Areas.DB, 1, 0, msg.encode())

except Exception as e:
    print("Error al conectar al servidor:", str(e))

#Desconectar el cliente
client.disconnect()
