#FAZENDO CALCULOS DE IP E REDE
import ipaddress

ip = '192.168.0.1/24'
rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)
