import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
    except Exception as e:
        pass

def main():
    host = input("Enter target IP or domain: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    main()
