
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
    from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return redirect(url_for('login'))
        return redirect(url_for('your_desired_route'))
    return render_template('login.html')
from app import db, User

user = User(username='your-username')
user.set_password('your-password')
db.session.add(user)
db.session.commit()