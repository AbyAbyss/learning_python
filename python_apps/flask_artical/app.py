from flask import Flask, render_template
from data import Articals


app = Flask(__name__)

Articals = Articals()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/articals')
def articals():
    return render_template('articals.html', articals=Articals)


@app.route('/artical/<string:id>/')
def artical(id):
    return render_template('artical.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
