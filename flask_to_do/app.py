from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Todo(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String(30), unique=False)
    done = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return "{'id': %s, 'things': %s, 'done': %s}" % (self.id, self.thing, self.done)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form.get('backlog') == '':
            content = {'data_table' : Todo.query.all(), 'warning' : "Please input something"}
            return render_template('home.html', warning=content['warning'])
        else:
            a_new_data = Todo(thing = request.form.get('backlog'), done=False)
            db.session.add(a_new_data)
            db.session.commit()
            content = {'data_table' : Todo.query.all(), 'message': "Update Complete."}
            return render_template('home.html', message=content['message'])
    elif request.method == "GET":
        content = {'list': Todo}
        return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/edit/', methods=['GET', 'POST'])
def edit():
    return render_template('edit.html')


@app.route('/delete/')
def delete():
    return redirect(url_for('home'))


@app.route('/mark/')
def mark():
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(return render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp
