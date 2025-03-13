from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

#app ek main ek krl database ek configure krnw
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#database ek configure krl user model ek create krnw
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'User(name = {self.name}, email={self.email})'

@app.route('/') 
def home():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(debug=True)