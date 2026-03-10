import socket

def scan_network():

    target = input("Enter target IP: ")

    for port in range(20,1025):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print("Open port:", port)

        s.close()
