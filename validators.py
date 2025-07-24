import validators
import socket
import requests

# Список доменов для проверки
domains = [
    "example.com",
    "google.com",
    "nonexistent12345.xyz",
    "invalid domain",
    "openai.com"
]

def is_valid_domain(domain):
    # Проверка формата домена
    return validators.domain(domain)

def is_resolvable(domain):
    # Проверка разрешимости через DNS
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def is_http_accessible(domain):
    # Проверка ответа от сайта
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

def check_domain(domain):
    print(f"\nПроверка: {domain}")
    if not is_valid_domain(domain):
        print("❌ Невалидный формат домена")
        return

    if not is_resolvable(domain):
        print("⚠️  Домен не резолвится (не найден через DNS)")
        return

    if is_http_accessible(domain):
        print("✅ Домен валидный и доступен")
    else:
        print("⚠️  Домен резолвится, но не отвечает по HTTP")

# Основной цикл
for domain in domains:
    check_domain(domain)
