# Password Manager Tool

A simple command-line password manager that allows you to securely store, retrieve, and generate passwords.

## Features

- **Secure Storage**: Passwords are stored in an encrypted format using `cryptography`.
- **Password Retrieval**: Easily retrieve stored passwords for any account.
- **Password Generation**: Generate strong random passwords.

## Requirements

- Python 3.x
- `cryptography` library (install using `pip install cryptography`)

## Usage 

### Step 1: Setup

1. **Install Dependencies**: Ensure you have Python installed and then install the required package using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

2. **Save the Code**: Save the Python script provided earlier as `password_manager.py` in your project directory.

### Step 2: Add a Password

1. **Run the Script**: Use the `add` command to store a new password for an account. For example, to add a password for an account named "email":

   ```bash
   python password_manager.py add email
   ```

2. **Enter the Password**: The script will prompt you to enter the password securely:

   ```
   Enter the password:
   ```

   Type your password and press Enter. The password will be encrypted and stored in `passwords.json`.

### Step 3: Retrieve a Password

1. **Get the Password**: To retrieve the password for an account, use the `get` command. For example, to retrieve the password for "email":

   ```bash
   python password_manager.py get email
   ```

2. **Output**: The script will display the decrypted password for the account:

   ```
   Password for email: your_password_here
   ```

### Step 4: Generate a Password

1. **Generate a New Password**: Use the `generate` command to create a new random password:

   ```bash
   python password_manager.py generate
   ```

2. **Specify Length**: The script will prompt you to enter the desired length of the password (default is 12):

   ```
   Enter the desired length of the password (default 12): 
   ```

   Press Enter to accept the default or enter your preferred length. The generated password will be displayed:

   ```
   Generated password: random_password_here
   ```

### Security and Management

- **Encryption Key**: The script generates and stores an encryption key in a file named `secret.key`. This key is used to encrypt and decrypt passwords. Keep this file secure, as losing it means you cannot decrypt your stored passwords.

- **Password File**: All encrypted passwords are stored in `passwords.json`. This file contains account-password mappings in an encrypted format.

### Example Commands

Here’s a quick summary of how to use the tool:

- **Add a Password**:

  ```bash
  python password_manager.py add facebook
  ```

- **Retrieve a Password**:

  ```bash
  python password_manager.py get facebook
  ```

- **Generate a Password**:

  ```bash
  python password_manager.py generate
  ```

### Notes

- Ensure that `passwords.json` and `secret.key` are in a secure location and properly backed up.
- The tool is simple and suitable for learning and small-scale use; for more robust applications, consider additional security features such as user authentication or integrating with secure storage solutions.
