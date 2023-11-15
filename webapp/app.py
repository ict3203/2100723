from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Function to check if the password meets the requirements
def is_valid_password(password, mfa_enabled=False):
    # Minimum length requirement
    min_length = 10 if not mfa_enabled else 8
    if len(password) < min_length:
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

        # In a real application, you should check whether MFA is enabled for the user
        mfa_enabled = False  # Replace with your MFA check logic

        # Validate the password
        if not is_valid_password(password, mfa_enabled):
            flash('Invalid password. Please meet the password requirements.')
            return redirect(url_for('home'))

        # If password is valid, go to the welcome page
        return redirect(url_for('welcome', password=password))

    # For GET requests or initial load, render the home page
    return render_template('home.html')

@app.route('/welcome/<password>')
def welcome(password):
    if request.method == 'POST':
        # Add any logout logic here if needed
        return redirect(url_for('home'))

    return render_template('welcome.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
