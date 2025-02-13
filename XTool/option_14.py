import os
import shutil
from discord_webhook import DiscordWebhook, DiscordEmbed, DiscordWebhook
import requests

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

print("\nWebhook Messenger".center(shutil.get_terminal_size(2).columns))
print("\n")
print("\nOptions:".center(shutil.get_terminal_size().columns))
print("\nHome: [HOME] | Quit: [Q]\n")

def send_discord_message(webhook_url, message, file_path=None):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    if file_path:
        with open(file_path, "rb") as f:
            webhook.add_file(file=f.read(), filename=os.path.basename(file_path))
    response = webhook.execute()
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

while True:
    webhook_url = input("Enter the Discord webhook URL: ").strip()
    
    if user_input == "q":
        break
    elif user_input == "home":
        os.system('cls' if os.name == 'nt' else 'clear')
        file_name = "main.py"
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r') as file:
                    exec(file.read())
            except Exception as e:
                print(f"An error occurred while executing {file_name}: {e}")
    
    while True:
        message = input("Enter the message to send (or type '.h' or '.help'): ").strip()
        if message.lower() in ['.q', '.quit']:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif message.lower() in ['.h', '.help']:
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            print("Type '.q' or '.quit' to stop sending messages.")
            print("Type '.s' or '.spam' to spam messages.")
            print("Type '.b' or '.bomb' to spam junk messages.")
            print()
            continue
        elif message.lower() in ['.s', '.spam']:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                spam_message = input("Enter the message to spam (or type '.q' or '.quit' to stop): ").strip()
                if spam_message.lower() in ['.q', '.quit']:
                    break
                try:
                    spam_messageint = int(input("Enter the amount of messages to spam(or type '.q' or '.quit' to stop): ").strip())
                    for i in range(spam_messageint):
                        send_discord_message(webhook_url, spam_message)
                except ValueError:
                    print("Please enter a valid number.")
                continue
        elif message.lower() in ['.b', '.bomb']:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("This feature is not available in this version.")
            print("Press .q or .quit to go back.")
            while True:
                bomb_file = input("Enter the path of the file to spam (type '.q' or '.quit' to stop or just press enter for the default file): ").strip()
                if bomb_file.lower() in ['.q', '.quit']:
                    break
                elif bomb_file == "":
                    bomb_file = "other_files\\hallo.txt"
                bomb_messageint = int(input("Enter the amount of messages to spam: "))
                for i in range(bomb_messageint):
                    send_discord_message(webhook_url, "@everyone", bomb_file) 
                continue
        elif message.lower() in ['.d', '.delete']:
            os.system('cls' if os.name == 'nt' else 'clear')

                # Eingabe des Webhook-Links vom Benutzer
                 # Bestätigung der Löschung durch den Benutzer
            confirmation = input((f"Do you really want to delete this webhook? (y/n): ")).lower()

            if confirmation == 'y':
                try:
                    response = requests.delete(webhook_url)

                    if response.status_code == 204:
                        print("Webhook successfully got deleted.")
                    else:
                        print(f"Error Webhook couldn't be deleted {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"An error occured {e}")

                # Option zum Abbrechen oder Neustarten der Schleife
            
        else:
            send_discord_message(webhook_url, message)
    
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