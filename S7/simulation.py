import snap7

server = snap7.server.Server()

server.start_to("127.0.0.1")

server.set_param(snap7.types.LocalPort, 200)

server.start()

print("Server created on address 192.168.0.1 in port 200")

# while True:
#     server.process()
#     client = snap7.client.Client()
#     client.connect("127.0.0.1", 200)  # Dirección IP del servidor
#     value = client.read_area(snap7.types.Areas.DB, 1, 0)
#     print(value)
#     client.disconnect()
#     break

# # Esto se ejecutará cuando salgas del bucle "while True"
# server.stop()
