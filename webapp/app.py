from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Function to check if the password meets the requirements
def is_valid_password(password):
    # Add your password requirements here (e.g., minimum length)
    if len(password) < 8:
        return False

    # Block common passwords from the list
    common_passwords = set(line.strip() for line in open('common_passwords.txt'))
    if password in common_passwords:
        return False

    # Add more password requirements as needed
    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']

        # Validate the password
        if not is_valid_password(password):
            flash('Invalid password. Please meet the password requirements.')
            return redirect(url_for('home'))

        # If password is valid, go to the welcome page
        return redirect(url_for('welcome', password=password))

    # For GET requests or initial load, render the home page
    return render_template('home.html')

@app.route('/welcome/<password>')
def welcome(password):
    return render_template('welcome.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
