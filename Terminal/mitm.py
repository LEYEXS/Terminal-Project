import os

os.system("clear")

def mitm_secenek():
    os.system("figlet Mitmproxy Saldiri Aracina hosgeldiniz")
    print("""
1  Exe Degistirme
2  Javascript Enjekte
3  Kendi scriptini olusturma
9  Cikis
    """)
    islemno = int(input("Islem numaranizi giriniz: "))

    if islemno == 1:
        os.system("python3 mitmsaldiri.py")

    elif islemno == 2:
        os.system("clear")
        a = input("Javascript Kodunu Belirtiniz: ")
        with open("java.txt", "w") as dosya:
            dosya.write(a)
        os.system("./mitmdump -s javascript.py")

    elif islemno == 3:
        os.system("python3 mitmscriptolusturucu.py")

    elif islemno == 9:
        exit()

    else:
        print("Geçersiz işlem numarası.")

