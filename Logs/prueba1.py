import logging

# Configurar el logger
logging.basicConfig(filename='registro.log', level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')

# Registrar mensajes

#Niveles en orden
logging.debug('Este es un mensaje de depuración') #1
logging.info('Información') #2
logging.warning('Advertencia') #3
logging.error('Error') #4
logging.critical('Error Crítico') #5
