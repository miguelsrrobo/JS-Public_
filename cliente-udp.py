import socket

target_host = '192.168.1.10'
target_port = 5000

#cria um objeto socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#envia alguns dados
client.sendto('AAABBBCCC',(target_host,target_port))

#recebe alguns dados
data, addr = client.recvfrom(4096)

print(data)
