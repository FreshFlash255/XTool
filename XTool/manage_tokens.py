import json
import os
import requests

os.system('cls' if os.name == 'nt' else 'clear')

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
    token = input("Enter your user token: ").strip()
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
            add_token()
        elif choice == "2":
            list_tokens()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")