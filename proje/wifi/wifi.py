import os 


os.system("clear")

print("1) wifite ")
print("9) Yardim ")


islemno = int(input("işlem numarasini giriniz: "))


if islemno==1:
	os.system("wifite")
elif islemno==9:
	os.system("python3 wifihelp.py")
