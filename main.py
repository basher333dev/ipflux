import time
import os
import subprocess
import random
import requests
import threading

subprocess.run(['python3', 'update.py'])

def instalar_dependencias():
    try:
        import requests
    except ImportError:
        os.system('pip3 install requests requests[socks]')
    
    try:
        subprocess.check_output('which tor', shell=True)
    except subprocess.CalledProcessError:
        os.system('sudo apt update && sudo apt install tor -y')

def ip_atual():
    url = 'http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    return requests.get(url, proxies=proxies).text.strip()

def trocar_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
    ]
    return random.choice(user_agents)

def trocar_ip():
    os.system('service tor reload')
    print(f'\033[1;32m[+] Novo IP: {ip_atual()}\033[0m')

def modo_beast():
    while True:
        time.sleep(0.001)
        trocar_user_agent()
        trocar_ip()

def main():
    os.system('clear')
    print('\033[1;36;40m' + '''   
 ██▓ ██▓███    █████▒██▓     █    ██ ▒██   ██▒
▓██▒▓██░  ██▒▓██   ▒▓██▒     ██  ▓██▒▒▒ █ █ ▒░
▒██▒▓██░ ██▓▒▒████ ░▒██░    ▓██  ▒██░░░  █   ░
░██░▒██▄█▓▒ ▒░▓█▒  ░▒██░    ▓▓█  ░██░ ░ █ █ ▒ 
░██░▒██▒ ░  ░░▒█░   ░██████▒▒▒█████▓ ▒██▒ ▒██▒
░▓  ▒▓▒░ ░  ░ ▒ ░   ░ ▒░▓  ░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░
 ▒ ░░▒ ░      ░     ░ ░ ▒  ░░░▒░ ░ ░ ░░   ░▒ ░
 ▒ ░░░        ░ ░     ░ ░    ░░░ ░ ░  ░    ░  
 ░                      ░  ░   ░      ░    ░  
                  IP Changer
    ''' + '\033[0m')

    instalar_dependencias()
    os.system('service tor start')

    beast_mode = input("Beast Mode? (y/n/i): ").strip().lower()
    if beast_mode == "y":
        threading.Thread(target=modo_beast).start()
    elif beast_mode == "n":
        intervalo_base = int(input("\033[1;33m[+] Intervalo entre trocas de IP (segundos) [60]: \033[0m") or 60)
        vezes = input("\033[1;33m[+] Quantas trocas? (Enter para infinito): \033[0m") or "0"

        if vezes == "0":
            while True:
                intervalo = max(1, random.randint(intervalo_base - 10, intervalo_base + 10))
                time.sleep(intervalo)
                trocar_user_agent()
                trocar_ip()
        else:
            for _ in range(int(vezes)):
                intervalo = max(1, random.randint(intervalo_base - 10, intervalo_base + 10))
                time.sleep(intervalo)
                trocar_user_agent()
                trocar_ip()
    elif beast_mode == "i":
        print("O Beast Mode altera o IP a cada milésimo de segundo usando workers.")
        input("Pressione Enter para voltar...")
        main()

if __name__ == "__main__":
    main()
