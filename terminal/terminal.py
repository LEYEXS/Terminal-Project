import subprocess
import socket
import os
import re
import ipaddress
import socket
from ping3 import ping
import time
import platform
from colorama import Fore, Style, init
import netifaces
from dene import oto_backdor,show_options,write_to_file
from scapy.all import *
from genel import msfvenom_olustur


init(autoreset=True)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        local_ip = s.getsockname()[0]
    except Exception as e:
        print(Fore.RED + "Yerel IP adresi alınamadı:", e)
        local_ip = None
    finally:
        s.close()
    return local_ip

def get_public_ip():
    try:
        response = subprocess.check_output(['curl', 'https://api64.ipify.org?format=json'])
        public_ip = response.decode('utf-8')
        public_ip = re.search(r'\"ip\":\"(\d+\.\d+\.\d+\.\d+)\"', public_ip).group(1)
    except Exception as e:
        print(Fore.RED + "Genel IP adresi alınamadı:", e)
        public_ip = None
    return public_ip

def list_files():
    try:
        files = os.listdir()
        print(Fore.GREEN + "\nBulunduğunuz Dizin:")
        for file in files:
            print(file)
    except Exception as e:
        print(Fore.RED + "Dosyalar listelenemedi:", e)


def scan_wifi(interface):
    try:
        result = subprocess.check_output(['sudo', 'iwlist', interface, 'scan'])
        result = result.decode('utf-8')
        return result
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Hata: {e}")
        return None

def parse_wifi_data(scan_result):
    networks = re.findall(r'Cell \d+ - Address: (.+?)\n(.+?)(?=Cell|$)', scan_result, re.DOTALL)
    parsed_networks = []

    for network in networks:
        bssid = network[0].strip()
        data = network[1].strip()
        if 'unknow' not in data.lower():  # Filtreleme işlemi burada yapılıyor
            parsed_networks.append((bssid, data))

    return parsed_networks

def print_wifi_data(parsed_networks):
    for index, (bssid, data) in enumerate(parsed_networks, start=1):
        print(Fore.YELLOW + f"\nNetwork {index} - BSSID: {bssid}")
        print(Fore.CYAN + data)





def monitormode(interface):
    try:
        subprocess.run(['sudo', 'ifconfig', interface, 'down'], check=True)
        subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'monitor'], check=True)
        subprocess.run(['sudo', 'ifconfig', interface, 'up'], check=True)
        print(Fore.GREEN + f"\n{interface} ağ arayüzü monitor moduna alındı.\n")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Hata: {e}")

def managemode(interface):
    try:
        subprocess.run(['sudo', 'ifconfig', interface, 'down'], check=True)
        subprocess.run(['sudo', 'iwconfig', interface, 'mode', 'managed'], check=True)
        subprocess.run(['sudo', 'ifconfig', interface, 'up'], check=True)
        print(Fore.GREEN + f"\n{interface} ağ arayüzü yönetim moduna alındı.\n")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Hata: {e}")







def port_tarama(hedef_ip, baslangic_port, bitis_port):
    for port in range(baslangic_port, bitis_port + 1):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        baglanti_durumu = soket.connect_ex((hedef_ip, port))
        if baglanti_durumu == 0:
            try:
                servis_adi = socket.getservbyport(port)
                banner = get_banner(hedef_ip, port)
                print(f"Port {port} ({servis_adi}): {banner}")
            except OSError:
                print(f"Port {port} açık, servis adı bulunamadı.")
        soket.close()
        










target_bssid = "00:11:22:33:44:55" 
target_channel = 6

def packet_callback(packet):
    if packet.haslayer(Dot11):
        if packet.addr2 == target_bssid:
            # Hedef ağın paketleri
            if packet.haslayer(Dot11Beacon):
                # Beacon paketleri (isteğe bağlı olarak işleme alınabilir)
                pass
            elif packet.haslayer(Dot11Auth) and packet.getlayer(Dot11Auth).subtype == 0:  # Open System Authentication
                print("Authentication Paketi: ", packet.summary())
            elif packet.haslayer(Dot11AssoReq):
                print("Association Request Paketi: ", packet.summary())
            elif packet.haslayer(Dot11AssoResp):
                print("Association Response Paketi: ", packet.summary())
            elif packet.haslayer(Dot11ProbeReq):
                print("Probe Request Paketi: ", packet.summary())
            elif packet.haslayer(Dot11ProbeResp):
                print("Probe Response Paketi: ", packet.summary())







