# Port Scanner

A simple TCP port scanner written in Python using the 'socket' module.

## Features

- Resolves a domain name to its IP address.
- Scans a user-defined range to TCP ports.
- Displays all open ports.
- Measures the scan execution time
- Validates user input (domain and port range).

## Project Structure

```text
port-scanner/
├── main.py             # Main entry point of the application
├── input_utils.py      # User input and validation
├── network.py          # Network-related functions
├── .gitignore          # Specifies intentionally untracked files to ignore
└── README.md           # Project documentation
```

## Requirements

- Python 3.x

## Run

```bash
python main.py
```

## Example
```
Введите домен: example.com
Введите через "-" диапазон сканирования (например, 1-1024. Максимальное число - 65535): 1-1024
Сканирование: порт 1024/1024

=============================================
Домен сервера: example.com

IP адрес сервера: 172.66.147.243
Проверено портов: 1023
Сканирование заняло 311.95 секунд.

Всего открытых портов: 2
Список открытых портов:
1: 80 HTTP
2: 443 HTTPS
=============================================
```

## Technologies 

- Python
- socket
- time
- sys

## What I learned

- Working with TCP sockets
- Resolving domain names to IP addresses
- Using timeouts
- Exception handling
- Organizing code into modules
