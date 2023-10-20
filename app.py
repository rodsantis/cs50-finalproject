import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///todolist.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show statistic page"""
    return render_template("index.html")


@app.route("/todo")
@login_required
def todo():
    todo = db.execute("SELECT * FROM todos WHERE user_id = ?;", session["user_id"])
    return render_template("todo.html", todo=todo)


@app.route("/add", methods=["GET", "POST"])
def add():
    todo = request.form['todo']
    db.execute("INSERT INTO todos (todo, user_id) VALUES (?, ?);", todo, session["user_id"])
    return redirect("/todo")


@app.route("/delete/<int:index>")
def delete(index):
    db.execute("DELETE FROM todos WHERE id=?;", index)
    return redirect("/todo")


@app.route("/outerfeedback", methods=["GET", "POST"])
def outerfeedback():
    # Getting the user feedback or request of help from the outside
    if request.method == "POST":
        if not request.form.get("outerfeedback"):
            return apology("feedback must have something written", 403)
        elif not request.form.get("outername"):
            return apology("name must have be provided", 403)
        elif not request.form.get("outeremail"):
            return apology("email must be provided", 403)
        else:
            name = request.form.get("outername")
            username = request.form.get("username")
            email = request.form.get("outeremail")
            age = request.form.get("outerage")
            heard_about = request.form.get("outerheard")
            text = request.form.get("outerfeedback")
            db.execute("INSERT INTO outerfeedback(feedback, name, username, email, age, heard) VALUES (?, ?, ?, ?, ?, ?);", text, name, username, email, age, heard_about)
            return render_template("thank.html")

    return render_template("outerfeedback.html")



@app.route("/feedback", methods=["GET", "POST"])
@login_required
def feedback():
    # Getting the userfeedback
    if request.method == "POST":
        if not request.form.get("feedback"):
            return apology("feedback must have something written", 403)
        else:
            name = request.form.get("name")
            age = request.form.get("age")
            heard_about = request.form.get("heard-us")
            text = request.form.get("feedback")
            db.execute("INSERT INTO feedback(feedback, name, age, heard, user_id) VALUES (?, ?, ?, ?, ?);", text, name, age, heard_about, session["user_id"])
            return render_template("thank.html")

    return render_template("feedback.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)


        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Setting variables to help on if-else below
    u_name = request.form.get("username")
    u_password = request.form.get("password")
    u_confirmp = request.form.get("confirmation")
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)
        # Ensure password is equal to confirmation password
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password doesn't match", 400)
        # Ensure that username is unique
        elif db.execute(
            "SELECT username FROM users WHERE username= ?;",
            request.form.get("username"),
        ):
            return apology("username already taken", 400)
        # Hashing password and adding information to SQLite table
        else:
            password_hash = generate_password_hash(u_password)
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?);",
                u_name,
                password_hash,
            )
            return render_template("login.html")
    # User reached via GET
    else:
        return render_template("register.html")