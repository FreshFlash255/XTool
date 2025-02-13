from discord_webhook import DiscordWebhook
import requests
import random
import string
import os
import concurrent.futures
import shutil

class NitroGen:  # Initialize the class
    def __init__(self):  # The initialization function
        self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in
        self.validFileName = "validcodes.txt"  # File for valid codes

    def main(self):  # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        num = int(input("\nInput How Many Codes to Generate and Check: "))

        # Get the webhook URL
        url = input("\nDo you wish to use a Discord webhook? \nIf so, type it here or press enter to ignore: ")
        webhook = url if url != "" else None  # If the URL is empty make it None instead

        valid = []  # Keep track of valid codes
        invalid = 0  # Keep track of how many invalid codes were detected

        # Generate and check codes in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.quickChecker, self.generateCode(), webhook) for _ in range(num)]
            for future in concurrent.futures.as_completed(futures):
                result, code = future.result()
                if result:  # If the code was valid
                    valid.append(code)  # Add the valid code to the list
                    self.saveValidCode(code)  # Save the valid code to file
                    print(f"✅ Valid | {code}")
                else:
                    invalid += 1  # Increase the invalid counter
                    print(f"❌ Invalid | {code}")

        # Display final results
        print(f"\nSummary:")
        print(f"❌ Invalid: {invalid}")
        print(f"✅ Valid: {len(valid)}")
        
        if len(valid) > 0:
            print("Valid Codes:")
            for code in valid:
                print(f"✅ {code}")

    def generateCode(self):  # Generate a Nitro code
        return "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))

    def quickChecker(self, code, webhook=None):  # Check a single code
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  # Get the response from Discord

        if response.status_code == 200:  # If the response went through
            if webhook:  # If a webhook is set up
                DiscordWebhook(
                    url=webhook,
                    content=f"✅ Valid Nitro Code detected! @everyone \nhttps://discord.gift/{code}"
                ).execute()
            return True, f"https://discord.gift/{code}"  # Return valid code
        else:
            return False, f"https://discord.gift/{code}"  # Return invalid code

    def saveValidCode(self, code):  # Save valid code to file
        with open(self.validFileName, "a", encoding="utf-8") as file:  # Open the file in append mode
            file.write(f"{code}\n")  # Write the valid code to the file

if __name__ == '__main__':
    Gen = NitroGen()  # Create the Nitro generator object
    Gen.main()  # Run the main code

    genmore = input("Do you want to Generate more? (y/n)")
    if genmore == "n":
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
    elif genmore == "y":
        __name__ == '__main__'
    else:
        print("Invalid Choice")
        genmore = input("Do you want to Generate more? (y/n)")