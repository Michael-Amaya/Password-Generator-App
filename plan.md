# Plan for Password Generator App
This file may change as time goes on, and as goals are achieved/wanted.
## Goals
- Make a functioning website with the following features:
    - Variable password length
    - Ability to exclude or include special characters
        - Special characters can be toggleable
    - Able to delete/create/view passwords
    - Be able to download web extension and standalone app from website
    - Have secure login system with master password
        - Master password should be very strict: high character count, symbols, uppercase and lowercase, etc.
- Make a functioning standalone app with the following features:
    - Many of the same features with the website
    - Login single time. Use master password to view crucial settings
    - Copy passwords to clipboard
- Make a functioning Browser Extension:
    - Whenever a password field is detected, ask the user if they want to use the app to automatically input the password


## Technical Requirements
- The website will be written in Python 3 with Flask 2.2.2
- The app will use PostgreSQL 13 or MySQL 8. 
- The website will be hosted on Heroku along with the database.
- Password generation logic will be written in Python 3.
- Website logic will be written in JavaScript ES6+ with JQuery 3.6.3.
- The browser extension will be written in JavaScript ES6+.

## Standalone Application Logic
- The application sets the default password length to 8
    - Allows for change with the usage of an input box
    - Click a button to confirm change
- The application allows for the user to toggle specific charcters to put into their password 
    - Green slider button means the character can be included
    - Red slider button means the character is excluded
- The application allows for the user to toggle between upper and lowercase characters
    - Green slider on uppercase means only uppercase
    - Green slider on lowercase means only lowercase
    - Green slider on both means both are included
    - Red slider on uppercase means no uppercase
    - Red slider on lowercase means no lowercase
    - Red slider on both means no letters
- The application allows for the user to toggle numbers
    - Green slider on numbers means numbers are included
    - Red slider on numbers means numbers are excluded
- The application creates the password
    - Use a button to create the password

