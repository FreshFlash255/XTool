import os
import shutil
from colorama import init, Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

# Initialize colorama
init(autoreset=True)

def draw_menu():
    terminal_width = shutil.get_terminal_size().columns
    
    ascii_art = f"""
    {Fore.RED}
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
    
    menu_options = [
        "1. Nitro Generator", "2. Channel Deleter", "3. Role Copier", "4. Role Deleter",
        "5. Create Channels", "6. User Kicker", "7. Spammer", "8. DM Sender",
        "9. Nuker", "10. Guild Leaver", "11. Message Deleter", "12. Webhook Spammer",
        "13. Messager", "14. Webhook Messager", "15. User Info", "16. Status Changer",
        "17. Users Manager", "18. VC Joiner", "19. Webhook Deleter", "20. Webhook Info"
    ]
    
    options_text = f"{Fore.GREEN}[TA] Add Tokens | [TR] Remove Tokens | [PA] Add Proxies | [PR] Remove Proxies"
    print(options_text.center(terminal_width))
    
    proxyBool = False
    proxyStatus = f"{Fore.GREEN}YES" if proxyBool else f"{Fore.RED}NO"
    proxy_info = f"Proxy: {proxyStatus}    Country: Austria"
    print(proxy_info.center(terminal_width))
    print("Options:".center(terminal_width))
    
    print("\n")
    
    cols = 4
    rows = len(menu_options) // cols + (len(menu_options) % cols > 0)
    col_width = max(len(option) for option in menu_options) + 4
    
    for i in range(rows):
        row_text = " ".join(menu_options[i + j * rows].ljust(col_width) for j in range(cols) if i + j * rows < len(menu_options))
        print(row_text.center(terminal_width))

draw_menu()
print()

while True:
    user_input = input("Enter your choice: ").strip().upper()
    
    if user_input == "Q":
        break
    
    menu_dict1 = {
        "TA": "Add Tokens", "TR": "Remove Tokens", "PA": "Add Proxies", "PR": "Remove Proxies"
    }
    
    if user_input in menu_dict1:
        os.system('cls' if os.name == 'nt' else 'clear')
        file_name = f"option_{user_input}.py"
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    exec(file.read())
            except Exception as e:
                print(f"An error occurred while executing {file_name}: {e}")
        else:
            print(f"File {file_name} does not exist.")
    
    menu_dict = {
        "1": "Nitro Generator", "2": "Channel Deleter", "3": "Role Copier", "4": "Role Deleter",
        "5": "Create Channels", "6": "User Kicker", "7": "Spammer", "8": "DM Sender",
        "9": "Nuker", "10": "Guild Leaver", "11": "Message Deleter", "12": "Webhook Spammer",
        "13": "Messager", "14": "Webhook Messager", "15": "User Info", "16": "Status Changer",
        "17": "Users Manager", "18": "VC Joiner", "19": "Webhook Deleter", "20": "Webhook Info"
    }
    
    if user_input in menu_dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        file_name = f"option_{user_input}.py"
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    exec(file.read())
            except Exception as e:
                print(f"An error occurred while executing {file_name}: {e}")
        else:
            print(f"File {file_name} does not exist.")