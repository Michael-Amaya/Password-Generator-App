const ButtonStates = {
    Show: 0,
    Hide: 1
};

let current_state = ButtonStates.Hide;

document.getElementById('show_hide_pass').addEventListener('click', () => {
    if (current_state === ButtonStates.Show) {
        current_state = ButtonStates.Hide;
        document.getElementById('password').type = 'password';
        document.getElementById('show_hide_pass').innerText = 'Show Password';
    } else {
        current_state = ButtonStates.Show;
        document.getElementById('password').type = 'text';
        document.getElementById('show_hide_pass').innerText = 'Hide Password';
    }
});