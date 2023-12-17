import os
import requests

os.system("apt-get install dirb")

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
                            break  # içteki while döngüsünden çık
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
            break  # dıştaki while döngüsünden çık
        else:
            print("Geçersiz bir seçim. Lütfen tekrar deneyin.")

# Kodu çalıştır
dirb()
