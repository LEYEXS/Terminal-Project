import socket

def tcp_client(server_address, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)
        client_socket.send(message.encode('utf-8'))
        print("Mesaj gönderildi.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_address = ("10.0.2.15", 4545)
    message = "Merhaba, bu bir TCP test mesajıdır."
    tcp_client(server_address, message)
