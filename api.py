from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app =Flask(__name__)

#app ek main ek krl database ek configure krnw
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#database ek configure krl user model ek create krnw
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __repr__(self): #represent 
        return f'User(name = {self.name}, email={self.email})'

#validate requests   
user_args = reqparse.RequestParser()
user_args.add_argument('name',type=str,required=True,help="Name cannot be blank")
user_args.add_argument('email',type=str,required=True,help="Email cannot be blank")

#api kiyl app eke instance ekak
api = Api(app) 

#json format ekt res gnna - userFields
userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String,
}


class Users(Resource):

    #get api
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users 
    
    #post api
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args() #arguments filter krnna 
        user = UserModel(name=args["name"] , email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users,201

class User(Resource):

    @marshal_with(userFields)
    def get(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404,"User not found")
        return user
    
    @marshal_with(userFields)
    def patch(self,id):
        user = UserModel.query.filter_by(id=id).first()
        args = user_args.parse_args() 
        if not user:
            abort(404,"User not found")
        
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        users = UserModel.query.all()
        return user
    
    @marshal_with(userFields)
    def delete(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404,"User not found")
        
        db.session.delete(user)
        db.session.commit()

        users = UserModel.query.all()
        return user
    
    
    
    

api.add_resource(Users,'/api/users/')
api.add_resource(User,'/api/users/<int:id>')




@app.route('/') 
def home():
    return '<h1>Flask Rest APIs</h1>'

if __name__ == '__main__':
    app.run(debug=True)