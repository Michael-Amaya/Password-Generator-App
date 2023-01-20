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