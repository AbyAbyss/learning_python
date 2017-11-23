# importing Flask and render_tamplate:to use external files
from flask import Flask, render_template, flash, redirect, url_for, session, request
# from data import Articles    # user module
from flask_mysqldb import MySQL  # pip install flask-mysql
# pip install Flask-WTF for using with form
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
# wraps function
from functools import wraps


app = Flask(__name__)

###############################################################################
# config MySQL
###############
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '!2abyabyss'
app.config['MYSQL_DB'] = 'article_app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
###############
# init MYSQL
###############
mysql = MySQL(app)
###############################################################################


# external data.py
# Articles = Articles()   # now reading from database


###############################################################################
# check if user logged in #imp# FOR AUTORIZATION
###############
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unautorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap
###############################################################################


###############################################################################
# root of the application
###############
@app.route('/')
def index():
    return render_template('home.html')
###############################################################################


###############################################################################
# /about page
###############
@app.route('/about')
def about():
    return render_template('about.html')
###############################################################################


###############################################################################
# goings to /articles and also sends the data to article
###############
@app.route('/articles')
def articles():
    # activating cursor to use the database
    cur = mysql.connection.cursor()

    # get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    # close connection
    cur.close()
###############################################################################


###############################################################################
# takes id and uses it so that it can display on the article
###############
@app.route('/article/<string:id>/')
@is_logged_in
def article(id):
    # cursor
    cur = mysql.connection.cursor()

    # get articles
    cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()
    return render_template('article.html', article=article)
###############################################################################


###############################################################################
# creating register form using Flask-WTF
###############
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
# register
###############
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

        ###################################
        # unique user names
        ###################################
        check_username = username
        cur.execute("SELECT COUNT(username) FROM users WHERE username=%s", [check_username])
        count_result = cur.fetchone()

        app.logger.info(count_result['COUNT(username)'])
        number_of_row = count_result['COUNT(username)']
        if number_of_row > 0:
            flash('Username not available', 'danger')
            return redirect(url_for('register'))
        ####################################
        # Unique name end
        ####################################

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


###############################################################################
# login
###############
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form normal way not by flaskWTF
        username = request.form['username']
        password_candidate = request.form['password']

        # cursor
        cur = mysql.connection.cursor()

        # Get username
        result = cur.execute(
            "SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # compare password      entered p/w      , hash p/w
            if sha256_crypt.verify(password_candidate, password):
                # after correct username/password
                app.logger.info('PASSWORD MATCHED')
                session['logged_in'] = True
                session['username'] = username

                flash('You are now Logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                app.logger.info('PASSWORD NOT MATCHED')
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # closed
            cur.close()

        else:
            app.logger.info('USER NOT FOUND')
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')
###############################################################################


###############################################################################
# logout
###############
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now Logged out', 'success')
    return redirect(url_for('login'))
###############################################################################


###############################################################################
# dashboard
###############
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # cursor
    cur = mysql.connection.cursor()
    user_name = session['username']
    # get articles
    result = cur.execute("SELECT * FROM articles WHERE author = %s", [user_name])

    articles = cur.fetchall()

    if result > 0:
        app.logger.info(user_name)
        return render_template('dashboard.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)
    # close connection
    cur.close()
###############################################################################


###############################################################################
# Article Form
###############
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
###############################################################################


###############################################################################
# dashboard
###############
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        # getting cursor
        cur = mysql.connection.cursor()

        # execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)", (title, body, session['username']))

        # committing the changes
        mysql.connection.commit()

        # close
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)
###############################################################################


###############################################################################
# Edit article
################
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # cursor
    cur = mysql.connection.cursor()
    # Get article
    cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()

    # get form
    form = ArticleForm(request.form)

    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():

        # ##############normal request method###############
        title = request.form['title']
        body = request.form['body']
        # ##################################################
        # getting cursor
        cur = mysql.connection.cursor()

        # execute
        cur.execute("UPDATE articles SET title=%s, body=%s WHERE id = %s", (title, body, id))

        # committing the changes
        mysql.connection.commit()

        # close
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)
###############################################################################


###############################################################################
# Delete Article
################
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    cur = mysql.connection.cursor()

    cur.execute("DELETE FROM articles WHERE id = %s", [id])

    mysql.connection.commit()

    cur.close()
    flash('Article Deleted', 'success')
    return redirect(url_for('dashboard'))
###############################################################################


###############################################################################
# starting app in debug mode
###############
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
