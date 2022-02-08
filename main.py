from flask import Flask
from routes import index, login, logout


app = Flask(__name__)
app.secret_key = 'LADlskajhd37289roialkjnsx8p%^@&*$IEdba678923r'

app.register_blueprint(index.index)
app.register_blueprint(login.login)
app.register_blueprint(logout.logout)

if __name__ == '__main__':
    app.run(debug=True)