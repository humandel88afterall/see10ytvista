import requests
import time

# Enlace que quieres visitar
url = "https://www.youtube.com/watch?v=nFULkyBktis"

# Lista de proxies con formato usuario:contraseña@ip:puerto
proxies_list = [
    "http://fefelvyg:1wg53jq25yl7@23.95.150.145:6114",
    "http://fefelvyg:1wg53jq25yl7@198.23.239.134:6540",
    "http://fefelvyg:1wg53jq25yl7@45.38.107.97:6014",
    "http://fefelvyg:1wg53jq25yl7@107.172.163.27:6543",
    "http://fefelvyg:1wg53jq25yl7@64.137.96.74:6641",
    "http://fefelvyg:1wg53jq25yl7@45.43.186.39:6257",
    "http://fefelvyg:1wg53jq25yl7@154.203.43.247:5536",
    "http://fefelvyg:1wg53jq25yl7@216.10.27.159:6837",
    "http://fefelvyg:1wg53jq25yl7@136.0.207.84:6661",
    "http://fefelvyg:1wg53jq25yl7@142.147.128.93:6593",
]

while True:
    for proxy in proxies_list:
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=10)
            print(f"[OK] Proxy {proxy} -> Status {response.status_code}")
        except Exception as e:
            print(f"[ERROR] Proxy {proxy} -> {e}")

    print("Esperando 2 minutos para la siguiente ronda...\n")
    time.sleep(120)  # 120 segundos = 2 minutos
