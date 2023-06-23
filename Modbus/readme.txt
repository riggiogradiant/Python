Tenemos un servidor y un cliente.

El CLIENTE envía solicitudes y recibe respuestas del servidor, actúa como MASTER

El SERVIDOR proporciona los datos, actúa como SLAVE
    
    En el protocolo Modbus, se definen varios tipos de registros que se utilizan para el intercambio de datos entre dispositivos.

    1-Coil (Bobina): También conocido como Output Coil (Bobina de salida), representa una salida digital discreta. Puede tener dos estados posibles: encendido (ON) o apagado (OFF). Los coils se utilizan típicamente para controlar dispositivos como relés, lámparas o contactores.

    2-Discrete Input (Entrada discreta): También conocido como Input Status (Estado de entrada), representa una entrada digital discreta. Al igual que los coils, los discrete inputs solo pueden tener dos estados: activado o desactivado. Los discrete inputs se utilizan para leer el estado de dispositivos de entrada como sensores o interruptores.

    3-Input Register (Registro de entrada): Los input registers se utilizan para almacenar datos de entrada analógica o digital. Estos registros suelen ser de 16 bits y pueden contener valores numéricos o información de estado. Los input registers se utilizan, por ejemplo, para leer datos de sensores analógicos como termómetros o medidores de presión.

    4-Holding Register (Registro de retención): Los holding registers se utilizan para almacenar datos de salida o datos de configuración. Al igual que los input registers, los holding registers son de 16 bits y pueden contener datos numéricos o de estado. Se utilizan para escribir datos en dispositivos o para configurar parámetros en dispositivos Modbus esclavos.