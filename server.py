from flask import Flask, jsonify, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from shared.validate import validate

app = Flask(__name__)
app.secret_key = "test"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_web'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        errors = validate(request.form.get)
        if not errors['isValid']:
            return render_template('signup.html', errors=errors, value=request.form.get)
        flash(u'Your registration is successfully done', 'success')
        return redirect(url_for('index'))
    return render_template("signup.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
