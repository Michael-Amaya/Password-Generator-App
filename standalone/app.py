import secrets
import string

# set default length to 8
password_length = 8

# sets up the usable characters which holds what is allowed to be used in the password
usable_characters = ""

# sets lower case letters and numbers to be on by default
lower_case = True
numbers = True

# creates variable for uppercase letters
upper_case = False

# creates variables for all symbols and includes them in an array
exclaimation_point = {'bool': False, 'char': '!'}
at_sign = {'bool': False, 'char': '@'}
pound = {'bool': False, 'char': '#'}
dollar = {'bool': False, 'char': '$'}
percent = {'bool': False, 'char': '%'}
carrot = {'bool': False, 'char': '^'}
ampersand = {'bool': False, 'char': '&'}
astrick = {'bool': False, 'char': '*'}
right_parenthesis = {'bool': False, 'char': '('}
left_parenthesis = {'bool': False, 'char': ')'}
period = {'bool': False, 'char': '.'}
comma = {'bool': False, 'char': ','}

symbols = [exclaimation_point, at_sign, pound, dollar, percent, carrot, ampersand, 
           astrick, right_parenthesis, left_parenthesis, period, comma]

# set password length function
def change_length():
    return 0

# this function creates a password using specified parameters. 
def create_password():
    global password_length
    global usable_characters

    # for all symbols check if they are allowed to be used
    for x in symbols:

        # if a symbol is not allowed, remove it from the usable characters
        if x['bool'] == False:
            usable_characters = usable_characters.replace(x['char'], '')
        
        # if a symbol is allowed, add it to the usable characters
        else:

            # if a symbol is not already in the usable characters, add it. If it already exists then there is no need to add a copy 
            if x['char'] not in usable_characters:
                usable_characters = usable_characters + x['char']

    # if upper case letters are allowed, add them if they are not already allowed
    if upper_case is True:
        if string.ascii_uppercase not in usable_characters:
            usable_characters = usable_characters + string.ascii_uppercase
    # if upper case letters are not included, remove them from the allowed characters
    else:
        usable_characters = usable_characters.replace(string.ascii_uppercase, '')

    # if lower case letters are allowed, add them if they are not already allowed
    if lower_case is True:
        if string.ascii_lowercase not in usable_characters:
            usable_characters = usable_characters + string.ascii_lowercase
    # if lower case letters are not included, remove them from the allowed characters
    else:
        usable_characters = usable_characters.replace(string.ascii_lowercase, '')

    # if numbers are allowed, add them if they are not already allowed
    if numbers is True:
        if string.digits not in usable_characters:
            usable_characters = usable_characters + string.digits
    # if numbers are not included, remove them from the allowed characters
    else:
        usable_characters = usable_characters.replace(string.digits, '')
    
    # create the actual password
    password = ''.join(secrets.choice(usable_characters) for i in range(password_length))














# from logging import root
# import string
# import secrets
# from textwrap import wrap
# import pyperclip
# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk

# password_length = 8

# def changeSize():

#     def change():
#         global password_length
#         password_length = int(e.get())
#         root.destroy()

#     root = Tk()
#     e = Entry(root, bg = "gray")
#     label = Label(root, text = "Enter desired length of password")
#     b = Button(root, text = "Change", command = change)
#     #exit_button = Button(root, text = "Exit", command = root.destroy)
    
#     label.grid(column = 1, row = 1)
#     e.grid(column = 1, row = 2)
#     b.grid(column = 1, row = 3)
#     #exit_button.grid(column = 1, row = 4)

# def makePassword():

#     global password_length
#     alphabet = string.ascii_letters + string.digits
#     password = ''.join(secrets.choice(alphabet) for i in range(password_length))
#     pyperclip.copy(password)
#     messagebox.showinfo("Password Generator", "Password has been copied to your clipboard")

# def makePasswordWithChars():

#     global password_length

#     alphabet = string.ascii_letters + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "\&"
#     password = ''.join(secrets.choice(alphabet) for i in range(password_length))
#     pyperclip.copy(password)
#     messagebox.showinfo("Password Generator", "Password has been copied to your clipboard")

# window = Tk()

# window.title('Password Generator')
# window.geometry("404x75")
# window.config(background = "white")

# button_changeNumber = Button(window, text = "Change Password Size", fg = "black", command = changeSize)
# button_makePassword = Button(window, text = "Make Password", fg = "black", command = makePassword)
# button_makePasswordWChars = Button(window, text = "Make Password w/ Special Chars", fg = "black", command = makePasswordWithChars)
# button_exit = Button(window, text = "Exit", fg = "red", command = window.destroy)

# button_changeNumber.grid(column = 3, row = 1)
# button_makePassword.grid(column = 1, row = 1)
# button_makePasswordWChars.grid(column = 2, row = 1)
# button_exit.grid(column = 2, row = 2)

# window.mainloop()