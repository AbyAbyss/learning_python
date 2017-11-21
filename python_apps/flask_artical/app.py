# importing Flask and render_tamplate:to use external files
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articals    # user module
from flask_mysqldb import MySQL  # pip install flask-mysql
# pip install Flask-WTF for using with form
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '!2abyabyss'
app.config['MYSQL_DB'] = 'artical_app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

# external data.py
Articals = Articals()


# root
@app.route('/')
def index():
    return render_template('home.html')


# /about
@app.route('/about')
def about():
    return render_template('about.html')

# goings to /articals and also sends the data from artical


@app.route('/articals')
def articals():
    return render_template('articals.html', articals=Articals)


# takes id and uses it and pass it so that it can display on the page
@app.route('/artical/<string:id>/')
def artical(id):
    return render_template('artical.html', id=id)


# modify
@app.route('/login')
def login():
    return render_template('login.html')



###############################################################################
class ResgisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
###############################################################################



###############################################################################
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = ResgisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
                    (name, email, username, password))

        # commit to DB
        mysql.connection.commit()

        # Close the connection
        cur.close()

        flash('You are now resgistered', 'success')

        # go to index after login
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
###############################################################################


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
