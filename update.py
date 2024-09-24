import requests
import os

def atualizar_script():
    local_file = 'main.py'
    url = 'https://raw.githubusercontent.com/basher333dev/ipflux/refs/heads/main/main.py'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        novo_conteudo = response.text

        with open(local_file, 'r') as file:
            conteudo_local = file.read()

        if conteudo_local != novo_conteudo:
            with open(local_file, 'w') as file:
                file.write(novo_conteudo)
            print(f'[+] {local_file} atualizado com sucesso.')
        else:
            print(f'[+] {local_file} já está atualizado.')
    
    except requests.RequestException as e:
        print(f'[!] Erro ao acessar o repositório: {e}')
    except Exception as e:
        print(f'[!] Ocorreu um erro: {e}')

if __name__ == "__main__":
    atualizar_script()
