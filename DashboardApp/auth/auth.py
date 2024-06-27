# DashboardApp/auth/auth.py
from flask import Blueprint, redirect, render_template, request, url_for, session, current_app
from flask_login import login_required, login_user, logout_user
from DashboardApp import login_manager
from .models.user import User

auth_bp = Blueprint(
    "auth", __name__, static_folder="static", template_folder="templates"
)

@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # logic for handling login

        # get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]

        # check if the username and password are correct
        if user := User.authenticate(username, password):
            # if the user is authenticated, redirect to the dashboard
            create_session(user)
            login_user(user, remember=True)
            return redirect(url_for("core.home"))
        else:
            # if the user is not authenticated, show an error message
            return render_template(
                "login.html",
                username=username,
                password=password,
                error_message="⚠️ Invalid username or password.",
            )

    return render_template("login.html")


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # logic for creating a new user account

        # get the username and password from the form
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]

        # check if the username already exists
        if user := User.authenticate(username, password):
            # if the user already exists, show an error message
            error_message = "⚠️ Username already exists."
        else:
            # if the user does not exist, try to create a new user account
            if password != confirm_password:
                error_message = "⚠️ Passwords do not match."

            # if username already exists
            elif User.user_exists(username):
                error_message = "⚠️ Username already exists."

            # should be able to create a new user
            else:
                new_user = User(username, password)
                new_user.save()

                create_session(new_user)
                login_user(user, remember=True)

                return redirect(url_for("core.home"))

            # return the signup page with the error message
            return render_template(
                "signup.html",
                username=username,
                password=password,
                confirm_password=confirm_password,
                error_message=error_message,
            )

    return render_template("signup.html")


@auth_bp.route("/logout")
@login_required
def logout():
    # check if the user is logged in
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    # get the user object
    user = User.get_user(session["user_id"])

    # logout user
    user.logout()
    logout_user()

    # Clear the user session
    session.clear()

    # redirect to the login page
    return redirect(url_for("core.home"))


def create_session(user: User):
    # set a session variable to indicate that the user is logged in
    session["user_id"] = user.id
    session["username"] = user.username

    # update user's last login timestamp
    user.login()

    return
