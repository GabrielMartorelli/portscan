import socket


def scan(target, ports):
    print("\n" + "Starting scan for " + str(target))
    for port in range(l, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("+ Port Opened " + str(port))
        sock.close()
    except:
        pass


targets = input("+ Enter the target IP to scan (slipt using ,): ")
ports = int(input("+ How many ports do you want to scan: "))

if "," in targets:
    print("+ Scanning multiple targets", "green")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(" "), ports)
else:
    scan(targets, ports)
