import os
from colorama import Fore, Style

def ana_menu():
    os.system("clear")
    os.system("figlet siber saldiri aracina hosgeldiniz")

def wordpress_tarama_menu():
    os.system("clear")
    os.system("figlet YUNUS")
    os.system("figlet WORDPRESS TARAMA")

    print("""
    WORDPRESS TARAMA aracına Hoş Geldin...
    1) Hızlı Tarama
    2) Eklenti Tarama
    3) Tema Tarama
    4) Yönetici Kullanıcı Adı Tarama
    """)

    islemno = int(input("İşlem numarası giriniz: "))

    if islemno in [1, 2, 3, 4]:
        site = input("Site adresi: ")

        # wpscan çıktısını bir dosyaya yaz
        dosya_adi = "wpscan_cikti.txt"
        komut = f"wpscan --url {site} --enumerate {islemno} > {dosya_adi}"
        os.system(komut)

        # wpscan çıktısını ekrana yazdır
        with open(dosya_adi, "r") as dosya:
            print(dosya.read())

    else:
        print("Yanlış seçim, program kapandı...")

while True:
    ana_menu()

    print("""
    1) web saldiri araclari
    2) wifi saldiri araclari
    3) Ağiçi saldırı araçları
    4) Backdor oluşturucu
    5) WordPress Tarama
    9) cikis
    """)

    try:
        a = int(input("İşlem numarasını giriniz: "))

        if a == 1:
            os.system("cd web && python3 web.py")
        elif a == 2:
            os.system("cd wifi && python3 wifi.py")
        elif a == 3:
            os.system("cd agicisaldiri && python3 agicisaldiri.py")
        elif a == 4:
            os.system("cd backdor && python3 backdor.py")
        elif a == 5:
            wordpress_tarama_menu()  # WordPress Tarama menüsünü çağır
        elif a == 9:
            os.system("python3 cikis.py")
            break  # Çıkış yapılırsa döngüden çık
        else:
            ana_menu()
            print(Fore.RED + "İşlemi yanlış yaptınız" + Style.RESET_ALL)
            input("Devam etmek için Enter tuşuna basın.")
    except ValueError:
        ana_menu()
        print(Fore.RED + "Hatalı bir giriş yaptınız. Lütfen bir sayı girin." + Style.RESET_ALL)
        input("Devam etmek için Enter tuşuna basın.")


