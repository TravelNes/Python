from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from auth import auth
app.register_blueprint(auth, url_prefix='/auth')
Bootstrap(app)


@app.route('/')
def index():
    s = 'you are not login'
    if 'username' in session:
        return render_template('index.html', name=session['username'])
    return render_template('index.html', name=s)


if __name__ == '__main__':
    app.run(debug=True)
