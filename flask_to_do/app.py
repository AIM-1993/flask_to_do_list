from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/delete')
def delete():
    return redirect(url_for('home'))

@app.route('/mark')
def mark():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
