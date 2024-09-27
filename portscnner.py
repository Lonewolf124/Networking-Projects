import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input('Enter the target website to scan: ')

def port_scan(port_number):
    try:
        connection = sock.connect((host, port_number))
        return True
    except:
        return False

for port in range(25):
    if port_scan(port):
        print('Port', port, 'is open')




