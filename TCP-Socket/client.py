import socket

HOST ="127.0.0.1" # IP del servidor al que nos vamos a conectar
PORT = 65123 # puerto a donde nos vamos a conectar 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    print('Client connected')

    #A partir de aquí ya se estableció la conexión 

    while True:
        msg_send = input('Introduce a msg to send to the server: ')
        s.sendall(msg_send.encode())
        data_from_server = s.recv(1024)
        print('Data received: ', data_from_server.decode())

    # for i in range (10):

    #     s.sendall(enviar.encode()) # la b es para indicar que es un string binario
    #     data_from_server = s.recv(1024)
    #     print('Data recibida desde el servidor:', data_from_server.decode(), 'numero: ',i)


#el encode y decode es para pasar la string a formato bit