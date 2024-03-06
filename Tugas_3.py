import socket

def service_protocol(port):
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        80: "HTTP",
        443: "HTTPS"
    }
    
    if port in services:
        service_name = services[port]
        print(f"Port: {port} => service name: {service_name}")
    else:
        print("Port tidak dikenal.")

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Anda mengakses {hostname} dengan alamat IP {ip_address}")
        print(f"dari komputer AISHA-PC dengan alamat IP 10.252.23.123")
    except socket.gaierror:
        print("Tidak dapat menemukan alamat IP untuk hostname yang diberikan.")

def main():
    while True:
        print("MENU PILIHAN:")
        print("1. MENGETAHUI SERVICE DAN PROTOKOL PADA JARINGAN")
        print("2. MENGETAHUI ALAMAT IP DARI SEBUAH WEBSITE")
        choice = input("Masukkan pilihan Anda (1/2): ")

        if choice == '1':
            port = int(input("Masukkan port protokol: "))
            service_protocol(port)
        elif choice == '2':
            website = input("Masukkan alamat web: ")
            get_ip_address(website)
        else:
            print("Pilihan tidak valid.")

        repeat = input("\nANDA INGIN MENGULANG (Y/T)? ")
        if repeat.upper() != 'Y':
            break

if __name__ == "__main__":
    main()
