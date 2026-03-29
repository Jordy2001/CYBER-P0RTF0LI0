import socket
import threading

# Simple network port scanner
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()

    except Exception as e:
        pass

def run_scanner():
    target = input("Enter target IP address: ")
    print(f"\nScanning {target}...\n")

    for port in range(1, 1025):  # Scan first 1024 ports
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    run_scanner()
