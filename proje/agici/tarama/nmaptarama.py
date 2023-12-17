#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os

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
elif 
	
