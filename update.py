import requests
import os
import sys

def atualizar_script(force_update):
    local_file = 'main.py'
    url = 'https://raw.githubusercontent.com/basher333dev/ipflux/refs/heads/main/main.py'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        novo_conteudo = response.text.strip()

        if os.path.exists(local_file):
            with open(local_file, 'r') as file:
                conteudo_local = file.read().strip()
        else:
            conteudo_local = ''

        if force_update or conteudo_local != novo_conteudo:
            with open(local_file, 'w') as file:
                file.write(novo_conteudo)
            print(f'[+] {local_file} atualizado com sucesso.')
        else:
            print(f'[+] {local_file} já está atualizado. // Dica: Use python3 update.py -f para forçar uma atualização')
    
    except requests.RequestException as e:
        print(f'[!] Erro ao acessar o repositório: {e}')
    except Exception as e:
        print(f'[!] Ocorreu um erro: {e}')

if __name__ == "__main__":
    force_update = '-f' in sys.argv
    atualizar_script(force_update)
