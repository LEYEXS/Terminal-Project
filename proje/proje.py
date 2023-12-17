#!/usr/bin/env python
import os 

os.system("clear")
os.system("figlet siber saldiri aracina hosgeldiniz")

print("""



1) web  saldiri araclari  
2) wifi saldiri araclari 
3) Ağiçi saldırı araçları
4) Backdor oluşturucu
9) cikis                 


""")



a=int(input("islem numarasi giriniz: "))

if   a==1:
	os.system("cd web && python3 web.py")
elif a==2:
	os.system("cd wifi && python3 wifi.py")
elif a==3:
	os.system("cd agicisaldiri && python3 agicisaldiri.py")
elif a==4:
	os.system("cd backdor && python3 backdor.py")
elif a==5:
	os.system("python3 backdor/backdor.py")
elif a==9:
	os.system("python3 cikis.py")	
else:
	os.system("clear")
	os.system("python3 proje.py")
	print("\033[91m" + "İşlemi yanlış yaptınız" + "\033[0m")

