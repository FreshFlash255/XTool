import os
import shutil
import requests
from tqdm import tqdm
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

def draw_menu():
    terminal_width = shutil.get_terminal_size().columns
    
    ascii_art = """
    ███   ██▄▄▄█████▓▒█████  ▒█████  ██▓    
    ▒▒ █ █ ▒▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒    
    ░░  █   ▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░    
     ░ █ █ ▒░ ▓██▓ ░▒██   ██▒██   ██▒██░    
    ▒██▒ ▒██▒ ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒
    ▒▒ ░ ░▓ ░ ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ░
    ░░   ░▒ ░   ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░
     ░    ░   ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░   
     ░    ░             ░ ░     ░ ░     ░  ░
    """
    print(ascii_art.center(terminal_width))

draw_menu()

print("\nAdd Proxies".center(shutil.get_terminal_size().columns))
print("\n")
print("\nOptions:".center(shutil.get_terminal_size().columns))
print("\nHome: [HOME] | Quit: [Q]\n")

def add_proxy():
    proxy_list = []
    while True:
        proxy = input("Enter proxy (IP:Port) (or type 'done' to finish): ").strip()
        if proxy.lower() == 'done':
            break
        if ':' not in proxy:
            print("Invalid format. Please enter the proxy in the format IP:Port.")
            continue
        proxy_list.append(proxy)
    
    # Save proxies to a file (optional)
    with open('other_files\\proxies.txt', 'a') as file:
        for proxy in proxy_list:
            file.write(proxy + '\n')
    
    print("Proxies added successfully.")

def load_proxies():
    proxies = []
    try:
        with open('other_files\\proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("No proxies found. Please add proxies first.")
    return proxies

def use_proxy_request(url, proxies):
    for proxy in tqdm(proxies, desc="Connecting", unit="proxy"):
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        try:
            response = requests.get(url, proxies=proxy_dict)
            if response.status_code == 200:
                print(Fore.GREEN + f"Successfully connected using proxy {proxy}")
            else:
                print(f"Response from {proxy}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error with proxy {proxy}: {e}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    add_proxy()
    
    # Example usage of proxies
    proxies = load_proxies()
    if proxies:
        test_url = "http://example.com"
        use_proxy_request(test_url, proxies)

while True:
    user_input = input("Enter your choice: ").strip().upper()
    
    if user_input == "Q":
        break
    elif user_input == "HOME":
        os.system('cls' if os.name == 'nt' else 'clear')
        file_name = "main.py"
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    exec(file.read())
            except Exception as e:
                print(f"An error occurred while executing {file_name}: {e}")
        else:
            print(f"File {file_name} does not exist.")
    else:
        print("Invalid choice. Please try again.")