import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print('[*] Listening on %s:%d' % (bind_ip,bind_port))

#esta é nossa thread para tratamento de clientes
def handle_client(client_socket):

    #exibe o que o cliente enviar
    request = client_socket.recv(1024)

    print('[*] Received: %s' % request)

    #envia um pacote de volta
    client_socket.send('ACK!')

    client_socket.close()
while True:
    client,adds = server.accept()

    print '[*] Accepted connection from: %s:%d' % (addr[0],addr[1])
    #coloca nossa thread de cliente em acoa para tratar dados de entrada client_handle = threading.thread(target = handle_client,args = (client,))
    client_handle.start()
