from flask import Blueprint, render_template, request, flash, redirect, url_for
from .form_val import check_email, check_name, check_password
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
    
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", category="success")
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password", category="error")
        else:
            flash("User doesn't exist.", category= "error")
        
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
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already in use', category='error')
        elif not check_email(email):
            flash("Invalid Email", category='error')
        elif not check_name(firstname):
            flash("Invalid Name", category='error')
        elif not check_password(password1, password2):
            flash("Invalid Passwords", category='error')
        else:
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='pbkdf2:sha1'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created", category="success")
            return redirect(url_for('views.home'))
        
    return render_template("signup.html")