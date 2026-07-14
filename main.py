import sys, time, socket
import get_domain, get_range

services: dict[str, int] = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

ip_address: str
domain_name: str
ip_address, domain_name = get_domain.get_domain()

start: int
end: int
start, end = get_range.get_range()

cnt: int = 0
open_ports: list[int] = []

start_time: float = time.time()

for port in range(start, end + 1):
    sys.stdout.write(f"\rСканирование: порт {port}/{end}")
    sys.stdout.flush()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        try:
            sock.connect((ip_address, port))
            cnt += 1
            open_ports.append(port)
        except:
            continue

        
end_time: float = time.time()

total_time: float = round(end_time - start_time, 2)
print("\n")
print("="*45)
print(f"Домен сервера: {domain_name}")
print(f"\nIP адрес сервера: {ip_address}")
print(f"Проверено портов: {end - start}")
print(f"Сканирование заняло {total_time} секунд.")

if cnt > 0:
    print(f"\nВсего открытых портов: {cnt}")
    print("Список открытых портов:")
    num: int = 0
    for open_port in open_ports:
        service = services.get(open_port, "Неизвестно")
        num += 1
        print(f"{num}: {open_port} {service}")

elif cnt == 0:
    print("Открытых портов не найдено.")

print("="*45)