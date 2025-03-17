import concurrent.futures
import os
from tqdm import tqdm
from colorama import Fore, Style, init

try:
    import dns.resolver
except ModuleNotFoundError:
    os.system("pip install dnspython")
    import dns.resolver

# Inicializa o colorama
init(autoreset=True)

# Configuração
def obter_configuracoes():
    dominio_alvo = input("Digite o domínio alvo: ")
    wordlist = input("Digite o caminho para a wordlist: ")
    return dominio_alvo, wordlist

# Resolver DNS
def resolver_subdominio(subdominio, dominio_alvo, subdominios_descobertos):
    try:
        full_domain = f"{subdominio}.{dominio_alvo}"
        resposta = dns.resolver.resolve(full_domain, 'A')
        ips = [ip.address for ip in resposta]
        print(f"{Fore.GREEN}[+] {full_domain} -> {', '.join(ips)}{Style.RESET_ALL}")
        subdominios_descobertos.append((full_domain, ips))
    except dns.resolver.NXDOMAIN:
        pass  # Domínio não existe
    except dns.resolver.NoAnswer:
        pass  # Nenhuma resposta
    except dns.resolver.LifetimeTimeout:
        print(f"{Fore.YELLOW}[-] Timeout em {full_domain}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro ao resolver {full_domain}: {e}{Style.RESET_ALL}")

# Leitura da wordlist
def carregar_wordlist(wordlist):
    if not os.path.exists(wordlist):
        print(f"{Fore.RED}[!] Arquivo {wordlist} não encontrado!{Style.RESET_ALL}")
        return []
    
    with open(wordlist, "r") as f:
        return [linha.strip() for linha in f if linha.strip()]

# Execução multithread
def main():
    dominio_alvo, wordlist = obter_configuracoes()
    subdominios = carregar_wordlist(wordlist)
    if not subdominios:
        print(f"{Fore.RED}[!] Nenhum subdomínio encontrado na wordlist.{Style.RESET_ALL}")
        return
    
    subdominios_descobertos = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        list(tqdm(executor.map(lambda subdominio: resolver_subdominio(subdominio, dominio_alvo, subdominios_descobertos), subdominios), total=len(subdominios)))
    
    if subdominios_descobertos:
        print(f"\n{Fore.BLUE}[i] Subdomínios descobertos:{Style.RESET_ALL}")
        relatorio_path = "C:/relatorio_subdominios.txt"
        with open(relatorio_path, "w") as relatorio:
            for subdominio, ips in subdominios_descobertos:
                relatorio.write(f"{subdominio} -> {', '.join(ips)}\n")
                print(f"{Fore.GREEN}{subdominio} -> {', '.join(ips)}{Style.RESET_ALL}")
        print(f"\n{Fore.BLUE}[i] Relatório salvo em '{relatorio_path}'{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}[i] Nenhum subdomínio foi descoberto.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
