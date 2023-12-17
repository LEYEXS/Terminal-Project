import os

os.system("clear")

os.system("figlet Mitmproxy Saldiri Aracina hosgeldiniz")

print("""


1  Exe  Degistirme
2 javascript enjekte
3 kendi scriptini olusturma
9 cikis


""")

islemno=int(input("islem numaranizi giriniz: "))

if islemno==1:
	os.system("python3 mitmsaldiri.py")
elif  islemno==2:
	os.system(clear)
	a=input("Java Script Kodunu Belirtiniz: ")
	with open("java.txt","w") as dosya:
         dosya.write(a)
    os.system("./mitmdump -s javascript.py")
elif islemno==3:
	os.system("python3 mitmscriptolusturucu.py")
else:
	os.system("mitmproxy.py")
