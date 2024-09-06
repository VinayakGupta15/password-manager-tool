import os
import sys
import json
import base64
import getpass
import secrets
import string
from cryptography.fernet import Fernet

PASSWORD_FILE = "passwords.json"
KEY_FILE = "secret.key"


def generate_key():
    """Generate a key for encryption and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    """Load the encryption key from the current directory."""
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()
    return key


def encrypt_password(password, key):
    """Encrypt a password using the given key."""
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password, key):
    """Decrypt a password using the given key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()


def load_passwords():
    """Load passwords from a JSON file."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}


def save_passwords(passwords):
    """Save passwords to a JSON file."""
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)


def generate_password(length=12):
    """Generate a random password with a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


def add_password(account, password, key):
    """Add a new password for an account."""
    passwords = load_passwords()
    encrypted_password = encrypt_password(password, key)
    passwords[account] = encrypted_password
    save_passwords(passwords)
    print(f"Password for {account} added successfully.")


def get_password(account, key):
    """Retrieve the password for an account."""
    passwords = load_passwords()
    encrypted_password = passwords.get(account)
    if encrypted_password:
        return decrypt_password(encrypted_password, key)
    else:
        print(f"No password found for account: {account}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python password_manager.py [add|get|generate] [account]")
        return

    command = sys.argv[1]
    key = load_key()

    if command == "add":
        if len(sys.argv) != 3:
            print("Usage: python password_manager.py add [account]")
            return
        account = sys.argv[2]
        password = getpass.getpass(prompt="Enter the password: ")
        add_password(account, password, key)

    elif command == "get":
        if len(sys.argv) != 3:
            print("Usage: python password_manager.py get [account]")
            return
        account = sys.argv[2]
        password = get_password(account, key)
        if password:
            print(f"Password for {account}: {password}")

    elif command == "generate":
        length = input("Enter the desired length of the password (default 12): ")
        if not length.isdigit():
            length = 12
        else:
            length = int(length)
        print(f"Generated password: {generate_password(length)}")

    else:
        print("Invalid command. Use 'add', 'get', or 'generate'.")


if __name__ == "__main__":
    main()