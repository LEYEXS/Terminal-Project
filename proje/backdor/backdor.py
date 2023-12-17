import os

def backdoor_olustur():
    os.system("clear")
    os.system("figlet backdoor olusturma moduluna hosgeldiniz")

    print("""
    1) Msfvenom
    2) VeilFrenwork
    3) Fatrat
    9) Cikis
    """)

    a = int(input("İşlem numarası giriniz: "))

    if a == 1:
        os.system("python3 msfvenom.py")
    elif a == 2:
        os.system("veil")
    elif a == 3:
        os.system("python3 /opt/TheFatrat/Fatrat")
    elif a == 4:
        os.system("python3 cikis.py")

# Fonksiyonu çağırarak çalıştırabilirsiniz
backdoor_olustur()
