from psutil import net_if_addrs
def get_ip():
    addrs = net_if_addrs()
    if 'Wi-Fi' in addrs:
        for snic in addrs['Wi-Fi']:
            if snic.family == 2:
                return snic.address
    return None

print(get_ip())