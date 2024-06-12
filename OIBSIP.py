from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database (replace with a proper database in real applications)
users = {'admin': 'admin123'}

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', message='Username already exists. Please choose a different one.')
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html', message='')

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('secured'))
        else:
            return render_template('login.html', message='Invalid username or password.')
    return render_template('login.html', message='')

# Secured page accessible after login
@app.route('/secured')
def secured():
    return render_template('secured.html')

if __name__ == '__main__':
    app.run(debug=True)
