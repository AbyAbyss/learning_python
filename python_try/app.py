# starting with flask
from flask import Flask
app = Flask(__name__)


# root of the app
@app.route('/')
def index():
	return '<h3>Hello World</h3>'


@app.route('/user/<name>')
def user(name):
	return '<h1 style="color:white;text-align:center;width:350;padding:20px;margin:20px;background-color:red">Hello, %s!</h1>' % name.title()


if __name__ == '__main__':
	app.run(debug=True)
