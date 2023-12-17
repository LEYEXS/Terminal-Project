import os

os.system("clear")

os.system("figlet Mitmproxy Saldiri Aracina hosgeldiniz")

print("""


1 Exe  Degistirme
2 Dns Spofing
2 javascript enjekte
3 kendi scriptini olusturma
9 cikis


""")

islemno=int(input("islem numaranizi giriniz: "))

if islemno==1:
	print("""
	1 Hazir Url(exe url'si 
	2 Backdor yolu
	""")
	exedegissec=int(input("islem numaranizi giriniz: "))
	if exedegissec==1:
		exeyol=input("url giriniz: ")
		mitmsaldirino=int(1)
	os.system("python3 mitmsaldiri.py")
elif  islemno==2:
	mitmsaldirino=int(2)
	enjektekod=input("enjekte edeceğiniz javascript kodunu veriniz: ")
	os.system("python3 mitmsaldiri.py")
elif islemno==3:
	os.system("python3 mitmscriptolusturucu.py")
else:
	os.system("mitmproxy.py")
