# -*- coding: utf-8 -*-

import uuid
import socket
import fcntl
import struct

# 获取mac地址
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

# 获取本机名称
myName = socket.getfqdn(socket.gethostname())
# 获取内网IP
myAddr = socket.gethostbyname(myName)
print myName
print myAddr

print get_mac_address()


# Linux下可用
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(
        fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                                    ifname[:15]))[20:24])

# 获取内网IP
print get_ip_address('lo')
# 获取外网IP
print get_ip_address('eth0')