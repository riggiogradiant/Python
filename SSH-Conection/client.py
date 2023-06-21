# import paramiko

# # Configuración del cliente SSH
# hostname = '0.0.0.0'  # Dirección IP o nombre de host del servidor SSH
# port = 22  # Puerto del servidor SSH
# username = 'us'  # Nombre de usuario para autenticación
# password = 'us'  # Contraseña para autenticación

# # Crea una instancia del cliente SSH
# client = paramiko.SSHClient()
# client.load_system_host_keys()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# try:
#     # Conecta al servidor SSH
#     print('Intentando conectar...')
#     client.connect(hostname, port, username, password)
#     print('Conectado al servidor')

#     # Ejecuta comandos en el servidor SSH
#     stdin, stdout, stderr = client.exec_command('ls')

#     # Lee la salida del comando
#     output = stdout.read().decode()

#     # Imprime la salida del comando
#     print(output)

# finally:
#     # Cierra la conexión SSH
#     client.close()

import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__': # para que se ejecute solo si se ejecuta desde terminal y no si es importa como módulo 
    import getpass
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
