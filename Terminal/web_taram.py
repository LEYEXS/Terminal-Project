import requests

def web_tarama2(url, wordlist):
    try:
        with open(wordlist, 'r') as file:
            words = file.read().splitlines()

        for word in words:
            full_url = f"{url}/{word}"
            response = requests.get(full_url)
            
            if response.status_code == 200:
                print(f"[+] Bulundu: {full_url}")
            elif response.status_code ==  301:
                print(f"[+] Bulundu: {full_url}")

    except Exception as e:
        print(f"Hata: {e}")


