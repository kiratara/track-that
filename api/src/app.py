import uuid
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from db import db
from resources.jobPost import JobPost, JobPostList
from resources.user import UserList, UserLogin, UserRegister
# from security import authenticate, identity


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #changes flask tracking because SQLalchemy has its own
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  #sqlite is going to be at the root of our folder
api = Api(app)
db.init_app(app)
# authenticate and identity is used by flask_jwt to know how to handle incoming JWT and what data to store in outgoing JWT
# this jwt isntantiation also automatically registsers '/auth' route that users can access
# api consumers can  send POST request to /auth with JSON payload - username, pw
# jwt = JWT(app, authenticate, identity)  

@app.before_first_request
def create_table():
    # sqlalchemy looks at the tables or "models" and creates those tables
    # example: above, we import job from resources.job which imports jobModel and jobModel has table description [name, columns]
    # data.db created
    db.create_all()


## ROUTES ##
# api.add_resource(UserRegister, '/signup', '/user/<int:user_id>', '/user')
# api.add_resource(UserLogin, '/login')

# authenticated only
# api.add_resource(UserList, '/users')

api.add_resource(JobPostList, '/posts')
api.add_resource(JobPost, "/post/<int:post_id>", "/post")


if __name__ == "__main__":
    app.run(debug=True)
