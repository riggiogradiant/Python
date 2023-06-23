from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_async_server ():
    nreg = 200
    #initialize data store
    store = ModbusSlaveContext(
        #   ModbusSequentialDataBlock(dirección inicial del bloque, lista de valores para inicializar valores),
        di= ModbusSequentialDataBlock(0, [15]*nreg),
        co= ModbusSequentialDataBlock(0, [16]*nreg),
        hr= ModbusSequentialDataBlock(0, [17]*nreg),
        ir= ModbusSequentialDataBlock(0, [18]*nreg))
    
    #Single=true --> Solo acepta 1 conexión a la vez
    context = ModbusServerContext(slaves= store, single = True)
    
    #inicializar info del server para que luego sea identificable
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Riggio'
    identity.ProductCode = 'CRD'
    identity.ProductName = 'Riggio Server'
    identity.ModelName = 'Riggio Server'
    identity.MajorMinorRevision = '3.0.2'

    #TCP Server -- Modbus utiliza el puerto 502 para las conexiones TCP/IP
    StartTcpServer(context=context, host='localhost', identity=identity, address=("127.0.0.1", 5020) )

if __name__ == "__main__":
    print('Modbus server started on localhost port 5020')
    run_async_server()

