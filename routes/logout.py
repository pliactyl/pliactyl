from flask import Blueprint, render_template, session, abort, redirect, url_for, request, flash

logout = Blueprint('logout', __name__, template_folder='templates')


@logout.route("/logout")
def _logout():
    session.pop('username', None)
    return redirect('/login')
