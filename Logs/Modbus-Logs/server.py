# from pymodbus.server import StartTcpServer
# from pymodbus.device import ModbusDeviceIdentification
# from pymodbus.datastore import ModbusSequentialDataBlock
# from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# import logging

# def run_async_server():
#     print("Dentro del run_async_server")
#     nreg = 200
#     # initialize data store
#     store = ModbusSlaveContext(
#         di=ModbusSequentialDataBlock(0, [15] * nreg),
#         co=ModbusSequentialDataBlock(0, [16] * nreg),
#         hr=ModbusSequentialDataBlock(0, [17] * nreg),
#         ir=ModbusSequentialDataBlock(0, [18] * nreg)
#     )

#     # Single=true --> Solo acepta 1 conexión a la vez
#     context = ModbusServerContext(slaves=store, single=True)

#     # Inicializar información del servidor para que sea identificable
#     identity = ModbusDeviceIdentification()
#     identity.VendorName = 'Riggio'
#     identity.ProductCode = 'CRD'
#     identity.ProductName = 'Riggio Server'
#     identity.ModelName = 'Riggio Server'
#     identity.MajorMinorRevision = '3.0.2'

#     print("Antes de iniciar el TCP server")

#     # TCP Server -- Modbus utiliza el puerto 502 para las conexiones TCP/IP
#     StartTcpServer(context=context, host='localhost', identity=identity, address=("127.0.0.1", 5020))

#     # Esperar solicitudes Modbus y acceder a los valores recibidos del cliente
#     print("Antes del WHILE")
#     while True:
#         print("Estamos dentro del while")
#         # Acceder a los valores de los registros de entrada discreta
#         di_values = store.di.getValues(0, nreg)
#         print("Valores de registros de entrada discreta:", di_values)

#         # Acceder a los valores de los registros de salida discreta
#         co_values = store.co.getValues(0, nreg)
#         print("Valores de registros de salida discreta:", co_values)

#         # Acceder a los valores de los registros de holding
#         hr_values = store.hr.getValues(0, nreg)
#         print("Valores de registros de holding:", hr_values)

#         # Acceder a los valores de los registros de entrada
#         ir_values = store.ir.getValues(0, nreg)
#         print("Valores de registros de entrada:", ir_values)

#         # Esperar la siguiente solicitud
#         context.select(0.1)


# if __name__ == "__main__":
#     logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
#     print('Modbus server started on localhost port 5020')
#     run_async_server()
    


import time
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import logging

def run_async_server():
    print("Dentro del run_async_server")
    nreg = 200
    # initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [15] * nreg),
        co=ModbusSequentialDataBlock(0, [16] * nreg),
        hr=ModbusSequentialDataBlock(0, [17] * nreg),
        ir=ModbusSequentialDataBlock(0, [18] * nreg)
    )

    # Single=true --> Solo acepta 1 conexión a la vez
    context = ModbusServerContext(slaves=store, single=True)

    # Inicializar información del servidor para que sea identificable
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Riggio'
    identity.ProductCode = 'CRD'
    identity.ProductName = 'Riggio Server'
    identity.ModelName = 'Riggio Server'
    identity.MajorMinorRevision = '3.0.2'

    print("Antes de iniciar el TCP server")

    # TCP Server -- Modbus utiliza el puerto 502 para las conexiones TCP/IP
    StartTcpServer(context=context, host='localhost', identity=identity, address=("127.0.0.1", 5020))

    # Esperar solicitudes Modbus y acceder a los valores recibidos del cliente
    print("Antes del WHILE")
    while True:
        print("Estamos dentro del while")
        # Acceder a los valores de los registros de entrada discreta
        di_values = store.di.getValues(0, nreg)
        print("Valores de registros de entrada discreta:", di_values)

        # Acceder a los valores de los registros de salida discreta
        co_values = store.co.getValues(0, nreg)
        print("Valores de registros de salida discreta:", co_values)

        # Acceder a los valores de los registros de holding
        hr_values = store.hr.getValues(0, nreg)
        print("Valores de registros de holding:", hr_values)

        # Acceder a los valores de los registros de entrada
        ir_values = store.ir.getValues(0, nreg)
        print("Valores de registros de entrada:", ir_values)

        # Esperar la siguiente solicitud
        context.select(0.1)


if __name__ == "__main__":
    logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
    print('Modbus server started on localhost port 5020')
    run_async_server()
    time.sleep(1)  # Pausa de 1 segundo para dar tiempo al servidor Modbus para iniciar completamente
    print("Antes del WHILE MAIN")
