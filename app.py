from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "mysecretkey123"

users = {}
students = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect('/login')
    return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"
    return render_template("login.html")

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    if request.method == "POST":
        name = request.form['name']
        roll = request.form['roll']
        cls = request.form['class']
        students.append({"name": name, "roll": roll, "class": cls})
    
    return render_template("dashboard.html", students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
