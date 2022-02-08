from flask import Blueprint, render_template, session, abort, redirect, url_for, request, flash

index = Blueprint('index', __name__, template_folder='templates')


@index.route("/")
def hello():
    if 'username' in session:
        return render_template('index.html', name=session['username'])
    return redirect('/login')
