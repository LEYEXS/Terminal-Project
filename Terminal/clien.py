import socket



server_address = ("10.0.2.15", 4545)
def server_cevap(server_address):
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        message = "Merhaba, bu bir test mesajıdır."
        client_socket.send(message.encode('utf-8'))
        client_socket.close()

server_cevap(server_address)
