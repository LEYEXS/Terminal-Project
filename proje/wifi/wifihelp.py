import os 

os.system("clear")
os.system("figlet YARDIM MENUSU")

print("""

1)wifite aracı size web , wpa , wpa2 ağlarına saldırı imkanı sağlar







1) geri dön 
9) çıkış    



""")



k =int(input("islem numarasini giriniz = " ))

if k==1:
	os.system("python3 wifi.py")

elif k==9:
	os.system("python3 cikis.py")
