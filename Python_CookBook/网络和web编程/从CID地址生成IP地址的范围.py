import ipaddress

# net = ipaddress.ip_network('123.45.67.64/27')  # ipv4
# print(net)
# for i in net:
#     print(i)
# net = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')  # ipv4
# for i in net:
#     print(i)

# print(net.num_addresses)
# print(net[0])
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)
