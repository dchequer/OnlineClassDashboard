# DashboardApp/auth/auth.py
from flask import Blueprint, redirect, render_template, request, url_for, session, flash
from .models.user import User

auth_bp = Blueprint(
    "auth", __name__, static_folder="static", template_folder="templates"
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # logic for handling login
        print("login POST request received")

        # get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]

        # check if the username and password are correct
        if user := User.authenticate(username, password):
            # if the user is authenticated, redirect to the dashboard
            print("User authenticated")
            create_session(user)
            return redirect(url_for("core.home"))
        else:
            # if the user is not authenticated, show an error message
            print("User not authenticated")
            return render_template("login.html", username=username, password=password, error_message="⚠️ Invalid username or password.")

    return render_template("login.html")


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # logic for creating a new user account
        print("signup POST request received")

        # get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]

        # check if the username already exists
        if user := User.authenticate(username, password):
            # if the user already exists, show an error message
            print("User already exists")
            error_message = "⚠️ Username already exists."
        else:
            # if the user does not exist, try to create a new user account
            if password != confirm_password:
                print("Passwords do not match")
                error_message = "⚠️ Passwords do not match."
            
            # if username already exists
            elif User.user_exists(username):
                print("Username already exists")
                error_message = "⚠️ Username already exists."

            # should be able to create a new user
            else:
                new_user = User(username, password)
                new_user.save()
                print("User created successfully")

                create_session(new_user)

                return redirect(url_for("core.home"))
            
            # return the signup page with the error message
            return render_template("signup.html", username=username, password=password, confirm_password=confirm_password, error_message=error_message)

    return render_template("signup.html")


@auth_bp.route("/logout")
def logout():
    # check if the user is logged in
    if "user_id" not in session:
        print("User not logged in")
        return redirect(url_for("auth.login"))
    
    # get the user object
    user = User.get_user(session["user_id"])

    # update user's last logout timestamp
    user.logout()

    # Clear the user session
    session.clear()


    # redirect to the login page
    return redirect(url_for('home.home')) 


def create_session(user: User):
    # set a session variable to indicate that the user is logged in
    session["user_id"] = user.id
    session["username"] = user.username

    # update user's last login timestamp
    user.login()

    return
