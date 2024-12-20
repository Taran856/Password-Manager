import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Forming a string of random letters, symbols and numbers
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # Creating a string from the list
    password = "".join(password_list)

    # Clearing the password field and adding the newly generated password
    password_entry.delete(0, END)
    password_entry.insert(END, password)

    # Copying the newly generated password to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {
        website_entry.get(): {
            "email": username_entry.get(),
            "password": password_entry.get()
        }
    }
    # Error handling if the password or website fields are empty
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            # Creating the text file we want to save our info in
            with open("data.json", "r") as data_file:
                # Reading the json file
                data = json.load(data_file)

                # Update the json file
                data.update(new_data)

        except:
            with open("data.json", "w") as data_file:
                # writing in a new file
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", "w") as data_file:
                # writing the updated file
                json.dump(data, data_file, indent=4)

        finally:
            # Deleting the entries for website and the password
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as data_file:
            # Reading the json file
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")

    else:
        try:
            messagebox.showinfo(title="Website Credential",
                                message=f"Website: {website_entry.get()}\nPassword: {data[website_entry.get()]}")

        except:
            messagebox.showinfo(title="Oops", message="No details for the website found")


# ---------------------------- UI SETUP ------------------------------- #

# Creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Inputs

website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, "taranpatel1006@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Buttons

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_pass, width=13)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
