from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', name=about)


@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
