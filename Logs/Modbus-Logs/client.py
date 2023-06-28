from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
import time

import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

print('Starting Modbus Client')
client = ModbusTcpClient('127.0.0.1', port=5020)
# logging.info('Usuario conectado al servidor con IP: 127.0.0.1 y puerto: 5020') 

#Variable que representa el registro Modbus donde se escribirán y lleran los datos
reg = 0

# Inicializar datos que se van a escribir en el registro ModBus
data = [0.1, 1.1, 2.1, 3.1, 4.1]

for i in range(10):
    print('-' * 5, 'Cycle', i, '-' * 30)
    time.sleep(1.0)

    for j, d in enumerate(data):
        data[j] = d + 1

    print('Write', data)

    #Creamos un constructor de carga útil de datos binarios que se escibirán en el registro Modbus, especificando el orden de bytes y de palabras
    builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)

    for d in data:

        #Introducimos al builde todos los valores de data en forma de enteros de 16 bits
        builder.add_16bit_int(int(d))

    #Construimos la carga útil 
    payload = builder.build()

    #Escribimos la carga útil en el registro ModBus, skip_encode= True: no es necesario codificar la info antes de enviarla
    result = client.write_registers(reg, payload, skip_encode=True)

    #Lee los registros ModBus y los printea
    print('Read', client.read_holding_registers(reg, len(data)).registers)

client.close()
