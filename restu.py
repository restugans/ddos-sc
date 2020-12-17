import os
import socket
import sys

ip = '103.152.118.111' #ip target
port = 80 #port target
size = 1024
pesan = "Aku Salah Mencitai Orang\n"

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((ip, port))

tcp_socket.send(bytes(pesan.encode("UTF-8")