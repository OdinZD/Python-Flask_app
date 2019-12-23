from flask import Flask, render_template, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email
from forms import Login_Form, Register_Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ovojetajnikljuc!'
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form=Login_Form()

    if form.validate_on_submit():
        #Za test da se vidi dali radi Login funkcija i forma. AKo radi na ekranu će vratiti podatke koje ste unijeli u Login polja.
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    form= Register_Form()

    if form.validate_on_submit():
        #Za test da se vidi dali radi signup funkcija i forma. AKo radi na ekranu će vratiti podatke koje ste unijeli u sign Up polja.
        return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

