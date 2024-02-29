from time import sleep
import random
import string

# User accounts dictionary
user_accounts = {
    "jay": "1234",
    "elliott": "5678",
    "sage": "!£$%"
}

def validChars(input_str):
    return input_str.isalnum()

def register():
    print("Welcome! Let's create a new account.")
    new_username = input("Enter your username: ")
    while not validChars(new_username):
        print("Username can only contain alphanumeric characters.")
        new_username = input("Enter your username: ")

    new_password = input("Enter your password: ")
    user_accounts[new_username] = new_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_accounts and user_accounts[username] == password:
        print(f"Welcome {username}! What would you like to buy?")
        return username
    else:
        print("Invalid username or password.")
        return None

def purchase(username):
    available_items = ["script kiddie shit", "coffee", "deep web links"]
    print("Available items:")
    for i, item in enumerate(available_items, 1):
        print(f"{i}. {item}")

    choice = input("Enter the number of the item you want to purchase: ")
    if choice.isdigit() and 1 <= int(choice) <= len(available_items):
        print(f"You have purchased: {available_items[int(choice) - 1]}")
        return True
    else:
        print("Invalid choice.")
        return False

def generate_key(length=12):
    alphanumeric_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric_characters) for _ in range(length))

if __name__ == "__main__":
    while True:
        ask_for_ac = input("Do you have an account with us? (yes/no): ")
        if ask_for_ac.lower() == "no":
            create_account = input("Would you like to make one? (yes/no): ")
            if create_account.lower() == "yes":
                register()
            else:
                print("Okay, goodbye.")
                break

        username = login()
        if username:
            if purchase(username):
                # Generate and verify access key
                access_key = generate_key()
                print(f"Random access key: {access_key}")

                key_check = input("Enter the key for verification: ")
                if key_check == access_key:
                    print("Purchase verified!")
                    sleep(10)
                else:
                    print("Wrong access key. Purchase failed.")
            else:
                print("Purchase failed.")

        stop_program = input("Do you want to stop the program? (yes/no): ")
        if stop_program.lower() == "yes":
            print("Okay, goodbye.")
            break
