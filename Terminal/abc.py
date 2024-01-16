import socket

def server_baslat(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # SO_REUSEADDR seçeneğini kullan

    try:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Sunucu {host}:{port} adresinde dinleniyor...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"{client_address} adresinden bağlantı kabul edildi.")

            data = client_socket.recv(1024)
            print(f"Gelen veri: {data.decode('utf-8')}")

            client_socket.close()
            # Sunucu sürekli olarak dinlemeye devam edecek
    except KeyboardInterrupt:
        print("Sunucu kapatıldı.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    server_baslat("10.0.2.15", 4545)
