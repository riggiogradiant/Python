import paramiko

def ssh_connect(ip, port, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    print('Connected to the SSH server.')

    # Abrir un canal SSH
    channel = client.get_transport().open_session()

    # Enviar una solicitud de canal del tipo "session"
    # channel.get_pty()
    # channel.invoke_shell()

    channel.send('Client succesfully connected')
    #print(channel.recv(1024).decode())
    print('============================================')
    
    while True:
        msg_send = input('Enter msg to send to server or <CR> to exit: ')
        if msg_send == '':
            break
        channel.send(msg_send)
        output = channel.recv(1024).decode()
        print('---MSG RECEIVED---')
        print(output, '\n')

    # Cerrar el canal y la conexión
    channel.close()
    client.close()

#main
if __name__ == '__main__':
    import getpass
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '127.0.0.1'
    port = input('Enter port or <CR>: ') or 22222
    ssh_connect(ip, port, user, password)


