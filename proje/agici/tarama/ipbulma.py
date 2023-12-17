import os

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
	os.system("python3 tarama.py")







print("""

geri dön = 1
cikis    = 2


""")

islemno =int(input("islem numarasini giriniz = "))


if islemno==1:
	os.system("python3 tarama.py")
elif islemno==2 :
	os.system("python3 cikis.py")
