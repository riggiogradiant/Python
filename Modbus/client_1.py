from pymodbus.client import ModbusTcpClient

#El cliente se va a conectar a la dirección 127.0.0.1
client = ModbusTcpClient('127.0.0.1', port = 5020)

#Envía solicitud a Server y escribe un True en la coil 1
client.write_coil(1,True)

#Asignamos a result lo que leamos de la bobina 1 (el otro 1 es para indicar que solo queremos leer de 1 bobina)
result = client.read_coils(1,1)

#Printea el valor de había en la primera bobina
print(result.bits[0])

#Cerramos cliente
client.close()
