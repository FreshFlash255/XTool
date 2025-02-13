import os
import shutil
import json
import requests
import pyperclip
import getpass

os.system('cls' if os.name == 'nt' else 'clear')

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


TOKENS_FILE = "tokens.json"

def load_tokens():
    if not os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE, "w") as file:
            json.dump({"tokens": []}, file)
    with open(TOKENS_FILE, "r") as file:
        return json.load(file)

def save_tokens(data):
    with open(TOKENS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_token():
    token = input("Enter your user token: ")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        if 'username' in user_data and 'discriminator' in user_data:
            username = f"{user_data['username']}#{user_data['discriminator']}"
            tokens_data = load_tokens()
            tokens_data["tokens"].append({"token": token, "username": username})
            save_tokens(tokens_data)
            print(f"Token for {username} added successfully.")
        else:
            print("Failed to retrieve username or discriminator from the response.")
    else:
        print("Invalid token. Please try again.")

def list_tokens():
    tokens_data = load_tokens()
    if tokens_data["tokens"]:
        print("Stored tokens and usernames:")
        for entry in tokens_data["tokens"]:
            print(f"Username: {entry['username']}, Token: {entry['token']}")
    else:
        print("No tokens stored.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Token")
        print("2. List Tokens")
        print("3. Quit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("1. Get Token(!!NOT WORKING)")
            print("2. Paste Token")
            choice2 = input("Enter your choice: ").strip()
            if choice2 == "1":
                def get_token(email, password):
                    URL = "https://discord.com/api/v6/auth/login"
                    headers = {
                      "authorization": "undefined",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                       "content-length": '148',
                        "content-type": "application/json"
                    }
                    payload = {"email": email, "password": password}
                    request = requests.post(URL, headers=headers, data=json.dumps(payload)).json()
                    return request['token']

                print("Discord Token Parser | github.com/hell")
                email = input("email:\n")
                password = getpass.getpass("password:\n")
                token = get_token(email=email, password=password)
                print(f"Your Discord token is {token}\n It has been copied to your clipboard.")
                pyperclip.copy(token)
    
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                }
                response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
                if response.status_code == 200:
                    user_data = response.json()
                    username = f"{user_data['username']}#{user_data['discriminator']}"
                    tokens_data = load_tokens()
                    tokens_data["tokens"].append({"token": token, "username": username})
                    save_tokens(tokens_data)
                    print(f"Token for {username} added successfully.")
                else:
                    print("Failed to retrieve user data. Token not saved.")
            elif choice2 == "2":
                add_token()
        elif choice == "2":
            print()
            print()
            list_tokens()
            print()
        elif choice == "3":
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