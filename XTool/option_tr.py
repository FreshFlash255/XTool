import json
import os
import shutil

os.system('cls' if os.name == 'nt' else 'clear')

TOKENS_FILE = "tokens.json"

print()

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



def load_tokens():
    if not os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE, "w") as file:
            json.dump({"tokens": []}, file)
    with open(TOKENS_FILE, "r") as file:
        return json.load(file)

def save_tokens(data):
    with open(TOKENS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def delete_token():
    tokens_data = load_tokens()
    if not tokens_data["tokens"]:
        print("No tokens stored.")
        return

    print("Stored tokens and usernames:")
    for index, entry in enumerate(tokens_data["tokens"], start=1):
        print(f"{index}. Username: {entry['username']}, Token: {entry['token']}")

    try:
        choice = int(input("Enter the number of the token to delete: ").strip())
        if 1 <= choice <= len(tokens_data["tokens"]):
            removed_token = tokens_data["tokens"].pop(choice - 1)
            save_tokens(tokens_data)
            print(f"Token for {removed_token['username']} deleted successfully.")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Delete Token")
        print("2. Quit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            delete_token()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
            
            print("\nChannel Cooler".center(shutil.get_terminal_size(2).columns))
print("\n")
print("\nOptions:".center(shutil.get_terminal_size().columns))
print("\nHome: [HOME] | Quit: [Q]\n")

while True:
    user_input = input("Enter your choice: ").strip().upper()
    
    if user_input == "Q":
        break
    elif user_input == "HOME":
        os.system('cls' if os.name == 'nt' else 'clear')
        file_name = "main.py"
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r') as file:
                    exec(file.read())
            except Exception as e:
                print(f"An error occurred while executing {file_name}: {e}")
        else:
            print(f"File {file_name} does not exist.")
    else:
        print("Invalid choice. Please try again.")