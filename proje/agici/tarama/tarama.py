import os

#-----------------------------ip_bulma_başlangıç-----------------------------------------

def ip_bulma():
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
		tarama_modul()
	elif islemno==2 :
		os.system("python3 cikis.py")

#-----------------------------ip_bulma_bitiş------------------------------------------------
#-----------------------------nmap_tarama_başlangıç-----------------------------------------

def nmap_tarama():
	ip=input("Lütfen ip ve ya alan adını giriniz: ")
 
	os.system("clear")
	os.system("figlet Nmap Tarama Modulu")
	print("""

 
	1) Açık Port Tarama
	2) Servis ve Versiyon Bilgisi
	3) İşletim Sistemi Bilgisi
	4) Detaylı Arama (Proxy gerekmekte)
	9)Geri Dön
 

 
	""")

	nmapislemno = int(input("işlem numarasini giriniz: "))
	if nmapislemno==1:
		os.system("nmap -Pn -sS -n -v --reason --open "+ip)
	elif nmapislemno==2:
		os.system(" nmap -sS -sV -sC -n -v -p-"+ip)
#-----------------------------nmap_tarama_bitiş-----------------------------------------
#-----------------------------tarama_modülü_başlangıç-----------------------------------------
def tarama_modul():
	
	os.system("clear")
	os.system("figlet TARAMA MODULUNE HOSGELDİNİZ")
	print("""


	1) ip bulma    
	2) nmap tarama 
	9) cikis       


	""")
	islemno = int(input("işlem numarasini giriniz: "))
	if islemno==1:
		os.system("python3 ipbulma.py")
	elif islemno==2:
		nmap_tarama()
	elif islemno==9:
		os.system("python3 cikis.py")

#-----------------------------tarama_modülü_bitiş-----------------------------------------
