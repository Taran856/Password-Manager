# Password Manager

A simple password manager application built using Python's Tkinter library. This tool generates secure passwords and stores them for easy access, helping you manage credentials efficiently and securely. 

## Purpose
I created this project because I struggled with managing passwords across various accounts, often resulting in weak, easy-to-remember passwords that I reused across multiple sites. This project helps me generate and securely store strong, unique passwords for each site, improving my overall online security.

## Features
- **Password Generator**: Generates strong passwords using random letters, symbols, and numbers.
- **Save Functionality**: Saves the website, username, and password to a text file for easy reference.
- **Clipboard Copying**: Automatically copies the newly generated password to your clipboard.
- **User-Friendly UI**: Built with Tkinter for a simple, accessible interface.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Taran856/password-manager.git
    cd password-manager
    ```
2. Ensure you have Python installed (version 3.6 or above).
3. Install the necessary packages:
    ```bash
    pip install pyperclip
    ```
4. Place an image file named `logo.png` in the same directory for the logo display on the UI.

## Usage
1. Run the program:
    ```bash
    python password_manager.py
    ```
2. **Generate a Password**:
   - Enter the website and email/username.
   - Click **Generate Password** to create a strong, random password, which will automatically be copied to your clipboard.
3. **Save a Password**:
   - Click **Add** to save the website, username, and password to `data.txt`.
   - If any field is empty, the program will prompt you to fill it in.
   - You’ll be asked to confirm before saving the information.
4. All saved credentials are stored in `data.txt` in the following format:
    website | username | password

## Code Structure
- **Password Generator**: Generates a strong password using a mix of letters, symbols, and numbers.
- **Save Function**: Saves credentials to `data.txt` with a prompt for confirmation.
- **Clipboard Functionality**: Automatically copies the generated password to the clipboard using `pyperclip`.
- **UI Setup**: Sets up the Tkinter

## Note
Ensure `data.txt` is stored securely, as it contains sensitive information.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, please reach out to [taranpatel1006@gmail.com](mailto:taranpatel1006@gmail.com).
