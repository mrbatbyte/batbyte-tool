from scapy.all import ARP, Ether, srp
import socket

def scanport():
    url_scan = input(" \033[1;32m|--- \033[1;31m Enter URL: \033[1;32m")
    from_port = input(" \033[1;32m|--- \033[1;31m From Port: \033[1;32m")
    to_port = input(" \033[1;32m|--- \033[1;31m To Port: \033[1;32m")

    print("")
    print(f"\033[1;31m Start Scanning With \033[1;32m" + url_scan)
    print("")
    
    open_ports = []
    for port in range(int(from_port), int(to_port)):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((url_scan, port))
            open_ports.append(port)
            print(f"\033[1;32m ~ \033[1;35m Port {port} \033[1;32m[OPEN] {socket.getservbyport(port)}")
        except:
            print(f"\033[1;32m ~~~ \033[1;35m Port {port} \033[1;31m[CLOSE]")

    for open_port in open_ports:
        print("""
+====================================+
    """)
        print(f"\033[1;32m ~~~ \033[1;35m Port {open_port} \033[1;32m[OPEN] ")
    print("")