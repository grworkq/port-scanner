import socket

def get_domain() -> tuple[str,str]:
    while True:
        domain: str = input('Введите домен: ')
        try:
            adr: str = socket.gethostbyname(domain)
            break
        except socket.gaierror:
            print('Некорректный домен (Корректный домен: example.com)')
    return adr, domain
