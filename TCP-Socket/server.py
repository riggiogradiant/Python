import socket
import sys

HOST ="127.0.0.1" # IP de la LoopBack
PORT = 65123 # puerto del ordenador donde va a escuchar


#socket.socket se usa para crear un socket
#socket.AF_INET indicamos que usa IPV4
#socket.SOCK_STREAM indicamos que va a usar TCP
#with...as... nos da un contexto de manejo, dentro del with podemos trabajar con s como si fuese el socket

#con los bloques with nos aseguramos de que se liberen los recursos una vez salimos del bloque

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST,PORT)) # bindeamos el socket al host y puerto
        s.listen() 
        print('Waiting request...')
        sin, addr =s.accept() # se queda esperando a aceptar una petición y va a guardar el socket de entrada y su dirección (del cliente) 

        with sin:
            print('Connected to ' ,addr)

            while True: 
                data_from_client = sin.recv(1024) # que esté siempre recibiendo del socket del cliente
                data_from_client = data_from_client.decode() # pasamos de binario a string
                data_send_to_client = data_from_client + ' [FROM SERVER]'
                sin.sendall(data_send_to_client.encode())
                print('Message sent to Client')
    
    except KeyboardInterrupt:
        print('Keyboard interrupt detected. Closing the connection.')
        s.close()
        sys.exit(0)
