from flask import Blueprint, render_template, session, abort, redirect, url_for, request, flash

login = Blueprint('login', __name__, template_folder='templates')


@login.route("/login", methods=['POST', 'GET'])
def _login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['username'] = request.form['username']
        else:
            flash("Invalid username or password")
            return render_template('login.html')
        return redirect('/')
    else:
        return render_template('login.html')
