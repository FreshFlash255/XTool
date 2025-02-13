import shutil
import os
import json
import discord

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

# Load the token from tokens.json
try:
    with open('tokens.json', 'r') as file:
        tokens_data = json.load(file)
        user_token = tokens_data['tokens'][0]['token']
except (FileNotFoundError, KeyError, IndexError) as e:
    print(f"Error loading token: {e}")
    exit(1)

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print("\nServers:")
    for guild in client.guilds:
        print(f"- {guild.name} (ID: {guild.id})")
        print("  Channels:")
        for channel in guild.channels:
            print(f"    - {channel.name} (ID: {channel.id})")
        print("  Categories:")
        for category in guild.categories:
            print(f"    - {category.name} (ID: {category.id})")

@client.event
async def on_message(message):
    if message.content.startswith('!list_servers'):
        response = "Servers:\n"
        for guild in client.guilds:
            response += f"- {guild.name} (ID: {guild.id})\n"
            response += "  Channels:\n"
            for channel in guild.channels:
                response += f"    - {channel.name} (ID: {channel.id})\n"
            response += "  Categories:\n"
            for category in guild.categories:
                response += f"    - {category.name} (ID: {category.id})\n"
        await message.channel.send(response)

client.run(user_token,)

print("\nWebhook Messenger".center(shutil.get_terminal_size(2).columns))
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