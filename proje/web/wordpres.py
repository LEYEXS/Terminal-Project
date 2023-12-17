import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet YUNUS")
os.system("figlet WORDPRESS TARAMA")

print("""
WORDPRESS TARAMA aracına Hoş Geldin...
1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Kullanıcı adı taram
5) Brutforce
""")

islemno=int(input("İşlem numarası giriniz : "))

if islemno==1:
	site=input("site adresi : ")
	os.system("wpscan --url "+site+"--random-user-agent")
elif islemno==2:
	site=input("site adresi : ")
	os.system("wpscan --url "+site+" --random-user-agent --enumerate p")
elif islemno==3:
	site=input("site adresi : ")
	os.system("wpscan --url "+site+" --random-user-agent --enumerate t")
elif islemno==4:
	site=input("site adresi : ")
	os.system("wpscan --url "+site+" --random-user-agent --enumerate u")
elif islemno==5:
	site=input("site adresi : ")
	wordlist=input("wordlist belirtirmisiniz : ")
	user=input("usernam verirmisiniz : ")
	os.system("wpscan –url "+site+" --wordlist+"+wordlist+" --username "+user)
elif islemno==6:
	site=input("site adresi : ")
	os.system("wpscan --url "+site+"--random-user-agent --enumerate vp ")
else:
	print("Yanlış seçim, program kapandı...")
