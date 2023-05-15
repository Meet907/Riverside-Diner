from flask import Flask, render_template, request, url_for, redirect, flash, session
from datetime import datetime
from Helper import sqlQuery, menuQuery, imageQuery
from flask_mail import Mail, Message

# read README.txt for how to use sqlQuery() function
# !!! type "flask run" to run server now instead of "python app.py" !!!!

app = Flask(__name__)
app.config.from_pyfile('config.py')  # condensed all our config lines
mail = Mail(app)


@app.route("/", methods=['GET'])
def index():

    return render_template('index.html', debug=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # login logic
    if request.method == 'POST':
        email = request.form['email']
        passwordd = request.form['passwordd']

        user = sqlQuery(
            f"Select * from Login Where email='{email}' AND passwordd='{passwordd}'")
        if user:
            session["email"] = user[0][3]
            session["name"] = user[0][1]  # user's first name
            session["id"] = user[0][0]  # user's id
            return redirect(url_for('index'))
    return render_template("/auth/login.html", message=" you not logged in")
    # ------Login cookie logic ----------------


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the user's input
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        passwordd = request.form['passwordd']
        phonenumber = request.form['phonenumber']

        # Check if the username or email already exists
        user = sqlQuery(
            f"Select * from Login Where email='{email}' AND passwordd='{passwordd}';")

        if user:
            # Show an error message
            return "Username or email already exists"
        else:
            # Insert the new user into the database
            sqlQuery(
                f"INSERT INTO Login (firstname, lastname, email, passwordd, phonenumber) values('{firstname}','{lastname}','{email}','{passwordd}','{phonenumber}')")

            return redirect(url_for("login"))
    else:
        return render_template("/auth/register.html")


@app.route('/logout')
def logout():
    session["name"] = None
    session["id"] = None
    return redirect(url_for("index"))


@app.route('/reservations', methods=['GET', 'POST'])
def reservations():

    if request.method == 'POST':

        if (session["id"] == None):
            return redirect(url_for("login"))

        else:

            num_guests = request.form['guests']
            comments = request.form['comments']
            r_time = request.form['time']
            l_id = session["id"]
            r_date = request.form['date']

            sqlQuery(
                f"INSERT INTO Reservation (r_date, num_guests, r_time, comments, l_id) VALUES ('{r_date}','{num_guests}','{r_time}','{comments}','{l_id}')")
            # Email User

            emailuser = sqlQuery(
                f"Select email from Login where id = '{l_id}'")
            print(emailuser[0][0])

            msg = Message('Hello from the other side!',
                          sender='restauranttablebooking1@gmail.com', recipients=[emailuser[0][0]])
            msg.body = "hey, sending out email from flask!!!"
            mail.send(msg)

            print(msg)
            print(emailuser)
            return redirect(url_for("index"))

    else:
        return render_template("reservations.html")


@app.route('/locations')
def locations():
    return render_template("locations.html")


@app.route('/account', methods=["POST", "GET"])
def account():
    if request.method == "GET":
        # grab image from table
        # grab info from table
        email = session["email"]
        info = sqlQuery(
            f"Select * from Login Where email='{email}'")
        # display info in forms
        return render_template("account.html", info=info)
    return "POST METHOD NOT IMPLEMNTED YET"


@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'GET':
        return "YOU SHOULDNT BE HERE"
    return "Temp"


@app.route('/reservationinfo', methods=['GET', 'POST'])
def reservationinfo():
    if request.method == 'GET':
        return "YOU SHOULDNT BE HERE"
    return "Temp"


@app.route('/breakfast')
def breakfast():
    bmenu = menuQuery(
        "select ItemName, price, itemDesc from Breakfast;")
    imageQuery(
        "select itemImg from Breakfast;", 1)
    length = len(bmenu)
    print(bmenu)
    return render_template("breakfastMenu.html", bmenu=bmenu, length=length)


@app.route('/lunch')
def lunch():
    lmenu = menuQuery(
        "select ItemName, price, itemDesc from Lunch;")
    imageQuery(
        "select itemImg from Lunch;", 2)
    length = len(lmenu)
    return render_template("lunchMenu.html", lmenu=lmenu, length=length)


@app.route('/dinner')
def dinner():
    dmenu = menuQuery(
        "select ItemName, price, itemDesc from Dinner;")
    imageQuery(
        "select itemImg from Dinner;", 3)
    length = len(dmenu)
    return render_template("dinnerMenu.html", dmenu=dmenu, length=length)
