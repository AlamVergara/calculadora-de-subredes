import ipaddress 

ip = input("Ingresa una red (ejemplo 192.168.1.0/24): ")

network = ipaddress.ip_network(ip)

print("Dirección de red:", network.network_address)
print("Broadcast:", network.broadcast_address)
print("Hosts disponibles:", network.num_addresses - 2) 
