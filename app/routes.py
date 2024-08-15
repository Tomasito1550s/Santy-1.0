from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Appointment
from . import mongo, bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = mongo.db.users.find_one({'email': email})

        if user and bcrypt.check_password_hash(user['password'], password):
            login_user(User(user))
            return redirect(url_for('main.admin'))
        else:
            flash('Invalid email or password')

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/admin')
@login_required
def admin():
    appointments = mongo.db.appointments.find()
    return render_template('admin.html', appointments=appointments)

@main.route('/reserve', methods=['POST'])
def reserve():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        mongo.db.appointments.insert_one({'date': date, 'time': time, 'name': name, 'status': 'Pending'})
        flash('Appointment reserved successfully!')
        return redirect(url_for('main.index'))
