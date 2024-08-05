from flask import Blueprint, render_template, request, flash
# from form_val import check_email, check_name, check_password
import re

def check_email(mail):
    if re.search(r"^.+@.+\..+", mail):
        return True
    return False

def check_name(name):
    if re.search(r"[a-zA-Z+]", name):
        return True
    return False

def check_password(password1, password2):
    
    if password1 == password2 and len(password1) >= 8:
        return True
    return False


auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
   
@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    
        # Refactor this code in the future
        if not check_email(email):
            flash("Invalid Email", category='error')
        elif not check_name(firstname):
            flash("Invalid Name", category='error')
        elif not check_password(password1, password2):
            flash("Invalid Passwords", category='error')
        else:
            # Add user to database
            flash("Account Created", category="success")

    return render_template("signup.html")