def get_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            s.sendall(b'GET / HTTP/1.1\r\n\r\n')
            banner = s.recv(1024)
            return banner.decode('utf-8').strip()
    except Exception as e:
        return str(e)






if __name__ == "__main__":
    try:
        while True:
            command = input(Fore.CYAN + "Komut girin : " + Style.RESET_ALL)

            if command.lower() == 'exit':
                break
            elif command.lower() == 'ifconfig':
                local_ip = get_local_ip()
                public_ip = get_public_ip()

                print(Fore.YELLOW + "\nYerel IP Adresi:", local_ip)
                print("Genel IP Adresi:", public_ip, "\n")
            elif command.lower() == 'ls':
                list_files()
            elif command.lower().startswith('cd '):
                try:
                    directory = command[3:]
                    os.chdir(directory)
                    print(Fore.GREEN + f"\nDizin değiştirildi: {os.getcwd()}\n")
                except Exception as e:
                    print(Fore.RED + "Dizin değiştirilemedi:", e)
            elif command.lower().startswith('cat '):
                try:
                    file_name = command[4:]
                    with open(file_name, 'r') as file:
                        content = file.read()
                        print(Fore.CYAN + f"\nDosya İçeriği ({file_name}):\n{content}\n")
                except Exception as e:
                    print(Fore.RED + "Dosya okunamadı:", e)
            elif command.lower().startswith('var '):
                try:
                    file_name = command[4:]
                    with open(file_name, 'w') as file:
                        print(Fore.GREEN + f"\nYeni Dosya Oluşturuldu: {file_name}\n")
                except Exception as e:
                    print(Fore.RED + "Dosya oluşturulamadı:", e)
            elif command.lower() == 'pwd':
                print(Fore.MAGENTA + f"\nMevcut Dizin: {os.getcwd()}\n")
            elif command.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
            elif command.lower().startswith("porttara"):				
                command_parts = command.split()
                if len(command_parts) == 7 and command_parts[1] == "-ip" and command_parts[3]=="-bp" and command_parts[5]=="-sp":
                    hedef_ip = command_parts[2]
                    baslangic_port = int(command_parts[4])
                    bitis_port = int(command_parts[6])
                    port_tarama(hedef_ip,baslangic_port,bitis_port)
                else:
                    print(Fore.RED + "porttara -ip  -bp -sp")
            elif command.lower() == "handshake":
                command_parts = command.split()
                if len(command_parts) == 7 and command_parts[1] == "--bssid" and command_parts[1] =="-bs" and command_parts[3]== "--chanel" and command_parts[3]== "-c" and command_parts[5]== "-i":
                    target_bssid  =  command_parts[1]
                    target_channel=  command_parts[4]
                    interface     =  command_parts[6]
                    os.system(f"iwconfig wlan0 channel {target_channel}")
                    sniff(prn=packet_callback, store=0, iface={interface}, count=100)
                else:
                    print(Fore.RED+"Geçersiz komut şöyle deneyin handshake -h ")
            elif command.lower().startswith('monitormod '):
                interface = command.split()[1]
                monitormode(interface)
            elif command.lower().startswith('managemod '):
                interface = command.split()[1]
                managemode(interface)
            elif command.lower().startswith('ag-tara'):
                command_parts = command.split()
                if len(command_parts) == 3 and command_parts[1] == '-i':
                    interface = command_parts[2]
                    scan_result = scan_wifi(interface)
                    if scan_result:
                        parsed_networks = parse_wifi_data(scan_result)
                        print_wifi_data(parsed_networks)
                else:
                    print(Fore.RED + "Geçersiz komut. 'ag-tara -i <ağ_adi>' komutunu doğru şekilde kullanın.")
            elif command.lower().startswith('oto-backdor'):
                oto_backdor()
            elif command.lower().startswith("msfvenom"):
                msfvenom_olustur()
            else:
                print(Fore.RED + "Geçersiz komut.")

    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram kapatıldı.")
