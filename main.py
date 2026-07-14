import sys
import time
import socket

services = {
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


domain = input('Введите домен: ')
try:
    adr = socket.gethostbyname(domain)
except:
    domain = input('пожалуйста введите корректный домен: ')
    adr = socket.gethostbyname(domain)

diapason = input('Введите через "-" диапазон сканирования (например, 1-1024): ')
try:
    start,end = map(int,diapason.split('-'))
except:
    diapason = input("пожалуйста введите корректный диапазон (пример: 1-1024): ")



cnt = 0
open_ports = []

symbols = ['|', '/', '-', '\\']

start_time = time.time()

for port in range(start, end + 1):
    ready_ports = port
    sys.stdout.write(f"\rСканирование: порт {ready_ports}/{end}")
    sys.stdout.flush()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        try:
            sock.connect((adr, port))
            cnt += 1
            open_ports.append(port)
        except:
            continue

        

end_time = time.time()

total_time = round(end_time - start_time, 2)
print("\n")
print("="*45)
print(f"Домен сервера: {domain}")
print(f"\nIP адрес сервера: {adr}")
print(f"Проверено портов: {end - start}")
print(f"Сканирование заняло {total_time} секунд.")


if cnt > 0:
    print(f"\nВсего открытых портов: {cnt}")
    print("Список открытых портов:")
    num = 0
    for open_port in open_ports:
        service = services.get(open_port, "Неизвестно")
        num += 1
        print(f"{num}: {open_port} {service}")

elif cnt == 0:
    print("Открытых портов не найдено.")

print("="*45)