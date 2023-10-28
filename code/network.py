from socket import gethostbyname
from sys import argv
from os import system
from psutil import net_if_addrs

def lookup(dn):
    return gethostbyname(dn)
    
def ping(ip):
    if system("ping " + ip) == 0:
        return "UP !"
    else :
        return "DOWN !"
    
def ip ():
    addrs = net_if_addrs()
    if 'Wi-Fi' in addrs:
        for snic in addrs['Wi-Fi']:
            if snic.family == 2:
                return snic.address
    return None

res = ""

if argv[1] == "lookup":
    res = lookup(argv[2])
elif argv[1] == "ping":
    res = ping(argv[2])
elif argv[1] == "ip":
    res = ip()
else :
    res = "'" + argv[1] + "'" + " is not an available command. Déso."
print(res)